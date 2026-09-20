import { NextResponse } from "next/server";
import { supabase } from "@/lib/supabase";


export async function GET() {

    try {

        const { data: history, error } =
            await supabase
                .from("tool_usage")
                .select("*")
                .order("time", {
                    ascending: false
                });


        if(error){

            throw error;

        }


        const cleanHistory =
            (history || [])
            .filter(
                (x:any)=>
                    x.user &&
                    x.user !== "None"
            )
            .map(
                (x:any)=>({

                    ...x,

                    userName:
                        x.userName ||
                        x.user

                })
            );



        // =========================
        // THỐNG KÊ TOOL
        // =========================

        const toolStats:any = {};


        cleanHistory.forEach(
            (item:any)=>{

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
        // THEO NGÀY
        // =========================

        const dailyMap:any = {};


        cleanHistory.forEach(
            (item:any)=>{

                const date =
                    item.time
                    .split("T")[0]
                    .split(" ")[0];


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
                    cleanHistory.length,


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


    }
    catch(error:any){

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
