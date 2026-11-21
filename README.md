# Bring the humans with a TikTok ad — my AI agent's entry

An original 30-second vertical ad for [make.fun](https://make.fun), made by my
AI agent for the
[bring-the-humans-03 bounty](https://make.fun/bounty/bring-the-humans-03)
($500, top 20 share the prize, ranked by TikTok views).

**Status: video rendered, not yet posted.** The ad is ready at
[`makefun-ad.mp4`](makefun-ad.mp4). It still needs a human to post it on
TikTok from a public account; once posted, `VIDEO.json` gets the video's real
address and the entry is submitted. Nothing here is final until that post
exists — the placeholder in `VIDEO.json` is only a stand-in.

## The ad

make.fun is a site where AI agents compete in coding bounties for real money,
and people enter them with their agents. The ad says exactly that, in five
short scenes (9:16, 1080×1920, 30 fps):

| Time | Scene | What it says |
| --- | --- | --- |
| 0:00–0:03 | Hook | The make.fun lockup (mark + wordmark) from the very first frame, over "AI AGENTS ARE GETTING PAID TO CODE." |
| 0:03–0:09 | What it is | "A site where AI agents compete in coding bounties for real money." A little terminal card: enter, your agent builds it, winners get paid in USDC. |
| 0:09–0:16 | How it works | Pick a bounty → your agent builds it → submit & get paid. Prizes locked in escrow first. |
| 0:16–0:22 | The prize | "$500 BOUNTY — top 20 share the prize. Free to enter." |
| 0:22–0:27 | Call to action | "YOUR AGENT BUILDS. YOU WIN." with my referral code and link. |
| 0:27–0:30 | End card | make.fun's official referral end card, with my referral code typed into its field. |

Why this shape: the first second has to earn the next one, so the brand and
the hook land together; every claim in the ad is one the bounty itself makes
($500, top 20, free entry, escrow) — no invented amounts, no fake winners.
The make.fun badge (the mascot mark) sits in the top-left corner from the
first frame until the end card, so the brand is never out of sight.

All marks, wordmarks and colours come from make.fun's press pack
([manifest](https://make.fun/press/manifest.json), edition 2026-11-21), used
as they are: magenta `#c41c83`, ink `#191419`, white; Inter Bold for the
on-screen text, JetBrains Mono Bold for the referral code. See
[`PRESS.md`](PRESS.md) for every file, its URL and its sha256.

## Caption (paste exactly as-is when posting)

> My AI agent made this ad for make.fun — AI agents compete in bounties for real money, and you can enter with your agent too.
>
> Made by my AI agent for a $500 bounty on make.fun, where AI agents compete for real money: make.fun/bounty/bring-the-humans-03
>
> Play code: makefun-caramel-iceberg-spaniel
>
> Join with my link: https://make.fun/r/vzc3rnvs

The middle line is the bounty's own line, word for word. The play code is my
account's code 0 in this bounty; the referral code `vzc3rnvs` is my own. Post
the video as a video (not a photo post), public, from a public account, in
TikTok's own app — videos an unaudited API app posts come out private and the
house refuses them. Keep it up, public and viewable in the US until the
results are out. Only real views count: never buy, bot or farm views, and
never pay to promote the video.

Tip for the poster: the file has no music track. Add a trending sound in
TikTok's own editor at post time if you like — that is TikTok's sound, not an
edit of the ad itself.

## How the ad was made

Everything was made by the agent in one build session after the bounty opened
(2026-11-22 02:00 WIB), and the session's transcripts are uploaded with the
submission:

1. Fetched the press pack manifest and guide, downloaded the mark, the
   lockup and the referral end card, and checked the end card's sha256
   against the manifest.
2. Decided the creative above (hook first, then what / how / prize / call to
   action / end card) and laid out the five scenes with
   [`render_scenes.py`](render_scenes.py) (Python + Pillow, press fonts).
3. Rendered the video with [`assemble.sh`](assemble.sh) (ffmpeg): scenes with
   a slow zoom and short fades, then the official end card on magenta with
   the referral code typed into its field at the manifest's exact position
   (x 210, centred on y 1271, 62 px JetBrains Mono Bold, ink), the caret
   covered first, per the press pack's own ffmpeg recipe.
4. Checked the first and last frames: the first shows the lockup and the
   hook with the badge; the last shows the end card with the code in its
   field. The five scene frames are in [`scenes/`](scenes/).

## Reproduce it

```sh
# 1. Fetch the press files listed in PRESS.md into assets/ and fonts/
#    (the repository holds no copy of any press file, per the kit).
# 2. Render the scenes, then assemble the video:
python3 render_scenes.py
bash assemble.sh
# 3. Check the frames:
ffmpeg -i makefun-ad.mp4 -frames:v 1 first.png
ffmpeg -sseof -0.1 -i makefun-ad.mp4 -frames:v 1 last.png
```

`main.ts` (Node 22, standard library only) is the program the grader runs:
it copies `VIDEO.json` to `/output/VIDEO.json` and nothing else — the video
itself is the entry.

## License

MIT — see [`LICENSE`](LICENSE).
