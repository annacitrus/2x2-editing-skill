# 2x2 UGC style specification

These values are practical starting points, not a required font match or recovered source-project specification. Adapt them to footage, brand requirements, and the intended platform.

## Format and story

Default canvas: 1080 x 1920, normally 30 fps. Preserve source motion; 60 fps capture alone does not require 60 fps output. Keep the result casual and presenter-led. Preserve real wording, experience, and claims; do not invent offers, testimonials, or engagement automations.

Useful story shapes include problem → useful points → practical solution → evidence → close, or identity hook → clause-matched imagery → explanation → close. Use only the beats supported by the recording. Keep explicitly approved openings; flag factual or count mismatches in review notes rather than silently rewriting them.

## Opening

Start on the first useful spoken frame. Use four relevant supplied or authorized images in an edge-to-edge two-column, two-row grid without decorative gutters. Crop deliberately and leave usable space for the face. For new videos in a series, choose a fresh collage where assets allow.

Headline: white Arial/Helvetica-like bold sans serif, approximately 64 px, sentence case, usually two or three lines, centered within x 90–990 and y 280–620. Use compact opaque black backing and about 12–20 px padding. Keep the promise specific and supported by the script. Hold through the opening thought, often 3–5 seconds, rather than using a rigid timer.

Place the moving presenter cutout below the title, about 40–52% of canvas width. Avoid rounded-avatar containers and heavy borders. Preserve face, hair, microphone, and meaningful gestures. The first frame should already show the settled layout.

## Stable presenter layouts

Choose named fixed presets after inspecting the actual matte aspect ratio. At 1080 x 1920, a centered opening around 500 px wide and smaller side positions around 410 px wide are useful starting points. Derive height from the matte; choose top/left positions to keep the speaker clear of captions and important visual content.

Keep intentional hard cuts between center, left, right, and full-frame layouts. Do not derive presenter size or position from clip age, title presence, springs, or CSS transitions. Natural body movement remains. A full-frame close is optional when it fits the recording; avoid importing transforms from unrelated footage.

## Supporting imagery and resource cards

Prefer real relevant supplied images: product details, use environments, tools, results, or scenes that support the spoken idea. Respect project-specific asset restrictions. Conceptual imagery can illustrate an abstract clause but is not evidence of a factual claim.

For a named resource, show its actual thumbnail or page with readable title/attribution. A resource in the upper third with clear space for the cutout below often works. Fit landscape resources rather than cropping away their meaning. Do not fabricate screenshots.

Change imagery when the thought, resource, or concrete concept changes. One image can support several caption cards. Hold resources long enough to read; avoid mechanical image changes every two seconds or at every caption.

Use hard cuts. Avoid decorative crossfades, glitches, particles, persistent still-image zooms, unrelated arrows, and dramatic grading unless the user requests a different treatment. The speaker, captions, and demonstrated actions provide movement.

## Captions

Default: short phrase cards, Arial Bold or similar, about 54 px, white fill, 4–6 px black outline, centered, line height 1.05–1.15. At 1080 x 1920, x 90, width 860, and top around 1395 are useful initial values; adjust to footage and platform overlays.

Usually use one or two lines and about 4–10 words, breaking by meaning. Split overlong cards before shrinking text. Preserve wording, punctuation, and voice; correct recognition errors in names and technical terms against audio. Match speech onsets within roughly 1–3 output frames and retain the card through its final word. Do not flash long phrases.

Use hard replacement, without typewriter, bounce, or karaoke sweep. A deliberately word-captioned explainer can use timestamped single words instead; keep the chosen caption mode consistent.

Keep text clear of faces, hands, product interaction points, controls, and resource titles. Headline and speech captions are separate. Avoid redundant demonstration labels unless they help the viewer understand the action. Do not reproduce social-player chrome, reaction bubbles, message bars, or phone status areas from references. Check phone-size readability and platform-overlay collisions.

## Demonstrations, when relevant

Show the sentence becoming true using real supplied or authorized recordings:

| Spoken idea | Useful evidence |
|---|---|
| Add an input or start a task | Actual input choice and action |
| A feature produces a result | Visible action followed by the resulting output |
| Change a setting | Visible control change and corresponding behavior |
| Use a physical product | The relevant interaction and observable result |
| Use on a particular device | Actual usage on that device when claimed |

Remove the cutout when it obstructs evidence. Orient and fit recordings deliberately; avoid unexplained sideways screens. Trim loading/navigation waits while preserving honest cause and effect. Hold useful results long enough to understand. A frozen screenshot or unrelated playback cannot prove missing behavior.

Keep missing-media explanations in review notes. Use presenter or relevant image coverage when suitable. If the user requests a rough cut that needs a temporary placeholder, identify it and resolve it before final delivery.

## Audio

Default to clear, even narration. Preserve natural breaths but remove idle gaps. Use short edge fades where needed to prevent clicks without fading consonants.

A practical starting target is approximately -16 to -14 LUFS integrated and at or below -1 dBTP; adapt to delivery requirements and judge intelligibility by ear. Avoid compounding normalization on every revision. Bake in a restrained music bed by default, about 16–18 dB under speech (see "Background music" in SKILL.md and the bundled `scripts/make_music.py`), and keep it out of the way of meaningful demonstration audio. Avoid a whoosh at every cut or forced beat sync. Do not claim an exact soundtrack or font match without evidence.
