# Suy Ngẫm Cá Nhân (Reflection) · Nguyễn Nhân Sâm

* **Họ và tên:** Nguyễn Nhân Sâm
* **Mã học viên:** `2A202602672`
* **Vai trò trong nhóm:** Eval & Red-Team QA Lead
* **Nhóm:** `K4-3A-E402-VuaVeNhi` · **Track:** Track A (VLearn Tutor)

---

### 1. Vai trò và phần việc chính đã đảm nhiệm
Là người giữ cán cân chất lượng (Quality Bar) của nhóm, nhiệm vụ của tôi là:
1. **Thiết kế Bộ Golden Set 20 Test Cases (`golden_set.json`):** Phân bổ khoa học thành 3 nhóm câu hỏi đại diện cho thực tế người dùng:
   - 12 ca **Happy Path (FOUND)**: Các câu hỏi mô tả trí nhớ mơ hồ, từ khóa gần đúng, tiếng Việt có dấu và không dấu.
   - 4 ca **Out-of-Scope (NOT_FOUND)**: Thử nghiệm độc hại, câu hỏi lạc đề (Crypto, Thời tiết, Hack đề) để kiểm tra tính chống ảo giác.
   - 4 ca **Ambiguous (CLARIFY)**: Các câu hỏi ngắn ngủn 1-2 từ (như *"agent"*, *"context"*) buộc AI phải kích hoạt hỏi lại.
2. **Xây dựng Script Benchmark tự động (`run_benchmark.py`):** Viết script tự động nạp test case, gửi request đến model, đối chiếu output thực tế với nhãn kỳ vọng, tính toán tỷ lệ chính xác và xuất báo cáo markdown (`benchmark_results.md`).
3. **Phân tích lỗi (Failure Mode Analysis):** Tìm ra nguyên nhân gốc rễ (Root Cause) của các ca không đạt và làm việc với Prompt Architect để điều chỉnh.

---

### 2. Quyết định quan trọng nhất trong quá trình Eval
Quyết định lớn nhất của tôi là **kiên quyết không "làm đẹp số liệu" và giữ nguyên 2 ca thất bại (TC14 & TC16) trong báo cáo nộp CP3 và CP4**.
* Trong lần chạy thử đầu tiên, hệ thống đạt 18/20 ca (90%). Hai ca TC14 và TC16 bị tính là lỗi vì khi người dùng nhập câu hỏi ngắn, AI đã tự đoán chủ đề thay vì hỏi `CLARIFY`.
* Lúc đó có ý kiến đề xuất sửa câu hỏi test case dài ra một chút để đạt 20/20 (100%) cho đẹp mắt. Tôi đã phản đối kịch liệt vì nguyên tắc của Hackathon: *"Số xấu mà thật và phân tích được nguyên nhân thì điểm cao hơn 100% ảo"*.
* Nhờ giữ lại 2 ca này, nhóm đã có một câu chuyện kỹ thuật cực kỳ đắt giá để trình bày trong Slide 4 và Slide 6: bài học về hiện tượng Over-confidence ở các mô hình AI ngôn ngữ.

---

### 3. Thách thức lớn nhất trong việc đánh giá AI
* Thách thức lớn nhất khi đánh giá hệ thống LLM so với phần mềm truyền thống là **tính phi tất định (non-deterministic)**: cùng một câu hỏi, mỗi lần chạy model có thể trả về câu chữ diễn đạt khác nhau.
* Để giải quyết bài toán này, tôi không kiểm tra bằng cách so khớp xâu ký tự thô (exact string match). Thay vào đó, tôi xây dựng bộ tiêu chí chấm 3 lớp:
  1. Quyết định luồng (`decision`) phải khớp chính xác (`FOUND`, `CLARIFY`, hoặc `NOT_FOUND`).
  2. Mã bài giảng và phạm vi slide trích dẫn phải bao hàm đúng ground-truth topic ID.
  3. Đo lường độ trễ thực tế để đảm bảo không vượt quá ngưỡng trần 10 giây.

---

### 4. Bài học cốt lõi rút ra
* **"Đừng tin lời hứa của mô hình ngôn ngữ, hãy tin vào bộ benchmark":** Rất nhiều người làm AI bị rơi vào bẫy "thấy test 1-2 câu chạy mượt thì tưởng là đã xong". Chỉ khi chạy qua một bộ test case có phân bổ ranh giới và góc cạnh rõ ràng, ta mới phát hiện ra mô hình bị lủng ở đâu.
* **"Red-teaming là bạn, không phải thù":** Tìm ra điểm yếu của sản phẩm trước khi người dùng và ban giám khảo tìm thấy chính là cách tốt nhất để bảo vệ chất lượng của cả đội.

---

### 5. Đánh giá sự phối hợp nhóm
Tôi rất may mắn được làm việc cùng 3 người bạn tuyệt vời:
* Bạn **Giang** có khả năng lắng nghe và sửa prompt dựa trên dữ liệu đo lường thực tế thay vì bảo thủ.
* Bạn **Nhân** xây dựng code backend rất sạch, hỗ trợ API endpoint giúp việc viết script test tự động của tôi diễn ra cực kỳ thuận lợi.
* Bạn **Hải** luôn đồng hành cùng tôi trong việc kiểm tra tính khả dụng thực tế của sản phẩm trên giao diện người dùng.
Sự gắn kết này đã tạo nên một sản phẩm vững chắc về cả lý thuyết lẫn số liệu thực nghiệm.
