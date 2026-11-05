# 2x2 Editing Skill

Turn your raw talking-head footage into a vertical video with a four-image background, a presenter cutout, short captions, and relevant product demos.

This is an instruction pack for an AI editing agent. It works with Claude Code or Codex in an environment that can access your footage, run editing tools, and render video. The repository is called `2x2-editing-skill`; the skill itself is named **`edit-2x2-ugc`**.

## The process

You give the agent your footage, images, and demos. It picks the best takes, cuts pauses and mistakes, adds your cutout over the visuals, and builds captions and music. Then it checks the edit and exports an MP4. Watch it, tell it what to change, and ask for a revised export.

## 1. Install the skill

### Easiest: ask your agent

Paste this into Claude Code or Codex:

> Install the skill from https://github.com/annacitrus/2x2-editing-skill for this project. Include the whole skill folder, with its references, scripts, and agents. Confirm that you can load the skill named edit-2x2-ugc.

Use a coding agent with file and terminal access for installation and rendering.

### Or install from a terminal

With [Node.js](https://nodejs.org/) installed, open a terminal in your editing project and run:

```bash
npx skills add annacitrus/2x2-editing-skill
```

Choose Claude Code or Codex when prompted. Choose a global installation if you want to reuse the skill across projects, or a project installation for just this project. Start a new agent session if the skill does not appear.

### Manual download for Claude Code

1. On this repository, click **Code → Download ZIP**, then unzip it.
2. Copy the entire extracted folder into `.claude/skills/edit-2x2-ugc/` inside your project. For reuse across projects, use `~/.claude/skills/edit-2x2-ugc/`.
3. Check that `SKILL.md` is directly inside that folder, alongside `references/`, `scripts/`, and `agents/`. Avoid an extra nested folder.
4. Open Claude Code in the project. Ask it to use `edit-2x2-ugc`, or invoke `/edit-2x2-ugc`.

Keep the supporting files: downloading only SKILL.md leaves out the detailed style rules and workflow.

## 2. Set up Remotion

[Remotion](https://www.remotion.dev/) is the tool the agent uses to build and export the video. **Remotion's skills are its instruction manual; the Remotion project is the actual editing workspace.**

Install the companion instructions:

```bash
npx skills add remotion-dev/skills
```

Select your agent and include **`remotion-best-practices`**. See the [official skills guide](https://www.remotion.dev/docs/ai/skills).

Then tell the agent:

> Set up a Remotion project for this edit, install its dependencies, and check that preview and MP4 rendering work. Use remotion-best-practices alongside edit-2x2-ugc.

If you prefer to create the project yourself, follow the [official setup guide](https://www.remotion.dev/docs/). The agent may also need transcription, background-removal, and media-processing tools; have it identify missing tools before starting.

## 3. Organize your media — recommended Google Drive setup

Connect Google Drive in your Codex/ChatGPT environment if that integration is available. Use the account containing your media, then give the agent the actual folder links. If your environment cannot retrieve the media files through Drive, download them into the editing project and provide local files instead.

Create these folders in Google Drive:

| Folder | What to put in it | Reuse? |
| --- | --- | --- |
| **Images** | Background photos, screenshots, logos, and other supporting images | Yes — use the same folder across chats and videos |
| **Demos** | Screen recordings or clips showing your product or process in action | Yes — use the same folder across chats and videos |
| **Raw footage / Video name** | Your original talking-head recordings for this particular video | Make a separate folder for each video |

Keep raw footage separate from your reusable Images and Demos folders. Give files descriptive names so the agent can choose the right visual.

Upload your raw video, then paste all three folder links into the chat. You can also attach footage directly if your environment supports it. In a new chat, provide the links again and explain which folders to reuse.

If you want a specific photo or demo at a specific moment, say so: “Show demo-login.mp4 when I say ‘here is how it works.’” Include a script or transcript if you have one, plus any reference video, required wording, or images to avoid. Use media you have permission to use.

## 4. Ask for your edit

Copy, paste, and replace the brackets:

```text
Edit my raw video using remotion-best-practices and
2x2-editing-skill (the installed skill is named edit-2x2-ugc).

Raw footage: [file or Google Drive folder link]
Reusable images: [Google Drive folder link]
Reusable demos: [Google Drive folder link]

Make a vertical 1080 × 1920 video. Choose the best takes,
remove mistakes and dead space, and preserve my words and gestures.
Use the skill's 2x2 visuals, presenter cutout, captions, and music.

Show [specific image/demo] when I say “[line]”.
[Add any other preferences here.]

Check that you can access the actual media files before starting.
Give me the final MP4, subtitles, and editable source project.
```

## 5. Review and revise

Watch the export and describe changes with a timestamp or exact line:

> At 0:12, replace the background with circuit-board.jpg. Keep the presenter size the same. Shorten the pause after “try this,” then export a revised MP4.

I highly suggest watching through specifically looking for repeating words/phrases and deadspace that is not cut out.

## 6. Adjust the skill for your needs

If there is a request or problem you are frequently facing. You can just ask your agent to change the skill on your personal device.
