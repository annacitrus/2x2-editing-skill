# Production and verification

## Inventory

Read current feedback and locate the latest approved source for revisions. Do not rebuild from an obsolete plan that restores removed sections. Preserve original recordings; derive proxies, audio, SDR footage, and mattes separately.

Inspect orientation/rotation metadata, dimensions, fps, duration, and audio. When HDR footage needs SDR delivery, use a controlled conversion and check skin tones/highlights. Resolve runtime and tool paths in the current environment.

Inspect actual supplied assets before assuming a claimed feature is demonstrated. Use connected file tools where appropriate. Ask for essential unavailable media after inspecting accessible material, while continuing independent work.

For a series or substantial asset library, maintain an image-source manifest with filenames, original IDs/URLs, identity/hash when available, and role. Compare recent selections for variety; renamed files are not fresh imagery. Record current project exclusions. Contact sheets help selection; resize oversized stills for working copies.

## Speech selection before compositing

1. Transcribe with word timestamps and correct names/technical terms against audio. Recognition output is a guide, not ground truth.
2. Review repeated passages with sound. Compare complete wording, fluency, emphasis, and direct lens contact; do not automatically choose the latest take. Remove unfinished lines, repeats, resets, and sustained unusable lookaways. Keep ordinary blinks and gestures. Cover essential wording with relevant visuals where appropriate if no usable camera-facing take exists.
2a. Whisper can collapse a false start into the following clean take, so "You don't need an Ar— you don't need an Arduino kit…" transcribes as one sentence. Compare each clip's word timings with energy segments: speech before a long pause, followed by a full reading, is usually a false start. After assembly, transcribe the export with a medium model and `condition_on_previous_text=False` to catch repeats.
3. Log kept and rejected source ranges and reasons, such as in `take-review.csv`.
4. Assemble speech only. Trim dead space and unnecessary breath gaps while preserving consonants, word tails, intentional emphasis, and natural articulation. Do not cut a word solely on amplitude.
5. A useful initial silence diagnostic is `silencedetect=noise=-36dB:d=0.18`; a 0.12-second pass can locate smaller candidates. Listen to flags and adapt thresholds to the recording. Necessary articulation is not dead space.
6. Listen to every joined boundary; re-transcribe when helpful. Check duplicate tails, missing conjunctions, clipped phonemes, empty fragments, sequence, and unintended new claims. Review camera contact and crop suitability across each retained range.
6a. Tighten remaining pauses after take selection. Shrink every quiet run of about 0.15 s or more that lies between transcribed words to roughly 0.08 s, keeping about 0.04 s on each side. Do not cut inside word spans, and do not merge gaps across short sounds. For leading and trailing silence, measure speech onset and end from energy, about 8 dB above the noise floor, and leave about 0.05 s. Whisper often places the first word at 0.00 and absorbs leading silence into it. Re-transcribe the tightened audio and compare it word for word with the intended script. Restore any lost word, such as a soft "the", a trailing plural "s", or a final word, before compositing. In the electronics project, `tools/tighten.py` lists candidate pauses and applies a removal plan, and `tools/remap_tsx.py` shifts beats, `at` offsets and captions onto the new timeline. Re-run the export-level quiet-run check relative to the noise floor: an absolute -36 dB silencedetect can miss pauses when the room tone sits near that level.
7. Record selection decisions, intentional pauses, and unresolved limitations in a brief pre-compositing note. Finish the speech review before building the visual rough cut.

## Timeline and compositing

Build a frame-aligned beat table with source/output timing, exact words, visual, layout, caption, and any demonstrated action. Example segment:

```json
{"name":"Tip-03","sourceIn":1182,"sourceOut":1266,"fromFrame":210,"duration":84,"visual":"detail-042.jpg","layout":"right","title":"Try this first"}
```

Here `sourceIn` and `sourceOut` are source frames at the working frame rate; `sourceOut` is exclusive. Duration equals sourceOut minus sourceIn. Output ranges should be contiguous and sum to total duration. Derive captions and edit-decision timestamps from final output timing, not original source timestamps.

Treat each source range as an editing unit, moving/trimming voice, visual, and caption clocks together. For Remotion, follow the companion skill for Sequence/Track markup and verify source-clock offsets in nested trims. Titles must not alter presenter geometry.

**A/V sync (a known failure).** In Remotion, a video inside a `<Sequence from={N}>` restarts at its own frame 0 unless it is trimmed. When the cutout matte or full-frame footage shares the speech cut's clock and is split across beat Sequences, give every instance `trimBefore={N}`, matching that Sequence's `from`. Otherwise every beat after the first replays the start of the footage while the voice keeps going, and still frames still look plausible. Verify the rendered file, not only the code. For a few frames late in the edit, compare the rendered presenter region with the same output frame of the speech-cut video. A large difference at frame N and a near-zero difference at frame N minus the beat start means the sync is broken.

Use a reliable matting method appropriate to footage and available tools. Inspect hair, fingers, microphone, mouth, dark clothing, and lower crop on light/dark backgrounds. Decode correct source frames; stateful matting needs chronological state or adequate warm-up. Verify frame counts and ranges, not merely folder existence.

Crop/scale consistently within shots and read actual matte dimensions before positioning. Avoid excessive enlargement and cutout detail loss. Keep generated media separate from originals.

## Post-rough-cut dead-space gate

Run this after the complete visual rough cut is assembled, before treating it as ready for final export or delivery. The pre-compositing speech pass does not replace this check.

1. Review the entire assembled rough cut with sound, including every take join, sentence boundary, mid-sentence hesitation, repeated pickup, and the opening and ending. Check the isolated narration as well as the full mix: music can hide pauses from a silence detector.
2. Scan the narration on the rough cut's output clock for quiet runs of about 0.15 s or longer, using a threshold relative to the recording's noise floor. `silencedetect=noise=-36dB:d=0.18` is a starting diagnostic, not a passing criterion; adapt it and use a shorter pass when needed. Inspect word timestamps and the waveform around every candidate. ASR can collapse false starts or duplicate readings, so check suspicious pickups against the audio rather than trusting the transcript alone.
3. Remove all remaining dead space, including short pauses that accumulate across the edit. Bring ordinary speech gaps to roughly 0.05–0.1 s while preserving complete words, soft consonants, word tails, and necessary articulation. Do not cut on amplitude alone or merge gaps across short sounds. Keep a longer pause only when it serves an intentional spoken or demonstrated beat, and record its timestamp and reason.
4. Apply each cut to narration and presenter footage together; retime captions, visuals, demonstrations, and edit decisions to the new output clock. Keep lip sync and stable presenter layouts. Keep the music continuous and update its ending fade rather than jump-cutting the bed with every speech trim.
5. Recheck every changed join with sound and re-transcribe the tightened narration, comparing it with the intended wording for lost words and surviving repeats. Repeat the scan and review until no unexplained dead-space candidates remain. After export, repeat the narration/full-mix check on the delivered file; music or a clean detector alone cannot establish a pass.

Record removed ranges, remaining intentional pauses, checks actually performed, and any limitation in `post-rough-cut-check.md`. Do not claim a listening review if only automated analysis was possible.

## Preview and render

For Remotion, follow its skill for Studio and rendering. Inspect an opening proof before a full new export. For a narrow revision, targeted proofs plus the revised full export may suffice. Honor the user's authorized export scope.

Practical delivery defaults: H.264, CRF 18, yuv420p, 1080 x 1920, normally 30 fps, AAC at 48 kHz. Adapt to platform/user requirements. Use actual entry/composition names and choose render concurrency based on resources; PNG-heavy matting can consume substantial memory.

For a stall, inspect logs and owned processes, stop only the affected renderer, and restart that export. Do not deliver an incomplete MP4 or rerender unaffected completed videos unnecessarily.

## Delivery checks

- Listen to the complete final edit and every speech join. Check dead space, resets, retakes, clipped words, and closing continuity. Review at phone size and full resolution.
- Inspect every cut immediately before/after and through the first second, including internal demonstration cuts. At 30 fps, useful samples are -2, -1, 0, 1, 2, 4, 8, 12, 16, 20, and 29 relative to the cut; adapt to output fps and inspect suspicious intervals in motion.
- Confirm lip sync in every beat, using the rendered-frame comparison above, not only the first beat.
- Confirm the first frame of each shot has the final presenter size/position. Natural body movement changes face centroids, so those alone cannot establish layout stability. Use visual review or rendered-frame/source comparison at the fixed transform; do not claim a code-only check proves rendered behavior.
- Check the opening promise, caption timing/line breaks, masks/missing frames, readable resource/product details, and unwanted placeholders or labels.
- Match claims to actual visible actions. Describe missing evidence in review notes; do not manufacture controls or substitute unrelated behavior.
- Decode the entire exported file. Useful initial diagnostics include black gaps of 0.10 s at 98% black and silence at -36 dB for 0.18 s. Review flags in context: dark screens and intentional articulation are not automatically errors. Measure loudness/true peak and run relevant source checks when implementing in code.
- With music:
  - Measure the bed against the voice (about 16–18 dB under) and the final true peak.
  - Transcribe the full mix to confirm no words are masked.
  - For a music-only revision, compare against the previous export. The video frames should be identical and the voice at zero lag, and the new-minus-old audio should be the bed at its mixed level.
- Confirm current feedback, asset restrictions, series imagery variation where applicable, and package reproducibility.

Report only checks actually performed and disclose limitations. Sampled frames do not establish full playback review.

## Deliverables

Put user-facing artifacts in the project's outputs directory and provide a direct final MP4 link. For a full edit, include a reproducible source project/package with necessary derived media, lockfile, and usable setup instructions. Omit dependency folders, caches, excluded assets, and unused intermediates. A local dependency junction must not be the only way the package works.

Include corrected output-timed SRT, timecoded edit decisions, take-review decisions, image manifest when applicable, and a concise quality note. Match scope to the request. Clearly identify the latest version; source/package and notes should match the delivered MP4. A narrow revision updates affected artifacts without regenerating unrelated media.
