import re

with open("/home/tiendv1/kpi-dashboard/telebot/tools/bypass/bypass.py", "r") as f:
    content = f.read()

# Split at "TÌNH TRẠNG BYPASS"
parts = content.split('        # =========================\n        # TÌNH TRẠNG BYPASS\n        # =========================')
if len(parts) >= 2:
    part1 = parts[0]
    
    # Split part2 to find the end of LÝ DO BYPASS
    end_parts = parts[1].split('        # Click Save (Optional, currently just waiting for Enter to submit)')
    if len(end_parts) >= 2:
        part3 = '        # Click Save (Optional, currently just waiting for Enter to submit)' + end_parts[1]
        
        new_middle = """        # =========================
        # TÌNH TRẠNG BYPASS
        # =========================
        log("Chọn tình trạng Bo Gong")
        try:
            edit_row = frame_target.locator("tr.k-grid-edit-row")
            if edit_row.count() == 0:
                edit_row = frame_target.locator("tbody tr").first
                
            tt_cell = edit_row.locator("td").nth(3)
            
            # Click lần 1 để kích hoạt ô thành dropdown
            tt_cell.click()
            page.wait_for_timeout(500)
            
            # Tìm dropdown vừa sinh ra và click để xổ danh sách
            dropdown = tt_cell.locator(".k-dropdown, .k-dropdown-wrap, .k-select, input")
            if dropdown.count() > 0:
                dropdown.first.click(force=True)
            else:
                tt_cell.click(force=True)
                
            page.wait_for_timeout(1000)
            
            # Chọn "Bo Gong" (chữ không dấu theo hình ảnh)
            bo_gong = page.locator(".k-animation-container").get_by_text("Bo Gong", exact=True)
            if bo_gong.count() == 0:
                 bo_gong = frame_target.get_by_text("Bo Gong", exact=True)
                 
            if bo_gong.count() > 0:
                 bo_gong.first.click(force=True)
                 log("Đã click chọn Bo Gong")
            else:
                 log("Không thấy tuỳ chọn Bo Gong, thử gõ phím")
                 page.keyboard.type("Bo Gong")
                 page.wait_for_timeout(200)
                 page.keyboard.press("Enter")
        except Exception as e:
            log(f"Lỗi chọn tình trạng: {e}")
            page.keyboard.press("Tab")
            page.keyboard.type("Bo Gong")
            page.keyboard.press("Enter")
            
        page.wait_for_timeout(1000)

        # =========================
        # LÝ DO BYPASS
        # =========================
        log("Chọn lý do Ha tang doi tac")
        try:
            edit_row = frame_target.locator("tr.k-grid-edit-row")
            if edit_row.count() == 0:
                edit_row = frame_target.locator("tbody tr").first
                
            ld_cell = edit_row.locator("td").nth(4)
            
            # Click lần 1 để kích hoạt ô thành dropdown
            ld_cell.click()
            page.wait_for_timeout(500)
            
            # Click lần 2 để xổ danh sách
            dropdown = ld_cell.locator(".k-dropdown, .k-dropdown-wrap, .k-select, input")
            if dropdown.count() > 0:
                dropdown.first.click(force=True)
            else:
                ld_cell.click(force=True)
                
            page.wait_for_timeout(1000)
            
            ly_do = page.locator(".k-animation-container").get_by_text("Ha tang doi tac", exact=True)
            if ly_do.count() == 0:
                 ly_do = frame_target.get_by_text("Ha tang doi tac", exact=True)
                 
            if ly_do.count() > 0:
                 ly_do.first.click(force=True)
                 log("Đã click chọn Ha tang doi tac")
            else:
                 log("Không thấy tuỳ chọn Ha tang doi tac, thử gõ phím")
                 page.keyboard.type("Ha tang doi tac")
                 page.wait_for_timeout(200)
                 page.keyboard.press("Enter")
        except Exception as e:
            log(f"Lỗi chọn lý do: {e}")
            page.keyboard.press("Tab")
            page.keyboard.type("Ha tang doi tac")
            page.keyboard.press("Enter")
            
        page.wait_for_timeout(1000)
        
"""
        final_content = part1 + new_middle + part3
        with open("/home/tiendv1/kpi-dashboard/telebot/tools/bypass/bypass.py", "w") as f:
            f.write(final_content)
        print("Successfully updated Dropdowns logic")
    else:
        print("Could not find the end block")
else:
    print("Could not find the start block")
