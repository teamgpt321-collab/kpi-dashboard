import re

with open("/home/tiendv1/kpi-dashboard/telebot/tools/bypass/bypass.py", "r") as f:
    content = f.read()

# For Bo Gong
old_bo_gong = """            # Chọn "Bo Gong" (tìm kiếm tương đối)
            bo_gong = page.locator(".k-animation-container li").filter(has_text="Bo Gong")
            if bo_gong.count() == 0:
                 bo_gong = frame_target.locator("li").filter(has_text="Bo Gong")
                 
            if bo_gong.count() > 0:
                 bo_gong.first.click(force=True)
                 log("Đã click chọn Bo Gong")
            else:
                 log("Không thấy tuỳ chọn Bo Gong, thử gõ phím")
                 page.keyboard.type("Bo Gong")
                 page.wait_for_timeout(200)
                 page.keyboard.press("Enter")"""

new_bo_gong = """            # Sử dụng Javascript để click thẳng vào thẻ li (tránh lỗi Playwright bị chặn)
            clicked = frame_target.evaluate('''() => {
                let items = Array.from(document.querySelectorAll('li.k-item'));
                let target = items.find(i => i.innerText.toLowerCase().includes('bo gong') || i.innerText.toLowerCase().includes('bỏ gông'));
                if (target) {
                    target.click();
                    return true;
                }
                // Nếu ở ngoài frame (k-animation-container thường render ở top document)
                items = Array.from(window.top.document.querySelectorAll('li.k-item'));
                target = items.find(i => i.innerText.toLowerCase().includes('bo gong') || i.innerText.toLowerCase().includes('bỏ gông'));
                if (target) {
                    target.click();
                    return true;
                }
                return false;
            }''')
            
            if clicked:
                 log("Đã click chọn Bo Gong qua JS")
            else:
                 log("Không tìm thấy option Bo Gong trong DOM, thử gõ phím")
                 page.keyboard.type("Bỏ Gông")
                 page.wait_for_timeout(200)
                 page.keyboard.press("Enter")"""

# For Ha tang doi tac
old_ly_do = """            ly_do = page.locator(".k-animation-container li").filter(has_text="Ha tang doi tac")
            if ly_do.count() == 0:
                 ly_do = frame_target.locator("li").filter(has_text="Ha tang doi tac")
                 
            if ly_do.count() > 0:
                 ly_do.first.click(force=True)
                 log("Đã click chọn Ha tang doi tac")
            else:
                 log("Không thấy tuỳ chọn Ha tang doi tac, thử gõ phím")
                 page.keyboard.type("Ha tang doi tac")
                 page.wait_for_timeout(200)
                 page.keyboard.press("Enter")"""

new_ly_do = """            clicked_ld = frame_target.evaluate('''() => {
                let items = Array.from(document.querySelectorAll('li.k-item'));
                let target = items.find(i => i.innerText.toLowerCase().includes('ha tang') || i.innerText.toLowerCase().includes('hạ tầng'));
                if (target) {
                    target.click();
                    return true;
                }
                items = Array.from(window.top.document.querySelectorAll('li.k-item'));
                target = items.find(i => i.innerText.toLowerCase().includes('ha tang') || i.innerText.toLowerCase().includes('hạ tầng'));
                if (target) {
                    target.click();
                    return true;
                }
                return false;
            }''')
            
            if clicked_ld:
                 log("Đã click chọn Ha tang doi tac qua JS")
            else:
                 log("Không tìm thấy option Ha tang doi tac, thử gõ phím")
                 page.keyboard.type("Hạ tầng đối tác")
                 page.wait_for_timeout(200)
                 page.keyboard.press("Enter")"""

if old_bo_gong in content and old_ly_do in content:
    content = content.replace(old_bo_gong, new_bo_gong)
    content = content.replace(old_ly_do, new_ly_do)
    with open("/home/tiendv1/kpi-dashboard/telebot/tools/bypass/bypass.py", "w") as f:
        f.write(content)
    print("Updated JS click logic")
else:
    print("Could not find the blocks to replace!")
