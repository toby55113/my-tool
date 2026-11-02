import sys
from collections import defaultdict
import openpyxl

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")


def main():
    input_file = "管線資料.xlsx"
    output_file = "統計結果.xlsx"

    wb = openpyxl.load_workbook(input_file, data_only=True)
    ws = wb.active

    rows = list(ws.iter_rows(values_only=True))
    if not rows:
        print("檔案中沒有資料。")
        return

    header = [str(col).strip() if col is not None else "" for col in rows[0]]
    idx_diameter = header.index("管徑")
    idx_length = header.index("長度")

    stats = defaultdict(lambda: {"count": 0, "total_length": 0.0})

    for row in rows[1:]:
        if not row or row[idx_diameter] is None:
            continue
        diameter = row[idx_diameter]
        length = float(row[idx_length]) if row[idx_length] is not None else 0.0
        stats[diameter]["count"] += 1
        stats[diameter]["total_length"] += length

    # 建立輸出 Excel
    out_wb = openpyxl.Workbook()
    out_ws = out_wb.active
    out_ws.title = "管徑統計結果"

    out_ws.append(["管徑", "數量", "總長度"])

    print(f"{'管徑':<10} | {'數量':<8} | {'總長度':<12}")
    print("-" * 36)

    for diameter in sorted(stats.keys(), key=lambda x: (float(x) if isinstance(x, (int, float)) else str(x))):
        count = stats[diameter]["count"]
        total_len = stats[diameter]["total_length"]
        if total_len.is_integer():
            total_len = int(total_len)
        else:
            total_len = round(total_len, 4)

        out_ws.append([diameter, count, total_len])
        print(f"{str(diameter):<10} | {count:<8} | {total_len:<12}")

    out_wb.save(output_file)
    print(f"\n已成功輸出至 {output_file}")


if __name__ == "__main__":
    main()
