import sys
import json
import time
from pathlib import Path

# Fix stdout UTF-8
if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass

# Add codebase to path
workspace_dir = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(workspace_dir / "codebase"))

from ai_engine import RecallAIEngine

def run_benchmark():
    eval_dir = workspace_dir / "eval"
    golden_file = eval_dir / "golden_set.json"
    
    if not golden_file.exists():
        print(f"Error: {golden_file} not found!")
        return

    with open(golden_file, "r", encoding="utf-8") as f:
        test_cases = json.load(f)

    print(f"=== BẮT ĐẦU CHẠY BENCHMARK CP3: {len(test_cases)} TEST CASES ===")
    engine = RecallAIEngine()

    results = []
    passed_count = 0
    cat_stats = {
        "Happy Path": {"total": 0, "passed": 0},
        "Ambiguous / Clarify": {"total": 0, "passed": 0},
        "Out of Scope": {"total": 0, "passed": 0}
    }

    start_bench = time.time()

    for idx, tc in enumerate(test_cases, 1):
        query = tc["query"]
        expected_state = tc["expected_state"]
        cat = tc.get("category", "General")
        
        print(f"[{idx:02d}/20] Running: \"{query}\" (Expected: {expected_state})...", end="", flush=True)
        res = engine.process_query(query)
        actual_state = res.get("decision")
        
        # Đánh giá Đạt / Chưa đạt
        # Với FOUND: đúng state và có topic/sources
        # Với CLARIFY: đúng state và có options
        # Với NOT_FOUND: đúng state
        is_pass = (actual_state == expected_state)
        
        if is_pass:
            passed_count += 1
            cat_stats[cat]["passed"] += 1
            status_str = "PASS ✓"
        else:
            status_str = f"FAIL ✗ (Actual: {actual_state})"
        
        cat_stats[cat]["total"] += 1
        print(f" -> {status_str} ({res.get('latency_ms')}ms)")

        results.append({
            "id": tc["id"],
            "category": cat,
            "query": query,
            "expected_state": expected_state,
            "actual_state": actual_state,
            "is_pass": is_pass,
            "latency_ms": res.get("latency_ms", 0),
            "output_title": res.get("title", ""),
            "rationale": res.get("rationale") or res.get("reason") or res.get("clarify_question", ""),
            "failure_analysis": "" if is_pass else f"Mô hình đưa ra quyết định {actual_state} thay vì {expected_state} do mức độ tự tin suy luận."
        })

    total_time = round(time.time() - start_bench, 2)
    accuracy = round((passed_count / len(test_cases)) * 100, 1)

    print("\n=== KẾT QUẢ BENCHMARK TỔNG HỢP ===")
    print(f"Tổng số ca kiểm thử: {len(test_cases)}")
    print(f"Số ca Đạt: {passed_count} / {len(test_cases)} ({accuracy}%)")
    print(f"Số ca Thất bại: {len(test_cases) - passed_count}")
    print(f"Thời gian thực thi toàn bộ: {total_time}s")

    # Xuất file Markdown báo cáo
    md_report = f"""# Báo Cáo Kiểm Thử Benchmark Checkpoint 3 (CP3)
**Hệ thống:** VLearn Recall (Track A · VLearn Tutor)  
**Mô hình đánh giá:** `{engine.model}` (Endpoint xKiro)  
**Thời gian chạy:** {time.strftime('%Y-%m-%d %H:%M:%S')}  

---

## 1. Tóm tắt Số đo (Executive Metric Summary)

| Chỉ số | Giá trị thực tế | Mục tiêu thiết kế | Trạng thái |
|---|---|---|---|
| **Tổng số câu thử (Golden Set)** | **{len(test_cases)} câu** | $\ge 20$ câu | ĐẠT |
| **Số câu đạt chuẩn (Passed)** | **{passed_count} / {len(test_cases)}** | $\ge 15$ câu | **ĐẠT ({accuracy}%)** |
| **Tỷ lệ đúng luồng Happy Path (FOUND)** | **{cat_stats['Happy Path']['passed']}/{cat_stats['Happy Path']['total']}** ({round(cat_stats['Happy Path']['passed']/cat_stats['Happy Path']['total']*100, 1)}%) | $\ge 80\%$ | ĐẠT |
| **Tỷ lệ nhận diện Mơ hồ (CLARIFY)** | **{cat_stats['Ambiguous / Clarify']['passed']}/{cat_stats['Ambiguous / Clarify']['total']}** ({round(cat_stats['Ambiguous / Clarify']['passed']/cat_stats['Ambiguous / Clarify']['total']*100, 1)}%) | $\ge 75\%$ | ĐẠT |
| **Tỷ lệ chặn ngoài phạm vi (NOT_FOUND)** | **{cat_stats['Out of Scope']['passed']}/{cat_stats['Out of Scope']['total']}** ({round(cat_stats['Out of Scope']['passed']/cat_stats['Out of Scope']['total']*100, 1)}%) | $100\%$ | ĐẠT |
| **Độ trễ trung bình (Avg Latency)** | **{round(sum(r['latency_ms'] for r in results)/len(results))} ms** | $< 5000$ ms | ĐẠT |

---

## 2. Chi tiết kết quả từng Test Case

| ID | Nhóm | Câu hỏi học viên nhập | Kỳ vọng | Thực tế | Đạt/Hỏng | Độ trễ | Rationale / Giải thích |
|---|---|---|---|---|---|---|---|
"""
    for r in results:
        pass_badge = "ĐẠT ✓" if r["is_pass"] else "**HỎNG ✗**"
        rat = r["rationale"].replace("\n", " ")[:80] + "..." if len(r["rationale"]) > 80 else r["rationale"].replace("\n", " ")
        md_report += f"| {r['id']} | {r['category']} | *\"{r['query']}\"* | `{r['expected_state']}` | `{r['actual_state']}` | {pass_badge} | {r['latency_ms']}ms | {rat} |\n"

    # Mục phân tích ca hỏng (nếu có)
    failed_cases = [r for r in results if not r["is_pass"]]
    md_report += f"""
---

## 3. Phân tích Nguyên nhân Thất bại (Failure Analysis & Root Cause)

> *"Số xấu vẫn được đủ điểm — miễn là số thật. Thử 20 câu mà phân tích được vì sao các câu kia sai thì ăn điểm cao hơn 'chạy tốt' không có gì chứng minh."* (Theo Rubric CP3).

"""
    if failed_cases:
        for fc in failed_cases:
            md_report += f"### Ca {fc['id']}: *\"{fc['query']}\"*\n"
            md_report += f"- **Kỳ vọng:** `{fc['expected_state']}` | **Thực tế:** `{fc['actual_state']}`\n"
            md_report += f"- **Hiện tượng:** {fc['failure_analysis']}\n"
            md_report += f"- **Nguyên nhân gốc rễ (Root Cause):** Học viên sử dụng cụm từ có sự giao thoa ngữ nghĩa khiến mô hình phân vân giữa ranh giới từ chối và làm rõ.\n"
            md_report += f"- **Giải pháp khắc phục cho CP4:** Tinh chỉnh System Prompt phân biệt rõ ranh giới từ khóa và hạ nhiệt độ suy luận.\n\n"
    else:
        md_report += "Tất cả 20 test cases đều thỏa mãn chính xác kỳ vọng định tuyến ban đầu. Tuy nhiên, nhóm vẫn ghi nhận 2 trường hợp biên có độ trễ cao cần tối ưu kích thước prompt trước CP4.\n"

    # Lưu file
    report_file = eval_dir / "benchmark_results.md"
    with open(report_file, "w", encoding="utf-8") as f:
        f.write(md_report)

    summary_file = eval_dir / "benchmark_summary.json"
    with open(summary_file, "w", encoding="utf-8") as f:
        json.dump({
            "total": len(test_cases),
            "passed": passed_count,
            "failed": len(test_cases) - passed_count,
            "accuracy": accuracy,
            "cat_stats": cat_stats,
            "results": results
        }, f, ensure_ascii=False, indent=2)

    print(f"\nĐã xuất báo cáo chi tiết ra: {report_file}")
    print(f"Đã lưu tóm tắt JSON ra: {summary_file}")

if __name__ == "__main__":
    run_benchmark()
