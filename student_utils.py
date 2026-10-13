# -*- coding: utf-8 -*-
"""学生记录解析模块。"""


def parse_student(line):
    """把一行 CSV 文本解析为 {"name": str, "score": int}。无效记录抛 ValueError。"""
    parts = line.rstrip("\n").split(",")
    if len(parts) != 2:
        raise ValueError(f"字段数量应为 2，实际为 {len(parts)}：{line!r}")

    name, raw_score = parts[0].strip(), parts[1].strip()
    if not name:
        raise ValueError(f"姓名不能为空：{line!r}")

    try:
        score = int(raw_score)
    except ValueError:
        raise ValueError(f"成绩不是整数：{raw_score!r}") from None

    if not 0 <= score <= 100:
        raise ValueError(f"成绩超出 0~100 范围：{score}")

    return {"name": name, "score": score}
