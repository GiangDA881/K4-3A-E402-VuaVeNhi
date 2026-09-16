import sys
import time
import subprocess
from pathlib import Path
from playwright.sync_api import sync_playwright

# Fix Windows console UTF-8 printing
if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass

def record_demo():
    workspace = Path(__file__).resolve().parent.parent
    index_html = (workspace / "codebase" / "index.html").resolve()
    recordings_dir = (workspace / "recordings").resolve()
    recordings_dir.mkdir(parents=True, exist_ok=True)

    file_url = f"file:///{index_html.as_posix()}"
    print(f"Recording detailed demo from: {file_url}")

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

        # Inject visible cursor for demo video
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

        def smooth_click(selector, wait_after=2.5):
            elem = page.wait_for_selector(selector)
            elem.scroll_into_view_if_needed()
            time.sleep(0.3)
            box = elem.bounding_box()
            if box:
                tx = box["x"] + box["width"] / 2
                ty = box["y"] + box["height"] / 2
                page.mouse.move(tx, ty, steps=18)
                time.sleep(0.4)
                page.mouse.down()
                time.sleep(0.15)
                page.mouse.up()
                time.sleep(wait_after)

        time.sleep(2.5)

        # -------------------------------------------------------------
        # 1. Kịch bản 1: HAPPY PATH (FOUND)
        # -------------------------------------------------------------
        print("Step 1: Demo Happy Path (ReAct & Tool Calling)")
        smooth_click("button[data-example='ReAct suy nghĩ rồi gọi tool']", wait_after=2.0)
        smooth_click("button[type='submit']", wait_after=3.5)

        # Đọc kết quả cards
        print("Step 2: Read source card and open modal")
        smooth_click("#cards article:first-child button", wait_after=4.0)

        # Xác nhận đúng phần mình cần
        print("Step 3: Confirm source (Success state)")
        smooth_click("#confirmSource", wait_after=3.5)

        # Reset tác vụ
        smooth_click("#restart", wait_after=2.0)

        # -------------------------------------------------------------
        # 2. Kịch bản 2: CLARIFY (Làm rõ câu hỏi mơ hồ)
        # -------------------------------------------------------------
        print("Step 4: Demo Clarify Path (Context carry-over vs Window)")
        smooth_click("button[data-example='Đoạn về context mình không nhớ rõ']", wait_after=2.0)
        smooth_click("button[type='submit']", wait_after=3.5)

        # Chọn chủ đề 1 trong bảng hỏi Clarify
        print("Step 5: Pick specific topic from Clarify options")
        smooth_click("button[data-topic='carry']", wait_after=3.5)

        # Mở xem nguồn và thử nút 'Chưa đúng, sửa câu hỏi' (User Repair)
        print("Step 6: Open source and test user repair flow")
        smooth_click("#cards article:first-child button", wait_after=3.5)
        smooth_click("#wrongSource", wait_after=2.5)

        # -------------------------------------------------------------
        # 3. Kịch bản 3: XEM SƠ ĐỒ LUỒNG (Flowchart)
        # -------------------------------------------------------------
        print("Step 7: View interactive flowchart dialog")
        smooth_click("#flowButton", wait_after=5.0)
        smooth_click("#closeFlow", wait_after=2.0)

        # -------------------------------------------------------------
        # 4. Kịch bản 4: NOT_FOUND (Nội dung ngoài bài học)
        # -------------------------------------------------------------
        print("Step 8: Demo Out-of-Scope Path (NOT_FOUND)")
        smooth_click("button[data-example='Dự báo giá Bitcoin tuần tới']", wait_after=2.0)
        smooth_click("button[type='submit']", wait_after=4.5)

        print("Finished detailed scenario, closing context...")
        context.close()
        video_path = page.video.path()
        browser.close()

    print(f"Raw video saved at: {video_path}")
    raw_file = Path(video_path)
    mp4_target = recordings_dir / "cp2_mockup_demo.mp4"

    ffmpeg_cmd = "ffmpeg"
    try:
        subprocess.run([
            ffmpeg_cmd, "-y", "-i", str(raw_file),
            "-c:v", "libx264", "-pix_fmt", "yuv420p", "-r", "30",
            str(mp4_target)
        ], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        print(f"Successfully converted detailed video to MP4: {mp4_target}")
    except Exception as e:
        print(f"FFmpeg error: {e}")

if __name__ == "__main__":
    record_demo()
