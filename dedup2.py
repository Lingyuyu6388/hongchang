html = open(r"C:\Users\Administrator\Documents\Codex\2026-07-17\gu\outputs\hongchang-site\original.html", "r", encoding="utf-8").read()

script_start = html.index("<script>") + 8
script_end = html.rfind("</script>")
js = html[script_start:script_end]

# 找到所有 </script> 的位置（在 JS 内容里的）
# 实际上只有一个真正的 </script> 标签
# 我们需要找到重复的模式

# 找 DOMContentLoaded 结束
dom_end = js.find("}); // DOMContentLoaded end")

# 取到 DOMContentLoaded 结束的内容
clean_js = js[:dom_end + len("}); // DOMContentLoaded end")]

# 验证
op_count = clean_js.count("function openPopup")
print(f"openPopup count: {op_count}")
print(f"closePopup count: {clean_js.count('function closePopup')}")
print(f"changePopupImg count: {clean_js.count('function changePopupImg')}")
print(f"changeDrillBox count: {clean_js.count('function changeDrillBox')}")
print(f"clean_js length: {len(clean_js)}")

# 写入
new_html = html[:script_start] + clean_js + html[script_end:]
open(r"C:\Users\Administrator\Documents\Codex\2026-07-17\gu\outputs\hongchang-site\index.html", "w", encoding="utf-8").write(new_html)
print("Done")
