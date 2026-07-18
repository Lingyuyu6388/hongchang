with open(r'C:\Users\Administrator\Documents\Codex\2026-07-17\gu\outputs\hongchang-site\index.html', 'r', encoding='utf-8') as f:
    html = f.read()

popup_start = html.find('<!-- 产品详情弹窗 -->')
popup_end = html.find('</body>')
popup_html = html[popup_start:popup_end]

html = html.replace(popup_html, '')

script_close = html.rfind('</script>')
html = html[:script_close+9] + '\n' + popup_html + '\n</body>\n</html>'

with open(r'C:\Users\Administrator\Documents\Codex\2026-07-17\gu\outputs\hongchang-site\index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print('Fixed')
