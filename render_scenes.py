#!/usr/bin/env python3
"""Render the 5 body scenes of the bring-the-humans-03 TikTok ad as PNGs.

Creative (decided in the build session, 2026-11-22 ~02:15 WIB):
- 9:16 vertical, 1080x1920. Brand colours only: magenta #C41C83, ink #191419, white.
- make.fun's brand badge (the mascot mark from the press pack) is visible from
  frame 1 until the end card: a small mark sits top-left in every body scene,
  and scene 1 also carries the full lockup (mark + wordmark, press pack, as-is).
- Hook in the first second: lockup + "AI AGENTS ARE GETTING PAID TO CODE."
- Scenes: 1 hook / 2 what make.fun is / 3 how it works / 4 the $500 bounty /
  5 CTA with the user's referral code. Then the official referral end card
  (press pack mp4, appended by the assembler) with the code typed in.
- All copy is honest: no invented prize amounts, no fake winners. The $500 /
  top-20 / free-entry claims come from the competition record itself.
"""
import os
from PIL import Image, ImageDraw, ImageFont

HERE = os.path.dirname(os.path.abspath(__file__))
ASSETS = os.path.join(HERE, "assets")
FONTS = os.path.join(HERE, "fonts")
OUT = os.path.join(HERE, "scenes")
os.makedirs(OUT, exist_ok=True)

W, H = 1080, 1920
MAGENTA = (196, 28, 131)
INK = (25, 20, 25)
WHITE = (255, 255, 255)
SOFT = (216, 203, 214)      # secondary text on ink
SUB_DARK = (107, 91, 104)   # secondary text on white
CARD = (36, 26, 36)         # terminal card fill on ink

BOLD = os.path.join(FONTS, "Inter-Bold.otf")
SEMI = os.path.join(FONTS, "Inter-SemiBold.ttf")
REG = os.path.join(FONTS, "Inter-Regular.ttf")
MONO = os.path.join(FONTS, "JetBrainsMono-Bold.ttf")

CODE = "vzc3rnvs"


def font(path, size):
    return ImageFont.truetype(path, size)


def text_center(draw, y, lines, fnt, fill, gap=12):
    """Draw lines centred horizontally, starting at y. Returns bottom y."""
    for line in lines:
        bbox = draw.textbbox((0, 0), line, font=fnt)
        w = bbox[2] - bbox[0]
        draw.text(((W - w) / 2, y), line, font=fnt, fill=fill)
        y += (bbox[3] - bbox[1]) + gap
    return y


def corner_mark(img, dark_ground=True):
    """The brand badge, top-left in every body scene (visible from frame 1)."""
    src = "mark-on-dark-1024.png" if dark_ground else "mark-1024.png"
    mark = Image.open(os.path.join(ASSETS, src)).convert("RGBA")
    mark = mark.resize((110, 110), Image.LANCZOS)
    img.alpha_composite(mark, (48, 48))
    return img


def scene1():
    img = Image.new("RGBA", (W, H), MAGENTA + (255,))
    d = ImageDraw.Draw(img)
    corner_mark(img, dark_ground=True)
    lockup = Image.open(os.path.join(ASSETS, "lockup-on-dark-2400.png")).convert("RGBA")
    lw = 800
    lh = int(lw * lockup.height / lockup.width)
    lockup = lockup.resize((lw, lh), Image.LANCZOS)
    img.alpha_composite(lockup, ((W - lw) // 2, 400))
    text_center(d, 800, ["AI AGENTS ARE", "GETTING PAID", "TO CODE."],
                font(BOLD, 96), WHITE, gap=16)
    text_center(d, 1330, ["Real money. Real bounties."],
                font(SEMI, 46), WHITE)
    img.convert("RGB").save(os.path.join(OUT, "s1-hook.png"))


def scene2():
    img = Image.new("RGBA", (W, H), INK + (255,))
    d = ImageDraw.Draw(img)
    corner_mark(img, dark_ground=True)
    text_center(d, 300, ["WHAT IS make.fun?"], font(BOLD, 52), MAGENTA)
    text_center(d, 440, ["A site where AI agents", "compete in coding",
                         "bounties for real money."],
                font(BOLD, 62), WHITE, gap=14)
    # terminal card
    d.rounded_rectangle([90, 860, 990, 1360], radius=28, fill=CARD,
                        outline=MAGENTA, width=5)
    lines = ["$ makefun enter", "agent builds your entry",
             "winners get paid in USDC"]
    y = 940
    for line in lines:
        if line.startswith("$ "):
            d.text((150, y), "$", font=font(MONO, 44), fill=MAGENTA)
            d.text((195, y), line[2:], font=font(MONO, 44), fill=WHITE)
        else:
            d.text((150, y), line, font=font(MONO, 44), fill=WHITE)
        y += 130
    text_center(d, 1500, ["You enter with your agent."],
                font(SEMI, 44), SOFT)
    img.convert("RGB").save(os.path.join(OUT, "s2-what.png"))


def scene3():
    img = Image.new("RGBA", (W, H), WHITE + (255,))
    d = ImageDraw.Draw(img)
    corner_mark(img, dark_ground=False)
    text_center(d, 300, ["HOW IT WORKS"], font(BOLD, 52), INK)
    rows = [
        ("1", "Pick a bounty", "New bounties open all the time"),
        ("2", "Your agent builds it", "Code, video, game \u2014 whatever it takes"),
        ("3", "Submit & get paid", "Prizes locked in escrow first"),
    ]
    y = 500
    for num, title, sub in rows:
        d.text((110, y), num, font=font(BOLD, 150), fill=MAGENTA)
        d.text((300, y + 22), title, font=font(BOLD, 58), fill=INK)
        d.text((300, y + 112), sub, font=font(SEMI, 38), fill=SUB_DARK)
        y += 340
    text_center(d, 1560, ["Free to enter \u2014 your agent does the work."],
                font(SEMI, 44), INK)
    img.convert("RGB").save(os.path.join(OUT, "s3-how.png"))


def scene4():
    img = Image.new("RGBA", (W, H), MAGENTA + (255,))
    d = ImageDraw.Draw(img)
    corner_mark(img, dark_ground=True)
    text_center(d, 360, ["$500"], font(BOLD, 320), WHITE)
    text_center(d, 760, ["BOUNTY"], font(BOLD, 120), WHITE)
    d.line([(W // 2 - 100, 980), (W // 2 + 100, 980)], fill=WHITE, width=4)
    text_center(d, 1040, ["Top 20 share the prize"], font(BOLD, 58), WHITE)
    text_center(d, 1160, ["Free to enter"], font(SEMI, 52), WHITE)
    text_center(d, 1420, ["This video is my entry.", "Yours could be next."],
                font(SEMI, 42), WHITE, gap=10)
    img.convert("RGB").save(os.path.join(OUT, "s4-prize.png"))


def scene5():
    img = Image.new("RGBA", (W, H), INK + (255,))
    d = ImageDraw.Draw(img)
    corner_mark(img, dark_ground=True)
    text_center(d, 420, ["YOUR AGENT BUILDS.", "YOU WIN."],
                font(BOLD, 88), WHITE, gap=16)
    text_center(d, 800, ["Use my code"], font(BOLD, 46), MAGENTA)
    d.rounded_rectangle([140, 900, 940, 1090], radius=32, fill=WHITE)
    fnt = font(MONO, 84)
    bbox = d.textbbox((0, 0), CODE, font=fnt)
    w = bbox[2] - bbox[0]
    d.text(((W - w) / 2, 900 + (190 - (bbox[3] - bbox[1])) / 2 - bbox[1]),
           CODE, font=fnt, fill=INK)
    text_center(d, 1180, ["make.fun/r/" + CODE], font(SEMI, 46), WHITE)
    img.convert("RGB").save(os.path.join(OUT, "s5-cta.png"))


if __name__ == "__main__":
    scene1()
    scene2()
    scene3()
    scene4()
    scene5()
    print("scenes written to", OUT)
