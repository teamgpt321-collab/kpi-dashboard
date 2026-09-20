import { NextResponse } from "next/server";
import fs from "fs";
import path from "path";


export async function POST(
    request: Request
) {

    try {

        const body = await request.json();


        const {
            tool,
            user,
            shd,
            time,
            result
        } = body;



        if(
            !tool ||
            !user ||
            !shd
        ){

            return NextResponse.json(
                {
                    error:"Missing data"
                },
                {
                    status:400
                }
            );

        }



        const filePath = path.join(
            process.cwd(),
            "telebot/data/usage_history.json"
        );



        let history:any[] = [];



        if(fs.existsSync(filePath)){

            history = JSON.parse(
                fs.readFileSync(
                    filePath,
                    "utf8"
                )
            );

        }



        history.push({

            tool,

            user:String(user),

            shd,

            time:
                time ||
                new Date()
                .toISOString()
                .replace("T"," ")
                .substring(0,19),

            result:
                result ||
                "success"

        });




        fs.writeFileSync(
            filePath,
            JSON.stringify(
                history,
                null,
                2
            ),
            "utf8"
        );



        return NextResponse.json({

            success:true

        });



    }
    catch(error:any){


        console.error(
            "SAVE TOOL USAGE ERROR:",
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
