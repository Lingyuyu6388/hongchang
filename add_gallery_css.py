import os

# 读取 CSS
css_path = r'C:\Users\Administrator\Documents\Codex\2026-07-17\gu\outputs\hongchang-site\css\style.css'
with open(css_path, 'r', encoding='utf-8') as f:
    css = f.read()

# 添加画廊样式
gallery_css = '''
/* ===== 钻头包装盒画廊 ===== */
.drill-box-gallery {
    width: 100%;
    position: relative;
}
.gallery-main {
    width: 100%;
    height: 220px;
    object-fit: cover;
    display: block;
    transition: opacity 0.3s;
    border-radius: 0;
}
.gallery-thumbs {
    display: flex;
    gap: 4px;
    padding: 4px;
    background: #f5f5f5;
}
.gallery-thumbs img {
    width: 25%;
    height: 60px;
    object-fit: cover;
    cursor: pointer;
    border: 2px solid transparent;
    border-radius: 4px;
    transition: border-color 0.3s;
}
.gallery-thumbs img.active,
.gallery-thumbs img:hover {
    border-color: #2563eb;
}'''

# 在 </style> 之前插入
if '</style>' in css:
    css = css.replace('</style>', gallery_css + '\n    </style>')
    with open(css_path, 'w', encoding='utf-8') as f:
        f.write(css)
    print('CSS 样式已添加')
else:
    print('未找到 </style>')
