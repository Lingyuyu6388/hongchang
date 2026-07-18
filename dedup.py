html = open(r"C:\Users\Administrator\Documents\Codex\2026-07-17\gu\outputs\hongchang-site\clean_bak.html", "r", encoding="utf-8").read()

# 找到 <script> 和 </script>
script_start = html.index("<script>") + 8
script_end = html.rfind("</script>")
js = html[script_start:script_end]

# 找到 DOMContentLoaded 结束
dom_end = js.find("}); // DOMContentLoaded end")
if dom_end == -1:
    print("ERROR: no DOMContentLoaded end")
    exit()

# 取第一部分（到 DOMContentLoaded 结束）
first_part = js[:dom_end + len("}); // DOMContentLoaded end")]

# 验证第一部分不包含重复函数
test_js = first_part
func_count = test_js.count("function openPopup")
print(f"openPopup count in first part: {func_count}")

# 构建新 HTML
new_html = html[:script_start] + first_part + html[script_end:]
open(r"C:\Users\Administrator\Documents\Codex\2026-07-17\gu\outputs\hongchang-site\index.html", "w", encoding="utf-8").write(new_html)
print(f"Done. New JS length: {len(first_part)}")
