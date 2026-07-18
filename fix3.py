import re

html_path = r"C:\Users\Administrator\Documents\Codex\2026-07-17\gu\outputs\hongchang-site\index.html"
html = open(html_path, "r", encoding="utf-8").read()

# 移除所有已有的 product-popup 内容
html = re.sub(r'<!-- 产品详情弹窗 -->.*?<div class="product-popup".*?</div>\s*</div>\s*</div>', '', html, flags=re.DOTALL)

# 找到 </script> 标签（最后一个）
script_match = re.search(r'</script>', html)
if script_match:
    script_end = script_match.end()
    popup = '''
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
'''
    html = html[:script_end] + popup + html[script_end:]
    open(html_path, "w", encoding="utf-8").write(html)
    print("OK: popup inserted after </script>")
    # 验证
    popup_idx = html.find('product-popup')
    script_end_idx = html.rfind('</script>')
    print(f"Popup at {popup_idx}, script end at {script_end_idx}")
    print(f"After script: {popup_idx > script_end_idx}")
else:
    print("ERROR: no </script> found")
