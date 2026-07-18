html = open(r"C:\Users\Administrator\Documents\Codex\2026-07-17\gu\outputs\hongchang-site\index.html", "r", encoding="utf-8").read()

# 找到真正的 </script> 标签（HTML 结构的，不是 JS 内容里的）
# 方法：从后往前找 </script> 后面紧跟 </body> 的那个
idx = html.rfind("</script>")
while idx > 0:
    rest = html[idx + 9:].strip()
    if rest.startswith("</body>"):
        break
    idx = html.rfind("</script>", 0, idx)

if idx > 0:
    popup = """
    <div class="product-popup" id="productPopup">
        <div class="popup-overlay" onclick="closePopup()"></div>
        <div class="popup-content">
            <span class="popup-close" onclick="closePopup()">&#10005;</span>
            <h2 data-zh="钻头包装盒" data-en="Drill Bit Box">钻头包装盒</h2>
            <div class="popup-main-img">
                <img id="popupMainImg" src="images/drill-box-1.jpg" alt="钻头包装盒">
            </div>
            <div class="popup-thumbs">
                <img src="images/drill-box-1.jpg" onclick="changePopupImg(0)" class="popup-thumb active">
                <img src="images/drill-box-2.jpg" onclick="changePopupImg(1)" class="popup-thumb">
                <img src="images/drill-box-3.jpg" onclick="changePopupImg(2)" class="popup-thumb">
                <img src="images/drill-box-4.jpg" onclick="changePopupImg(3)" class="popup-thumb">
            </div>
            <p class="popup-desc" data-zh="优质塑胶材质，多规格收纳，防尘防水，携带方便" data-en="High-quality plastic material, multi-specification storage, dustproof and waterproof, easy to carry">优质塑胶材质，多规格收纳，防尘防水，携带方便</p>
        </div>
    </div>
"""
    # 先移除已有的弹窗（如果在 </body> 之前）
    body_idx = html.rfind("</body>")
    popup_start = html.find('product-popup')
    if popup_start > 0 and popup_start < body_idx:
        popup_end = html.find("</div>", popup_start + 100) + 6
        html = html[:popup_start] + html[popup_end:]
    
    # 在 </script> 之后插入弹窗
    html = html[:idx + 9] + "\n" + popup + html[idx + 9:]
    open(r"C:\Users\Administrator\Documents\Codex\2026-07-17\gu\outputs\hongchang-site\index.html", "w", encoding="utf-8").write(html)
    print(f"OK: popup at {html.find('product-popup')}, script_end at {html.rfind('</script>')}")
else:
    print("ERROR: cannot find </script> before </body>")
