import { NextResponse } from "next/server";
import { supabase } from "@/lib/supabase";


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



        if (
            !tool ||
            !user ||
            !shd
        ) {

            return NextResponse.json(
                {
                    error: "Missing data"
                },
                {
                    status: 400
                }
            );

        }



        const data = {

            tool,

            user: String(user),

            shd,

            time:
                time ||
                new Date()
                    .toISOString()
                    .replace("T", " ")
                    .substring(0, 19),

            result:
                result ||
                "success"

        };



        console.log(
            "INSERT DATA:",
            data
        );


        console.log(
            "SUPABASE URL:",
            process.env.SUPABASE_URL
        );


        const {
            data: inserted,
            error
        } = await supabase
            .from("tool_usage")
            .insert(data)
            .select();



        if (error) {

            console.error(
                "SUPABASE ERROR:",
                error
            );


            return NextResponse.json(
                {
                    error: error.message,
                    details: error
                },
                {
                    status: 500
                }
            );

        }



        return NextResponse.json(
            {
                success: true,
                data: inserted
            }
        );


    }
    catch (error: any) {


        console.error(
            "SAVE TOOL USAGE ERROR:",
            error
        );


        console.error(
            "CAUSE:",
            error?.cause
        );


        return NextResponse.json(
            {
                error: error.message,
                cause: String(error?.cause)
            },
            {
                status: 500
            }
        );

    }

}
