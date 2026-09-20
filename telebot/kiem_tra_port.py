from playwright.sync_api import sync_playwright
import re


URL = "http://port.fpt.net/Index.aspx"

USERNAME = "phuongnam.tiendv1@fpt.net"
PASSWORD = "Tien060895@"

SHD = "SGAEW5685"



def log(msg):
    print("=" * 60)
    print(msg)
    print("=" * 60)



def find_menu_frame(page, selector):

    for frame in page.frames:

        try:

            if frame.locator(selector).count() > 0:

                print(
                    "FOUND FRAME:",
                    frame.name,
                    frame.url
                )

                return frame

        except:
            pass


    return None



with sync_playwright() as p:


    browser = p.chromium.launch(
        headless=False,
        slow_mo=300
    )


    context = browser.new_context(
        viewport={
            "width":1920,
            "height":1080
        }
    )


    page = context.new_page()



    try:


        # =========================
        # LOGIN
        # =========================

        log("MỞ PORT")


        page.goto(URL)


        page.wait_for_timeout(5000)



        page.locator(
            "#username"
        ).fill(USERNAME)



        page.locator(
            "#password"
        ).fill(PASSWORD)



        page.locator(
            "#kc-login"
        ).click()



        log("LOGIN OK")


        page.wait_for_timeout(10000)



        # =========================
        # MENU
        # =========================


        menu_frame = find_menu_frame(
            page,
            'a[onclick="Action(1072)"]'
        )


        if not menu_frame:

            raise Exception(
                "Không tìm thấy FTTH NEW"
            )



        # FTTH NEW

        log("CLICK FTTH NEW")


        menu_frame.locator(
            'a[onclick="Action(1072)"]'
        ).click()


        page.wait_for_timeout(5000)



        # HỢP ĐỒNG

        log("CLICK HỢP ĐỒNG")


        menu_frame.locator(
            'a[onclick="Action(1302)"]'
        ).click()


        page.wait_for_timeout(5000)



        # TÌM KIẾM

        log("CLICK TÌM KIẾM")


        menu_frame.locator(
            'a[onclick*="1322"]'
        ).click()


        page.wait_for_timeout(7000)



        # =========================
        # MAIN FRAME
        # =========================


        main_frame = page.frame(
            name="mainFrame"
        )


        if not main_frame:

            raise Exception(
                "Không có mainFrame"
            )


        log("MAIN FRAME OK")



        # =========================
        # NHẬP SHD
        # =========================


        main_frame.locator(
            "#txtContract"
        ).fill(
            SHD
        )


        log(
            "NHẬP SHD: " + SHD
        )



        # CLICK SEARCH

        main_frame.locator(
            "#btnSearch"
        ).click()



        log("ĐÃ TÌM KIẾM")


        page.wait_for_timeout(10000)



        # =========================
        # CLICK LINK HỢP ĐỒNG
        # =========================


        contract_link = main_frame.locator(
            'a.link[href*="/FTTH_NewPort/Contract/Insert/"]'
        )


        print(
            "SỐ HỢP ĐỒNG:",
            contract_link.count()
        )



        contract_link.first.click()



        log(
            "ĐÃ MỞ CHI TIẾT HỢP ĐỒNG"
        )


        page.wait_for_timeout(10000)



        # =========================
        # LẤY THÔNG TIN HTML
        # =========================


        detail_frame = page.frame(
            name="mainFrame"
        )


        if not detail_frame:

            detail_frame = page



        body_text = detail_frame.locator(
            "body"
        ).inner_text()



        print("\n===== DATA TRANG CHI TIẾT =====")

        print(body_text)


        print("==============================")



        # =========================
        # LẤY THÔNG SỐ THI CÔNG
        # =========================


        match = re.search(
            r"Thông số thi công:\s*(.+)",
            body_text
        )



        if match:

            thong_so = match.group(1).strip()


            print(
                "\nTHÔNG SỐ THI CÔNG:",
                thong_so
            )


        else:


            print(
                "KHÔNG TÌM THẤY THÔNG SỐ THI CÔNG"
            )



        # screenshot kiểm tra

        page.screenshot(
            path="port_detail_check.png",
            full_page=True
        )



        log("HOÀN TẤT")



    except Exception as e:


        print(
            "LỖI:",
            e
        )



    input(
        "Enter để đóng..."
    )


    browser.close()
