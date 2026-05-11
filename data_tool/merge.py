import json
import csv

# ---------- 配置 ----------
JSON_PATH = "tag_groups.json"
CSV_INPUT = "tags_enhanced.csv"
CSV_OUTPUT = "tags_with_groups.csv"
OUTPUT_ENCODING = "utf-8-sig"
GROUP_SEPARATOR = ","

# 按优先级排列的候选编码列表
CANDIDATE_ENCODINGS = ["utf-8-sig", "utf-8", "gb18030", "gbk", "gb2312", "utf-16", "latin-1"]


def detect_encoding(filepath: str) -> str:
    """依次尝试候选编码，返回第一个能完整解码的编码"""
    with open(filepath, "rb") as f:
        raw = f.read()
    for enc in CANDIDATE_ENCODINGS:
        try:
            raw.decode(enc)
            print(f"检测到文件编码：{enc}")
            return enc
        except (UnicodeDecodeError, UnicodeError):
            continue
    # 全部失败时兜底 latin-1（它能解码任意字节）
    print("未能确定编码，使用 latin-1 兜底")
    return "latin-1"


# ---------- 读取 JSON ----------
with open(JSON_PATH, "r", encoding="utf-8") as f:
    data = json.load(f)

tag_to_groups = data["tag_to_groups"]
group_cn_names = data["group_cn_names"]

# ---------- 自动检测 CSV 编码 ----------
input_encoding = detect_encoding(CSV_INPUT)

# ---------- 处理 CSV ----------
with open(CSV_INPUT, "r", encoding=input_encoding, newline="") as fin, \
     open(CSV_OUTPUT, "w", encoding=OUTPUT_ENCODING, newline="") as fout:

    reader = csv.DictReader(fin)
    fieldnames = reader.fieldnames + ["group"]
    writer = csv.DictWriter(fout, fieldnames=fieldnames, quoting=csv.QUOTE_MINIMAL)
    writer.writeheader()

    matched = 0
    total = 0

    for row in reader:
        total += 1
        tag_name = row["name"]
        groups = tag_to_groups.get(tag_name, [])
        cn_groups = [group_cn_names[g] for g in groups if g in group_cn_names]
        row["group"] = GROUP_SEPARATOR.join(cn_groups)
        writer.writerow(row)

        if cn_groups:
            matched += 1

print(f"完成！共处理 {total} 条，其中 {matched} 条匹配到分组。")
print(f"输出文件：{CSV_OUTPUT}")
