import os
import sys
import time
import subprocess
from pathlib import Path
from playwright.sync_api import sync_playwright

# Fix Windows console UTF-8
if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass

def run_live_recording():
    workspace = Path(__file__).resolve().parent.parent
    recordings_dir = workspace / "recordings"
    recordings_dir.mkdir(parents=True, exist_ok=True)

    print("Starting FastAPI backend server on http://127.0.0.1:8000...")
    server_process = subprocess.Popen(
        [sys.executable, "-m", "uvicorn", "codebase.server:app", "--host", "127.0.0.1", "--port", "8000"],
        cwd=str(workspace),
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE
    )

    # Wait for server to start
    time.sleep(3)

    target_url = "http://127.0.0.1:8000"
    print(f"Connecting to live app: {target_url}")

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context(
            record_video_dir=str(recordings_dir),
            record_video_size={"width": 1280, "height": 720},
            viewport={"width": 1280, "height": 720},
        )
        page = context.new_page()
        page.goto(target_url)
        page.wait_for_load_state("networkidle")

        # Inject visible cursor
        page.evaluate("""
        () => {
            const cursor = document.createElement('div');
            cursor.id = 'visual-cursor';
            cursor.style.cssText = 'position:fixed;width:18px;height:18px;border-radius:50%;background:rgba(220,38,38,0.85);border:2px solid #ffffff;pointer-events:none;z-index:999999;transform:translate(-50%,-50%);transition:transform 0.08s ease, background 0.15s;box-shadow:0 2px 8px rgba(0,0,0,0.35);left:-100px;top:-100px;';
            document.body.appendChild(cursor);
            window.addEventListener('mousemove', e => {
                cursor.style.left = e.clientX + 'px';
                cursor.style.top = e.clientY + 'px';
            });
            window.addEventListener('mousedown', () => {
                cursor.style.transform = 'translate(-50%,-50%) scale(0.65)';
                cursor.style.background = 'rgba(234,179,8,0.95)';
            });
            window.addEventListener('mouseup', () => {
                cursor.style.transform = 'translate(-50%,-50%) scale(1)';
                cursor.style.background = 'rgba(220,38,38,0.85)';
            });
        }
        """)

        def smooth_click(selector, wait_after=1.5):
            elem = page.wait_for_selector(selector)
            elem.scroll_into_view_if_needed()
            time.sleep(0.2)
            box = elem.bounding_box()
            if box:
                tx = box["x"] + box["width"] / 2
                ty = box["y"] + box["height"] / 2
                page.mouse.move(tx, ty, steps=15)
                time.sleep(0.3)
                page.mouse.down()
                time.sleep(0.1)
                page.mouse.up()
                time.sleep(wait_after)

        time.sleep(1.5)

        # -------------------------------------------------------------
        # 1. LIVE AI CALL: HAPPY PATH (ReAct)
        # -------------------------------------------------------------
        print("Step 1: User enters query for ReAct pattern")
        smooth_click("button[data-example='ReAct suy nghĩ rồi gọi tool']", wait_after=1.0)
        
        print("Step 2: Submitting query to live AI model...")
        smooth_click("button[type='submit']", wait_after=1.0)

        # Chờ AI trả về kết quả thật (hiện badge FOUND AI TRUY HỒI THỰC TẾ)
        print("Step 3: Waiting for live LLM inference and response...")
        page.wait_for_selector("#aiRationale", timeout=15000)
        time.sleep(4.0)

        # Mở xem chi tiết nguồn do AI trích dẫn
        print("Step 4: Opening verified source modal...")
        smooth_click("#cards article:first-child button", wait_after=3.5)

        # Xác nhận đúng phần cần ôn
        print("Step 5: Confirming source...")
        smooth_click("#confirmSource", wait_after=2.5)

        # Reset
        smooth_click("#restart", wait_after=1.5)

        # -------------------------------------------------------------
        # 2. LIVE AI CALL: CLARIFY PATH
        # -------------------------------------------------------------
        print("Step 6: Testing Ambiguous Query with live AI...")
        smooth_click("button[data-example='Đoạn về context mình không nhớ rõ']", wait_after=1.0)
        smooth_click("button[type='submit']", wait_after=1.0)

        # Chờ AI trả về CLARIFY
        page.wait_for_selector("#clarifyButtons button", timeout=15000)
        time.sleep(3.5)

        # Chọn option làm rõ
        print("Step 7: Selecting clarify option...")
        smooth_click("#clarifyButtons button:first-child", wait_after=1.0)
        page.wait_for_selector("#aiRationale", timeout=15000)
        time.sleep(3.0)

        print("Finished CP3 Live AI Demo recording!")
        context.close()
        video_path = page.video.path()
        browser.close()

    # Terminate server
    server_process.terminate()
    try:
        server_process.wait(timeout=3)
    except Exception:
        server_process.kill()

    print(f"Raw video saved at: {video_path}")
    raw_file = Path(video_path)
    mp4_target = recordings_dir / "cp3_ai_live_demo.mp4"

    ffmpeg_cmd = "ffmpeg"
    try:
        subprocess.run([
            ffmpeg_cmd, "-y", "-i", str(raw_file),
            "-c:v", "libx264", "-pix_fmt", "yuv420p", "-r", "30",
            str(mp4_target)
        ], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        print(f"Successfully converted CP3 live AI video to MP4: {mp4_target}")
    except Exception as e:
        print(f"FFmpeg notice: {e}")

if __name__ == "__main__":
    run_live_recording()
