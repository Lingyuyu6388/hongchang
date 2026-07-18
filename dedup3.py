html = open(r"C:\Users\Administrator\Documents\Codex\2026-07-17\gu\outputs\hongchang-site\original.html", "r", encoding="utf-8").read()

script_start = html.index("<script>") + 8
script_end = html.rfind("</script>")
js = html[script_start:script_end]

# 取到第一个完整的周期：DOMContentLoaded + 所有唯一函数
dom_end = js.find("}); // DOMContentLoaded end")
after_dom = js[dom_end + len("}); // DOMContentLoaded end"):]

# 找到第一个重复的 function changeDrillBox
first_cd = after_dom.find("function changeDrillBox")
second_cd = after_dom.find("function changeDrillBox", first_cd + 1)

if second_cd > 0:
    clean_after = after_dom[:second_cd]
else:
    clean_after = after_dom

# 构建完整 JS
clean_js = js[:dom_end + len("}); // DOMContentLoaded end")] + clean_after

# 验证
print(f"openPopup: {clean_js.count('function openPopup')}")
print(f"closePopup: {clean_js.count('function closePopup')}")
print(f"changePopupImg: {clean_js.count('function changePopupImg')}")
print(f"changeDrillBox: {clean_js.count('function changeDrillBox')}")
print(f"clean_js length: {len(clean_js)}")

new_html = html[:script_start] + clean_js + html[script_end:]
open(r"C:\Users\Administrator\Documents\Codex\2026-07-17\gu\outputs\hongchang-site\index.html", "w", encoding="utf-8").write(new_html)
print("Done")
