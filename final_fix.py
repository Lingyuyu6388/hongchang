html = open(r"C:\Users\Administrator\Documents\Codex\2026-07-17\gu\outputs\hongchang-site\clean_bak.html", "r", encoding="utf-8").read()

# 找到 <script> 标签
script_start = html.index("<script>") + 8
script_end = html.rfind("</script>")
js = html[script_start:script_end]

# 找到唯一的 DOMContentLoaded 结束
dom_end = js.find("}); // DOMContentLoaded end")
if dom_end == -1:
    print("ERROR")
    exit()

dom_inside = js[:dom_end + len("}); // DOMContentLoaded end")]
dom_outside = js[dom_end + len("}); // DOMContentLoaded end"):]

# 提取函数（每个只提取第一次出现的）
funcs = ["function openPopup", "function closePopup", "function changePopupImg", "function changeDrillBox"]
extracted = {}
seen = set()

for fname in funcs:
    if fname in seen:
        continue
    idx = dom_inside.find(fname)
    if idx == -1:
        print(f"Not found: {fname}")
        continue
    seen.add(fname)
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

new_js = dom_inside + "\n\n" + "\n\n".join(extracted.values()) + "\n\n" + dom_outside
new_html = html[:script_start] + new_js + html[script_end:]
open(r"C:\Users\Administrator\Documents\Codex\2026-07-17\gu\outputs\hongchang-site\index.html", "w", encoding="utf-8").write(new_html)
print(f"Extracted: {list(extracted.keys())}")
