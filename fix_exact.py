import re

with open("/home/tiendv1/kpi-dashboard/telebot/tools/bypass/bypass.py", "r") as f:
    content = f.read()

# Replace Bo Gong selection
old_bo_gong = """            # Chọn "Bo Gong" (chữ không dấu theo hình ảnh)
            bo_gong = page.locator(".k-animation-container").get_by_text("Bo Gong", exact=True)
            if bo_gong.count() == 0:
                 bo_gong = frame_target.get_by_text("Bo Gong", exact=True)
                 
            if bo_gong.count() > 0:
                 bo_gong.first.click(force=True)
                 log("Đã click chọn Bo Gong")"""

new_bo_gong = """            # Chọn "Bo Gong" (tìm kiếm tương đối)
            bo_gong = page.locator(".k-animation-container li").filter(has_text="Bo Gong")
            if bo_gong.count() == 0:
                 bo_gong = frame_target.locator("li").filter(has_text="Bo Gong")
                 
            if bo_gong.count() > 0:
                 bo_gong.first.click(force=True)
                 log("Đã click chọn Bo Gong")"""

# Replace Ha tang doi tac selection
old_ly_do = """            ly_do = page.locator(".k-animation-container").get_by_text("Ha tang doi tac", exact=True)
            if ly_do.count() == 0:
                 ly_do = frame_target.get_by_text("Ha tang doi tac", exact=True)
                 
            if ly_do.count() > 0:
                 ly_do.first.click(force=True)
                 log("Đã click chọn Ha tang doi tac")"""

new_ly_do = """            ly_do = page.locator(".k-animation-container li").filter(has_text="Ha tang doi tac")
            if ly_do.count() == 0:
                 ly_do = frame_target.locator("li").filter(has_text="Ha tang doi tac")
                 
            if ly_do.count() > 0:
                 ly_do.first.click(force=True)
                 log("Đã click chọn Ha tang doi tac")"""

content = content.replace(old_bo_gong, new_bo_gong)
content = content.replace(old_ly_do, new_ly_do)

with open("/home/tiendv1/kpi-dashboard/telebot/tools/bypass/bypass.py", "w") as f:
    f.write(content)
print("Updated matching logic")
