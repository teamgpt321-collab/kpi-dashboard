from playwright.sync_api import sync_playwright
import re


URL = "http://port.fpt.net/Index.aspx"

USERNAME = "phuongnam.tiendv1@fpt.net"
PASSWORD = "Tien060895@"



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







def run(shd):


    log(
        f"[KIỂM TRA PORT] {shd}"
    )



    result = {
        "shd": shd,
        "thong_so_thi_cong": "Không tìm thấy"
    }



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



            # =========================
            # LOGIN
            # =========================


            log("MỞ PORT")


            page.goto(URL)


            page.wait_for_timeout(5000)



            page.locator(
                "#username"
            ).fill(
                USERNAME
            )



            page.locator(
                "#password"
            ).fill(
                PASSWORD
            )



            page.locator(
                "#kc-login"
            ).click()



            log("LOGIN OK")


            page.wait_for_timeout(10000)





            # =========================
            # MENU FRAME
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

                shd

            )



            log(
                f"NHẬP SHD: {shd}"
            )





            # SEARCH


            main_frame.locator(

                "#btnSearch"

            ).click()



            log("ĐÃ TÌM KIẾM")



            page.wait_for_timeout(10000)





            # =========================
            # CLICK HỢP ĐỒNG
            # =========================


            contract_link = main_frame.locator(

                'a.link[href*="/FTTH_NewPort/Contract/Insert/"]'

            )



            if contract_link.count() == 0:


                raise Exception(
                    "Không tìm thấy hợp đồng"
                )



            contract_link.first.click()



            log(
                "ĐÃ MỞ CHI TIẾT HỢP ĐỒNG"
            )



            page.wait_for_timeout(10000)





            # =========================
            # LẤY DATA
            # =========================


            detail_frame = page.frame(

                name="mainFrame"

            )



            if not detail_frame:

                detail_frame = page




            body_text = detail_frame.locator(

                "body"

            ).inner_text()



            print(body_text)





            # =========================
            # THÔNG SỐ THI CÔNG
            # =========================


            match = re.search(

                r"Thông số thi công:\s*(.+)",

                body_text

            )



            if match:


                thong_so = match.group(1).strip()


                result["thong_so_thi_cong"] = thong_so




            return (
                f"""
📋 KẾT QUẢ KIỂM TRA PORT

SHĐ:
{result['shd']}

🔌 Thông số thi công:
{result['thong_so_thi_cong']}
"""
            )



        except Exception as e:


            log(
                f"LỖI: {e}"
            )


            raise



        finally:


            browser.close()
