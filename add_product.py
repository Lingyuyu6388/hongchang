import os

html_path = r'C:\Users\Administrator\Documents\Codex\2026-07-17\gu\outputs\hongchang-site\index.html'

with open(html_path, 'r', encoding='utf-8') as f:
    html = f.read()

new_card = '''                <div class="product-card fade-in">
                    <div class="product-badge" data-zh="热销" data-en="Hot">热销</div>
                    <div class="product-img">
                        <div class="drill-box-gallery">
                            <img src="images/drill-box-1.jpg" alt="钻头包装盒" class="gallery-main">
                            <div class="gallery-thumbs">
                                <img src="images/drill-box-1.jpg" alt="正面" class="thumb active" onclick="changeDrillBox(0)">
                                <img src="images/drill-box-2.jpg" alt="打开" class="thumb" onclick="changeDrillBox(1)">
                                <img src="images/drill-box-3.jpg" alt="内部" class="thumb" onclick="changeDrillBox(2)">
                                <img src="images/drill-box-4.jpg" alt="背面" class="thumb" onclick="changeDrillBox(3)">
                            </div>
                        </div>
                    </div>
                    <div class="product-info">
                        <h3 data-zh="钻头包装盒" data-en="Drill Bit Box">钻头包装盒</h3>
                        <p data-zh="优质塑胶材质，多规格收纳，防尘防水，携带方便" data-en="High-quality plastic material, multi-specification storage, dustproof and waterproof, easy to carry">优质塑胶材质，多规格收纳，防尘防水，携带方便</p>
                        <a href="#contact" class="product-contact" data-zh="了解详情 →" data-en="Learn More →">了解详情 →</a>
                    </div>
                </div>'''

idx = html.find('<div class="product-card fade-in">')
if idx > 0:
    html = html[:idx] + new_card + html[idx:]
    with open(html_path, 'w', encoding='utf-8') as f:
        f.write(html)
    print('产品卡片已添加成功')
else:
    print('未找到目标位置')
