# Suy Ngẫm Cá Nhân (Reflection) · Nguyễn Xuân Trường Giang

* **Họ và tên:** Nguyễn Xuân Trường Giang
* **Mã học viên:** `2A202602446`
* **Vai trò trong nhóm:** Đội trưởng (Team Lead) & Prompt Architect
* **Nhóm:** `K4-3A-E402-VuaVeNhi` · **Track:** Track A (VLearn Tutor)

---

### 1. Vai trò và phần việc chính đã đảm nhiệm
Với vai trò Đội trưởng, tôi chịu trách nhiệm chính về:
1. **Định hình bài toán và lát cắt:** Từ 5 track ban đầu, tôi cùng nhóm phân tích khảo sát 11 học viên lớp 3A và quyết định chọn lát cắt cực hẹp: **VLearn Recall (Truy hồi bài giảng từ trí nhớ mơ hồ dưới 45 giây)** thay vì làm một chatbot trợ giảng đa năng chung chung.
2. **Chủ trì soạn thảo `spec.md`:** Viết §1 Bằng chứng nỗi đau, §2 Mục tiêu JTBD, §3 Ràng buộc công nghệ, §4 Thiết kế tương tác 4 trạng thái theo nguyên tắc HAX/PAIR, và khóa chuẩn Quality Bar tại CP4.
3. **Thiết kế Prompt System & Guardrails:** Xây dựng prompt phân loại 3 nhánh (`FOUND`, `CLARIFY`, `NOT_FOUND`), quy định định dạng JSON có cấu trúc nghiêm ngặt và cấm mô hình bịa đặt nguồn tài liệu.
4. **Quản trị tiến độ và tích hợp Repo:** Điều phối 4 thành viên theo sát từng mốc CP1 đến CP5, đảm bảo 100% tài liệu và số liệu đo lường minh bạch trên GitHub.

---

### 2. Quyết định quan trọng nhất trong suốt 48 giờ
Quyết định mang tính bước ngoặt nhất của tôi là **cắt bỏ toàn bộ tính năng sinh câu trả lời dài (generative tutoring) và chỉ giữ lại duy nhất cơ chế Source-First Retrieval (trích dẫn nguồn bài giảng gốc)**.
* Ban đầu, cả nhóm từng có ý định làm một con AI có thể giảng lại toàn bộ kiến thức như thầy giáo. Nhưng khi nhìn vào khảo sát, 81.8% học viên nói họ không cần một con bot dài dòng, họ chỉ cần biết *"cái đoạn đó nằm ở trang slide nào hoặc video nào để tự vào xem"*.
* Quyết định "chọn bỏ" này đã giúp nhóm tiết kiệm 70% thời gian xây dựng prompt, giảm thiểu tối đa rủi ro ảo giác kiến thức của LLM và đưa sản phẩm giải quyết đúng trọng tâm nỗi đau nhất của người học.

---

### 3. Thách thức lớn nhất và cách vượt qua
* **Thách thức:** Hiện tượng **Over-confidence (quá tự tin)** của mô hình AI khi gặp các câu hỏi cực ngắn hoặc mơ hồ (như test case TC14 và TC16 trong Golden Set). Thay vì hỏi lại để làm rõ (`CLARIFY`), mô hình có xu hướng tự đoán đại một chủ đề và trả về `FOUND`.
* **Cách giải quyết:** Tôi đã cùng bạn Sâm (QA) và Nhân (Backend) mổ xẻ từng log lỗi. Thay vì cố gắng sửa bằng cách thêm hàng chục dòng prompt mơ hồ, tôi đã đưa ra các ví dụ cụ thể (few-shot examples) vào prompt hệ thống, phân định ranh giới giữa một câu hỏi đủ dữ kiện và một câu hỏi mơ hồ có nhiều thực thể trùng lặp. Kết quả đã nâng tỷ lệ chính xác toàn diện lên 90% (18/20 ca).

---

### 4. Bài học cốt lõi rút ra (AI Product Thinking vs Vibe-coding)
Trước khi tham gia Mini Hackathon, tôi từng nghĩ làm AI là chỉ cần dùng cursor/chat gõ vài câu lệnh vibe-code là có ngay sản phẩm. Nhưng qua 48 giờ thực chiến:
* **"Code chỉ là 20%, tư duy định nghĩa bài toán chiếm 80%":** Nếu không có `spec.md`, nhóm sẽ cãi nhau không hồi kết về việc bot phải trả lời thế nào. Khi spec đã chốt rõ 4 trạng thái và tiêu chuẩn Quality Bar, việc code backend và UI chỉ mất vài giờ.
* **"Không có số đo thì mọi tuyên bố đều vô nghĩa":** Nói "AI của tôi rất thông minh" là vô giá trị. Nhưng khi nói *"Thử 20 ca thật, 18 ca đạt trúng đích (90%), 2 ca sai do thiên kiến câu ngắn và nhóm đã khoanh vùng được nguyên nhân"*, đó mới là tư duy làm sản phẩm kỹ thuật nghiêm túc.

---

### 5. Đánh giá sự phối hợp nhóm
Tôi vô cùng tự hào về 3 người đồng đội:
* Bạn **Võ Doanh Nhân** triển khai backend FastAPI và tích hợp LLM cực kỳ nhanh, xử lý timeout và schema JSON chuẩn xác.
* Bạn **Nguyễn Nhân Sâm** xây dựng bộ Golden Set 20 ca rất gai góc, không ngần ngại chỉ ra điểm yếu của prompt để tôi hoàn thiện.
* Bạn **Đào Đức Hải** chăm chút từng chi tiết giao diện, kiên nhẫn ngồi quan sát 5 người dùng ngoài nhóm test và quay các video demo chuẩn chỉ.
Tinh thần làm việc kỷ luật, minh bạch và tôn trọng sự thật đã giúp cả nhóm hoàn thành xuất sắc cả 5 checkpoint đúng hạn.
