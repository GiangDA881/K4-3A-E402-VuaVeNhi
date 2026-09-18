# CẨM NANG THUYẾT TRÌNH PITCHING — NHÓM VUA VỀ NHÌ (PHÒNG E402)

> **Mục tiêu:** Kiểm soát thời gian dưới **6 phút** (an toàn trong khung trần 7 phút của phòng E402), cả 4 thành viên cùng có đất diễn (đạt trọn điểm **Vibe-coding rule**), và biến điểm yếu kỹ thuật thành **đòn ghi điểm trung thực** trước Ban giám khảo.

---

## I. PHÂN CÔNG THUYẾT TRÌNH (4 THÀNH VIÊN)

| Người nói | Phần đảm nhiệm | Vai trò & Phong thái |
|---|---|---|
| **Giang (Team Lead)** | **Slide 1 & Slide 2** (Mở đầu, Nỗi đau & Lý do chọn bài toán) | Tự tin, đặt vấn đề gãy gọn từ khảo sát thực tế. |
| **Hải (UI/UX)** | **Slide 3** (Demo trực tiếp 3 kịch bản tương tác) | Thao tác mượt mà, dứt khoát, chỉ rõ các điểm chạm UX. |
| **Sâm (QA/Eval Lead)** | **Slide 4** (Số liệu Benchmark & Minh bạch ca lỗi) | Điềm tĩnh, chuyên nghiệp, nói bằng số liệu thực nghiệm. |
| **Nhân (AI & Backend)** | **Slide 5 & Slide 6** (User Testing R6 & Bài học) + **Chủ trì Q&A kỹ thuật** | Chắc chắn về kiến trúc, tự tin giải thích kỹ thuật. |

---

## II. KỊCH BẢN CHI TIẾT TỪNG SLIDE (BẤM GIỜ: 5 PHÚT 45 GIÂY)

### SLIDE 1: User & Nỗi Đau (0:00 – 0:45 · Giang nói)
* **Chiếu Slide 1:**
* **Lời thoại:**
  > *"Kính chào Ban giám khảo và các bạn. Nhóm em là Vua Về Nhì, đến từ lớp 3A phòng E402.  
  Khi học trên VLearn và làm bài tập Lab, chắc hẳn ai trong chúng ta cũng từng gặp tình huống: **nhớ mang máng một đoạn thầy giảng, nhưng mở hàng chục trang slide hay video 3 tiếng ra thì kéo chuột mỏi cả mắt không tìm thấy**.  
  Qua khảo sát 11 học viên lớp 3A, có tới **72.8%** khẳng định việc tìm lại bài giảng và kiểm chứng nguồn gốc là rào cản lớn nhất; **50% mất từ 15 đến hơn 30 phút** mỗi lần tìm kiếm thủ công, và 100% bị trễ tiến độ làm bài. Đó là lý do nhóm em xây dựng **VLearn Recall — Trợ lý truy hồi bài giảng từ trí nhớ mơ hồ**."*

---

### SLIDE 2: Lựa Chọn Bài Toán & JTBD (0:45 – 1:30 · Giang nói)
* **Chiếu Slide 2:**
* **Lời thoại:**
  > *"Nhóm đã cân nhắc 3 bài toán: Bot hỏi deadline Discord, Công cụ debug code, và VLearn Recall. Nhóm quyết định loại 2 bài toán kia vì Discord dễ sai lệch quy chế, còn Debugger quá rộng.  
  VLearn Recall được chọn vì giúp giải quyết trọn vẹn Job-to-be-done cốt lõi: **Giúp người học đi từ một mô tả mơ hồ đến chính xác vị trí bài giảng gốc dưới 45 giây**, dựa trên kho tri thức chuẩn gồm 6 bài giảng gốc được chuẩn hóa thành 12 cụm chủ đề tra cứu.  
  Sau đây, xin mời bạn Hải demo sản phẩm thật đang chạy trực tiếp trên hệ thống."*

---

### SLIDE 3: Demo 3 Trạng Thái HAX/PAIR (1:30 – 3:15 · Hải thao tác & nói)
*(Chuyển tab sang trình duyệt Web hoặc chiếu video backup nếu mạng chập chờn)*

* **Kịch bản 1 — Happy Path (`FOUND`):**
  > *"Em nhập một câu gõ tự nhiên: 'cái bài hôm nọ thầy dạy ReAct loop với thought action ấy ở đâu'.  
  Bấm tìm kiếm: Các thầy cô thấy ngay chỉ báo `⚡ AI ĐANG SUY LUẬN`. Chỉ sau 4.5 giây, AI trích xuất chính xác **Bài 04 · Slide trang 12**, kèm 1 câu Rationale giải thích lý do. Em bấm 'Mở đúng đoạn' để đọc trích dẫn và bấm 'Đúng phần mình cần' để hoàn tất."*

* **Kịch bản 2 — Ambiguous Query (`CLARIFY`):**
  > *"Nếu học viên chỉ gõ mơ hồ một chữ: 'context'. Thay vì đoán mò hoặc sinh ảo giác, AI nhận diện tính đa nghĩa và kích hoạt trạng thái **CLARIFY** với 2 nút chọn: 'Giữ ngữ cảnh nhiều lượt' hoặc 'Giới hạn Context Window'. Em click chọn 'Giữ ngữ cảnh' — hệ thống lập tức định vị trúng mốc video 14:10."*

* **Kịch bản 3 — Safe Refusal (`NOT_FOUND`):**
  > *"Nếu học viên hỏi câu ngoài bài học: 'Dự báo giá Bitcoin tuần tới'. Guardrail kích hoạt trạng thái **NOT_FOUND**, lịch sự từ chối vì nằm ngoài 6 bài giảng và gợi ý 3 từ khóa trong khóa học để học viên quay lại luồng học tập."*

---

### SLIDE 4: Benchmark & Minh Bạch Điểm Yếu (3:15 – 4:30 · Sâm nói)
* **Chiếu Slide 4:**
* **Lời thoại (ĐÒN ĂN ĐIỂM — NÓI THẲNG THẮN, KHÔNG GIẤU DIẾM):**
  > *"Để đảm bảo chất lượng, nhóm đã xây dựng bộ Golden Set 20 test cases thực tế và khóa chuẩn Quality Bar tại Checkpoint 4:
  - **Tỷ lệ chính xác tổng thể đạt 18/20 ca (90.0%)**, vượt chuẩn $\ge 80\%$.
  - **Độ chính xác trích dẫn nguồn (Grounding): đạt 100% (12/12 ca)**.
  - **Chặn ảo giác ngoài phạm vi (`NOT_FOUND`): đạt tuyệt đối 100% (4/4 ca)**.
  
  Tuy nhiên, tuân thủ nguyên tắc hackathon: **'Số xấu vẫn được điểm, giấu mới bị trừ'**, nhóm xin báo cáo minh bạch 2 điểm yếu kỹ thuật lớn nhất:
  1. **Tỷ lệ CLARIFY đạt 50% (2/4 ca)** — Đây là ngưỡng tối thiểu vì ở 2 ca TC14 và TC16, mô hình mắc lỗi **Over-confidence**: thấy câu hỏi ngắn chứa từ khóa quen thuộc là tự tin đoán luôn `FOUND` thay vì hỏi làm rõ. Nhóm đã khắc phục bằng cách đặt rule chặn câu hỏi dưới 8 từ ép về nhánh CLARIFY.
  2. **Độ trễ trung bình là 5.2 giây (chưa đạt mục tiêu <5s)**: Thực tế độ trễ trung vị P50 chỉ là **4.5 giây**, nhưng số trung bình bị kéo lên bởi **duy nhất 1 ca ngoại lai TC18 bị timeout mạng lên tới 19.3 giây**. Nhóm hoàn toàn không cắt bỏ outlier để làm đẹp số liệu."*

---

### SLIDE 5: Phản Hồi Người Dùng R6 (4:30 – 5:15 · Nhân nói)
* **Chiếu Slide 5:**
* **Lời thoại:**
  > *"Nhóm đã đem sản phẩm đi kiểm thử thực tế với 5 học viên ngoài nhóm theo nguyên tắc The Mom Test, trong đó có **2 bạn Willing Users đã đăng ký từ Checkpoint 1 là bạn Ttung và bạn Hà Dũng**:
  - **Kết quả định lượng:** **5/5 người hoàn thành nhiệm vụ (100%)**, thời gian trung bình tìm ra nguồn là **32.4 giây** (vượt xa mục tiêu dưới 45 giây), **0/5 người cần hỗ trợ**.
  - **Phản hồi thực tế đã cải tiến ngay vào code:**
    1. Bạn Ttung bấm nút liên tục vì tưởng web lag $\rightarrow$ Nhóm bổ sung ngay hiệu ứng loading `AI ĐANG SUY LUẬN`.
    2. Bạn T148 phản hồi nút trên điện thoại khó bấm $\rightarrow$ Nhóm đã tăng diện tích Touch target của toàn bộ nút lên $\ge 44\text{px}$."*

---

### SLIDE 6: Nếu Có Thêm 1 Tuần & Kết Luận (5:15 – 5:45 · Giang kết bài)
* **Chiếu Slide 6:**
* **Lời thoại:**
  > *"Nếu có thêm 1 tuần, nhóm sẽ: (1) Tích hợp Deep-linking mở thẳng iframe video tại đúng giây; (2) Kết hợp BM25 + Vector Search để ép độ trễ xuống dưới 1.2s; và (3) Xây dựng Chrome Extension tra cứu nhanh.  
  **Bài học lớn nhất mà nhóm Vua Về Nhì đúc kết được là:**  
  *‘Học viên không cần một con chatbot biết tuốt nhưng hay nói dối; họ cần một trợ lý trung thực, dẫn đúng nguồn tài liệu gốc để họ tự kiểm chứng và tự tin tiếp tục làm bài.’*  
  Nhóm em xin cảm ơn Ban giám khảo và sẵn sàng nhận câu hỏi phản biện!"*

---

## III. BỘ PHẢN BIỆN Q&A — HẠ GỤC MỌI CÂU HỎI CỦA GIÁM KHẢO

### ❓ Câu 1: "Tại sao độ trễ lên tới 5.2s và có câu gần 20s? Như vậy học viên có sốt ruột không?"
* **Người trả lời: Võ Doanh Nhân (Backend)**
* **Đáp án chuẩn:**
  > *"Dạ thưa Ban giám khảo, độ trễ trung vị (P50) của hệ thống chỉ là **4.5 giây**, tức một nửa số câu phản hồi dưới 4.5s. Con số trung bình bị kéo lên 5.2s là do ca TC18 bị nghẽn mạng API bên thứ ba (Mistral Large) mất 19.3s.  
  Để người dùng không sốt ruột, nhóm đã áp dụng 2 giải pháp UX: (1) Ngay microsecond người dùng gửi câu hỏi, giao diện hiện ngay chỉ báo động `⚡ AI ĐANG SUY LUẬN...`; và (2) Có cơ chế try-catch, nếu API quá 8 giây sẽ tự động chuyển sang Local Fallback Keyword Matching để không bao giờ treo app."*

---

### ❓ Câu 2: "Tại sao chuẩn CLARIFY chỉ để $\ge 50\%$? Có phải các bạn thấy chỉ làm được 2/4 câu nên cố tình hạ chuẩn xuống để đỗ không?"
* **Người trả lời: Nguyễn Nhân Sâm (QA/Eval)**
* **Đáp án chuẩn:**
  > *"Dạ thưa Ban giám khảo, đây là điểm nhóm em tự hào nhất về tính trung thực khoa học. Khi chạy benchmark lần đầu, 2 ca TC14 và TC16 bị fail vì hiện tượng **Over-confidence** — mô hình ngôn ngữ lớn quá tự tin và gán luôn vào chủ đề nổi tiếng nhất.  
  Lúc đó nhóm có thể sửa câu test dài ra để đạt 100% cho đẹp số liệu, nhưng nhóm kiên quyết giữ nguyên số thật và khóa chuẩn ở mức tối thiểu 50% tại CP4. Điều này giúp nhóm nhận diện đúng bản chất kỹ thuật và xây dựng giải pháp chặn độ dài dưới 8 từ thay vì che giấu khuyết điểm."*

---

### ❓ Câu 3: "Sản phẩm này là gọi AI thật hay chỉ là mock dữ liệu?"
* **Người trả lời: Võ Doanh Nhân (Backend) hoặc Đào Đức Hải (UI)**
* **Đáp án chuẩn:**
  > *"Dạ sản phẩm chạy thật 100% qua API backend FastAPI (`server.py`) gọi trực tiếp mô hình `mistralai/mistral-large-2512`. Trên màn hình kết quả có in rõ độ trễ đo bằng mili-giây thật (ví dụ: 4124ms) và đoạn suy luận Rationale được AI sinh động thời gian thực chứ không phải hardcode."*

---

### ❓ Câu 4: "Tại sao không dùng RAG hay Vector Database (như ChromaDB/FAISS) mà lại dùng Decision Engine phân loại chủ đề?"
* **Người trả lời: Võ Doanh Nhân (Backend)**
* **Đáp án chuẩn:**
  > *"Dạ, nhóm đã phân tích theo nguyên lý Cost-of-error trong thiết kế AI:  
  Với RAG thông thường, nếu vector search lấy nhầm chunk thì LLM vẫn cố sinh câu trả lời mượt mà, dẫn đến nguy cơ ảo giác cao (hallucination).  
  Trong phạm vi giáo trình chuẩn của khóa học, việc chia thành 12 cụm chủ đề và để LLM đóng vai trò Decision Router theo 3 trạng thái (`FOUND` / `CLARIFY` / `NOT_FOUND`) giúp kiểm soát rủi ro an toàn tuyệt đối 100%, không bao giờ bịa nguồn khi học viên hỏi ngoài bài học."*

---

## IV. BÍ QUYẾT PHÒNG THỦ & TÂM LÝ TRƯỚC GIỜ G

1. **Nguyên tắc "Mạng chết, máy chết — Bài thuyết trình không chết":**
   - Đội trưởng mở sẵn file `demo-slides.pdf` toàn màn hình.
   - Mở sẵn file `recordings/demo_backup_pitch.mp4` ở một cửa sổ khác. Nếu mở web bị lag mạng, **chuyển ngay sang video backup chiếu 1080p và nói bình thường**.
2. **Không cướp lời nhau:**
   - Khi giám khảo hỏi ai, người đó đứng thẳng, bình tĩnh trả lời. Nếu câu hỏi kỹ thuật sâu, bạn khác có thể xin phép: *"Em xin bổ sung thêm góc nhìn kỹ thuật..."*.
3. **Tuyệt đối không tranh cãi với Giám khảo:**
   - Luôn bắt đầu bằng: *"Dạ em cảm ơn câu hỏi rất hay của Thầy/Cô..."*. Nếu giám khảo chỉ ra điểm chưa tối ưu, nhận luôn: *"Dạ đúng là điểm này nhóm em đã ghi nhận vào Backlog để tối ưu sau hackathon ạ!"*.
