import re

with open("/home/tiendv1/kpi-dashboard/telebot/tools/bypass/bypass.py", "r") as f:
    content = f.read()

# I will replace the block under "BỎ QUA POPUP TRỢ GIÚP"

old_block = """        # =========================
        # BỎ QUA POPUP TRỢ GIÚP
        # =========================
        log("Ẩn popup trợ giúp")
        page.evaluate(\"\"\"
            () => {
                document.querySelectorAll('.modal').forEach(x => { x.style.display = 'none'; });
                document.querySelectorAll('.modal-backdrop').forEach(x => { x.remove(); });
                document.body.classList.remove('modal-open');
            }
        \"\"\")
        page.wait_for_timeout(1000)"""

new_block = """        # =========================
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
                
        page.wait_for_timeout(2000)"""

if old_block in content:
    content = content.replace(old_block, new_block)
    with open("/home/tiendv1/kpi-dashboard/telebot/tools/bypass/bypass.py", "w") as f:
        f.write(content)
    print("Fixed popup close logic")
else:
    print("Could not find the old block to replace!")

