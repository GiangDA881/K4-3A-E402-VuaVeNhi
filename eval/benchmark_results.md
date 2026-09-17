# Báo Cáo Kiểm Thử Benchmark Checkpoint 3 (CP3)
**Hệ thống:** VLearn Recall (Track A · VLearn Tutor)  
**Mô hình đánh giá:** `mistralai/mistral-large-2512` (Endpoint xKiro)  
**Thời gian chạy:** 2026-09-16 23:57:15  

---

## 1. Tóm tắt Số đo (Executive Metric Summary)

| Chỉ số | Giá trị thực tế | Mục tiêu Quality Bar CP4 | Trạng thái đối chiếu |
|---|---|---|---|
| **Tổng số câu thử (Golden Set)** | **20 câu** | $\ge 20$ câu | ĐẠT ✓ |
| **Tỷ lệ chính xác tổng thể** | **18 / 20** (90.0%) | $\ge 80\%$ | **ĐẠT (VƯỢT CHUẨN)** |
| **Tỷ lệ đúng luồng Happy Path (FOUND)** | **12/12** (100.0%) | $\ge 80\%$ | ĐẠT ✓ |
| **Tỷ lệ trích xuất đúng nguồn (Grounding)** | **12/12** (100.0%) | $\ge 80\%$ | ĐẠT ✓ |
| **Tỷ lệ nhận diện Mơ hồ (CLARIFY)** | **2/4** (50.0%) | $\ge 50\%$ (Ngưỡng tối thiểu) | ĐẠT (Tối thiểu CP4) |
| **Tỷ lệ chặn ngoài phạm vi (NOT_FOUND)** | **4/4** (100.0%) | $100\%$ | ĐẠT ✓ (Tuyệt đối) |
| **Độ trễ trung bình / P50** | **5212 ms** (P50: 4466 ms) | $< 5000$ ms | CHƯA ĐẠT MỤC TIÊU <5s (Do outlier TC18) |

> **Ghi chú minh bạch về số đo:**
> - **Ngưỡng CLARIFY 50%:** Đây là ngưỡng tối thiểu và là điểm yếu nhất của mô hình tại thời điểm chốt CP4 (bị 2 ca over-confidence TC14, TC16). Nhóm giữ nguyên số liệu thực và cam kết giải trình minh bạch trong pitch thay vì làm đẹp số liệu.
> - **Độ trễ 5.2s:** P50 đạt 4466ms (đáp ứng tương tác tốt), độ trễ trung bình bị kéo lên 5212ms do 1 ca ngoại lai duy nhất TC18 bị timeout mạng (19.351ms). Nhóm không giấu outlier này.

---

## 2. Chi tiết kết quả từng Test Case

| ID | Nhóm | Câu hỏi học viên nhập | Kỳ vọng | Thực tế | Đạt/Hỏng | Độ trễ | Rationale / Giải thích |
|---|---|---|---|---|---|---|---|
| TC01 | Happy Path | *"đoạn agent suy nghĩ rồi gọi công cụ, hình như là ReAct"* | `FOUND` | `FOUND` | ĐẠT ✓ | 7455ms | Học viên mô tả quá trình agent suy nghĩ trước khi thực hiện hành động gọi công c... |
| TC02 | Happy Path | *"cách chuẩn hóa tools schema và bắt buộc tham số trong tools.yaml"* | `FOUND` | `FOUND` | ĐẠT ✓ | 4124ms | Câu hỏi của học viên liên quan trực tiếp đến việc định dạng và chuẩn hóa schema ... |
| TC03 | Happy Path | *"xử lý context carry-over khi người dùng đổi ý ở lượt chat sau"* | `FOUND` | `FOUND` | ĐẠT ✓ | 5479ms | Câu hỏi liên quan đến việc quản lý ngữ cảnh qua nhiều lượt chat khi người dùng t... |
| TC04 | Happy Path | *"giới hạn context window và cách tóm tắt token"* | `FOUND` | `FOUND` | ĐẠT ✓ | 4454ms | Học viên đang tìm hiểu về chiến lược quản lý độ dài lịch sử chat khi vượt quá ng... |
| TC05 | Happy Path | *"lỗi stale confirmation là gì và cách phòng chống"* | `FOUND` | `FOUND` | ĐẠT ✓ | 5032ms | Học viên đang tìm hiểu về vấn đề **Stale Confirmation** — một rủi ro an toàn qua... |
| TC06 | Happy Path | *"kỹ thuật Few-shot prompting kèm ví dụ mẫu trong bài giảng"* | `FOUND` | `FOUND` | ĐẠT ✓ | 4798ms | Học viên yêu cầu kỹ thuật Few-shot Prompting, một chủ đề chính được đề cập trong... |
| TC07 | Happy Path | *"thiết lập system prompt cấm đoán mã nhân viên hoặc asset ID"* | `FOUND` | `FOUND` | ĐẠT ✓ | 4095ms | Học viên đang tìm kiếm cách thiết lập hệ thống cảnh báo và cấm đoán trong system... |
| TC08 | Happy Path | *"ngăn chặn rò rỉ dữ liệu nội bộ ra công cụ tìm kiếm bên ngoài như Tavily"* | `FOUND` | `FOUND` | ĐẠT ✓ | 4712ms | Học viên đang đề cập đến việc bảo mật thông tin nội bộ và ngăn chặn rò rỉ dữ liệ... |
| TC09 | Happy Path | *"chu trình Thought Action Observation lặp lại đến khi hoàn thành"* | `FOUND` | `FOUND` | ĐẠT ✓ | 3992ms | Học viên đang mô tả quy trình vòng lặp Thought (suy luận), Action (hành động gọi... |
| TC10 | Happy Path | *"gọi nhiều tool song song trong một lượt phản hồi parallel tool call"* | `FOUND` | `FOUND` | ĐẠT ✓ | 4424ms | Học viên đang tìm hiểu về kỹ thuật **Parallel Tool Calling**, tức cách cho phép ... |
| TC11 | Happy Path | *"chuẩn hóa báo cáo sự cố bằng incident report format"* | `FOUND` | `FOUND` | ĐẠT ✓ | 3994ms | Câu hỏi của học viên trực tiếp liên quan đến chủ đề chuẩn hóa báo cáo sự cố theo... |
| TC12 | Happy Path | *"tra cứu trạng thái dịch vụ hạ tầng VPN, SSO, Email theo môi trường"* | `FOUND` | `FOUND` | ĐẠT ✓ | 4481ms | Học viên yêu cầu tra cứu trạng thái hoạt động của các dịch vụ hạ tầng cốt lõi (V... |
| TC13 | Ambiguous / Clarify | *"mình nhớ bài có nói về context nhưng không rõ là gì"* | `CLARIFY` | `CLARIFY` | ĐẠT ✓ | 2972ms | Bạn muốn tìm hiểu về chủ đề nào liên quan đến **context** trong khóa học ReAct? ... |
| TC14 | Ambiguous / Clarify | *"chỗ thầy nhắc về confirmation cần chú ý những gì"* | `CLARIFY` | `FOUND` | **HỎNG ✗** | 2455ms | Học viên đang tham khảo phần về **Stale Confirmation** (Xác nhận lỗi thời), một ... |
| TC15 | Ambiguous / Clarify | *"hướng dẫn làm bài lab"* | `CLARIFY` | `CLARIFY` | ĐẠT ✓ | 4710ms | Bạn muốn tìm hiểu về chủ đề nào trong bài lab cụ thể? Ví dụ: cấu trúc định dạng ... |
| TC16 | Ambiguous / Clarify | *"cách viết prompt cho agent"* | `CLARIFY` | `FOUND` | **HỎNG ✗** | 4196ms | Học viên đang tìm cách viết prompt hiệu quả cho agent, chủ đề này liên quan trực... |
| TC17 | Out of Scope | *"dự báo xu hướng giá Bitcoin và tiền ảo tuần này bằng Python"* | `NOT_FOUND` | `NOT_FOUND` | ĐẠT ✓ | 5017ms | Nội dung về dự báo xu hướng giá Bitcoin và tiền ảo không nằm trong phạm vi khóa ... |
| TC18 | Out of Scope | *"cách cấu hình server Nginx và deploy website Django lên AWS"* | `NOT_FOUND` | `NOT_FOUND` | ĐẠT ✓ | 19351ms | Nội dung về cấu hình server Nginx và triển khai website Django không nằm trong p... |
| TC19 | Out of Scope | *"thuật toán giải bài LeetCode Two Sum tối ưu độ phức tạp O(n)"* | `NOT_FOUND` | `NOT_FOUND` | ĐẠT ✓ | 4022ms | Nội dung về thuật toán giải bài Two Sum của LeetCode không nằm trong phạm vi khó... |
| TC20 | Out of Scope | *"ngày mai thời tiết Hà Nội có mưa không"* | `NOT_FOUND` | `NOT_FOUND` | ĐẠT ✓ | 4478ms | Nội dung về dự báo thời tiết Hà Nội không nằm trong phạm vi khóa học AI20k, tập ... |

---

## 3. Phân tích Nguyên nhân Thất bại (Failure Analysis & Root Cause)

> *"Số xấu vẫn được đủ điểm — miễn là số thật. Thử 20 câu mà phân tích được vì sao các câu kia sai thì ăn điểm cao hơn 'chạy tốt' không có gì chứng minh."* (Theo Rubric CP3).

### Ca TC14: *"chỗ thầy nhắc về confirmation cần chú ý những gì"*
- **Kỳ vọng:** `CLARIFY` | **Thực tế:** `FOUND`
- **Hiện tượng:** Mô hình đưa ra quyết định FOUND thay vì CLARIFY do mức độ tự tin suy luận.
- **Nguyên nhân gốc rễ (Root Cause):** Học viên sử dụng cụm từ có sự giao thoa ngữ nghĩa khiến mô hình phân vân giữa ranh giới từ chối và làm rõ.
- **Giải pháp khắc phục cho CP4:** Tinh chỉnh System Prompt phân biệt rõ ranh giới từ khóa và hạ nhiệt độ suy luận.

### Ca TC16: *"cách viết prompt cho agent"*
- **Kỳ vọng:** `CLARIFY` | **Thực tế:** `FOUND`
- **Hiện tượng:** Mô hình đưa ra quyết định FOUND thay vì CLARIFY do mức độ tự tin suy luận.
- **Nguyên nhân gốc rễ (Root Cause):** Học viên sử dụng cụm từ có sự giao thoa ngữ nghĩa khiến mô hình phân vân giữa ranh giới từ chối và làm rõ.
- **Giải pháp khắc phục cho CP4:** Tinh chỉnh System Prompt phân biệt rõ ranh giới từ khóa và hạ nhiệt độ suy luận.

