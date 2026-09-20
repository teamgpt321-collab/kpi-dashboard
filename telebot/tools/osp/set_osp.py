from telebot.usage_log import save_usage
from playwright.sync_api import sync_playwright
import time


LOGIN_URL = "http://login.fpt.net/?urlreturn=inside.fpt.net"

USERNAME = "viettq3"
PASSWORD = "Ngoc1234567890@"


def log(msg):
    print("=" * 50)
    print("[OSP]", msg)
    print("=" * 50)



def run(shd, telegram_user=None):

    log(f"Bắt đầu Set OSP SHĐ: {shd}")


    p = sync_playwright().start()


    browser = p.chromium.launch(
        headless=True,
        slow_mo=500
    )


    context = browser.new_context()

    page = context.new_page()


    try:

        # =====================
        # LOGIN INSIDE
        # =====================

        log("Mở trang login")

        page.goto(
            LOGIN_URL,
            wait_until="networkidle"
        )


        page.wait_for_timeout(3000)


        log("Nhập tài khoản")


        page.locator(
            "#fUserName"
        ).fill(
            USERNAME
        )


        page.locator(
            "#fPassword"
        ).fill(
            PASSWORD
        )


        page.get_by_text(
            "ĐĂNG NHẬP",
            exact=True
        ).click()



        page.wait_for_timeout(
            10000
        )


        log("Login thành công")


        # =====================
        # TÌM MENU OSP
        # =====================

        log("Đang tìm ô search menu")


        search_input = None


        for frame in page.frames:

            try:

                inputs = frame.locator("input")


                for i in range(inputs.count()):

                    inp = inputs.nth(i)


                    if inp.is_visible():

                        search_input = inp
                        break


                if search_input:
                    break


            except:
                pass



        if search_input is None:

            raise Exception(
                "Không tìm thấy ô tìm kiếm"
            )


        search_input.fill(
            "osp"
        )


        log(
            "Đã nhập osp, gửi Enter tìm kiếm"
        )


        search_input.press(
            "Enter"
        )


        page.wait_for_timeout(
            8000
        )


        log(
            "Đã tìm kiếm OSP xong"
        )


        # =====================
        # CLICK XÁC THỰC OSP
        # =====================

        log("Đang click Xác thực OSP")


        clicked = False


        for frame in page.frames:

            try:

                locator = frame.locator(
                    'a[data-english-name="Xac thuc OSP"]'
                )


                count = locator.count()


                log(
                    f"Tìm Xác thực OSP trong frame: {count}"
                )


                if count > 0:


                    locator.first.wait_for(
                        state="attached",
                        timeout=10000
                    )


                    locator.first.evaluate(
                        "(el)=>el.click()"
                    )


                    clicked = True


                    log(
                        "Click Xác thực OSP thành công"
                    )


                    break


            except Exception as e:

                print(
                    "Frame error:",
                    e
                )



        if not clicked:

            raise Exception(
                "Không tìm thấy Xác thực OSP"
            )


        page.wait_for_timeout(
            8000
        )


        log(
            "Đã vào màn hình Xác thực OSP"
        )


        # =====================
        # TODO OSP
        # =====================

        log(
            f"Đã vào Inside, chuẩn bị xử lý SHĐ {shd}"
        )


        # tạm dừng để lấy selector
        # =====================
        # NHẬP SHĐ AUTHEN OSP
        # =====================

        log(
            f"Đang nhập SHĐ: {shd}"
        )


        contract_input = None


        for frame in page.frames:

            try:

                locator = frame.locator(
                    "#txtcontract"
                )


                if locator.count() > 0:

                    locator.wait_for(
                        state="visible",
                        timeout=10000
                    )

                    contract_input = locator

                    log(
                        f"Tìm thấy txtcontract trong frame: {frame.url}"
                    )

                    break

            except Exception as e:

                print(
                    "Frame input lỗi:",
                    e
                )


        if contract_input is None:

            raise Exception(
                "Không tìm thấy ô nhập SHĐ txtcontract"
            )


        contract_input.fill(
            shd
        )


        log(
            f"Đã nhập SHĐ {shd}"
        )


        # =====================
        # CLICK DEACTIVE
        # =====================

        log(
            "Đang click DeActive"
        )


        clicked = False


        for frame in page.frames:

            try:

                btn = frame.get_by_text(
                    "DeActive",
                    exact=True
                )


                if btn.count() > 0:

                    btn.first.click()


                    clicked = True


                    log(
                        "Click DeActive thành công"
                    )


                    # =========================
                    # LƯU HISTORY OSP
                    # =========================

                    print(
                        "=== SAVE OSP HISTORY ===",
                        telegram_user,
                        shd
                    )


                    print(
                        "=== SAVE OSP HISTORY ===",
                        telegram_user,
                        shd
                    )


                    save_usage(
                        "osp",
                        telegram_user or "unknown",
                        shd,
                        "success"
                    )


                    print(
                        "=== SAVED OSP HISTORY DONE ==="
                    )


                    print(
                        "=== SAVED OSP HISTORY DONE ==="
                    )


                    break


            except Exception as e:

                print(
                    "DeActive frame lỗi:",
                    e
                )



        if not clicked:

            raise Exception(
                "Không tìm thấy nút DeActive"
            )



        page.wait_for_timeout(
            5000
        )


        log(
            "Đã thực hiện DeActive"
        )




        return (
            f"Đã mở Inside xử lý SHĐ {shd}"
        )


    except Exception as e:


        log(
            f"Lỗi: {e}"
        )


        return (
            f"Lỗi Set OSP: {e}"
        )


    finally:

        browser.close()

        p.stop()



if __name__ == "__main__":

    print(
        run("TEST123")
    )
