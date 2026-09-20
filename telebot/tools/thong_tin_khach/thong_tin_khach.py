from playwright.sync_api import sync_playwright
import time


URL = "http://partner.fpt.net/pt-portal/monitor"

USERNAME = "phuongnam.tiendv1"
PASSWORD = "Thithao1996@"



def log(msg):

    print("=" * 60)
    print(msg)
    print("=" * 60)



def run(shd):


    log(
        f"[THÔNG TIN KHÁCH] {shd}"
    )


    with sync_playwright() as p:


        browser = p.chromium.launch(
            headless=True,
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


            # LOGIN

            log("Mở trang")


            page.goto(
                URL
            )


            page.wait_for_timeout(
                5000
            )



            log("Login")


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


            page.locator(
                "#btnLogin"
            ).click()



            page.wait_for_timeout(
                10000
            )



            log("Login OK")



            # NHẬP SHD


            search = page.locator(
                'input[placeholder="Nhập số hợp đồng..."]'
            )


            search.wait_for(
                timeout=20000
            )


            search.fill(
                shd
            )


            old_pages = context.pages


            page.keyboard.press(
                "Enter"
            )



            # CHỜ TAB MỚI


            new_page = None


            for i in range(30):


                page.wait_for_timeout(
                    1000
                )


                if len(context.pages) > len(old_pages):

                    new_page = context.pages[-1]

                    break



            if not new_page:

                new_page = page



            log(
                "Đã vào trang thông tin"
            )



            # LOAD FULL


            new_page.wait_for_load_state(
                "networkidle",
                timeout=30000
            )


            new_page.wait_for_timeout(
                15000
            )



            # scroll toàn trang

            new_page.evaluate(
                """
                window.scrollTo(
                    0,
                    document.body.scrollHeight
                )
                """
            )


            new_page.wait_for_timeout(
                3000
            )


            new_page.evaluate(
                """
                window.scrollTo(
                    0,
                    0
                )
                """
            )


            new_page.wait_for_timeout(
                3000
            )



            # CHỤP ẢNH


            path = (
                "/home/tiendv1/kpi-dashboard/"
                "thong_tin_khach_result.png"
            )


            new_page.screenshot(
                path=path,
                full_page=True
            )



            log(
                "Đã chụp xong"
            )


            return path



        except Exception as e:


            log(
                f"LỖI: {e}"
            )


            raise



        finally:


            browser.close()
