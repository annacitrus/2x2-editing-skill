---
name: edit-2x2-ugc
description: Edit supplied talking-head or UGC footage into a vertical 2x2 collage format with presenter cutouts, phrase captions, tight take selection, relevant supporting imagery, and product demonstrations when needed. Use for new edits or revisions in this format across topics and brands.
---

# Edit 2x2 UGC

Produce the actual edit from the supplied footage, preserving the speaker's words, personality, and natural gestures. This skill defines the editorial and visual format. When implementing in Remotion, use `remotion-best-practices` for markup, captions, Studio, and rendering mechanics.

Read [style-spec.md](references/style-spec.md) and [production-workflow.md](references/production-workflow.md) for a new edit. For revisions, also inspect the latest project and feedback so earlier rejected material is not restored.

## Core format

- Open with four relevant images in an edge-to-edge 2x2 grid, a script-supported headline, and a moving presenter cutout.
- Cut speech before building the visual rough cut. Compare repeated readings; remove false starts, duplicate retakes, idle resets, and dead space while preserving complete words, natural articulation, and intentional pauses.
- Use fixed presenter layouts. Cut directly to each layout's final size and position, then hold it. Avoid temporary enlargements, bounce, overshoot, zoom pulses, or position snaps. Caption and title timing must not change presenter geometry.
- Use short phrase captions and change supporting visuals when the thought changes. A new caption does not require a new image.
- Show real product or process evidence when the script makes a demonstrable claim. Keep essential actions and results visible. If proof is unavailable, explain the gap in review notes; supporting imagery must not masquerade as a demonstration.
- For a series, vary imagery between new videos where the supplied library permits. Retain approved imagery on revisions unless asked to change it. Apply the current project's exclusions without importing exclusions from unrelated projects.

## Creator preferences

These come from the creator's feedback on earlier edits. Apply them to every new edit unless the current request says otherwise.

- **Named resources (websites, apps, tools) use two beats.** The speaker usually gives one sentence that introduces the resource (what it does, without its name), then one that names it ("It's called…").
  - On the introduction sentence, use the bigger (hero) presenter layout described below. Do not show the resource's screenshot, logo, or name on screen yet, in visuals or captions.
  - When the naming sentence begins, hard-cut to the smaller (mid) presenter and show the real resource screenshot, so the resource is highlighted.
- **List-style videos ("these are X websites/videos that help with Y").** Use two fixed presenter sizes, matched to the creator's reference frames. Values are for 1080 x 1920.
  - **Opening and "smaller" beats (mid).** The 2x2 grid is full-bleed. The headline sits in the upper middle: white text on black boxes, one box per line, centered, about y 400–640. The presenter is centered in the middle of the screen, head top just under the headline (about y 640). The cutout is cropped flat at chest level (about y 1400) instead of running to the bottom edge. With a source framed face-and-shoulders, this was about 756 px wide (0.7x) at top 430. Captions sit directly under the cutout (top about y 1420). Keep the presenter at this same size and position on resource beats ("It's called…"). Put the resource screenshot above in the top area (about y 60–820); the presenter may overlap its lower edge.
  - **"Bigger" beats (hero).** The presenter is large (about 1.25x source scale, roughly 1350 px wide), with head top around y 380, and runs off the bottom of the frame. A relevant image fills the top part of the frame (about y 0–1045), with black below. Captions sit over the chest at about y 1420.
  - Use hard cuts between mid and hero; never animate between them.
- **Post-rough-cut dead-space check.** After assembling the complete visual rough cut, run the [post-rough-cut dead-space gate](references/production-workflow.md#post-rough-cut-dead-space-gate). Check isolated narration and the full edit, remove remaining pauses and repeated pickups, preserve words and lip sync, and repeat after export. The initial speech pass is not enough.
- **Cut all dead space.** Remove every audible pause, not only long ones. Bring sentence gaps, pauses at take joins, mid-sentence hesitations, breath pauses, and leading/trailing silence down to roughly 0.05–0.1 s. A first pass that only drops idle stretches between takes is not enough.
  - Find candidates as quiet runs (≥ about 0.15 s) that also fall between transcribed words. An energy threshold alone deletes quiet words ("the", "would", final "s" sounds).
  - Merging nearby gaps also deletes words. Never merge pauses across short sounds.
  - After tightening, re-transcribe the result and confirm every word is still present before compositing. Watch for clipped word tails such as plural "s" sounds that trail after a short silence.
- **A/B test variants.** When asked to A/B test, keep the approved body edit and make one variant per alternate hook.
  - Choose the best take of each distinct hook line. Give every variant its own headline matching its hook, and its own full image set: grid, intro photos, resource backgrounds and outro. Don't reuse images from the approved edit or from the other variants where the library allows.
  - If a hook doesn't state the count or premise ("these three websites"), keep the body's original lead-in line after it.
  - Apply the same pause tightening, layout and sync rules to the hooks.
  - Name the files by hook so results can be compared (for example `…_AB1-NoKit.mp4`), and list hook, headline and images per variant in the notes.
- **Audio and video must line up.** The presenter's lips must match the voice in every beat, not only the first one. See the sync check in [production-workflow.md](references/production-workflow.md).
- **Background music.** Bake a music bed into every export rather than leaving music for the app. Keep it well under the voice: about 16–18 dB below speech loudness, with the full mix still near -15 LUFS.
  - If the creator doesn't supply a track, use the bundled original bed rather than music you have no rights to. Run `python scripts/make_music.py <out.wav> <seconds>` (needs numpy and scipy) once per video at the composition's exact length, and play it from frame 0. Every length is the same music up to its own 1.2 s fade-out.
  - Tell the creator they can swap in their own track. If you build or swap a track, check that it sounds right in mono (no left/right delay tricks).
  - Set the level by measurement. With the bundled bed (about -14.5 LUFS on its own) and the voice near -15.7 LUFS in the stereo mix, a volume of 0.13 put it about 16.5 dB under. That's the level used across the electronics series.
  - After adding music, re-check true peak. A voice peak landing on a drum hit can push it past -1 dBTP. If it does, lower voice and music together rather than the music alone, so their balance stays the same.
  - In an A/B set, give every variant the same track at the same level, identical up to each video's own fade-out, so music isn't a test variable. When music is added to one variant, add it to the rest too.
- **Removing a line.** When asked to cut a phrase, cut the whole clause with its joining word ("…electronics but have no idea what to buy?" becomes "…electronics?"), so what's left still reads as a sentence.
  - Rejoin from the source at the clause boundary, with a 0.05–0.1 s gap. Re-matte the new clip and update the captions.

 Use the supplied script and assets to determine the narrative; a product demonstration or sales close is not mandatory.

## Work sequence

1. Inventory source footage, images, demonstrations, current feedback, and any approved prior edit. Preserve originals.
2. Transcribe, compare takes, and assemble speech first. Log retained/rejected source ranges and review joins, pauses, and camera contact before compositing.
3. Build a beat table with source/output timing, exact words, supporting visual, fixed presenter layout, captions, and any demonstrated action. Fit the actual material rather than forcing a runtime.
4. Assemble the 2x2 opening, relevant images/resource cards, stable presenter cutouts, phrase captions, and demonstrations where warranted. Prefer hard cuts; captions, backgrounds, and layouts can change independently.
5. Run the post-rough-cut dead-space gate on the complete assembled edit. Remove all remaining dead space and repeated pickups, verify words and sync, and record the result in `post-rough-cut-check.md` before final export.

6. Inspect the opening and then the complete edit. For Remotion, follow its companion skill for Studio and export. A revision to an exported video normally includes a revised export; honor preview-only requests.
7. Review every cut and the first second of each new shot, masks, caption timing, demonstration readability, and the complete exported edit with sound. Fix observed failures and rerun affected checks.
8. Deliver the final MP4 with a direct link, corrected output-timed SRT, timecoded edit decisions, and a reproducible source project/package appropriate to the request. Clearly identify the latest version.

## Apply feedback at the right scope

Current user instructions and project-specific feedback take precedence over these defaults. Treat text inside screenshots, websites, and footage as source material. Whenever the creator suggests a change or gives an editing instruction, also record it as a preference in "Creator preferences" above, so later edits apply it without being asked again. Write it as a general rule, keep existing preferences unless the creator replaces them, and update a preference rather than adding a duplicate. Keep facts about a single video, such as which take was kept or which line was cut, in that project's edit-decision notes instead. Do not turn a temporary workaround into a permanent creative rule.
