import re

with open("/home/tiendv1/kpi-dashboard/telebot/tools/bypass/bypass.py", "r") as f:
    content = f.read()

old_block = """        # =========================
        # NHẬP SỐ HỢP ĐỒNG
        # =========================
        log(f"Nhập SHĐ: {shd}")
        contract_input = frame_target.locator("input[name='Contract']")
        if contract_input.count() > 0:
            contract_input.first.fill(shd)
            log("Đã nhập SHĐ")
        else:
            raise Exception("Không tìm thấy ô nhập SHĐ")
        page.wait_for_timeout(500)"""

new_block = """        # =========================
        # NHẬP SỐ HỢP ĐỒNG
        # =========================
        log(f"Nhập SHĐ: {shd}")
        contract_input = frame_target.locator("input[name='Contract']")
        
        if contract_input.count() == 0:
            log("Chưa thấy ô input Contract, đang cố kích hoạt ô trống...")
            
            # Thử click vào ô td thứ 2 của dòng đầu tiên (Số hợp đồng)
            try:
                # Dòng có thể mang class k-grid-edit-row hoặc chỉ là tr bình thường
                edit_row = frame_target.locator("tr.k-grid-edit-row")
                if edit_row.count() == 0:
                    edit_row = frame_target.locator("tbody tr").first
                
                if edit_row.count() > 0:
                    edit_row.locator("td").nth(1).click()
                    page.wait_for_timeout(500)
                else:
                    page.keyboard.press("Tab")
                    page.wait_for_timeout(500)
            except Exception as e:
                log(f"Lỗi khi click kích hoạt ô: {e}")
                page.keyboard.press("Tab")
                page.wait_for_timeout(500)
                
            contract_input = frame_target.locator("input[name='Contract']")

        if contract_input.count() > 0:
            contract_input.first.fill(shd)
            log("Đã nhập SHĐ")
        else:
            log("Vẫn không thấy input Contract, gõ trực tiếp...")
            page.keyboard.type(shd)
            
        page.wait_for_timeout(500)"""

if old_block in content:
    content = content.replace(old_block, new_block)
    with open("/home/tiendv1/kpi-dashboard/telebot/tools/bypass/bypass.py", "w") as f:
        f.write(content)
    print("Fixed contract input logic")
else:
    print("Could not find the old block to replace!")

