# Suy Ngẫm Cá Nhân (Reflection) · Đào Đức Hải

* **Họ và tên:** Đào Đức Hải
* **Mã học viên:** `2A202602752`
* **Vai trò trong nhóm:** UI/UX & Validation Coordinator
* **Nhóm:** `K4-3A-E402-VuaVeNhi` · **Track:** Track A (VLearn Tutor)

---

### 1. Vai trò và phần việc chính đã đảm nhiệm
Là người chịu trách nhiệm về trải nghiệm người dùng và cầu nối với thế giới bên ngoài:
1. **Thiết kế & Xây dựng Giao diện Prototype (`codebase/index.html`):** Thiết kế giao diện web tối giản theo phong cách học thuật hiện đại, tuân thủ nghiêm ngặt các nguyên tắc HAX (Human-AI eXperience) và PAIR của Google: rõ ràng trạng thái hệ thống, hỗ trợ sửa sai và minh bạch nguồn gốc dữ liệu.
2. **Xây dựng Sơ đồ luồng (CP2):** Thiết kế luồng 4 trạng thái (`FOUND`, `CLARIFY`, `NOT_FOUND`, `EDIT_QUERY`), giúp cả nhóm có chung một bức tranh rõ ràng trước khi viết code.
3. **Sản xuất Video Demo:** Trực tiếp dàn dựng và quay video thao tác 30s cho CP3 và video demo dự phòng pitching cho CP5.
4. **Tổ chức Khảo sát & User Validation Ngoài Nhóm (Khối R6):** Điều phối và trực tiếp ngồi quan sát 5 học viên ngoài nhóm dùng thử sản phẩm (gồm `Ttung` và `hadunghb2003` từ CP1, cùng `T148`, `kyanh2k666`, `NewbieAgent`), ghi lại nhật ký và quote nguyên văn tại `validation/user_testing_log.md`.

---

### 2. Quyết định quan trọng nhất trong thiết kế UI/UX
Quyết định quan trọng nhất của tôi là **thiết kế card kết quả dạng "Trích dẫn nguồn là nhân vật chính" (Source-First Card), kèm nút "Mở đúng đoạn →" dẫn vào modal xem chi tiết**.
* Thay vì để AI trả lời một tràng dài khiến người dùng phải đọc mỏi mắt, giao diện chỉ hiển thị đúng 3 thông tin cốt lõi: Tên bài giảng, Mốc trang Slide/Thời gian video, và 1 câu tóm tắt nội dung chính.
* Khi người dùng bấm "Mở đúng đoạn", một modal hiện lên với đoạn trích nguyên văn để họ tự đối chiếu. Thiết kế này giải quyết triệt để tâm lý nghi ngờ thông tin của học viên và mang lại cảm giác kiểm soát hoàn toàn cho người học.

---

### 3. Thách thức lớn nhất trong quá trình User Testing (R6)
* Thách thức lớn nhất là **"phải kiềm chế bản thân không giải thích hay chỉ dẫn khi thấy người dùng bị kẹt"**.
* Khi quan sát bạn `Ttung` bấm tìm kiếm và thấy màn hình đứng yên 4 giây do đang chờ LLM phản hồi, tôi rất muốn nhắc bạn ấy là *"đợi xíu AI đang gọi API đó"*. Nhưng tuân theo nguyên tắc The Mom Test, tôi đã cắn răng ngồi im quan sát. Nhờ vậy, tôi mới chứng kiến bạn ấy bấm nút submit thêm 2 lần vì tưởng máy bị đơ.
* Chính quan sát đắt giá này đã dẫn đến quyết định sửa giao diện ngay lập tức: bổ sung badge và loading spinner `⚡ AI ĐANG SUY LUẬN...` để giao diện phản hồi ngay ở mili-giây đầu tiên. Đây là minh chứng rõ nhất cho giá trị của việc đem sản phẩm ra cho người thật thử.

---

### 4. Bài học cốt lõi rút ra
* **"Giao diện cho AI khác hoàn toàn giao diện CRUD thông thường":** Ứng dụng AI luôn có độ trễ và khả năng trả về kết quả không như ý. Một UX AI tốt phải cung cấp cơ chế hồi đáp trạng thái liên tục, cho phép người dùng sửa câu hỏi dễ dàng mà không làm mất nội dung cũ, và luôn tạo đường lui an toàn khi AI không tìm thấy câu trả lời.
* **"Lắng nghe người dùng chê còn quý hơn nghe người ta khen":** Lời khen xã giao không giúp sản phẩm tốt lên. Những câu càm ràm như *"sao màn hình đứng im"*, *"nút này bấm dễ hụt quá"* mới chính là những chỉ dẫn vàng để hoàn thiện sản phẩm.

---

### 5. Đánh giá sự phối hợp nhóm
Tôi thực sự may mắn khi được làm việc trong một tập thể có tính kỷ luật cao và tư duy cởi mở:
* Bạn **Giang** luôn định hướng rõ ràng mục tiêu và giữ vững nhịp độ cho cả nhóm.
* Bạn **Nhân** hỗ trợ tôi hết mình trong việc tích hợp API và tối ưu tốc độ response.
* Bạn **Sâm** cung cấp các test case rất thực tế giúp tôi lường trước được mọi trạng thái giao diện có thể xảy ra.
Mỗi người một thế mạnh, tôn trọng lẫn nhau và hướng tới một mục tiêu chung đã giúp nhóm tạo ra một sản phẩm hoàn chỉnh và thuyết phục.
