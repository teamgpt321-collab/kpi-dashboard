import re

with open("/home/tiendv1/kpi-dashboard/telebot/tools/bypass/bypass.py", "r") as f:
    content = f.read()

old_block = """        # =========================
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
            
        page.wait_for_timeout(500)"""

new_block = """        # =========================
        # NHÂN VIÊN KỸ THUẬT
        # =========================
        log("Nhập nhân viên kỹ thuật")
        try:
            edit_row = frame_target.locator("tr.k-grid-edit-row")
            if edit_row.count() == 0:
                edit_row = frame_target.locator("tbody tr").first
            
            nv_cell = edit_row.locator("td").nth(2)
            
            # Click đúp để chắc chắn vào chế độ edit (phòng hờ)
            nv_cell.dblclick()
            page.wait_for_timeout(500)
            
            nv_input = nv_cell.locator("input")
            if nv_input.count() > 0:
                nv_input.first.fill("phuongnam.tiendv1@fpt.net")
                page.wait_for_timeout(200)
                # Kendo thường cần phím Enter hoặc Tab để xác nhận edit cell
                nv_input.first.press("Enter")
                log("Đã nhập nhân viên bằng thẻ input")
            else:
                log("Gõ trực tiếp tên nhân viên")
                page.keyboard.type("phuongnam.tiendv1@fpt.net")
                page.wait_for_timeout(200)
                page.keyboard.press("Enter")
        except Exception as e:
            log(f"Lỗi nhập nhân viên: {e}")
            page.keyboard.press("Tab")
            page.wait_for_timeout(300)
            page.keyboard.type("phuongnam.tiendv1@fpt.net")
            page.keyboard.press("Enter")
            
        page.wait_for_timeout(500)"""

if old_block in content:
    content = content.replace(old_block, new_block)
    with open("/home/tiendv1/kpi-dashboard/telebot/tools/bypass/bypass.py", "w") as f:
        f.write(content)
    print("Fixed NVKT logic")
else:
    print("Could not find NVKT block to replace")
