import re

with open("/home/tiendv1/kpi-dashboard/telebot/tools/bypass/bypass.py", "r") as f:
    content = f.read()

# Replace the Bo Gong regex
old_bo_regex = r're.compile(r"bo gong|bỏ gông", re.IGNORECASE)'
new_bo_regex = r're.compile(r"^Bo Gong$", re.IGNORECASE)'

# Replace the Ha tang doi tac regex
old_lydo_regex = r're.compile(r"ha tang|hạ tầng", re.IGNORECASE)'
new_lydo_regex = r're.compile(r"^Ha tang doi tac$", re.IGNORECASE)'

if old_bo_regex in content:
    content = content.replace(old_bo_regex, new_bo_regex)
    content = content.replace(old_lydo_regex, new_lydo_regex)
    with open("/home/tiendv1/kpi-dashboard/telebot/tools/bypass/bypass.py", "w") as f:
        f.write(content)
    print("Fixed regex to exact match")
else:
    print("Could not find the regex strings to replace")

