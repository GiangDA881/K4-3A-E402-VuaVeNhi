import os
import json
import time
from pathlib import Path
from dotenv import load_dotenv
from openai import OpenAI

# Load .env
workspace_dir = Path(__file__).resolve().parent.parent
load_dotenv(workspace_dir / ".env")

KB_PATH = Path(__file__).resolve().parent / "knowledge_base.json"

def load_kb():
    if KB_PATH.exists():
        with open(KB_PATH, "r", encoding="utf-8") as f:
            return json.load(f)
    return {"topics": {}}

class RecallAIEngine:
    def __init__(self):
        self.api_key = os.getenv("OPENAI_API_KEY")
        self.base_url = os.getenv("OPENAI_BASE_URL")
        self.model = os.getenv("LLM_MODEL", "mistralai/mistral-large-2512")
        self.kb = load_kb()
        
        self.client = OpenAI(
            api_key=self.api_key,
            base_url=self.base_url
        )

    def process_query(self, query: str) -> dict:
        start_time = time.time()
        topics_info = {}
        for k, v in self.kb.get("topics", {}).items():
            topics_info[k] = {
                "title": v["title"],
                "summary": v["summary"]
            }

        system_prompt = f"""Bạn là Bộ não Phân tích & Quyết định (Decision Engine) của hệ thống VLearn Recall — Trợ lý truy hồi tài liệu bài giảng cho học viên AI20k.

KHO CHỦ ĐỀ CHÍNH THỨC CỦA KHÓA HỌC:
{json.dumps(topics_info, ensure_ascii=False, indent=2)}

NHIỆM VỤ:
Phân tích mô tả của học viên và đưa ra đúng 1 quyết định trong 3 trạng thái sau:
1. "FOUND": Học viên đang tìm một kiến thức cụ thể CÓ TRONG kho bài giảng với độ tin cậy cao (dù học viên dùng từ ngữ dân dã, nhớ mang máng hay viết tắt).
   -> Chọn đúng `topic_key` phù hợp nhất.
   -> Viết `rationale`: 1-2 câu giải thích vì sao chủ đề này giải quyết đúng nhu cầu học viên.
2. "CLARIFY": Câu hỏi quá ngắn (dưới 8 từ), đa nghĩa, thiếu thực thể hoặc ngữ cảnh cụ thể để xác định chính xác bài giảng đích (ví dụ: chỉ nhập một thuật ngữ đơn lẻ, câu hỏi mơ hồ không rõ chủ đề hoặc bài thực hành nào).
   -> Đưa ra `clarify_question`: Câu hỏi định hướng ngắn gọn.
   -> Đưa ra `clarify_options`: Danh sách 2-3 lựa chọn cụ thể, mỗi lựa chọn gồm `label` (mô tả ngắn) và `target_topic` (chủ đề tương ứng).
3. "NOT_FOUND": Câu hỏi hoàn toàn nằm NGOÀI phạm vi khóa học AI20k (ví dụ: tiền ảo Bitcoin, làm web Django, thuật toán Leetcode, tán gẫu thời tiết).
   -> Đưa ra `reason`: Giải thích lịch sự vì sao nội dung này không nằm trong 6 bài giảng chính thức (12 cụm chủ đề tra cứu).
   -> Đưa ra `suggested_keywords`: Gợi ý 2-3 từ khóa có trong khóa học để học viên thử lại.

YÊU CẦU BẮT BUỘC:
- Chỉ trả về duy nhất 1 JSON object hợp lệ. Không viết thêm markdown hay lời chào.
- Cấu trúc JSON:
{{
  "decision": "FOUND" | "CLARIFY" | "NOT_FOUND",
  "topic_key": "<tên topic nếu FOUND>",
  "rationale": "<lý do nếu FOUND>",
  "clarify_question": "<câu hỏi nếu CLARIFY>",
  "clarify_options": [
    {{"label": "<tiêu đề lựa chọn>", "target_topic": "<topic_key>"}}
  ],
  "reason": "<lý do từ chối nếu NOT_FOUND>",
  "suggested_keywords": ["keyword 1", "keyword 2"]
}}
"""

        try:
            resp = self.client.chat.completions.create(
                model=self.model,
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": query}
                ],
                temperature=0.1,
                max_tokens=400,
                response_format={"type": "json_object"}
            )
            raw_content = resp.choices[0].message.content.strip()
            parsed = json.loads(raw_content)
        except Exception as e:
            # Fallback nếu API có sự cố định dạng
            parsed = self._rule_based_fallback(query)
            parsed["fallback_note"] = f"API error handled: {str(e)}"

        latency_ms = int((time.time() - start_time) * 1000)
        decision = parsed.get("decision", "NOT_FOUND").upper()

        result = {
            "query": query,
            "decision": decision,
            "latency_ms": latency_ms,
            "timestamp": time.strftime("%Y-%m-%d %H:%M:%S")
        }

        if decision == "FOUND":
            tkey = parsed.get("topic_key")
            topic_data = self.kb.get("topics", {}).get(tkey)
            if topic_data:
                result["topic_key"] = tkey
                result["title"] = topic_data["title"]
                result["summary"] = topic_data["summary"]
                result["sources"] = topic_data["sources"]
                result["rationale"] = parsed.get("rationale", "")
            else:
                # Nếu LLM sinh key không tồn tại, chuyển về clarify
                result["decision"] = "CLARIFY"
                result["clarify_question"] = "Chưa xác định chính xác chủ đề, bạn có ý tìm một trong các phần sau?"
                result["clarify_options"] = [
                    {"label": "ReAct Agent", "target_topic": "react_pattern"},
                    {"label": "Tools Schema", "target_topic": "tool_schema"}
                ]
        elif decision == "CLARIFY":
            result["clarify_question"] = parsed.get("clarify_question", "Bạn đang tìm nội dung cụ thể nào?")
            result["clarify_options"] = parsed.get("clarify_options", [])
        else:
            result["decision"] = "NOT_FOUND"
            result["reason"] = parsed.get("reason", "Nội dung này nằm ngoài phạm vi 6 bài giảng chính thức của khóa học.")
            result["suggested_keywords"] = parsed.get("suggested_keywords", ["ReAct", "Tool calling", "Context"])

        return result

    def _rule_based_fallback(self, query: str) -> dict:
        q = query.lower()
        if any(w in q for w in ["bitcoin", "django", "leetcode", "thời tiết"]):
            return {"decision": "NOT_FOUND", "reason": "Nội dung ngoài bài giảng AI20k"}
        if "context" in q:
            return {
                "decision": "CLARIFY",
                "clarify_question": "Bạn muốn tìm loại context nào?",
                "clarify_options": [
                    {"label": "Giữ ngữ cảnh qua nhiều lượt", "target_topic": "context_carryover"},
                    {"label": "Giới hạn Context Window", "target_topic": "context_window"}
                ]
            }
        return {"decision": "FOUND", "topic_key": "react_pattern", "rationale": "Phát hiện chủ đề liên quan ReAct"}

if __name__ == "__main__":
    import sys
    sys.stdout.reconfigure(encoding="utf-8")
    engine = RecallAIEngine()
    test_q = "đoạn agent suy nghĩ rồi gọi tool trong bài ReAct"
    print(f"Testing Query: {test_q}")
    res = engine.process_query(test_q)
    print(json.dumps(res, ensure_ascii=False, indent=2))
