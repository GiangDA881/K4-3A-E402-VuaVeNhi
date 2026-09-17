import os
import sys
from pathlib import Path
from playwright.sync_api import sync_playwright

def generate_pdf():
    workspace = Path(__file__).resolve().parent.parent
    output_pdf = workspace / "demo-slides.pdf"

    html_content = """<!DOCTYPE html>
<html lang="vi">
<head>
<meta charset="UTF-8">
<style>
  @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap');

  @page {
    size: 1920px 1080px;
    margin: 0;
  }
  * {
    box-sizing: border-box;
    margin: 0;
    padding: 0;
  }
  body {
    font-family: 'Plus Jakarta Sans', sans-serif;
    color: #0f172a;
    background: #ffffff;
    -webkit-print-color-adjust: exact;
  }
  .slide {
    width: 1920px;
    height: 1080px;
    page-break-after: always;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    padding: 80px 100px;
    position: relative;
    background: #ffffff;
    overflow: hidden;
  }
  .slide::before {
    content: '';
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 10px;
    background: linear-gradient(90deg, #10b981, #059669, #0284c7);
  }
  .header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-bottom: 30px;
  }
  .badge {
    display: inline-flex;
    align-items: center;
    gap: 8px;
    background: #ecfdf5;
    color: #059669;
    border: 1.5px solid #a7f3d0;
    padding: 8px 18px;
    border-radius: 30px;
    font-size: 18px;
    font-weight: 700;
    letter-spacing: 0.5px;
  }
  .slide-num {
    font-size: 20px;
    font-weight: 700;
    color: #94a3b8;
  }
  .title {
    font-size: 54px;
    font-weight: 800;
    letter-spacing: -1.5px;
    color: #0f172a;
    line-height: 1.15;
    margin-bottom: 12px;
  }
  .subtitle {
    font-size: 24px;
    color: #64748b;
    font-weight: 500;
    max-width: 1300px;
    margin-bottom: 40px;
  }
  .content {
    flex: 1;
    display: flex;
    flex-direction: column;
    justify-content: center;
  }
  .grid-2 {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 40px;
  }
  .grid-3 {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 35px;
  }
  .card {
    background: #f8fafc;
    border: 1.5px solid #e2e8f0;
    border-radius: 20px;
    padding: 35px;
    position: relative;
  }
  .card-highlight {
    background: #ecfdf5;
    border-color: #10b981;
    box-shadow: 0 12px 30px rgba(16, 185, 129, 0.08);
  }
  .card-title {
    font-size: 24px;
    font-weight: 700;
    color: #0f172a;
    margin-bottom: 15px;
    display: flex;
    align-items: center;
    gap: 12px;
  }
  .stat-val {
    font-size: 60px;
    font-weight: 800;
    color: #059669;
    line-height: 1;
    margin-bottom: 10px;
  }
  .stat-desc {
    font-size: 19px;
    color: #475569;
    line-height: 1.45;
  }
  .quote-box {
    background: #ffffff;
    border-left: 5px solid #059669;
    border-radius: 12px;
    padding: 20px 25px;
    font-style: italic;
    font-size: 20px;
    color: #334155;
    margin-top: 15px;
    box-shadow: 0 4px 15px rgba(0,0,0,0.03);
  }
  .table {
    width: 100%;
    border-collapse: collapse;
    background: #ffffff;
    border-radius: 16px;
    overflow: hidden;
    border: 1.5px solid #e2e8f0;
  }
  .table th, .table td {
    padding: 22px 28px;
    text-align: left;
    font-size: 20px;
  }
  .table th {
    background: #f1f5f9;
    font-weight: 700;
    color: #334155;
    border-bottom: 2px solid #cbd5e1;
  }
  .table td {
    border-bottom: 1px solid #e2e8f0;
    color: #1e293b;
  }
  .footer {
    display: flex;
    justify-content: space-between;
    align-items: center;
    border-top: 1.5px solid #e2e8f0;
    padding-top: 25px;
    color: #94a3b8;
    font-size: 18px;
    font-weight: 600;
  }
  .tag {
    display: inline-block;
    padding: 4px 12px;
    border-radius: 6px;
    font-size: 16px;
    font-weight: 700;
  }
  .tag-pass { background: #dcfce7; color: #15803d; }
  .tag-fail { background: #fee2e2; color: #b91c1c; }
  .tag-warn { background: #fef3c7; color: #b45309; }
</style>
</head>
<body>

<!-- SLIDE 1: USER & JOB -->
<div class="slide">
  <div class="header">
    <div class="badge">TRACK A · VLEARN TUTOR</div>
    <div class="slide-num">01 / 06</div>
  </div>
  <div class="content">
    <h1 class="title">User & Nỗi Đau: Muốn Kiểm Chứng Nguồn Nhưng Bị Kẹt</h1>
    <p class="subtitle">Job Executor: Học viên lớp 3A khóa AI20k đang tự ôn bài hoặc thực hiện bài tập Lab mini.</p>
    
    <div class="grid-2">
      <div class="card card-highlight">
        <div class="card-title">🎯 Core Job-To-Be-Done (JTBD)</div>
        <p style="font-size: 24px; line-height: 1.5; color: #065f46; font-weight: 600;">
          "Khi nhớ mang máng một kiến thức đã học, tôi muốn nhanh chóng định vị chính xác vị trí bài giảng và tài liệu gốc tương ứng, để đối chiếu, hiểu sâu và hoàn thành bài tập đúng hạn."
        </p>
        <div class="quote-box">
          "Tôi nhớ mang máng thầy có demo chỗ parse JSON, mà tua đi tua lại video 3 tiếng kéo chuột mỏi cả mắt vẫn không trúng đoạn thầy gõ code."
          <div style="font-size: 16px; color: #64748b; margin-top: 5px; font-weight: 700;">— Bạn N.V.T (Học viên lớp 3A)</div>
        </div>
      </div>

      <div class="grid-2" style="gap: 20px;">
        <div class="card">
          <div class="stat-val">72.8%</div>
          <div class="stat-desc">Học viên khảo sát coi <strong>tìm lại bài giảng & kiểm chứng nguồn gốc</strong> là rào cản nhức nhối nhất (Khảo sát N=11).</div>
        </div>
        <div class="card">
          <div class="stat-val">50.0%</div>
          <div class="stat-desc">Mất từ <strong>15 đến >30 phút</strong> cho mỗi lần tìm kiếm tài liệu thủ công; 0% giải quyết được dưới 2 phút.</div>
        </div>
        <div class="card">
          <div class="stat-val">100%</div>
          <div class="stat-desc">Chịu ảnh hưởng tiêu cực: <strong>70% trễ tiến độ</strong>, 30% phải bỏ dở bài tập đang làm.</div>
        </div>
        <div class="card">
          <div class="stat-val">50.0%</div>
          <div class="stat-desc">Tự xoay sở chỉ giải quyết được một phần hoặc <strong>vẫn nghi ngờ không chắc đúng</strong>.</div>
        </div>
      </div>
    </div>
  </div>
  <div class="footer">
    <div>Nhóm Vua Về Nhì · Lớp 3A · Phòng E402</div>
    <div>Mini Hackathon AI — Batch 04</div>
  </div>
</div>

<!-- SLIDE 2: VÌ SAO CHỌN TÍNH NĂNG NÀY -->
<div class="slide">
  <div class="header">
    <div class="badge">ĐÁNH GIÁ & LỰA CHỌN BÀI TOÁN</div>
    <div class="slide-num">02 / 06</div>
  </div>
  <div class="content">
    <h1 class="title">Bảng So Sánh 3 Bài Toán Ứng Viên & Quyết Định Chọn</h1>
    <p class="subtitle">Đưa ra quyết định dựa trên bằng chứng định lượng từ khảo sát học viên và tính khả thi 48 giờ.</p>
    
    <table class="table">
      <thead>
        <tr>
          <th>Bài toán ứng viên</th>
          <th>Tỷ lệ nhu cầu</th>
          <th>Tổn thất mỗi lần</th>
          <th>Tính khả thi 48h</th>
          <th>Quyết định & Căn cứ</th>
        </tr>
      </thead>
      <tbody>
        <tr style="background: #f0fdf4;">
          <td><strong style="font-size: 22px; color: #15803d;">1. VLearn Recall (Truy hồi bài giảng)</strong></td>
          <td><strong style="color: #15803d;">72.8% (Số 1)</strong></td>
          <td>15–30 phút/lần; trễ hạn nộp</td>
          <td><span class="tag tag-pass">Rất cao (Ground truth sẵn)</span></td>
          <td><strong style="color: #15803d;">CHỌN ✓</strong> — Nhu cầu cao nhất, đo được bằng số</td>
        </tr>
        <tr>
          <td><strong>2. Discord Admin Bot (Hạn nộp & XP)</strong></td>
          <td>45.5% (Chọn ưu tiên: 9.1%)</td>
          <td>5–10 phút tra tin nhắn</td>
          <td><span class="tag tag-warn">Trung bình (Dữ liệu đổi liên tục)</span></td>
          <td><strong>LOẠI ✗</strong> — Tỷ lệ ưu tiên thấp, rủi ro tin mâu thuẫn</td>
        </tr>
        <tr>
          <td><strong>3. Socratic Code Debugger</strong></td>
          <td>63.6% gặp bug khi code</td>
          <td>Mất 30–60 phút khi kẹt</td>
          <td><span class="tag tag-fail">Thấp (Cần Sandbox phức tạp)</span></td>
          <td><strong>LOẠI ✗</strong> — Phạm vi quá rộng, dễ làm hộ học viên</td>
        </tr>
      </tbody>
    </table>

    <div class="card" style="margin-top: 30px; background: #f8fafc;">
      <div style="font-size: 21px; color: #334155; line-height: 1.5;">
        💡 <strong>Kết luận:</strong> Chọn <strong>VLearn Recall</strong> vì giải quyết bài toán có <strong>tần suất lặp lại cao nhất (2–4 lần/tuần)</strong>, có bộ dữ liệu chuẩn (6 transcripts + 2 slide decks) để kiểm chứng, và cam kết giảm thời gian tìm kiếm từ <strong>15–30 phút xuống dưới 45 giây</strong>.
      </div>
    </div>
  </div>
  <div class="footer">
    <div>Nhóm Vua Về Nhì · Lớp 3A · Phòng E402</div>
    <div>Mini Hackathon AI — Batch 04</div>
  </div>
</div>

<!-- SLIDE 3: GIẢI PHÁP & KỊCH BẢN DEMO -->
<div class="slide">
  <div class="header">
    <div class="badge">LÁT CẮT & THIẾT KẾ TRẢI NGHIỆM</div>
    <div class="slide-num">03 / 06</div>
  </div>
  <div class="content">
    <h1 class="title">Lát Cắt Một Câu & 2 Kịch Bản Demo Trực Tiếp</h1>
    <p class="subtitle">Lát cắt: 1 học viên · 1 mô tả mơ hồ · 1 quyết định AI (FOUND / CLARIFY / NOT_FOUND) · 3 nguồn đối chiếu dưới 45s.</p>
    
    <div class="grid-2">
      <div class="card card-highlight">
        <div class="card-title">🟢 Demo Case 1: Happy Path (FOUND)</div>
        <p style="font-size: 20px; color: #334155; margin-bottom: 12px;">
          <strong>Học viên nhập:</strong> <em>"đoạn agent suy nghĩ rồi gọi tool trong bài ReAct"</em>
        </p>
        <ul style="font-size: 19px; color: #475569; line-height: 1.6; padding-left: 25px;">
          <li><strong>AI Suy luận (4.8s):</strong> Phân loại chính xác `FOUND` với chủ đề `react_loop`.</li>
          <li><strong>Đầu ra có kiểm chứng:</strong> Trích dẫn <strong>Bài 04 · Slide trang 14</strong> kèm Rationale 2 câu giải thích lý do chọn.</li>
          <li><strong>Hành động:</strong> Mở modal trích dẫn → Bấm *"Đúng phần mình cần"* → Hoàn tất.</li>
        </ul>
      </div>

      <div class="card" style="border-left: 5px solid #eab308;">
        <div class="card-title">🟡 Demo Case 2: Chỗ Khó (CLARIFY & Boundary)</div>
        <p style="font-size: 20px; color: #334155; margin-bottom: 12px;">
          <strong>Case 2a (Mơ hồ):</strong> <em>"mình nhớ bài có nói về context"</em>
        </p>
        <ul style="font-size: 19px; color: #475569; line-height: 1.6; padding-left: 25px; margin-bottom: 15px;">
          <li><strong>Xử lý:</strong> AI không đoán mò, kích hoạt `CLARIFY` (HAX 9, 10) đưa 2 tùy chọn: <em>Giữ ngữ cảnh nhiều lượt</em> vs <em>Context window</em>.</li>
        </ul>
        <p style="font-size: 20px; color: #334155; margin-bottom: 12px;">
          <strong>Case 2b (Ngoài bài giảng):</strong> <em>"dự báo giá Bitcoin bằng Python"</em>
        </p>
        <ul style="font-size: 19px; color: #475569; line-height: 1.6; padding-left: 25px;">
          <li><strong>Xử lý:</strong> Kích hoạt `NOT_FOUND` — Từ chối thẳng thắn, không bịa nguồn (Zero Hallucination).</li>
        </ul>
      </div>
    </div>

    <div class="quote-box" style="font-style: normal; margin-top: 25px; font-size: 19px;">
      ⚙️ <strong>Quy tắc Automation (Conditional):</strong> Chi phí sai sót (cost-of-error) cao do học viên dễ học sai kiến thức nếu AI bịa nguồn. Do đó, hệ thống <strong>chỉ trả lời khi đủ chắc</strong>, <strong>hỏi lại khi mơ hồ</strong> và <strong>từ chối khi ngoài phạm vi</strong>.
    </div>
  </div>
  <div class="footer">
    <div>Nhóm Vua Về Nhì · Lớp 3A · Phòng E402</div>
    <div>Mini Hackathon AI — Batch 04</div>
  </div>
</div>

<!-- SLIDE 4: KẾT QUẢ ĐO -->
<div class="slide">
  <div class="header">
    <div class="badge">ĐO LƯỜNG & KIỂM THỬ THỰC TẾ</div>
    <div class="slide-num">04 / 06</div>
  </div>
  <div class="content">
    <h1 class="title">Số Đo Golden Set: Vượt Chuẩn Quality Bar Đã Khóa</h1>
    <p class="subtitle">Đo đạc thực tế trên bộ 20 câu hỏi kiểm thử với mô hình Mistral Large (Endpoint xKiro) tại CP3.</p>
    
    <div class="grid-2">
      <table class="table">
        <thead>
          <tr>
            <th>Chỉ số kiểm thử</th>
            <th>Quality Bar đã khóa</th>
            <th>Kết quả đo thật</th>
            <th>Trạng thái</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><strong>Toàn bộ Golden Set</strong></td>
            <td>&ge; 80.0% (16/20)</td>
            <td><strong style="color: #15803d; font-size: 22px;">18 / 20 (90.0%)</strong></td>
            <td><span class="tag tag-pass">VƯỢT CHUẨN</span></td>
          </tr>
          <tr>
            <td><strong>Happy Path (FOUND Routing)</strong></td>
            <td>&ge; 80.0% (10/12)</td>
            <td><strong style="color: #15803d;">12 / 12 (100%)</strong></td>
            <td><span class="tag tag-pass">TUYỆT ĐỐI</span></td>
          </tr>
          <tr>
            <td><strong>Trích xuất đúng nguồn (Grounding)</strong></td>
            <td>&ge; 80.0% (10/12)</td>
            <td><strong style="color: #15803d;">12 / 12 (100%)</strong></td>
            <td><span class="tag tag-pass">KHỚP ĐÍCH</span></td>
          </tr>
          <tr>
            <td><strong>Ngoài phạm vi (NOT_FOUND)</strong></td>
            <td>100% (Zero Hallucination)</td>
            <td><strong style="color: #15803d;">4 / 4 (100%)</strong></td>
            <td><span class="tag tag-pass">ĐẠT CHUẨN</span></td>
          </tr>
          <tr>
            <td><strong>Làm rõ mơ hồ (CLARIFY)</strong></td>
            <td>&ge; 50.0% (Ngưỡng tối thiểu)</td>
            <td><strong style="color: #b45309;">2 / 4 (50.0%)</strong></td>
            <td><span class="tag tag-warn">TỐI THIỂU (ĐIỂM YẾU)</span></td>
          </tr>
          <tr>
            <td><strong>Độ trễ trung bình / P50</strong></td>
            <td>&lt; 5000 ms</td>
            <td><strong>5.2s (P50: 4.5s)</strong></td>
            <td><span class="tag tag-fail">CHƯA ĐẠT (1 OUTLIER)</span></td>
          </tr>
        </tbody>
      </table>

      <div class="card" style="border-left: 5px solid #ef4444;">
        <div class="card-title" style="color: #b91c1c;">⚠️ Minh Bạch Điểm Yếu & Ca Thất Bại</div>
        <p style="font-size: 18px; color: #334155; line-height: 1.4; margin-bottom: 12px;">
          <strong>1. Độ trễ 5.2s:</strong> P50 đạt 4.5s rất mượt, nhưng trung bình bị kéo lên do 1 ca cá biệt TC18 bị timeout mạng (19.3s). Không giấu outlier.<br>
          <strong>2. Ca TC14 & TC16:</strong> <em>"chỗ thầy nhắc confirmation"</em> và <em>"cách viết prompt cho agent"</em> bị AI đoán thành `FOUND` thay vì `CLARIFY`.
        </p>
        <div style="background: #ffffff; padding: 14px; border-radius: 10px; border: 1px solid #fed7aa; margin-bottom: 10px; font-size: 16px;">
          <strong>Nguyên nhân gốc rễ (Root Cause):</strong> Hiện tượng <strong>Over-confidence</strong>. Khi câu hỏi quá ngắn (&lt; 8 từ) chứa từ khóa quen thuộc, LLM thiên kiến đoán ngay chủ đề thay vì hỏi làm rõ.
        </div>
        <p style="font-size: 17px; color: #065f46; font-weight: 600;">
          ➔ <strong>Khắc phục cho CP5:</strong> Bổ sung rule chặn câu hỏi &lt; 8 từ ép về nhánh `CLARIFY` + tối ưu timeout.
        </p>
      </div>
    </div>
  </div>
  <div class="footer">
    <div>Nhóm Vua Về Nhì · Lớp 3A · Phòng E402</div>
    <div>Mini Hackathon AI — Batch 04</div>
  </div>
</div>

<!-- SLIDE 5: USER THẬT NÓI GÌ -->
<div class="slide">
  <div class="header">
    <div class="badge">VALIDATION KHỐI R6</div>
    <div class="slide-num">05 / 06</div>
  </div>
  <div class="content">
    <h1 class="title">Phản Hồi Người Dùng Thật & Thay Đổi Đã Làm</h1>
    <p class="subtitle">Thực nghiệm trên 5 người dùng ngoài nhóm (bao gồm 2 Willing Users đã đăng ký từ CP1).</p>
    
    <div class="grid-3">
      <div class="card">
        <div class="card-title" style="font-size: 21px;">👤 Bạn Ttung (Lớp 3A)</div>
        <div style="font-size: 16px; color: #64748b; margin-bottom: 10px;">Khai báo từ CP1 · Task: Tìm bài ReAct</div>
        <div class="quote-box" style="font-size: 17px; line-height: 1.4;">
          "Ơ bấm tìm xong sao màn hình đứng im mấy giây tưởng lag... nhưng lúc hiện ra trích đúng Bài 04 Slide 12 với file react_agent.py thì chuẩn phết!"
        </div>
        <div style="font-size: 16px; color: #059669; font-weight: 700; margin-top: 12px;">
          ✓ Xác nhận: Trích nguồn chính xác, nhưng cần hiển thị loading khi chờ.
        </div>
      </div>

      <div class="card">
        <div class="card-title" style="font-size: 21px;">👤 Bạn Hà Dũng (Lớp 3A)</div>
        <div style="font-size: 16px; color: #64748b; margin-bottom: 10px;">Khai báo từ CP1 · Task: Tìm Context</div>
        <div class="quote-box" style="font-size: 17px; line-height: 1.4;">
          "Lúc đầu gõ mỗi chữ context tính chê bot nếu ra linh tinh, ai ngờ nó bật ra 2 nhánh hỏi lại mình cần loại nào. Chọn xong ra trúng phóc video hôm nọ."
        </div>
        <div style="font-size: 16px; color: #059669; font-weight: 700; margin-top: 12px;">
          ✓ Xác nhận: Luồng CLARIFY 2 nhánh phân định mơ hồ hiệu quả.
        </div>
      </div>

      <div class="card" style="border-color: #f59e0b;">
        <div class="card-title" style="font-size: 21px;">👤 Bạn T148 (Lớp 3A)</div>
        <div style="font-size: 16px; color: #64748b; margin-bottom: 10px;">Thử trên điện thoại · Task: Đọc trích dẫn</div>
        <div class="quote-box" style="font-size: 17px; line-height: 1.4;">
          "Bot hiểu được cả câu càm ràm của mình, ra đúng bài rồi. Cơ mà nút 'Mở đúng đoạn' trên mobile hơi nhỏ, bấm dễ hụt quá."
        </div>
        <div style="font-size: 16px; color: #d97706; font-weight: 700; margin-top: 12px;">
          ⚠️ Phát hiện vấn đề: Cần mở rộng Touch Target nút bấm &ge; 44px.
        </div>
      </div>
    </div>

    <div class="card card-highlight" style="margin-top: 25px; padding: 20px 30px;">
      <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 10px;">
        <div style="font-size: 20px; font-weight: 700; color: #065f46;">
          🛠️ Thay đổi đã thực hiện ngay vào mã nguồn (Ghi nhận §9 Changelog):
        </div>
        <div style="font-size: 15px; font-weight: 700; background: #dcfce7; color: #15803d; padding: 5px 12px; border-radius: 20px;">
          📊 Định lượng: 5/5 Task hoàn thành (100%) · Thời gian TB: 32.4s (&lt; 45s) · 0/5 cần trợ giúp
        </div>
      </div>
      <p style="font-size: 18px; color: #334155; line-height: 1.5;">
        1. Bổ sung trạng thái <strong>"⚡ AI ĐANG SUY LUẬN & TRUY HỒI NGUỒN..."</strong> kèm spinner để người dùng an tâm.<br>
        2. Tăng diện tích bấm nút <strong>"Mở đúng đoạn →"</strong> (min-height &ge; 44px, padding 12x20px) và cập nhật nhãn Working Prototype.
      </p>
    </div>
  </div>
  <div class="footer">
    <div>Nhóm Vua Về Nhì · Lớp 3A · Phòng E402</div>
    <div>Mini Hackathon AI — Batch 04</div>
  </div>
</div>

<!-- SLIDE 6: NẾU CÓ THÊM 1 TUẦN -->
<div class="slide">
  <div class="header">
    <div class="badge">BÀI HỌC & ĐỊNH HƯỚNG</div>
    <div class="slide-num">06 / 06</div>
  </div>
  <div class="content">
    <h1 class="title">Nếu Có Thêm 1 Tuần & Bài Học Lớn Nhất</h1>
    <p class="subtitle">Tập trung giải quyết các phản hồi người dùng còn tồn đọng và đúc kết tư duy sản phẩm AI.</p>
    
    <div class="grid-3" style="margin-bottom: 40px;">
      <div class="card">
        <div class="card-title">1. Deep-linking Video Player</div>
        <p class="stat-desc">
          Tích hợp trực tiếp với API trình phát video VLearn, cho phép học viên click chuột là <strong>nhảy ngay đến đúng giây thứ 18:25</strong> thay vì xem timestamp text.
        </p>
      </div>

      <div class="card">
        <div class="card-title">2. Hybrid Vector Search</div>
        <p class="stat-desc">
          Kết hợp BM25 Keyword Search và Local Embedding (BGE-M3) để <strong>cắt giảm độ trễ từ 4.5s xuống dưới 1.2s</strong> và khắc phục lỗi over-confidence ở câu hỏi ngắn.
        </p>
      </div>

      <div class="card">
        <div class="card-title">3. Chrome Extension Tra Cứu</div>
        <p class="stat-desc">
          Xây dựng extension trên trình duyệt để học viên bôi đen từ khóa hoặc bấm phím tắt tra cứu tức thì ngay khi đang xem slide hoặc làm bài lab.
        </p>
      </div>
    </div>

    <div class="card card-highlight" style="padding: 40px; text-align: center;">
      <div style="font-size: 22px; color: #059669; font-weight: 700; letter-spacing: 1px; margin-bottom: 12px;">
        💡 BÀI HỌC LỚN NHẤT CỦA NHÓM VUA VỀ NHÌ
      </div>
      <div style="font-size: 32px; font-weight: 800; color: #064e3b; line-height: 1.4;">
        "Một lát cắt nhỏ giải quyết đúng nỗi đau thật, có trích dẫn nguồn kiểm chứng và biết từ chối khi ngoài phạm vi, có giá trị gấp trăm lần một chatbot vạn năng nhưng thường xuyên ảo giác."
      </div>
    </div>
  </div>
  <div class="footer">
    <div>Nhóm Vua Về Nhì · Lớp 3A · Phòng E402</div>
    <div>Mini Hackathon AI — Batch 04</div>
  </div>
</div>

</body>
</html>
"""

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.set_content(html_content)
        page.wait_for_load_state("networkidle")
        
        # Export high-res vector PDF 1920x1080 (16:9 widescreen)
        page.pdf(
            path=str(output_pdf),
            width="1920px",
            height="1080px",
            print_background=True,
            prefer_css_page_size=True,
            margin={"top": "0", "right": "0", "bottom": "0", "left": "0"}
        )
        browser.close()

    print(f"Successfully generated 6-page presentation PDF: {output_pdf}")

if __name__ == "__main__":
    generate_pdf()
