html_path = r"C:\Users\Administrator\Documents\Codex\2026-07-17\gu\outputs\hongchang-site\index.html"
html = open(html_path, "r", encoding="utf-8").read()

# 找到 <script> 和 </script> 之间的 JS 代码
script_start = html.index("<script>") + 8
script_end = html.rfind("</script>")
js_code = html[script_start:script_end]

# 找到 DOMContentLoaded 块的结束位置
dom_end = js_code.rfind("}); // DOMContentLoaded end")
if dom_end == -1:
    dom_end = js_code.rfind("});")

# 提取 DOMContentLoaded 内部的 JS
dom_inside = js_code[:dom_end + len("}); // DOMContentLoaded end")]

# 提取 DOMContentLoaded 外部的 JS（全局函数）
dom_outside = js_code[dom_end + len("}); // DOMContentLoaded end"):]

# 找出需要移到外部的函数
global_funcs = []
remaining_inside = []
inside_lines = dom_inside.split("\n")
brace_count = 0
in_func = False
func_start = 0
func_name = ""

for i, line in enumerate(inside_lines):
    stripped = line.strip()
    if stripped.startswith("function openPopup") or stripped.startswith("function closePopup") or stripped.startswith("function changePopupImg") or stripped.startswith("function changeDrillBox"):
        func_name = stripped.split("(")[0].replace("function ", "")
        in_func = True
        func_start = i
        brace_count = 0
    
    if in_func:
        brace_count += stripped.count("{") - stripped.count("}")
        if brace_count <= 0 and "{" in "".join(inside_lines[func_start:i+1]):
            # 函数结束
            func_block = "\n".join(inside_lines[func_start:i+1])
            global_funcs.append(func_block)
            in_func = False
    
    if not in_func:
        remaining_inside.append(line)

# 构建新的 JS
new_dom_inside = "\n".join(remaining_inside)
new_global_funcs = "\n\n".join(global_funcs)
new_js = new_dom_inside + "\n\n" + new_global_funcs + "\n\n" + dom_outside

# 替换 HTML 中的脚本
new_html = html[:script_start] + new_js + html[script_end:]
open(html_path, "w", encoding="utf-8").write(new_html)

print(f"Global funcs extracted: {len(global_funcs)}")
for gf in global_funcs:
    print(f"  - {gf.split(chr(10))[0]}")
