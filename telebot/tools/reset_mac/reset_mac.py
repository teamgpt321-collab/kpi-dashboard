from playwright.sync_api import sync_playwright


LOGIN_URL = "http://login.fpt.net/?urlreturn=inside.fpt.net"

USERNAME = "viettq3"
PASSWORD = "Ngoc1234567890@"


def log(msg):
    print("=" * 50)
    print("[RESET MAC]", msg)
    print("=" * 50)



def find_in_frames(page, selector):

    for i, frame in enumerate(page.frames):

        try:

            loc = frame.locator(selector)

            if loc.count() > 0:
                return loc.first, frame, i


        except:
            pass


    return None, None, None



def run(shd="SGAES2776"):

    p = sync_playwright().start()

    browser = p.chromium.launch(
        headless=True,
        slow_mo=500
    )

    context = browser.new_context()

    page = context.new_page()


    try:


        # =========================
        # LOGIN
        # =========================

        log("Mở login")


        page.goto(
            LOGIN_URL,
            wait_until="networkidle"
        )


        page.wait_for_timeout(3000)


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



        # =========================
        # VÀO RESET MAC
        # =========================


        search, _, frame_id = find_in_frames(
            page,
            "input[placeholder='Tìm kiếm...']"
        )


        if not search:

            raise Exception(
                "Không tìm thấy search menu"
            )


        search.fill(
            "Reset Mac"
        )


        page.keyboard.press(
            "Enter"
        )


        page.wait_for_timeout(
            3000
        )


        menu, _, frame_id = find_in_frames(
            page,
            "text=Reset Mac"
        )


        if not menu:

            raise Exception(
                "Không tìm thấy Reset Mac"
            )


        menu.click()


        page.wait_for_timeout(
            5000
        )


        log(
            "Đã vào Reset Mac"
        )



        # =========================
        # NHẬP SHĐ
        # =========================


        shd_input, _, frame_id = find_in_frames(
            page,
            "#fAgentName"
        )


        if not shd_input:

            raise Exception(
                "Không tìm thấy #fAgentName"
            )


        shd_input.fill(
            shd
        )


        log(
            f"Đã nhập SHĐ {shd}"
        )



        # =========================
        # SEARCH
        # =========================


        search_btn, _, frame_id = find_in_frames(
            page,
            "#btnSearch"
        )


        if not search_btn:

            raise Exception(
                "Không tìm thấy #btnSearch"
            )


        search_btn.click(
            force=True
        )


        page.wait_for_timeout(
            5000
        )


        log(
            "Đã tìm kiếm"
        )



        # =========================
        # CLICK DÒNG KẾT QUẢ
        # =========================


        clicked = False


        for frame in page.frames:

            try:

                rows = frame.locator(
                    "tbody tr"
                )


                if rows.count() > 0:


                    rows.first.click(
                        force=True
                    )


                    clicked = True

                    break


            except:
                pass



        if not clicked:

            raise Exception(
                "Không click được dòng kết quả"
            )


        page.wait_for_timeout(
            3000
        )


        log(
            "Đã mở popup Reset MAC"
        )



        # =========================
        # XÓA MAC
        # =========================


        mac_input = None


        for frame in page.frames:

            try:

                inputs = frame.locator(
                    "input"
                )


                for i in range(inputs.count()):

                    inp = inputs.nth(i)


                    if inp.is_visible():

                        value = inp.input_value()


                        if ":" in value:

                            mac_input = inp
                            break


                if mac_input:
                    break


            except:
                pass



        if not mac_input:

            raise Exception(
                "Không tìm thấy địa chỉ MAC"
            )



        mac_input.fill(
            ""
        )


        log(
            "Đã xóa địa chỉ MAC"
        )



        # =========================
        # CLICK CẬP NHẬT
        # =========================


        update_btn, _, frame_id = find_in_frames(
            page,
            "#btnChange"
        )


        if not update_btn:

            raise Exception(
                "Không tìm thấy #btnChange"
            )


        update_btn.click(
            force=True
        )


        page.wait_for_timeout(
            2000
        )


        log(
            "Đã click Cập nhật"
        )



        # =========================
        # POPUP XÁC NHẬN
        # =========================


        ok_btn, _, frame_id = find_in_frames(
            page,
            "input.confirm_yes"
        )


        if not ok_btn:

            raise Exception(
                "Không tìm thấy nút OK xác nhận"
            )


        ok_btn.click(
            force=True
        )


        page.wait_for_timeout(
            5000
        )


        log(
            "Đã xác nhận OK Reset MAC"
        )


        return (
            f"✅ Reset MAC hoàn tất\n"
            f"SHĐ: {shd}"
        )



    except Exception as e:

        log(
            f"Lỗi: {e}"
        )


        return (
            f"❌ Reset MAC lỗi: {e}"
        )



    finally:

        browser.close()

        p.stop()



if __name__ == "__main__":

    print(
        run("SGAES2776")
    )
