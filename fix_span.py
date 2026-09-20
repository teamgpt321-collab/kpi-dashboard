import re

with open("/home/tiendv1/kpi-dashboard/telebot/tools/bypass/bypass.py", "r") as f:
    content = f.read()

old_js = """let items = Array.from(document.querySelectorAll('li.k-item'));
                let target = items.find(i => i.innerText.trim().toLowerCase() === 'bo gong');"""

new_js = """let items = Array.from(document.querySelectorAll('li.k-item, span.k-input, div.k-item'));
                let target = items.find(i => i.innerText && i.innerText.trim().toLowerCase() === 'bo gong' && i.closest('.k-animation-container'));
                if (!target) target = items.find(i => i.innerText && i.innerText.trim().toLowerCase() === 'bo gong');"""

if old_js in content:
    content = content.replace(old_js, new_js)
    with open("/home/tiendv1/kpi-dashboard/telebot/tools/bypass/bypass.py", "w") as f:
        f.write(content)
    print("Added span.k-input to JS selector")
else:
    print("Could not find the JS block to replace")
