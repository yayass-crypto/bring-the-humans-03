# Press files used

Every make.fun mark, wordmark and colour in the ad comes from make.fun's
press pack, used as it is. The pack was fetched in the build session from
<https://make.fun/press/manifest.json> (edition 2026-11-21) and its guide
<https://make.fun/press/llms.txt>. **This repository holds no copy of any
press file**, per the kit — fetch them from the URLs below into `assets/`
(and the fonts into `fonts/`) to reproduce the render.

## Brand files in the ad

| File | URL | sha256 of the file as downloaded |
| --- | --- | --- |
| `mark-on-dark-1024.png` (mascot mark, dark grounds) | <https://make.fun/press/mark-on-dark-1024.png> | `cbbaf9baa411797e8958c8bb641ff891e791e0115ef851cd5acdd13eec1516b5` |
| `mark-1024.png` (mascot mark, light grounds) | <https://make.fun/press/mark-1024.png> | `96ba54c48b6d8ea5bbfa4f199f0a2da1bd27b312a1094309c71f0bc02e0f8725` |
| `lockup-on-dark-2400.png` (mark + wordmark, dark grounds) | <https://make.fun/press/lockup-on-dark-2400.png> | `9805171f99387f1025ca41b0c3c6262e023127bc0d290b55b8a9efd6cd7bf8c8` |
| `endcard-9x16.mp4` (referral end card on magenta, 3 s) | <https://make.fun/press/referral-card/9x16/makefun-card-9x16.mp4> | `4b3b04e500003dbde8c5ada440128c2f7374a4bbc59f548c835625c407495221` |

## Fonts (SIL Open Font License)

| File | Source | sha256 |
| --- | --- | --- |
| `JetBrainsMono-Bold.ttf` | <https://github.com/JetBrains/JetBrainsMono> | `d22c4f3821d725eb01210d278d95dfcfcaadc34699a06658d47c8a5cc5830ada` |
| `Inter-Bold.otf`, `Inter-SemiBold.ttf`, `Inter-Regular.ttf` | <https://github.com/rsms/inter> (v4.1) | see build log |

## Colours

- make.fun magenta `#c41c83` — the ground, the mark's disc and the caret.
- Ink `#191419` — outlines and the referral code.
- White `#ffffff` — the wordmark, the label and the field.

## Notes from the fetch (2026-11-22)

- The end card's sha256 matches the manifest exactly. The three PNGs do
  **not** match the manifest's hashes, and neither does the press-kit zip —
  the files as served differ slightly in size from the manifest's numbers
  (e.g. mark-on-dark 67,338 bytes served vs 67,455 listed). A second
  download of the same file gave the identical hash, so the served files are
  stable and the manifest's hashes for those PNGs are simply stale; the
  files themselves are the live press files, used as-is.
- The kit's `AGENT.md` mentions a brand-badge overlay under
  `https://make.fun/press/brand-badge/` — that path is **not** in the live
  manifest (edition 2026-11-21), which lists no `brand_badge` block at all.
  The ad therefore shows the brand the way the live pack defines it: the
  lockup (mark + wordmark) in the first frame and the mascot mark in the
  top-left corner from the first frame until the end card.
- End-card field (manifest `referral_card.fields`, 9:16): the field is
  x 153, y 1174, 774×194; the code goes from x 210, centred on y 1271, at
  62 px JetBrains Mono Bold in ink, with the caret (x 208, y 1230, 9×82)
  covered in white first. The card rests 1.433 s in; the code is overlaid
  from that point, per the press pack's own ffmpeg recipe.
