import { NextResponse } from "next/server";
import fs from "fs";
import path from "path";


export async function GET() {

    try {

        const historyPath = path.join(
            process.cwd(),
            "telebot/data/usage_history.json"
        );


        const userPath = path.join(
            process.cwd(),
            "telebot/data/telegram_users.json"
        );


        const history = JSON.parse(
            fs.readFileSync(
                historyPath,
                "utf8"
            )
        );


        let userMap:any = {};


        if (fs.existsSync(userPath)) {

            const telegramUsers = JSON.parse(
                fs.readFileSync(
                    userPath,
                    "utf8"
                )
            );


            telegramUsers.forEach(
                (u:any)=> {

                    userMap[String(u.id)] =
                        u.name ||
                        (
                            u.username
                            ? "@" + u.username
                            : u.id
                        );

                }
            );

        }



        const cleanHistory =
            history
            .filter(
                (x:any)=>
                    x.user &&
                    x.user !== "None"
            )
            .map(
                (x:any)=>({

                    ...x,

                    userName:
                        userMap[String(x.user)]
                        || x.user

                })
            )
            .reverse();



        // =========================
        // THỐNG KÊ THEO TOOL ĐỘNG
        // =========================

        const toolStats:any = {};


        history.forEach(
            (item:any)=> {

                const tool =
                    item.tool || "unknown";


                if(!toolStats[tool]){

                    toolStats[tool] = 0;

                }


                toolStats[tool]++;

            }
        );



        // =========================
        // USER UNIQUE
        // =========================

        const uniqueUsers = [
            ...new Set(
                cleanHistory.map(
                    (x:any)=>x.user
                )
            )
        ];



        // =========================
        // THỐNG KÊ THEO NGÀY
        // =========================

        const dailyMap:any = {};


        cleanHistory.forEach(
            (item:any)=> {


                const date =
                    item.time.split(" ")[0];



                if(!dailyMap[date]){

                    dailyMap[date] = {
                        date
                    };

                }



                const tool =
                    item.tool || "unknown";


                if(!dailyMap[date][tool]){

                    dailyMap[date][tool] = 0;

                }


                dailyMap[date][tool]++;


            }
        );



        return NextResponse.json({

            summary: {

                total:
                    history.length,


                tools:
                    toolStats,


                users:
                    uniqueUsers.length

            },


            history:
                cleanHistory,


            dailyUsage:
                Object.values(dailyMap)

        });



    } catch(error:any){


        console.error(
            "TOOL USAGE ERROR:",
            error
        );


        return NextResponse.json(
            {
                error:error.message
            },
            {
                status:500
            }
        );

    }

}
