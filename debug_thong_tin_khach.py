from playwright.sync_api import sync_playwright
import os
import json
import shutil
import time


URL = "http://partner.fpt.net/pt-portal/monitor"

USERNAME = "phuongnam.tiendv1"
PASSWORD = "Thithao1996@"


OUTPUT = "/home/tiendv1/kpi-dashboard/debug_khachhang"


def log(msg):
    print("=" * 60)
    print(msg)
    print("=" * 60)



def run(shd):

    # Xóa kết quả cũ
    if os.path.exists(OUTPUT):
        shutil.rmtree(OUTPUT)

    os.makedirs(OUTPUT)


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

            log("MỞ TRANG")

            page.goto(URL)

            page.wait_for_timeout(5000)



            # LOGIN

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



            # NHẬP SHD

            search = page.locator(
                'input[placeholder="Nhập số hợp đồng..."]'
            )


            search.wait_for(
                timeout=20000
            )


            search.fill(shd)

            old_pages = context.pages


            page.keyboard.press("Enter")



            new_page = page


            for i in range(30):

                page.wait_for_timeout(1000)

                if len(context.pages) > len(old_pages):

                    new_page = context.pages[-1]
                    break



            log("ĐÃ VÀO THÔNG TIN KHÁCH")



            new_page.wait_for_load_state(
                "networkidle",
                timeout=30000
            )


            new_page.wait_for_timeout(10000)



            # ============================
            # CHỤP FULL PAGE
            # ============================

            new_page.screenshot(
                path=f"{OUTPUT}/01_full_page.png",
                full_page=True
            )



            # ============================
            # TÌM VÙNG SCROLL
            # ============================


            scroll_data = new_page.evaluate("""
            () => {

                let result=[];


                document.querySelectorAll("*").forEach((e,index)=>{

                    let style=getComputedStyle(e);


                    if(
                        e.scrollHeight > e.clientHeight + 100
                        &&
                        (
                            style.overflow=="auto"
                            ||
                            style.overflow=="scroll"
                            ||
                            style.overflowY=="auto"
                            ||
                            style.overflowY=="scroll"
                        )
                    ){

                        result.push({

                            index:index,

                            tag:e.tagName,

                            id:e.id,

                            class:e.className,

                            scrollHeight:e.scrollHeight,

                            clientHeight:e.clientHeight

                        });

                    }


                });


                return result;

            }
            """)



            with open(
                f"{OUTPUT}/scroll_info.json",
                "w",
                encoding="utf-8"
            ) as f:

                json.dump(
                    scroll_data,
                    f,
                    indent=4,
                    ensure_ascii=False
                )



            print("CÁC VÙNG SCROLL:")

            print(
                json.dumps(
                    scroll_data,
                    indent=4,
                    ensure_ascii=False
                )
            )



            # ============================
            # CUỘN TỪNG VÙNG
            # ============================


            for i,item in enumerate(scroll_data):


                result = new_page.evaluate("""
                (index)=>{

                    let arr=[...document.querySelectorAll("*")];

                    let e=arr[index];


                    if(!e)
                        return false;



                    e.style.height=e.scrollHeight+"px";

                    e.style.maxHeight="none";

                    e.style.overflow="visible";

                    return true;

                }
                """, item["index"])



                new_page.wait_for_timeout(3000)



                new_page.screenshot(
                    path=f"{OUTPUT}/scroll_{i}.png",
                    full_page=True
                )



            # TEXT

            text = new_page.locator(
                "body"
            ).inner_text()


            with open(
                f"{OUTPUT}/text.txt",
                "w",
                encoding="utf-8"
            ) as f:

                f.write(text)



            log("DEBUG HOÀN TẤT")

            print(
                "Kết quả:",
                OUTPUT
            )



        except Exception as e:

            print("LỖI:",e)


        finally:

            browser.close()



if __name__=="__main__":

    shd=input(
        "Nhập SHD: "
    )


    run(shd)
