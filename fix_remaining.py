import re

with open("/home/tiendv1/kpi-dashboard/telebot/tools/bypass/bypass.py", "r") as f:
    content = f.read()

# We will split at "NHÂN VIÊN KỸ THUẬT" and "Click Save"
parts = content.split('        # =========================\n        # NHÂN VIÊN KỸ THUẬT\n        # =========================')
if len(parts) >= 2:
    part1 = parts[0]
    part2 = parts[1]
    
    # split part2 to find the end of LÝ DO BYPASS
    end_parts = part2.split('        # Click Save (Optional, currently just waiting for Enter to submit)')
    if len(end_parts) >= 2:
        part3 = '        # Click Save (Optional, currently just waiting for Enter to submit)' + end_parts[1]
        
        new_middle = """        # =========================
        # NHÂN VIÊN KỸ THUẬT
        # =========================
        log("Nhập nhân viên kỹ thuật")
        try:
            edit_row = frame_target.locator("tr.k-grid-edit-row")
            if edit_row.count() == 0:
                edit_row = frame_target.locator("tbody tr").first
            
            nv_cell = edit_row.locator("td").nth(2)
            nv_cell.click()
            page.wait_for_timeout(500)
            
            nv_input = nv_cell.locator("input")
            if nv_input.count() > 0:
                nv_input.first.fill("phuongnam.tiendv1@fpt.net")
            else:
                page.keyboard.type("phuongnam.tiendv1@fpt.net")
            log("Đã nhập nhân viên kỹ thuật")
        except Exception as e:
            log(f"Lỗi nhập nhân viên: {e}")
            page.keyboard.press("Tab")
            page.wait_for_timeout(300)
            page.keyboard.type("phuongnam.tiendv1@fpt.net")
            
        page.wait_for_timeout(500)

        # =========================
        # TÌNH TRẠNG BYPASS
        # =========================
        log("Chọn tình trạng Bỏ Gông")
        try:
            edit_row = frame_target.locator("tr.k-grid-edit-row")
            if edit_row.count() == 0:
                edit_row = frame_target.locator("tbody tr").first
                
            tt_cell = edit_row.locator("td").nth(3)
            tt_cell.click()
            page.wait_for_timeout(500)
            
            dropdown_arrow = tt_cell.locator(".k-select, span.k-input")
            if dropdown_arrow.count() > 0:
                dropdown_arrow.first.click()
            else:
                page.keyboard.press("ArrowDown")
            page.wait_for_timeout(1000)
            
            bo_gong = page.locator(".k-animation-container").get_by_text("Bỏ Gông", exact=True)
            if bo_gong.count() == 0:
                 bo_gong = frame_target.get_by_text("Bỏ Gông", exact=True)
                 
            if bo_gong.count() > 0:
                 bo_gong.first.click(force=True)
                 log("Đã chọn Bỏ Gông")
            else:
                 page.keyboard.type("Bo Gong")
                 page.keyboard.press("Enter")
        except Exception as e:
            log(f"Lỗi chọn tình trạng: {e}")
            page.keyboard.press("Tab")
            page.keyboard.type("Bo Gong")
            page.keyboard.press("Enter")
            
        page.wait_for_timeout(500)

        # =========================
        # LÝ DO BYPASS
        # =========================
        log("Chọn lý do Ha tang doi tac")
        try:
            edit_row = frame_target.locator("tr.k-grid-edit-row")
            if edit_row.count() == 0:
                edit_row = frame_target.locator("tbody tr").first
                
            ld_cell = edit_row.locator("td").nth(4)
            ld_cell.click()
            page.wait_for_timeout(500)
            
            dropdown_arrow = ld_cell.locator(".k-select, span.k-input")
            if dropdown_arrow.count() > 0:
                dropdown_arrow.first.click()
            else:
                page.keyboard.press("ArrowDown")
            page.wait_for_timeout(1000)
            
            ly_do = page.locator(".k-animation-container").get_by_text("Ha tang doi tac", exact=True)
            if ly_do.count() == 0:
                 ly_do = frame_target.get_by_text("Ha tang doi tac", exact=True)
                 
            if ly_do.count() > 0:
                 ly_do.first.click(force=True)
                 log("Đã chọn Ha tang doi tac")
            else:
                 page.keyboard.type("Ha tang doi tac")
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
        print("Successfully updated remaining fields logic")
    else:
        print("Could not find the end block")
else:
    print("Could not find the start block")

