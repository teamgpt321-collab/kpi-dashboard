from playwright.sync_api import sync_playwright
import os
import shutil


URL = "http://partner.fpt.net/pt-portal/monitor"

USERNAME = "phuongnam.tiendv1"
PASSWORD = "Thithao1996@"

OUTPUT = "/home/tiendv1/kpi-dashboard/debug_khachhang"



def log(msg):
    print("=" * 60)
    print(msg)
    print("=" * 60)



def run(shd):

    # Xóa dữ liệu debug cũ
    if os.path.exists(OUTPUT):
        shutil.rmtree(OUTPUT)

    os.makedirs(OUTPUT)



    with sync_playwright() as p:


        browser = p.chromium.launch(
            headless=False
        )


        context = browser.new_context()



        page = context.new_page()



        try:


            log("MỞ TRANG")


            page.goto(URL)



            page.wait_for_timeout(5000)



            # LOGIN

            if page.locator("#fUserName").count() > 0:


                log("LOGIN")


                page.locator(
                    "#fUserName"
                ).fill(USERNAME)


                page.locator(
                    "#fPassword"
                ).fill(PASSWORD)


                page.locator(
                    "#btnLogin"
                ).click()


                page.wait_for_timeout(10000)



            log("LOGIN OK")



            # tìm ô SHD

            search = page.locator(
                'input[placeholder="Nhập số hợp đồng..."]'
            )


            search.wait_for(
                timeout=20000
            )


            search.fill(shd)



            old_pages = context.pages.copy()



            page.keyboard.press(
                "Enter"
            )



            new_page = None



            # bắt tab mới

            for i in range(30):

                page.wait_for_timeout(1000)


                for pg in context.pages:


                    if pg not in old_pages:

                        new_page = pg

                        break


                if new_page:

                    break



            if new_page is None:

                new_page = page



            new_page.bring_to_front()



            log(
                "TAB ĐANG XỬ LÝ:"
            )

            print(
                new_page.url
            )



            # đợi dữ liệu render

            new_page.wait_for_timeout(15000)



            # =========================
            # DEBUG TEXT TOÀN BỘ TRANG
            # =========================


            text = new_page.locator(
                "body"
            ).inner_text()



            txt_file = (
                OUTPUT
                +
                "/thong_tin_khach.txt"
            )


            with open(
                txt_file,
                "w",
                encoding="utf-8"
            ) as f:

                f.write(text)



            # lấy kích thước thật

            size = new_page.evaluate(
                """
                () => {
                    return {
                        width: document.documentElement.scrollWidth,
                        height: document.documentElement.scrollHeight,
                        clientWidth: document.documentElement.clientWidth,
                        clientHeight: document.documentElement.clientHeight
                    }
                }
                """
            )



            print(
                "KÍCH THƯỚC TRANG:"
            )

            print(size)



            print(
                "SỐ KÝ TỰ LẤY ĐƯỢC:",
                len(text)
            )



            # screenshot hiện tại

            img = (
                OUTPUT
                +
                "/screenshot.png"
            )


            new_page.screenshot(
                path=img
            )



            log(
                "DEBUG HOÀN TẤT"
            )


            print(
                "TEXT:",
                txt_file
            )


            print(
                "IMAGE:",
                img
            )



        except Exception as e:


            print(
                "LỖI:",
                e
            )



        finally:


            browser.close()



if __name__ == "__main__":


    shd = input(
        "Nhập SHD: "
    )


    run(shd)
