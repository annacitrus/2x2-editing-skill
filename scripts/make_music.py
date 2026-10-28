# Original background music bed for 2x2 edits (synthesized here, so no licensing issues).
#   python scripts/make_music.py <out.wav> <seconds>   (needs numpy and scipy)
# Make one bed per video at the composition's exact length; play it from frame 0.
# Light lo-fi electronic loop at 100 BPM in C: Fmaj9 - G6/9 - Em7 - Am9.
# FM electric piano, sine bass, kick/clap/hats, and a plucked arpeggio that
# enters after the first 4 bars. Mixed to sit under speech: low end cleaned,
# a dip around 2.5 kHz, peak-normalized; the video sets the bed's level.
import sys, wave, numpy as np
from scipy.signal import butter, sosfilt, fftconvolve, lfilter

SR = 48000; BPM = 100; BEAT = 60 / BPM; BAR = 4 * BEAT
# At least 12 bars are always rendered, the reverb IR is drawn after bar 12 and the
# gain is set on the first 27.4 s, so beds of any length sound identical up to their
# own fade (a series or A/B set shares one piece of music).
SHARED_BARS, SHARED_S = 12, 27.4
dst = sys.argv[1]; secs = float(sys.argv[2]) if len(sys.argv) > 2 else 30.0
bars = max(int(np.ceil(secs / BAR)), SHARED_BARS)
N = int(bars * BAR * SR) + SR
rng = np.random.default_rng(7)
STEMS = {}  # name -> (2, N) so each part's level can be checked

def hz(m): return 440 * 2 ** ((m - 69) / 12)
def lp(x, f): return sosfilt(butter(2, f, "low", fs=SR, output="sos"), x)
def hp(x, f): return sosfilt(butter(2, f, "high", fs=SR, output="sos"), x)
def bp(x, a, b): return sosfilt(butter(2, [a, b], "band", fs=SR, output="sos"), x)

def put(stem, sig, t, gl=1.0, gr=1.0, delay_r=0.0):
    sig = sig.copy(); sig[-240:] *= np.linspace(1, 0, 240)  # 5 ms tail fade, no clicks
    st = STEMS.setdefault(stem, np.zeros((2, N)))
    i = int(t * SR); j = i + int(delay_r * SR)
    if i < N: n = min(len(sig), N - i); st[0, i:i + n] += sig[:n] * gl
    if j < N: n = min(len(sig), N - j); st[1, j:j + n] += sig[:n] * gr

def env(n, a, rel, hold):
    e = np.ones(n); na = max(1, int(a * SR)); e[:na] = np.linspace(0, 1, na)
    h = int(hold * SR); nr = int(rel * SR)
    if h < n: e[h:h + nr] *= np.linspace(1, 0, min(nr, n - h)); e[h + nr:] = 0
    return e

def epiano(m, dur, vel):
    f = hz(m); n = int((dur + 0.5) * SR); t = np.arange(n) / SR
    idx = (1.2 + vel) * np.exp(-t / 0.35)
    tone = np.sin(2 * np.pi * f * t + idx * np.sin(2 * np.pi * f * t))
    tine = 0.12 * np.sin(2 * np.pi * f * 7 * t) * np.exp(-t / 0.04)
    trem = 1 + 0.08 * np.sin(2 * np.pi * 4.5 * t)
    return lp((tone + tine) * np.exp(-t / 1.6) * trem * env(n, 0.004, 0.12, dur) * vel, 3200)

def bass(m, dur, vel):
    f = hz(m); n = int((dur + 0.1) * SR); t = np.arange(n) / SR
    s = np.sin(2 * np.pi * f * t) + 0.4 * np.sin(4 * np.pi * f * t)  # 2nd harmonic carries on phone speakers
    return lp(np.tanh(1.6 * s * env(n, 0.006, 0.06, dur) * np.exp(-t / 0.9)) * vel, 400)

def kick(vel):
    n = int(0.45 * SR); t = np.arange(n) / SR
    ph = 2 * np.pi * np.cumsum(46 + 80 * np.exp(-t / 0.035)) / SR
    click = rng.normal(0, 1, n) * np.exp(-t / 0.003) * 0.15
    return (np.sin(ph) * np.exp(-t / 0.22) + click) * vel

def clap(vel):
    n = int(0.4 * SR); t = np.arange(n) / SR
    noise = bp(rng.normal(0, 1, n), 900, 5200)
    bursts = sum(np.exp(-np.clip(t - d, 0, None) / (0.006 if d < 0.02 else 0.11)) * (t >= d) for d in (0, 0.009, 0.019))
    body = 0.35 * np.sin(2 * np.pi * 185 * t) * np.exp(-t / 0.05)
    return (noise * bursts * 0.5 + body) * vel

def hat(vel, open_=False):
    n = int((0.25 if open_ else 0.06) * SR); t = np.arange(n) / SR
    return hp(rng.normal(0, 1, n), 7500) * np.exp(-t / (0.09 if open_ else 0.018)) * vel

def pluck(m, vel):
    f = hz(m); n = int(0.5 * SR); t = np.arange(n) / SR
    saw = 2 * ((f * t) % 1) - 1; sq = np.sign(np.sin(2 * np.pi * f * t))
    s = (0.6 * saw + 0.4 * sq) * np.exp(-t / 0.12)
    return lp(s, 2600) * env(n, 0.002, 0.05, 0.4) * vel

CHORDS = [  # (bass root, voicing)
    (41, [57, 60, 64, 67]),  # Fmaj9 (A C E G over F)
    (43, [59, 62, 64, 69]),  # G6/9 (B D E A over G)
    (40, [59, 62, 64, 67]),  # Em7 (B D E G over E)
    (45, [60, 64, 67, 71]),  # Am9 (C E G B over A)
]
ARP = [0, 1, 2, 3, 2, 1, 2, 3]
def room_ir():
    n_ir = int(1.3 * SR); t = np.arange(n_ir) / SR
    return np.stack([lp(rng.normal(0, 1, n_ir), 5000) * np.exp(-t / 0.35) for _ in range(2)]) * 0.012
for b in range(bars):
    t0 = b * BAR; root, voicing = CHORDS[b % 4]
    sw = lambda beat: t0 + beat * BEAT + (0.06 * BEAT if (beat * 2) % 2 == 1 else 0)  # swung 8ths
    # Electric piano: long chord on 1, re-strike on the "and" of 3.
    for beat, dur, vel in ((0, 2.3, 0.55), (2.5, 1.4, 0.42)):
        for k, m in enumerate(voicing):
            put('keys', epiano(m, dur * BEAT, vel * (0.9 if k == 0 else 1.0)) * 0.15, sw(beat) + 0.006 * k, *((1.0, 0.75) if k % 2 == 0 else (0.75, 1.0)))  # voices spread L/R, mono-safe
    # Bass.
    for beat, dur, m in ((0, 1.3, root), (1.5, 0.45, root), (2, 1.2, root), (3.5, 0.45, root + 12)):
        put('bass', bass(m, dur * BEAT, 0.8) * 0.21, sw(beat))
    # Drums.
    for beat in (0, 1.5, 2.5) + ((3.75,) if b % 4 == 3 else ()):
        put('kick', kick(0.95 if beat == 0 else 0.75) * 0.5, sw(beat))
    for beat in (1, 3):
        put('clap', clap(0.8) * 1.5, sw(beat), 0.95, 1.0)
    for i in range(8):
        v = (0.55 if i % 2 == 0 else 0.35) * rng.uniform(0.85, 1.05)
        put('hats', hat(v, open_=(i == 7 and b % 2 == 1)) * 0.58, sw(i / 2), 0.8, 1.0)
    # Arpeggio from bar 5: chord tones an octave up, 8ths, alternating pan.
    if b >= 4:
        for i, a in enumerate(ARP):
            put('arp', pluck(voicing[a] + 12, rng.uniform(0.8, 1.0)) * 0.55, sw(i / 2), 1.0 if i % 2 else 0.6, 0.6 if i % 2 else 1.0)
    if b == SHARED_BARS - 1: ir = room_ir()

for k, v in STEMS.items():
    print(f"{k:5s} rms {20 * np.log10(np.sqrt(np.mean(v[:, :int(secs * SR)] ** 2)) + 1e-9):6.1f} dB")
mix = sum(STEMS.values())
# Room: short synthetic reverb (decaying filtered noise IR), mixed low.
mix = mix + np.stack([fftconvolve(mix[c], ir[c])[:N] for c in range(2)])
# Clean lows, dip the speech presence band (RBJ peaking EQ, -4 dB at 2.5 kHz, Q 0.9).
A = 10 ** (-4 / 40); w0 = 2 * np.pi * 2500 / SR; al = np.sin(w0) / (2 * 0.9)
bq = np.array([1 + al * A, -2 * np.cos(w0), 1 - al * A]); aq = np.array([1 + al / A, -2 * np.cos(w0), 1 - al / A])
mix = np.stack([lfilter(bq, aq, hp(c, 35)) for c in mix])
peak = np.abs(mix[:, :int(SHARED_S * SR)]).max()
mix = mix[:, :int(secs * SR)]
fade = int(1.2 * SR); mix[:, -fade:] *= np.linspace(1, 0, fade) ** 2
mix = np.tanh(1.2 * mix / peak) / np.tanh(1.2) * 0.89  # gentle soft clip, about -1 dBFS peak
out = wave.open(dst, "wb"); out.setnchannels(2); out.setsampwidth(2); out.setframerate(SR)
out.writeframes((mix.T * 32767).astype(np.int16).tobytes()); out.close()
print(dst, secs, "s,", bars, "bars")
