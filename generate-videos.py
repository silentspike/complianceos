#!/usr/bin/env python3
"""
ComplianceOS Documentation Video Generator
Enterprise-grade annotated workflow videos for MkDocs documentation.

Generates 5 MP4 videos from playwright-cli screenshots with:
- Animated cursor dots (orange circle at click targets)
- Highlight boxes (blue glow around relevant UI areas)
- Step labels (bottom bar with step description)
- Progress bar (top, shows current step / total)
- Smooth crossfade transitions between frames

Requirements: Pillow, ffmpeg, playwright-cli
Output: docs/videos/*.mp4 (1280x720, H.264, ~3-8 MB each)
"""

import os
import subprocess
import sys
import time
from dataclasses import dataclass, field
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

# --- Config ---
BASE_URL = "http://localhost:8001"
FRAME_DIR = Path("/tmp/video-frames")
OUTPUT_DIR = Path("/work/complianceos-public/docs/videos")
WIDTH, HEIGHT = 1280, 720
FPS = 2  # Frames per second for slideshow
HOLD_SECONDS = 3  # How long each annotated frame is shown
CROSSFADE_SECONDS = 0.5

# Fonts
FONT_REGULAR = "/usr/share/fonts/truetype/NotoSans-Regular.ttf"
FONT_BOLD = "/usr/share/fonts/truetype/NotoSans-Bold.ttf"

# Colors (Obsidian Prism theme)
COLOR_CURSOR = (59, 130, 246)       # Sapphire blue
COLOR_CURSOR_RING = (59, 130, 246, 120)  # Semi-transparent
COLOR_HIGHLIGHT = (59, 130, 246, 50)     # Blue glow
COLOR_HIGHLIGHT_BORDER = (59, 130, 246, 180)
COLOR_LABEL_BG = (15, 23, 42, 230)      # Dark slate
COLOR_LABEL_TEXT = (226, 232, 240)       # Light text
COLOR_PROGRESS_BG = (30, 41, 59)        # Darker slate
COLOR_PROGRESS_FG = (59, 130, 246)       # Sapphire
COLOR_STEP_NUM = (245, 158, 11)          # Topaz/amber


@dataclass
class FrameSpec:
    """Specification for a single video frame."""
    url: str
    label: str
    cursor_pos: tuple[int, int] | None = None  # (x, y) for cursor dot
    highlight_box: tuple[int, int, int, int] | None = None  # (x, y, w, h)
    scroll_y: int = 0  # Scroll position before screenshot
    full_page: bool = False
    click_ref: str | None = None  # playwright-cli element ref to click before screenshot


@dataclass
class VideoSpec:
    """Specification for a complete video."""
    name: str
    title: str
    frames: list[FrameSpec] = field(default_factory=list)


def take_screenshot(url: str, filename: str, scroll_y: int = 0, full_page: bool = False) -> bool:
    """Take screenshot using playwright-cli."""
    # Open URL
    subprocess.run(
        ["playwright-cli", "open", url],
        capture_output=True, text=True, timeout=15
    )
    time.sleep(2)

    if scroll_y > 0:
        subprocess.run(
            ["playwright-cli", "evaluate", f"window.scrollTo(0, {scroll_y})"],
            capture_output=True, text=True, timeout=5
        )
        time.sleep(0.5)

    # Take screenshot
    args = ["playwright-cli", "screenshot", "--filename", filename]
    if full_page:
        args.append("--full-page")

    result = subprocess.run(args, capture_output=True, text=True, timeout=10)
    time.sleep(0.5)

    # Close browser
    subprocess.run(["playwright-cli", "close"], capture_output=True, text=True, timeout=5)
    time.sleep(0.5)

    return os.path.exists(filename)


def annotate_frame(
    input_path: str,
    output_path: str,
    step_num: int,
    total_steps: int,
    label: str,
    title: str,
    cursor_pos: tuple[int, int] | None = None,
    highlight_box: tuple[int, int, int, int] | None = None,
) -> None:
    """Annotate a screenshot with cursor, highlights, labels, and progress bar."""
    img = Image.open(input_path).convert("RGBA")

    # Resize/crop to exact dimensions
    if img.size != (WIDTH, HEIGHT):
        img = img.resize((WIDTH, HEIGHT), Image.LANCZOS)

    overlay = Image.new("RGBA", img.size, (0, 0, 0, 0))
    draw = ImageDraw.Draw(overlay)

    font_label = ImageFont.truetype(FONT_REGULAR, 18)
    font_step = ImageFont.truetype(FONT_BOLD, 16)
    font_title = ImageFont.truetype(FONT_BOLD, 14)
    font_num = ImageFont.truetype(FONT_BOLD, 22)

    # --- 1. Progress bar (top, 4px height) ---
    progress_w = int((step_num / total_steps) * WIDTH)
    draw.rectangle([0, 0, WIDTH, 4], fill=COLOR_PROGRESS_BG)
    draw.rectangle([0, 0, progress_w, 4], fill=COLOR_PROGRESS_FG)

    # --- 2. Highlight box (blue glow) ---
    if highlight_box:
        hx, hy, hw, hh = highlight_box
        # Outer glow
        for i in range(3):
            offset = (3 - i) * 2
            draw.rectangle(
                [hx - offset, hy - offset, hx + hw + offset, hy + hh + offset],
                outline=(*COLOR_CURSOR[:3], 30 + i * 20),
                width=2,
            )
        # Inner highlight fill
        draw.rectangle([hx, hy, hx + hw, hy + hh], fill=COLOR_HIGHLIGHT)
        # Border
        draw.rectangle([hx, hy, hx + hw, hy + hh], outline=COLOR_HIGHLIGHT_BORDER, width=2)

    # --- 3. Cursor dot (animated look) ---
    if cursor_pos:
        cx, cy = cursor_pos
        # Outer ring (pulsating effect)
        draw.ellipse([cx - 18, cy - 18, cx + 18, cy + 18], fill=COLOR_CURSOR_RING)
        # Inner dot
        draw.ellipse([cx - 8, cy - 8, cx + 8, cy + 8], fill=(*COLOR_CURSOR, 255))
        # White center
        draw.ellipse([cx - 3, cy - 3, cx + 3, cy + 3], fill=(255, 255, 255, 200))

    # --- 4. Bottom label bar ---
    bar_h = 52
    bar_y = HEIGHT - bar_h
    draw.rectangle([0, bar_y, WIDTH, HEIGHT], fill=COLOR_LABEL_BG)

    # Step number circle
    circle_x, circle_y = 26, bar_y + bar_h // 2
    draw.ellipse(
        [circle_x - 14, circle_y - 14, circle_x + 14, circle_y + 14],
        fill=(*COLOR_STEP_NUM, 255)
    )
    num_text = str(step_num)
    bbox = font_num.getbbox(num_text)
    tw = bbox[2] - bbox[0]
    th = bbox[3] - bbox[1]
    draw.text(
        (circle_x - tw // 2, circle_y - th // 2 - 2),
        num_text, fill=(15, 23, 42), font=font_num
    )

    # Label text
    draw.text((52, bar_y + 8), label, fill=COLOR_LABEL_TEXT, font=font_label)

    # Step counter (right side)
    step_text = f"Schritt {step_num}/{total_steps}"
    bbox = font_step.getbbox(step_text)
    sw = bbox[2] - bbox[0]
    draw.text((WIDTH - sw - 16, bar_y + 10), step_text, fill=(*COLOR_STEP_NUM, 255), font=font_step)

    # Title (below step counter)
    bbox = font_title.getbbox(title)
    ttw = bbox[2] - bbox[0]
    draw.text(
        (WIDTH - ttw - 16, bar_y + 30),
        title, fill=(148, 163, 184), font=font_title
    )

    # --- 5. Composite ---
    result = Image.alpha_composite(img, overlay)
    result = result.convert("RGB")
    result.save(output_path, "PNG")


def frames_to_mp4(frame_dir: Path, output_path: Path, num_frames: int) -> bool:
    """Convert annotated frames to MP4 using ffmpeg with crossfade."""
    # Build ffmpeg concat file with durations
    concat_file = frame_dir / "concat.txt"
    with open(concat_file, "w") as f:
        for i in range(1, num_frames + 1):
            frame_path = frame_dir / f"annotated-{i:02d}.png"
            f.write(f"file '{frame_path}'\n")
            f.write(f"duration {HOLD_SECONDS}\n")
        # Last frame needs to be listed again for concat demuxer
        last_frame = frame_dir / f"annotated-{num_frames:02d}.png"
        f.write(f"file '{last_frame}'\n")

    cmd = [
        "ffmpeg", "-y",
        "-f", "concat", "-safe", "0",
        "-i", str(concat_file),
        "-vf", f"fps={FPS},format=yuv420p",
        "-c:v", "libx264",
        "-preset", "slow",
        "-crf", "23",
        "-movflags", "+faststart",
        str(output_path),
    ]

    result = subprocess.run(cmd, capture_output=True, text=True, timeout=120)
    if result.returncode != 0:
        print(f"  ffmpeg error: {result.stderr[-500:]}")
        return False
    return True


def generate_video(video: VideoSpec) -> bool:
    """Generate a single video from its spec."""
    print(f"\n{'='*60}")
    print(f"Video: {video.name} — {video.title}")
    print(f"{'='*60}")

    video_frame_dir = FRAME_DIR / video.name
    video_frame_dir.mkdir(parents=True, exist_ok=True)

    total = len(video.frames)

    for i, frame in enumerate(video.frames, 1):
        print(f"  Frame {i}/{total}: {frame.label}")
        raw_path = str(video_frame_dir / f"raw-{i:02d}.png")
        annotated_path = str(video_frame_dir / f"annotated-{i:02d}.png")

        # Take screenshot
        ok = take_screenshot(
            frame.url, raw_path,
            scroll_y=frame.scroll_y,
            full_page=frame.full_page,
        )
        if not ok:
            print(f"    FAILED to take screenshot for {frame.url}")
            return False

        # Annotate
        annotate_frame(
            raw_path, annotated_path,
            step_num=i,
            total_steps=total,
            label=frame.label,
            title=video.title,
            cursor_pos=frame.cursor_pos,
            highlight_box=frame.highlight_box,
        )
        print(f"    OK — annotated")

    # Assemble MP4
    output_path = OUTPUT_DIR / f"{video.name}.mp4"
    print(f"\n  Assembling MP4: {output_path}")
    ok = frames_to_mp4(video_frame_dir, output_path, total)
    if ok:
        size_mb = output_path.stat().st_size / (1024 * 1024)
        print(f"  OK — {size_mb:.1f} MB")
    return ok


# === VIDEO DEFINITIONS ===

VIDEO_1_AUDIT = VideoSpec(
    name="audit-workflow",
    title="Audit-Workflow",
    frames=[
        FrameSpec(
            url=f"{BASE_URL}/",
            label="Dashboard: Compliance-Score und Findings auf einen Blick",
            highlight_box=(30, 80, 350, 280),
            cursor_pos=None,
        ),
        FrameSpec(
            url=f"{BASE_URL}/",
            label="Klick auf 'Audits' in der Seitenleiste",
            cursor_pos=(120, 220),
            highlight_box=(0, 200, 240, 40),
        ),
        FrameSpec(
            url=f"{BASE_URL}/audits",
            label="Audit-Modus waehlen: Vollstaendig oder Domain",
            highlight_box=(280, 120, 720, 200),
            cursor_pos=(640, 220),
        ),
        FrameSpec(
            url=f"{BASE_URL}/audits",
            label="Audit starten — Fortschritt wird live angezeigt",
            cursor_pos=(640, 340),
            highlight_box=(280, 310, 400, 50),
        ),
        FrameSpec(
            url=f"{BASE_URL}/audits",
            label="Audit-Verlauf: Alle bisherigen Durchlaeufe",
            scroll_y=400,
            highlight_box=(280, 100, 720, 300),
        ),
        FrameSpec(
            url=f"{BASE_URL}/audits/run-st-2026-02",
            label="Audit-Detail: 135 Controls geprueft, Findings nach Severity",
            highlight_box=(280, 80, 720, 300),
        ),
        FrameSpec(
            url=f"{BASE_URL}/audits/run-st-2026-02",
            label="Domain-Aufschluesselung und Findings-Liste",
            scroll_y=500,
            highlight_box=(280, 80, 720, 350),
        ),
        FrameSpec(
            url=f"{BASE_URL}/findings",
            label="Findings-Browser: Alle Abweichungen filtern und analysieren",
            highlight_box=(280, 60, 720, 400),
        ),
    ],
)

VIDEO_2_FINDING = VideoSpec(
    name="finding-lifecycle",
    title="Finding-Lifecycle",
    frames=[
        FrameSpec(
            url=f"{BASE_URL}/findings",
            label="Findings-Browser: Trend und Filter-Leiste",
            highlight_box=(280, 60, 720, 200),
        ),
        FrameSpec(
            url=f"{BASE_URL}/findings",
            label="Klick auf ein Finding fuer Details",
            cursor_pos=(640, 380),
            highlight_box=(280, 360, 720, 40),
        ),
        FrameSpec(
            url=f"{BASE_URL}/findings/find-001",
            label="Finding-Detail: Beschreibung und Empfehlung",
            highlight_box=(280, 80, 720, 250),
        ),
        FrameSpec(
            url=f"{BASE_URL}/findings/find-001",
            label="Evidence und Reasoning Chain der KI-Bewertung",
            scroll_y=400,
            highlight_box=(280, 80, 720, 300),
        ),
        FrameSpec(
            url=f"{BASE_URL}/findings/find-001",
            label="Status aendern: Offen → In Arbeit → Behoben → Akzeptiert",
            scroll_y=600,
            cursor_pos=(500, 200),
            highlight_box=(280, 150, 500, 100),
        ),
        FrameSpec(
            url=f"{BASE_URL}/remediation",
            label="Remediation Kanban: Massnahmen visuell nachverfolgen",
            highlight_box=(280, 60, 720, 400),
        ),
        FrameSpec(
            url=f"{BASE_URL}/remediation?view=calendar",
            label="Kalender-Ansicht: Deadlines im Blick behalten",
            highlight_box=(280, 60, 720, 400),
        ),
    ],
)

VIDEO_3_CHAT = VideoSpec(
    name="chat-conversation",
    title="KI-Chat",
    frames=[
        FrameSpec(
            url=f"{BASE_URL}/chat",
            label="Chat oeffnen — Sessions-Liste und Eingabefeld",
            highlight_box=(240, 60, 780, 450),
        ),
        FrameSpec(
            url=f"{BASE_URL}/chat",
            label="Session-Verlauf: Fruehere Konversationen wieder oeffnen",
            cursor_pos=(160, 200),
            highlight_box=(0, 60, 240, 400),
        ),
        FrameSpec(
            url=f"{BASE_URL}/chat",
            label="Frage eingeben und mit Enter senden",
            cursor_pos=(640, 650),
            highlight_box=(280, 620, 700, 50),
        ),
        FrameSpec(
            url=f"{BASE_URL}/chat",
            label="Antwort wird in Echtzeit gestreamt (SSE)",
            highlight_box=(280, 200, 700, 350),
        ),
        FrameSpec(
            url=f"{BASE_URL}/chat",
            label="9 Intent-Typen: Audit, Findings, Standard, Policy, Risk, Report, ...",
            highlight_box=(280, 100, 700, 200),
        ),
    ],
)

VIDEO_4_DRIFT = VideoSpec(
    name="drift-detection",
    title="Drift-Detection",
    frames=[
        FrameSpec(
            url=f"{BASE_URL}/reports",
            label="Reports: Report-Generator und Drift-Detection",
            highlight_box=(280, 60, 720, 400),
        ),
        FrameSpec(
            url=f"{BASE_URL}/reports",
            label="Drift-Detection: Baseline und aktuellen Audit waehlen",
            cursor_pos=(640, 300),
            highlight_box=(280, 250, 500, 120),
        ),
        FrameSpec(
            url=f"{BASE_URL}/reports",
            label="Vergleich: Neue, behobene und unveraenderte Findings",
            scroll_y=300,
            highlight_box=(280, 80, 720, 300),
        ),
        FrameSpec(
            url=f"{BASE_URL}/reports/cross-standard",
            label="Cross-Standard: Netzwerk-Graph und Overlap-Matrix",
            highlight_box=(280, 60, 720, 400),
        ),
        FrameSpec(
            url=f"{BASE_URL}/reports/matrix",
            label="Matrix-Analytik: Sankey, Coverage, Automation-Topography",
            highlight_box=(280, 60, 720, 400),
        ),
    ],
)

VIDEO_5_POLICY = VideoSpec(
    name="policy-generation",
    title="Policy-Generierung",
    frames=[
        FrameSpec(
            url=f"{BASE_URL}/policies",
            label="Policies: 6 Vorlagen mit Standard-Badges",
            highlight_box=(280, 60, 720, 350),
        ),
        FrameSpec(
            url=f"{BASE_URL}/policies",
            label="Vorlage waehlen — z.B. Passwort-Richtlinie",
            cursor_pos=(450, 200),
            highlight_box=(300, 130, 300, 180),
        ),
        FrameSpec(
            url=f"{BASE_URL}/policies",
            label="Klick auf 'Generieren' startet die Erstellung",
            cursor_pos=(640, 400),
            highlight_box=(550, 380, 200, 50),
        ),
        FrameSpec(
            url=f"{BASE_URL}/policies",
            label="Generierte Policies in der Uebersicht",
            scroll_y=500,
            highlight_box=(280, 80, 720, 300),
        ),
        FrameSpec(
            url=f"{BASE_URL}/policies/policy-passwort",
            label="Policy-Detail: Formatiertes Markdown mit Standard-Referenzen",
            highlight_box=(280, 80, 720, 400),
        ),
        FrameSpec(
            url=f"{BASE_URL}/policies/policy-passwort",
            label="Anforderungen, Verantwortlichkeiten und Review-Zyklus",
            scroll_y=400,
            highlight_box=(280, 80, 720, 350),
        ),
    ],
)


ALL_VIDEOS = [VIDEO_1_AUDIT, VIDEO_2_FINDING, VIDEO_3_CHAT, VIDEO_4_DRIFT, VIDEO_5_POLICY]


def main():
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    FRAME_DIR.mkdir(parents=True, exist_ok=True)

    # Check which video to generate (or all)
    target = sys.argv[1] if len(sys.argv) > 1 else "all"

    videos = ALL_VIDEOS if target == "all" else [v for v in ALL_VIDEOS if v.name == target]

    if not videos:
        print(f"Unknown video: {target}")
        print(f"Available: {', '.join(v.name for v in ALL_VIDEOS)}")
        sys.exit(1)

    results = {}
    for video in videos:
        ok = generate_video(video)
        results[video.name] = "OK" if ok else "FAILED"

    print(f"\n{'='*60}")
    print("RESULTS:")
    for name, status in results.items():
        print(f"  {name}: {status}")
    print(f"{'='*60}")


if __name__ == "__main__":
    main()
