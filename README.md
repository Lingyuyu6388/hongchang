# 宏昌塑胶 - 独立站

这是一个为宏昌塑胶制作的静态产品展示网站。

## 文件结构

`
hongchang-site/
├── index.html      # 主页面
├── css/
│   └── style.css   # 样式文件
├── js/
│   └── main.js     # 交互脚本
└── README.md       # 说明文档
`

## 如何预览

直接双击打开 index.html 文件即可在浏览器中预览网站。

## 如何部署到 GitHub Pages

### 第一步：创建 GitHub 仓库

1. 登录你的 GitHub 账号：https://github.com
2. 点击右上角 "+" 号，选择 "New repository"
3. 仓库名称填写：hongchang（或其他你喜欢的名字）
4. 设置为 Public（公开）
5. 点击 "Create repository"

### 第二步：上传文件

方法一（推荐新手）：
1. 进入你创建的仓库页面
2. 点击 "uploading an existing file" 链接
3. 把所有文件拖进去上传
4. 点击 "Commit changes" 保存

方法二（用 Git 命令）：
`powershell
# 在你的电脑上打开 PowerShell
cd "C:\Users\Administrator\Documents\Codex\2026-07-17\gu\outputs\hongchang-site"
git init
git add .
git commit -m "初始版本"
git branch -M main
git remote add origin https://github.com/你的用户名/hongchang.git
git push -u origin main
`

### 第三步：开启 GitHub Pages

1. 进入仓库页面，点击 "Settings"
2. 左侧菜单找到 "Pages"
3. 在 "Source" 下选择 "main" 分支
4. 点击 "Save"
5. 等待约 2-3 分钟，你的网站就会上线了！

网址格式：https://你的用户名.github.io/hongchang/

## 如何修改产品

打开 index.html 文件，找到"产品中心"部分，修改以下内容：

- **产品名称**：修改 <h3>塑胶零件-A型</h3> 中的文字
- **产品描述**：修改 <p> 标签中的文字
- **产品图片**：把 <div class="product-img placeholder"> 改成 <img src="你的图片路径.jpg" alt="产品名称">

## 如何添加新产品

复制一个产品卡片模板，粘贴到 product-grid 里面：

`html
<div class="product-card">
    <div class="product-img placeholder"></div>
    <div class="product-info">
        <h3>新产品名称</h3>
        <p>产品描述文字</p>
        <span class="product-tag">标签</span>
    </div>
</div>
`

## 联系方式修改

在 index.html 中找到"联系我们"部分，修改对应的微信、电话、邮箱等信息。
