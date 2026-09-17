# Suy Ngẫm Cá Nhân (Reflection) · Võ Doanh Nhân

* **Họ và tên:** Võ Doanh Nhân
* **Mã học viên:** `2A202602770`
* **Vai trò trong nhóm:** Tool & Backend Engineer
* **Nhóm:** `K4-3A-E402-VuaVeNhi` · **Track:** Track A (VLearn Tutor)

---

### 1. Vai trò và phần việc chính đã đảm nhiệm
Trong dự án VLearn Recall, tôi phụ trách toàn bộ hạ tầng kỹ thuật và tích hợp mô hình:
1. **Xây dựng AI Engine (`ai_engine.py`):** Kết nối trực tiếp mô hình ngôn ngữ lớn `mistralai/mistral-large-2512` thông qua OpenAI SDK client, thiết kế logic xử lý response, đo lường latency chính xác đến từng mili-giây.
2. **Xây dựng Knowledge Base (`knowledge_base.json`):** Chuẩn hóa kho dữ liệu 12 cụm bài giảng AI20k thành định dạng JSON có cấu trúc gồm tiêu đề, tóm tắt, từ khóa, định vị slide và transcript mốc thời gian.
3. **Phát triển Backend Server (`server.py`):** Xây dựng REST API bằng FastAPI với endpoint `/api/recall` và `/api/health`, cấu hình CORS, xử lý timeout và ngoại lệ mạng.
4. **Hiện thực hóa Kịch bản rủi ro kỹ thuật (§5-§6 trong `spec.md`):** Xây dựng cơ chế fallback an toàn phía client nếu API mất kết nối hoặc timeout quá 10 giây.

---

### 2. Quyết định kỹ thuật quan trọng nhất
Quyết định kỹ thuật sống còn mà tôi đã bảo vệ là **ép mô hình trả về định dạng JSON thuần túy (Structured Outputs) và parse bằng Pydantic/Strict Regex thay vì nhận text tự do**.
* Trong các bài lab trước, tôi nhận thấy LLM rất hay tự ý chèn các câu mở đầu lịch sự như *"Chào bạn, tôi tìm thấy đoạn này..."*, làm hỏng hoàn toàn logic bóc tách dữ liệu phía frontend.
* Bằng cách thiết lập System Prompt nghiêm ngặt yêu cầu trả về đúng JSON schema `{decision, title, summary, rationale, sources, clarify_question, ...}` và viết hàm trích xuất regex JSON tự làm sạch markdown, backend đảm bảo 100% response trả về đều parse được, không bao giờ gây crash giao diện người dùng.

---

### 3. Thách thức lớn nhất và cách khắc phục
* **Độ trễ API và rủi ro Timeout:** Vì sử dụng model lớn `mistral-large-2512` qua mạng bên ngoài, độ trễ trung bình dao động từ 3.5s đến 6s tùy tải mạng. Lúc đầu, frontend chưa có chỉ báo gì khiến người dùng tưởng hệ thống bị treo.
* **Giải pháp:** Tôi đã tối ưu payload gửi lên LLM (chỉ đưa phần context cô đọng của 12 bài học thay vì toàn bộ transcript dài hàng chục ngàn dòng), đồng thời phối hợp với bạn Hải để hiển thị trạng thái `⚡ AI ĐANG SUY LUẬN...` ngay lập tức và thiết lập timeout 12 giây kèm cơ chế fallback sang dữ liệu heuristic có sẵn nếu API gặp sự cố.

---

### 4. Bài học về Kỹ thuật & Tư duy sản phẩm AI
* **"AI không phải phép màu, AI là một module có xác suất và độ trễ":** Một kỹ sư backend làm sản phẩm AI không chỉ biết gọi `client.chat.completions.create()`, mà phải quản trị được tính bất định của output: chuyện gì xảy ra nếu model bịa ra một trang slide không tồn tại? Chuyện gì xảy ra nếu token quota cạn? Chuyện gì xảy ra khi mạng chập chờn trên sân khấu pitch?
* Nhờ có tài liệu `spec.md` và bảng rủi ro §5-§6 được cả nhóm thống nhất từ đầu, tôi đã xây dựng sẵn các kịch bản bọc lót (`Safe Refusal`, `Timeout Fallback`), giúp sản phẩm có độ bền vững cao trước mọi thử thách demo.

---

### 5. Đánh giá sự phối hợp nhóm
Cả 4 thành viên đã phối hợp vô cùng ăn ý:
* Anh **Giang** có tư duy bao quát và khả năng viết prompt chặt chẽ, giúp tôi không phải tốn thời gian mò mẫm prompt engineering.
* Bạn **Sâm** cung cấp bộ test case cực kỳ bài bản, tự động hóa script chạy test giúp tôi đo lường ngay lập tức hiệu quả mỗi lần sửa code.
* Bạn **Hải** phản hồi rất nhanh các yêu cầu về schema và trải nghiệm người dùng, giúp kết nối giữa Backend và Frontend diễn ra trơn tru chỉ trong 1 lần tích hợp.
