/**
 * Tự động tạo Google Form khảo sát AI20k chuẩn 100%
 * Đã sửa lỗi "Invalid data updating form" bằng cách khởi tạo toàn bộ các Phần (PageBreak)
 * trước khi thiết lập rẽ nhánh (Page Navigation).
 */
function createAI20kSurveyForm() {
  var formTitle = "Khảo sát trải nghiệm học và tìm thông tin trong AI20k";
  var form = FormApp.create(formTitle);
  
  form.setDescription(
    "Chào bạn! Nhóm mình đang tìm hiểu những trải nghiệm thực tế khi học trên VLearn và sử dụng Discord của khóa AI20k, phục vụ Mini Hackathon.\n\n" +
    "Khảo sát mất khoảng 4–5 phút. Bạn hãy trả lời dựa trên trải nghiệm trong 7 ngày gần nhất. Nếu không gặp khó khăn, câu trả lời đó cũng rất hữu ích.\n\n" +
    "Việc tham gia hoàn toàn tự nguyện. Nhóm chỉ sử dụng phản hồi cho bài hackathon, ẩn danh khi tổng hợp và không công khai thông tin liên hệ."
  );
  
  form.setAllowResponseEdits(true);
  form.setProgressBar(true);

  // ==========================================
  // PHẦN 1 — BỐI CẢNH SỬ DỤNG
  // ==========================================
  var item1 = form.addMultipleChoiceItem();
  item1.setTitle("Câu 1. Bạn đang học lớp nào?")
    .setRequired(true);

  var item2 = form.addCheckboxItem();
  item2.setTitle("Câu 2. Trong 7 ngày gần nhất, bạn đã thực hiện những việc nào?")
    .setHelpText("Mô tả: Nếu chọn “Chưa thực hiện…”, không chọn các mục khác.")
    .setChoiceValues([
      "Xem bài giảng, slide hoặc tài liệu trên VLearn",
      "Hỏi AI tutor trên VLearn",
      "Đọc hoặc tìm thông báo trên Discord",
      "Hỏi bot trợ lý trên Discord",
      "Hỏi bạn học hoặc TA/giảng viên để được hỗ trợ",
      "Chưa thực hiện việc nào ở trên"
    ])
    .setRequired(true);

  // ==========================================
  // PHẦN 2 — NHỮNG VIỆC THỰC SỰ ĐÃ XẢY RA
  // ==========================================
  var sec2 = form.addPageBreakItem();
  sec2.setTitle("Phần 2 — Những việc thực sự đã xảy ra");

  // Câu 3: Lưới trắc nghiệm
  var item3 = form.addGridItem();
  item3.setTitle("Câu 3. Trong 7 ngày gần nhất, mỗi tình huống dưới đây xảy ra với bạn bao nhiêu lần?")
    .setHelpText("Bắt buộc mỗi hàng. Không bật giới hạn một câu trả lời mỗi cột.")
    .setRows([
      "Muốn xem lại một ý đã học nhưng không tìm được đúng đoạn tài liệu hoặc video",
      "Đọc câu trả lời của tutor nhưng không tìm thấy đoạn nguồn để đối chiếu",
      "Đọc giải thích của tutor nhưng vẫn chưa hiểu phần mình đang vướng",
      "Tìm thông tin về hạn nộp, cách nộp, điểm danh hoặc XP nhưng chưa xác định được thông tin áp dụng cho mình",
      "Đã hỏi trên Discord nhưng chưa nhận được câu trả lời giúp mình tiếp tục công việc"
    ])
    .setColumns([
      "Không sử dụng/chưa có nhu cầu",
      "Có sử dụng/có nhu cầu nhưng không gặp",
      "1 lần",
      "2–3 lần",
      "4 lần trở lên",
      "Không nhớ"
    ])
    .setRequired(true);

  // Câu 4
  var item4 = form.addMultipleChoiceItem();
  item4.setTitle("Câu 4. Trong các tình huống đã gặp, tình huống nào ảnh hưởng đến việc học của bạn nhiều nhất?")
    .setRequired(true);

  // ==========================================
  // PHẦN 3 — KỂ VỀ LẦN GẦN NHẤT
  // ==========================================
  var sec3 = form.addPageBreakItem();
  sec3.setTitle("Phần 3 — Kể về lần gần nhất");
  sec3.setHelpText("Mô tả phần: Hãy trả lời về lần gần nhất bạn gặp tình huống vừa chọn, không cần kể tất cả các lần.");

  var item5 = form.addParagraphTextItem();
  item5.setTitle("Câu 5. Khi đó bạn đang muốn hoàn thành việc gì, và đã vướng ở đâu?")
    .setHelpText("Bạn có thể ghi chủ đề, loại bài tập hoặc thông tin cần tìm. Không cần gửi nội dung riêng tư hay chép hội thoại của người khác.")
    .setRequired(true);

  var item6 = form.addCheckboxItem();
  item6.setTitle("Câu 6. Bạn đã làm những gì để giải quyết lần đó?")
    .setChoiceValues([
      "Tìm lại trong slide/tài liệu",
      "Tua hoặc xem lại video",
      "Hỏi hoặc hỏi lại tutor trên VLearn",
      "Tìm kiếm thông báo/tin nhắn Discord",
      "Hỏi bot Discord",
      "Hỏi bạn học",
      "Hỏi TA/giảng viên/BTC",
      "Tìm trên web hoặc công cụ AI khác",
      "Tạm dừng/chưa tìm cách xử lý"
    ])
    .showOtherOption(true)
    .setRequired(true);

  var item7 = form.addMultipleChoiceItem();
  item7.setTitle("Câu 7. Bạn đã dành khoảng bao nhiêu thời gian trực tiếp tìm hoặc thử cách xử lý?")
    .setHelpText("Mô tả: Không tính thời gian chờ người khác phản hồi.")
    .setChoiceValues([
      "Dưới 2 phút",
      "Từ 2 đến dưới 5 phút",
      "Từ 5 đến dưới 15 phút",
      "Từ 15 đến dưới 30 phút",
      "Từ 30 phút trở lên",
      "Không nhớ"
    ])
    .setRequired(true);

  var item8 = form.addMultipleChoiceItem();
  item8.setTitle("Câu 8. Kết quả cuối cùng của lần đó là gì?")
    .setChoiceValues([
      "Giải quyết xong và tiếp tục được công việc",
      "Giải quyết được một phần",
      "Có câu trả lời nhưng vẫn chưa chắc đúng",
      "Chưa giải quyết được",
      "Không còn cần giải quyết"
    ])
    .showOtherOption(true)
    .setRequired(true);

  var item9 = form.addCheckboxItem();
  item9.setTitle("Câu 9. Lần đó đã gây ra những ảnh hưởng nào?")
    .setHelpText("Mô tả: Chỉ chọn điều thực sự xảy ra. Nếu chọn “Không có ảnh hưởng đáng kể”, không chọn các mục khác.")
    .setChoiceValues([
      "Mất thêm thời gian nhưng vẫn hoàn thành như dự kiến",
      "Phải nhờ người khác hỗ trợ",
      "Phải sửa hoặc làm lại một phần công việc",
      "Phải hoãn hoặc bỏ dở việc đang làm",
      "Bỏ lỡ một mốc cần thực hiện",
      "Không có ảnh hưởng đáng kể"
    ])
    .showOtherOption(true)
    .setRequired(true);

  var item10 = form.addParagraphTextItem();
  item10.setTitle("Câu 10. Cụ thể điều gì khiến cách bạn đã thử chưa hiệu quả? Nếu đã giải quyết được, điều gì đã giúp bạn?")
    .setRequired(false);

  // ==========================================
  // PHẦN 4 — BỔ SUNG VÀ ĐĂNG KÝ DÙNG THỬ
  // ==========================================
  var sec4 = form.addPageBreakItem();
  sec4.setTitle("Phần 4 — Bổ sung và đăng ký dùng thử");

  var item11 = form.addParagraphTextItem();
  item11.setTitle("Câu 11. Có khó khăn nào khác trong việc học của khóa mà form chưa đề cập?")
    .setHelpText("Nếu có, hãy kể một lần cụ thể gần đây.")
    .setRequired(false);

  var item12 = form.addMultipleChoiceItem();
  item12.setTitle("Câu 12. Bạn có đồng ý để nhóm liên hệ mời thử một bản mẫu trong khoảng 10 phút trước buổi demo không?")
    .setRequired(true);

  // ==========================================
  // PHẦN 5 — THÔNG TIN LIÊN HỆ TỰ NGUYỆN
  // ==========================================
  var sec5 = form.addPageBreakItem();
  sec5.setTitle("Phần 5 — Thông tin liên hệ tự nguyện");

  var item13 = form.addTextItem();
  item13.setTitle("Câu 13. Tên hoặc biệt danh và một cách liên hệ thuận tiện với bạn?")
    .setHelpText("Ví dụ: tên Discord hoặc email. Thông tin này chỉ dùng để hẹn thử, không đưa vào repo công khai.")
    .setRequired(true);

  var item14 = form.addTextItem();
  item14.setTitle("Câu 14. Bạn thuận tiện thử vào khoảng thời gian nào trước buổi demo?")
    .setRequired(false);

  // ==========================================
  // THIẾT LẬP CÁC LỰA CHỌN & RẼ NHÁNH (Sau khi đã có đầy đủ các Section)
  // ==========================================
  item1.setChoices([
    item1.createChoice("3A", FormApp.PageNavigationType.CONTINUE),
    item1.createChoice("3B", FormApp.PageNavigationType.CONTINUE),
    item1.createChoice("Lớp khác trong AI20k", FormApp.PageNavigationType.CONTINUE),
    item1.createChoice("Không phải học viên AI20k", FormApp.PageNavigationType.SUBMIT)
  ]);

  item4.setChoices([
    item4.createChoice("Tìm lại nội dung đã học", FormApp.PageNavigationType.CONTINUE),
    item4.createChoice("Tìm nguồn để kiểm chứng câu trả lời của tutor", FormApp.PageNavigationType.CONTINUE),
    item4.createChoice("Hiểu phần kiến thức còn vướng sau khi hỏi tutor", FormApp.PageNavigationType.CONTINUE),
    item4.createChoice("Xác định thông tin hành chính áp dụng cho mình", FormApp.PageNavigationType.CONTINUE),
    item4.createChoice("Nhận được hỗ trợ hữu ích sau khi hỏi trên Discord", FormApp.PageNavigationType.CONTINUE),
    item4.createChoice("Một khó khăn khác", FormApp.PageNavigationType.CONTINUE),
    item4.createChoice("Không gặp khó khăn nào", sec4)
  ]);

  item12.setChoices([
    item12.createChoice("Có", sec5),
    item12.createChoice("Chưa chắc, có thể liên hệ để trao đổi thêm", sec5),
    item12.createChoice("Không", FormApp.PageNavigationType.SUBMIT)
  ]);

  Logger.log("=== TẠO FORM THÀNH CÔNG ===");
  Logger.log("Link chỉnh sửa (Edit URL): " + form.getEditUrl());
  Logger.log("Link gửi học viên (Published URL): " + form.getPublishedUrl());
}
