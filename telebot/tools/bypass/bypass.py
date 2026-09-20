from telebot.tools.bypass.history import save_history
from telebot.usage_log import save_usage
import re
from playwright.sync_api import sync_playwright
import time

LOGIN_URL = "http://login.fpt.net/?urlreturn=inside.fpt.net"

USERNAME = "viettq3"
PASSWORD = "Ngoc1234567890@"

def log(msg):
    print("="*50)
    print("[BYPASS]", msg)
    print("="*50)

def run(shd, telegram_user=None):
    log(f"Bắt đầu Bypass SHĐ: {shd}")

    p = sync_playwright().start()
    browser = p.chromium.launch(headless=True, slow_mo=500)
    context = browser.new_context()
    page = context.new_page()

    try:
        log("Mở trang login")
        page.goto(LOGIN_URL, wait_until="networkidle")
        page.wait_for_timeout(3000)

        page.locator("#fUserName").fill(USERNAME)
        page.locator("#fPassword").fill(PASSWORD)
        page.get_by_text("ĐĂNG NHẬP", exact=True).click()

        page.wait_for_timeout(10000)
        log("Login thành công")
        
        log("Đang tìm ô search menu trong frame")
        search = None
        for i, frame in enumerate(page.frames):
            try:
                loc = frame.locator("input[placeholder='Tìm kiếm...']")
                if loc.count() > 0:
                    search = loc
                    break
            except Exception:
                pass

        if not search:
            raise Exception("Không tìm thấy ô search menu")

        search.fill("bypass")
        page.keyboard.press("Enter")
        page.wait_for_timeout(3000)

        log("Đang click Quản Lý ByPass")
        bypass_menu = None
        for i, frame in enumerate(page.frames):
            try:
                loc = frame.get_by_text("Quản Lý ByPass", exact=True)
                if loc.count() > 0:
                    bypass_menu = loc
                    break
            except Exception:
                pass

        if not bypass_menu:
            raise Exception("Không tìm thấy menu Quản Lý ByPass")

        bypass_menu.first.click()
        page.wait_for_timeout(5000)

        log("Đang click tab Import")
        import_tab = None
        for i, frame in enumerate(page.frames):
            try:
                loc = frame.locator("#ImportMenu")
                if loc.count() > 0:
                    import_tab = loc
                    break
            except Exception:
                pass

        if not import_tab:
            raise Exception("Không tìm thấy tab Import")

        import_tab.click()
        page.wait_for_timeout(3000)
        
        # =========================
        # ĐÓNG POPUP TRỢ GIÚP
        # =========================
        log("Đang đóng popup trợ giúp")
        for i, frame in enumerate(page.frames):
            try:
                # Tìm nút X trong title bar của popup Kendo hoặc Bootstrap
                close_btn = frame.locator(".k-window-titlebar .k-window-action, button.close, .k-icon.k-i-close").first
                if close_btn.count() > 0:
                    close_btn.click(force=True)
                    log(f"Đã click đóng popup ở frame {i}")
                    page.wait_for_timeout(1000)
                
                # Chạy JS ẩn đè lên phòng trường hợp click không hoạt động
                frame.evaluate('''() => {
                    document.querySelectorAll('.k-window, .modal, .k-dialog, .k-overlay, .modal-backdrop').forEach(x => x.style.display = 'none');
                }''')
            except:
                pass
                
        page.wait_for_timeout(2000)

        log("Bắt đầu nhập thông tin ByPass")

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
            except Exception:
                pass
        
        if not frame_target:
            raise Exception("Không chọn được loại Hợp đồng")
        page.wait_for_timeout(1000)

        # =========================
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
            
        page.wait_for_timeout(500)

        # =========================
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
            
            # Rà xuống tìm mục Bo Gong bằng Javascript để loại bỏ hoàn toàn khoảng trắng ẩn
            clicked_bo_gong = frame_target.evaluate('''() => {
                let items = Array.from(document.querySelectorAll('li.k-item, span.k-input, div.k-item'));
                let target = items.find(i => i.innerText && i.innerText.trim().toLowerCase() === 'bo gong' && i.closest('.k-animation-container'));
                if (!target) target = items.find(i => i.innerText && i.innerText.trim().toLowerCase() === 'bo gong');
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
                log("Đã chọn Bo Gong bằng phím mũi tên")
                
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
            
            # Rà xuống tìm mục Ha tang doi tac bằng Javascript
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
                page.keyboard.press("Enter")
                
        except Exception as e:
            log(f"Lỗi chọn lý do: {e}")
            
        page.wait_for_timeout(1000)


        # =========================
        # DỪNG KIỂM TRA TRƯỚC SAVE
        # =========================

        log(
            "Đã nhập xong dữ liệu ByPass - dừng để kiểm tra màn hình"
        )



        # =========================
        # HOÀN TẤT NHẬP THÔNG TIN
        # =========================

        log(
            "Nhập thông tin hoàn tất"
        )


        # =========================
        # TÌM VÀ CLICK SAVE
        # =========================

        log(
            "Bắt đầu quét nút Save"
        )


        save_clicked = False


        for i, frame in enumerate(page.frames):

            try:

                buttons = frame.locator(
                    "button"
                )

                count = buttons.count()


                log(
                    f"Frame {i} có {count} button"
                )


                for j in range(count):

                    try:

                        text = buttons.nth(j).inner_text().strip()


                        if text == "Save":

                            log(
                                f"Tìm thấy nút Save frame {i}"
                            )


                            buttons.nth(j).click(
                                force=True
                            )


                            log(
                                "Click Save thành công"
                            )


                            save_clicked = True

                            break


                    except:
                        pass



                if save_clicked:
                    break



            except Exception as e:

                log(
                    f"Lỗi quét frame {i}: {e}"
                )



        if not save_clicked:

            raise Exception(
                "Không tìm thấy nút Save"
            )


        page.wait_for_timeout(
            5000
        )


        log(
            "Hoàn tất Save ByPass"
        )


        # =========================
        # LƯU LỊCH SỬ TOOL
        # =========================

        print(
            "=== SAVE BYPASS HISTORY ===",
            telegram_user,
            shd
        )


        save_usage(
            "bypass",
            telegram_user,
            shd,
            "success"
        )



        # =========================
        # LƯU HISTORY
        # =========================

        if telegram_user:

            save_history(
                telegram_user,
                shd,
                "Thành công"
            )


        return (
            f"✅ Bypass thành công\n\n"
            f"SHĐ: {shd}\n"
            f"Kết quả: Thành công"
        )



        return f"Đã chạy Bypass {shd}"

    except Exception as e:
        log(str(e))
        return f"Lỗi Bypass: {e}"
        
    finally:
        browser.close()
        p.stop()

if __name__ == "__main__":
    pass

