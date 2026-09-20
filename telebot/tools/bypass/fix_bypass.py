import re

with open("/home/tiendv1/kpi-dashboard/telebot/tools/bypass/bypass.py", "r") as f:
    content = f.read()

parts = content.split('        log(\n            "Bắt đầu nhập thông tin ByPass"\n        )')

if len(parts) >= 2:
    new_content = parts[0] + '        log(\n            "Bắt đầu nhập thông tin ByPass"\n        )\n\n'
    
    interaction_logic = """
        # =========================
        # CHỌN LOẠI HỢP ĐỒNG
        # =========================
        log("Chọn loại Hợp đồng")
        
        frame_target = None
        for i, frame in enumerate(page.frames):
            try:
                dropdown = frame.locator("span.k-input").filter(has_text="-- Chọn loại --")
                if dropdown.count() > 0:
                    dropdown.first.click()
                    page.wait_for_timeout(1000)
                    
                    option = page.locator(".k-animation-container").get_by_text("Hợp đồng", exact=True)
                    if option.count() == 0:
                        option = frame.get_by_text("Hợp đồng", exact=True)
                    option.first.click(force=True)
                    
                    frame_target = frame
                    log("Đã chọn Hợp đồng")
                    break
            except Exception as e:
                pass
        
        if not frame_target:
            raise Exception("Không chọn được loại Hợp đồng")

        page.wait_for_timeout(1000)

        # =========================
        # NHẬP SỐ HỢP ĐỒNG
        # =========================
        log(f"Nhập SHĐ: {shd}")
        contract_input = frame_target.locator("input[name='Contract']")
        if contract_input.count() > 0:
            contract_input.first.fill(shd)
            log("Đã nhập SHĐ")
        else:
            raise Exception("Không tìm thấy ô nhập SHĐ")
            
        page.wait_for_timeout(500)

        # =========================
        # NHÂN VIÊN KỸ THUẬT
        # =========================
        log("Nhập nhân viên kỹ thuật")
        page.keyboard.press("Tab")
        page.wait_for_timeout(500)
        page.keyboard.type("phuongnam.tiendv1@fpt.net")
        log("Đã nhập nhân viên kỹ thuật")

        page.wait_for_timeout(500)

        # =========================
        # TÌNH TRẠNG BYPASS
        # =========================
        log("Chọn tình trạng Bỏ Gông")
        page.keyboard.press("Tab")
        page.wait_for_timeout(500)
        
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
             log("Đã nhập Bo Gong")
             
        page.wait_for_timeout(500)

        # =========================
        # LÝ DO BYPASS
        # =========================
        log("Chọn lý do Ha tang doi tac")
        page.keyboard.press("Tab")
        page.wait_for_timeout(500)
        
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
             log("Đã nhập Ha tang doi tac")
             
        page.wait_for_timeout(1000)

        # =========================
        # HOÀN THÀNH
        # =========================
        log("Nhập thông tin hoàn tất")
        
        input("Kiểm tra dữ liệu rồi ENTER...")
        
        return f"Đã chạy Bypass {shd}"
"""
    
    tail_parts = parts[1].split('    except Exception as e:')
    
    final_content = new_content + interaction_logic + '\n    except Exception as e:' + tail_parts[-1]
    
    with open("/home/tiendv1/kpi-dashboard/telebot/tools/bypass/bypass.py", "w") as f:
        f.write(final_content)
    print("Updated bypass.py successfully.")
else:
    print("Could not find the target block.")

