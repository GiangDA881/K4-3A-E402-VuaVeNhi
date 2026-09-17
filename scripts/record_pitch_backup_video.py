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

def run_pitch_backup_recording():
    workspace = Path(__file__).resolve().parent.parent
    recordings_dir = workspace / "recordings"
    recordings_dir.mkdir(parents=True, exist_ok=True)

    print("=" * 60)
    print("STARTING CP5 PITCH BACKUP VIDEO RECORDING (1080p)")
    print("=" * 60)

    print("1. Launching FastAPI backend server on http://127.0.0.1:8000...")
    server_process = subprocess.Popen(
        [sys.executable, "-m", "uvicorn", "codebase.server:app", "--host", "127.0.0.1", "--port", "8000"],
        cwd=str(workspace),
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE
    )

    # Wait for server to initialize
    time.sleep(3)

    target_url = "http://127.0.0.1:8000"
    print(f"2. Connecting Playwright to: {target_url}")

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context(
            record_video_dir=str(recordings_dir),
            record_video_size={"width": 1920, "height": 1080},
            viewport={"width": 1920, "height": 1080},
        )
        page = context.new_page()
        page.goto(target_url)
        page.wait_for_load_state("networkidle")

        # Inject styling tweaks for high-res 1080p presentation display + visible mouse cursor
        page.evaluate("""
        () => {
            // Visible cursor
            const cursor = document.createElement('div');
            cursor.id = 'visual-cursor';
            cursor.style.cssText = 'position:fixed;width:24px;height:24px;border-radius:50%;background:rgba(220,38,38,0.88);border:2.5px solid #ffffff;pointer-events:none;z-index:999999;transform:translate(-50%,-50%);transition:transform 0.08s ease, background 0.15s;box-shadow:0 3px 12px rgba(0,0,0,0.35);left:-100px;top:-100px;';
            document.body.appendChild(cursor);
            window.addEventListener('mousemove', e => {
                cursor.style.left = e.clientX + 'px';
                cursor.style.top = e.clientY + 'px';
            });
            window.addEventListener('mousedown', () => {
                cursor.style.transform = 'translate(-50%,-50%) scale(0.7)';
                cursor.style.background = 'rgba(234,179,8,0.95)';
            });
            window.addEventListener('mouseup', () => {
                cursor.style.transform = 'translate(-50%,-50%) scale(1)';
                cursor.style.background = 'rgba(220,38,38,0.88)';
            });

            // Add Pitch Tag
            const headerRow = document.querySelector('header .row');
            if (headerRow) {
                const pitchBadge = document.createElement('span');
                pitchBadge.className = 'tag';
                pitchBadge.style.cssText = 'background:#ecfdf5;color:#059669;font-weight:700;border:1px solid #10b981;padding:6px 14px;border-radius:20px;';
                pitchBadge.textContent = 'CP5 · PITCH DEMO (LIVE AI BACKEND)';
                headerRow.prepend(pitchBadge);
            }
        }
        """)

        def smooth_move_to(selector, steps=20):
            elem = page.wait_for_selector(selector)
            elem.scroll_into_view_if_needed()
            time.sleep(0.2)
            box = elem.bounding_box()
            if box:
                tx = box["x"] + box["width"] / 2
                ty = box["y"] + box["height"] / 2
                page.mouse.move(tx, ty, steps=steps)
                time.sleep(0.3)
                return tx, ty
            return None, None

        def smooth_click(selector, wait_after=1.5):
            tx, ty = smooth_move_to(selector)
            if tx is not None:
                page.mouse.down()
                time.sleep(0.12)
                page.mouse.up()
                time.sleep(wait_after)

        def type_text(selector, text, delay=35):
            smooth_click(selector, wait_after=0.5)
            page.fill(selector, "")
            time.sleep(0.3)
            for char in text:
                page.type(selector, char, delay=delay)
            time.sleep(0.8)

        # Overview pause
        time.sleep(2.5)

        # =============================================================
        # SCENE 1: HAPPY PATH (Mô tả trí nhớ mơ hồ về ReAct)
        # =============================================================
        print("[Pitch Scene 1] User asks vague question about ReAct loop...")
        type_text("#query", "cái bài hôm nọ thầy dạy ReAct loop với thought action ấy nằm ở đâu nhỉ", delay=30)
        time.sleep(1.0)
        
        print("[Pitch Scene 1] Submitting to AI...")
        smooth_click("button[type='submit']", wait_after=1.0)

        # Chờ AI trả về
        page.wait_for_selector("#aiRationale", timeout=15000)
        time.sleep(4.0)

        # Mở xem chi tiết nguồn
        print("[Pitch Scene 1] Inspecting verified source...")
        smooth_click("#cards article:first-child button", wait_after=3.5)

        # Xác nhận đúng bài cần ôn
        print("[Pitch Scene 1] Confirming source...")
        smooth_click("#confirmSource", wait_after=2.5)

        # Reset tìm nội dung khác
        smooth_click("#restart", wait_after=1.5)

        # =============================================================
        # SCENE 2: AMBIGUOUS QUERY (Hỏi mơ hồ từ khóa Context -> CLARIFY)
        # =============================================================
        print("[Pitch Scene 2] User inputs ambiguous keyword 'context'...")
        type_text("#query", "Đoạn về context mình không nhớ rõ", delay=35)
        time.sleep(0.8)
        smooth_click("button[type='submit']", wait_after=1.0)

        # Chờ trạng thái CLARIFY
        print("[Pitch Scene 2] AI detects ambiguity and triggers CLARIFY...")
        page.wait_for_selector("#clarifyButtons button", timeout=15000)
        time.sleep(4.0)

        # Chọn option 'Giữ ngữ cảnh qua nhiều lượt'
        print("[Pitch Scene 2] User chooses specific topic...")
        smooth_click("#clarifyButtons button:first-child", wait_after=1.0)

        # Chờ kết quả sau khi clarify
        page.wait_for_selector("#aiRationale", timeout=15000)
        time.sleep(3.5)

        # Mở xem nguồn mốc video transcript
        smooth_click("#cards article:first-child button", wait_after=3.0)
        smooth_click("#closeSource", wait_after=1.5)

        # =============================================================
        # SCENE 3: RED-TEAM / OUT-OF-SCOPE (Kiểm soát ảo giác -> NOT_FOUND)
        # =============================================================
        print("[Pitch Scene 3] Red-teaming out-of-scope query...")
        smooth_click("#editQuery", wait_after=1.0)
        type_text("#query", "Dự báo giá Bitcoin tuần tới và phân tích kỹ thuật", delay=30)
        time.sleep(0.8)
        smooth_click("button[type='submit']", wait_after=1.0)

        # Chờ trạng thái NOT_FOUND
        print("[Pitch Scene 3] AI guardrail safe refusal activated...")
        page.wait_for_selector("#notfoundReason", timeout=15000)
        time.sleep(4.0)

        # Quay lại luồng chính
        print("[Pitch Scene 3] Seamless fallback back to learning flow...")
        smooth_click("#tryReact", wait_after=1.0)
        page.wait_for_selector("#aiRationale", timeout=15000)
        time.sleep(3.5)

        print("[Pitch Demo] Recording completed successfully!")
        context.close()
        video_path = page.video.path()
        browser.close()

    # Dừng backend server
    server_process.terminate()
    try:
        server_process.wait(timeout=3)
    except Exception:
        server_process.kill()

    print(f"Raw video saved at: {video_path}")
    raw_file = Path(video_path)
    mp4_target = recordings_dir / "demo_backup_pitch.mp4"

    print(f"Converting with FFmpeg to 1080p MP4: {mp4_target}")
    try:
        subprocess.run([
            "ffmpeg", "-y", "-i", str(raw_file),
            "-c:v", "libx264", "-pix_fmt", "yuv420p", "-r", "30",
            str(mp4_target)
        ], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        print(f"SUCCESS: Created pitch backup demo video: {mp4_target}")
    except Exception as e:
        print(f"FFmpeg error: {e}")

if __name__ == "__main__":
    run_pitch_backup_recording()
