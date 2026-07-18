html = open(r"C:\Users\Administrator\Documents\Codex\2026-07-17\gu\outputs\hongchang-site\clean_bak.html", "r", encoding="utf-8").read()

script_start = html.index("<script>") + 8
script_end = html.rfind("</script>")
js = html[script_start:script_end]

# 找到 DOMContentLoaded 的结束
dom_end_marker = "}); // DOMContentLoaded end"
dom_end = js.find(dom_end_marker)
if dom_end == -1:
    print("ERROR: cannot find DOMContentLoaded end")
    exit()

dom_inside = js[:dom_end + len(dom_end_marker)]
dom_outside = js[dom_end + len(dom_end_marker):]

# 提取四个函数并移到外部
funcs_to_extract = ["function openPopup", "function closePopup", "function changePopupImg", "function changeDrillBox"]

extracted = {}
for fname in funcs_to_extract:
    idx = dom_inside.find(fname)
    if idx == -1:
        print(f"WARNING: {fname} not found")
        continue
    # 找到函数结束（匹配的括号）
    brace = 0
    started = False
    end_idx = idx
    for ci in range(idx, len(dom_inside)):
        if dom_inside[ci] == "{":
            brace += 1
            started = True
        elif dom_inside[ci] == "}":
            brace -= 1
            if started and brace == 0:
                end_idx = ci + 1
                break
    func_body = dom_inside[idx:end_idx]
    extracted[fname] = func_body
    dom_inside = dom_inside[:idx] + dom_inside[end_idx:]

# 构建新的 JS
new_js = dom_inside + "\n\n" + "\n\n".join(extracted.values()) + "\n\n" + dom_outside

# 替换
new_html = html[:script_start] + new_js + html[script_end:]
open(r"C:\Users\Administrator\Documents\Codex\2026-07-17\gu\outputs\hongchang-site\index.html", "w", encoding="utf-8").write(new_html)

print(f"Extracted {len(extracted)} functions:")
for k in extracted:
    print(f"  - {k}")
