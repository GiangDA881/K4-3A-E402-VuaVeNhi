import os
import time
import subprocess
from pathlib import Path
from playwright.sync_api import sync_playwright

def record_demo():
    workspace = Path(__file__).resolve().parent.parent
    index_html = (workspace / "codebase" / "index.html").resolve()
    recordings_dir = (workspace / "recordings").resolve()
    recordings_dir.mkdir(parents=True, exist_ok=True)

    file_url = f"file:///{index_html.as_posix()}"
    print(f"Recording demo from: {file_url}")

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context(
            record_video_dir=str(recordings_dir),
            record_video_size={"width": 1280, "height": 720},
            viewport={"width": 1280, "height": 720},
        )
        page = context.new_page()
        page.goto(file_url)
        page.wait_for_load_state("networkidle")
        time.sleep(2)

        # 1. Kịch bản 1: FOUND (ReAct & Gọi tool)
        print("Step 1: Test ReAct (FOUND flow)")
        page.click("button[data-example='ReAct suy nghĩ rồi gọi tool']")
        time.sleep(1.5)
        page.click("button[type='submit']")
        time.sleep(2.5)

        # Mở modal xem nguồn
        print("Step 2: Open source details modal")
        source_buttons = page.query_selector_all("#cards button")
        if source_buttons:
            source_buttons[0].click()
            time.sleep(2.5)
            # Xác nhận đúng phần cần ôn
            page.click("#confirmSource")
            time.sleep(2.5)

        # Reset tìm nội dung khác
        print("Step 3: Reset and try Context (CLARIFY flow)")
        page.click("#restart")
        time.sleep(1.5)

        # 2. Kịch bản 2: CLARIFY (Mình nhớ về context...)
        page.click("button[data-example='Đoạn về context mình không nhớ rõ']")
        time.sleep(1.5)
        page.click("button[type='submit']")
        time.sleep(2.5)

        # Chọn chủ đề 1 trong CLARIFY
        print("Step 4: Select topic in Clarify")
        choice_buttons = page.query_selector_all("button[data-topic]")
        if choice_buttons:
            choice_buttons[0].click()
            time.sleep(2.5)

        # 3. Kịch bản 3: Sơ đồ luồng (Xem luồng)
        print("Step 5: View flowchart dialog")
        page.click("#flowButton")
        time.sleep(3.5)
        page.click("#closeFlow")
        time.sleep(1.5)

        # 4. Kịch bản 4: NOT_FOUND (Nội dung ngoài bài học)
        print("Step 6: Test Out-of-Scope (NOT_FOUND flow)")
        page.click("button[data-example='Dự báo giá Bitcoin tuần tới']")
        time.sleep(1.5)
        page.click("button[type='submit']")
        time.sleep(3)

        print("Finished scenario, closing context to finalize video...")
        context.close()
        video_path = page.video.path()
        browser.close()

    print(f"Raw video saved at: {video_path}")
    raw_file = Path(video_path)
    mp4_target = recordings_dir / "cp2_mockup_demo.mp4"

    # Convert to MP4 using ffmpeg if available
    ffmpeg_cmd = "ffmpeg"
    try:
        subprocess.run([
            ffmpeg_cmd, "-y", "-i", str(raw_file),
            "-c:v", "libx264", "-pix_fmt", "yuv420p", "-r", "30",
            str(mp4_target)
        ], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        print(f"Successfully converted to MP4: {mp4_target}")
    except Exception as e:
        print(f"FFmpeg conversion notice: {e}, using original video: {raw_file}")

if __name__ == "__main__":
    record_demo()
