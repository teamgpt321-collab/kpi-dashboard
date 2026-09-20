import re

with open("/home/tiendv1/kpi-dashboard/telebot/tools/bypass/bypass.py", "r") as f:
    content = f.read()

parts = content.split('        # =========================\n        # TÌNH TRẠNG BYPASS\n        # =========================')
if len(parts) >= 2:
    part1 = parts[0]
    
    end_parts = parts[1].split('        # Click Save (Optional, currently just waiting for Enter to submit)')
    if len(end_parts) >= 2:
        part3 = '        # Click Save (Optional, currently just waiting for Enter to submit)' + end_parts[1]
        
        new_middle = """        # =========================
        # TÌNH TRẠNG BYPASS
        # =========================
        log("Chọn tình trạng Bỏ Gông")
        try:
            edit_row = frame_target.locator("tr.k-grid-edit-row")
            if edit_row.count() == 0:
                edit_row = frame_target.locator("tbody tr").first
                
            tt_cell = edit_row.locator("td").nth(3)
            
            # Click vào ô để kích hoạt
            tt_cell.click()
            page.wait_for_timeout(500)
            
            # Click vào mũi tên để mở danh sách xổ xuống
            tt_dropdown = tt_cell.locator(".k-dropdown, .k-dropdown-wrap, .k-select, span.k-input")
            if tt_dropdown.count() > 0:
                tt_dropdown.first.click(force=True)
            else:
                tt_cell.click(force=True)
                
            page.wait_for_timeout(1000)
            
            # Rà xuống tìm mục Bo Gong trong danh sách và click
            bo_gong_item = frame_target.locator("li.k-item").filter(has_text=re.compile(r"bo gong|bỏ gông", re.IGNORECASE))
            if bo_gong_item.count() > 0:
                bo_gong_item.first.click(force=True)
                log("Đã click chọn Bo Gong")
            else:
                log("Không tìm thấy dòng Bo Gong trong danh sách")
                
        except Exception as e:
            log(f"Lỗi chọn tình trạng: {e}")
            
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
            
            # Qua tiếp ô Lý do Bypass và click kích hoạt
            ld_cell.click()
            page.wait_for_timeout(500)
            
            # Click mũi tên xổ danh sách
            ld_dropdown = ld_cell.locator(".k-dropdown, .k-dropdown-wrap, .k-select, span.k-input")
            if ld_dropdown.count() > 0:
                ld_dropdown.first.click(force=True)
            else:
                ld_cell.click(force=True)
                
            page.wait_for_timeout(1000)
            
            # Rà xuống tìm mục Ha tang doi tac và click
            ly_do_item = frame_target.locator("li.k-item").filter(has_text=re.compile(r"ha tang|hạ tầng", re.IGNORECASE))
            if ly_do_item.count() > 0:
                ly_do_item.first.click(force=True)
                log("Đã click chọn Ha tang doi tac")
            else:
                log("Không tìm thấy dòng Ha tang doi tac trong danh sách")
                
        except Exception as e:
            log(f"Lỗi chọn lý do: {e}")
            
        page.wait_for_timeout(1000)
        
"""
        # Note: Need to make sure `re` is imported in bypass.py at the top.
        if "import re" not in part1:
            part1 = "import re\n" + part1
            
        final_content = part1 + new_middle + part3
        with open("/home/tiendv1/kpi-dashboard/telebot/tools/bypass/bypass.py", "w") as f:
            f.write(final_content)
        print("Updated natural click flow")
    else:
        print("Could not find the end block")
else:
    print("Could not find the start block")
