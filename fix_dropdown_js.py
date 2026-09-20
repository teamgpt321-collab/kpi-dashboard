import re

with open("/home/tiendv1/kpi-dashboard/telebot/tools/bypass/bypass.py", "r") as f:
    content = f.read()

# Replace Bo Gong block
old_bo_block = """            # Rà xuống tìm mục Bo Gong trong danh sách và click
            bo_gong_item = frame_target.locator("li.k-item").filter(has_text=re.compile(r"^Bo Gong$", re.IGNORECASE))
            if bo_gong_item.count() > 0:
                bo_gong_item.first.click(force=True)
                log("Đã click chọn Bo Gong")
            else:
                log("Không tìm thấy dòng Bo Gong trong danh sách")"""

new_bo_block = """            # Rà xuống tìm mục Bo Gong bằng Javascript để loại bỏ hoàn toàn khoảng trắng ẩn
            clicked_bo_gong = frame_target.evaluate('''() => {
                let items = Array.from(document.querySelectorAll('li.k-item'));
                let target = items.find(i => i.innerText.trim().toLowerCase() === 'bo gong');
                if (target) {
                    target.click();
                    return true;
                }
                return false;
            }''')
            
            if clicked_bo_gong:
                log("Đã click chọn Bo Gong qua JS")
            else:
                log("Dùng phím mũi tên để chọn Bo Gong (nhấn xuống 3 lần)")
                page.keyboard.press("ArrowDown")
                page.wait_for_timeout(200)
                page.keyboard.press("ArrowDown")
                page.wait_for_timeout(200)
                page.keyboard.press("ArrowDown")
                page.wait_for_timeout(200)
                page.keyboard.press("Enter")
                log("Đã chọn Bo Gong bằng phím mũi tên")"""

# Replace Ha tang doi tac block
old_lydo_block = """            # Rà xuống tìm mục Ha tang doi tac và click
            ly_do_item = frame_target.locator("li.k-item").filter(has_text=re.compile(r"^Ha tang doi tac$", re.IGNORECASE))
            if ly_do_item.count() > 0:
                ly_do_item.first.click(force=True)
                log("Đã click chọn Ha tang doi tac")
            else:
                log("Không tìm thấy dòng Ha tang doi tac trong danh sách")"""

new_lydo_block = """            # Rà xuống tìm mục Ha tang doi tac bằng Javascript
            clicked_ly_do = frame_target.evaluate('''() => {
                let items = Array.from(document.querySelectorAll('li.k-item'));
                let target = items.find(i => i.innerText.trim().toLowerCase() === 'ha tang doi tac');
                if (target) {
                    target.click();
                    return true;
                }
                return false;
            }''')
            
            if clicked_ly_do:
                log("Đã click chọn Ha tang doi tac qua JS")
            else:
                log("Không tìm thấy dòng Ha tang doi tac trong danh sách, thử gõ phím")
                page.keyboard.type("Ha tang doi tac")
                page.wait_for_timeout(200)
                page.keyboard.press("Enter")"""

if old_bo_block in content:
    content = content.replace(old_bo_block, new_bo_block)
    content = content.replace(old_lydo_block, new_lydo_block)
    with open("/home/tiendv1/kpi-dashboard/telebot/tools/bypass/bypass.py", "w") as f:
        f.write(content)
    print("Fixed dropdown JS exact match and added arrow fallback")
else:
    print("Could not find the blocks to replace")
