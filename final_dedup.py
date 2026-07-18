html = open(r"C:\Users\Administrator\Documents\Codex\2026-07-17\gu\outputs\hongchang-site\index.html", "r", encoding="utf-8").read()

# 找到第二个 drillBoxImages 并删除它
first = html.find("const drillBoxImages")
second = html.find("const drillBoxImages", first + 1)

if second > 0:
    # 找到第二个 const drillBoxImages 所在行的末尾
    line_end = html.find("];", second) + 2
    # 找到下一个换行
    next_line = html.find("\n", line_end)
    # 删除从 const 到下一个换行
    html = html[:second] + html[next_line:]
    open(r"C:\Users\Administrator\Documents\Codex\2026-07-17\gu\outputs\hongchang-site\index.html", "w", encoding="utf-8").write(html)
    print(f"Removed duplicate at position {second}")
else:
    print("No duplicate found")

# 验证
html2 = open(r"C:\Users\Administrator\Documents\Codex\2026-07-17\gu\outputs\hongchang-site\index.html", "r", encoding="utf-8").read()
print(f"Remaining drillBoxImages count: {html2.count('const drillBoxImages')}")
print(f"Remaining openPopup count: {html2.count('function openPopup')}")
