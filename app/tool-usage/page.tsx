"use client";

import { useEffect, useMemo, useState } from "react";


export default function ToolUsagePage(){

    const [data,setData] = useState<any>(null);

    const [tool,setTool] = useState("all");
    const [user,setUser] = useState("all");

    const [fromDate,setFromDate] = useState("");
    const [toDate,setToDate] = useState("");



    useEffect(()=>{

        fetch("/api/tool-usage")
        .then(res=>res.json())
        .then(result=>{
            setData(result);
        })

    },[]);




    const history = data?.history || [];



    const tools = useMemo(()=>{

        return [
            "all",
            ...Array.from(
                new Set(
                    history.map(
                        (x:any)=>x.tool
                    )
                )
            )
        ];

    },[history]);



    const users = useMemo(()=>{

        return [
            "all",
            ...Array.from(
                new Set(
                    history.map(
                        (x:any)=>x.userName
                    )
                )
            )
        ];

    },[history]);




    const filteredHistory = useMemo(()=>{


        return history.filter(
            (item:any)=>{


                const date =
                    item.time.substring(0,10);



                return (

                    (
                        tool==="all"
                        ||
                        item.tool===tool
                    )

                    &&

                    (
                        user==="all"
                        ||
                        item.userName===user
                    )

                    &&

                    (
                        !fromDate
                        ||
                        date>=fromDate
                    )

                    &&

                    (
                        !toDate
                        ||
                        date<=toDate
                    )

                );

            }
        );


    },[
        history,
        tool,
        user,
        fromDate,
        toDate
    ]);





    const toolCount:any = {};


    filteredHistory.forEach(
        (item:any)=>{

            toolCount[item.tool] =
                (toolCount[item.tool] || 0) + 1;

        }
    );




    const topUsers:any = Object.values(

        filteredHistory.reduce(
            (acc:any,item:any)=>{


                if(!acc[item.userName]){

                    acc[item.userName]={
                        name:item.userName,
                        count:0
                    };

                }


                acc[item.userName].count++;


                return acc;

            },
            {}
        )

    )
    .sort(
        (a:any,b:any)=>
            b.count-a.count
    );





    if(!data){

        return (
            <div className="p-10">
                Loading...
            </div>
        );

    }




    return (

        <div className="p-8 bg-slate-50 min-h-screen">


            <h1 className="text-2xl font-bold mb-1">
                Tool Usage Dashboard
            </h1>


            <p className="text-sm text-slate-500 mb-6">
                Thống kê sử dụng các tool Telegram
            </p>




            {/* SUMMARY */}

            <div className="grid grid-cols-4 gap-4 mb-6">


                <div className="bg-white rounded-xl shadow p-5">

                    <div className="text-slate-500">
                        Tổng lượt chạy
                    </div>

                    <div className="text-3xl font-bold">
                        {filteredHistory.length}
                    </div>

                </div>



                {
                    Object.entries(toolCount)
                    .slice(0,2)
                    .map(
                        ([name,count]:any)=>(

                        <div
                            key={name}
                            className="bg-white rounded-xl shadow p-5"
                        >

                            <div className="text-slate-500">
                                {name}
                            </div>

                            <div className="text-3xl font-bold">
                                {count}
                            </div>

                        </div>

                        )
                    )
                }



                <div className="bg-white rounded-xl shadow p-5">

                    <div className="text-slate-500">
                        Nhân sự
                    </div>

                    <div className="text-3xl font-bold">
                        {
                            new Set(
                                filteredHistory.map(
                                    (x:any)=>x.user
                                )
                            ).size
                        }
                    </div>

                </div>


            </div>







            {/* FILTER */}

            <div className="bg-white rounded-xl shadow p-5 mb-6">


                <div className="font-bold mb-4">
                    🔎 Bộ lọc
                </div>


                <div className="flex gap-3">


                    <select
                        className="border rounded-lg p-2"
                        value={tool}
                        onChange={
                            e=>setTool(e.target.value)
                        }
                    >

                        {
                            tools.map(
                                (x:any)=>
                                <option key={x}>
                                    {x==="all"?"Tất cả tool":x}
                                </option>
                            )
                        }

                    </select>



                    <select
                        className="border rounded-lg p-2"
                        value={user}
                        onChange={
                            e=>setUser(e.target.value)
                        }
                    >

                        {
                            users.map(
                                (x:any)=>
                                <option key={x}>
                                    {x==="all"?"Tất cả nhân sự":x}
                                </option>
                            )
                        }

                    </select>



                    <input
                        type="date"
                        className="border rounded-lg p-2"
                        value={fromDate}
                        onChange={
                            e=>setFromDate(e.target.value)
                        }
                    />


                    <input
                        type="date"
                        className="border rounded-lg p-2"
                        value={toDate}
                        onChange={
                            e=>setToDate(e.target.value)
                        }
                    />


                </div>


            </div>







            <div className="grid grid-cols-3 gap-6">


                {/* TOP USER */}

                <div className="bg-white rounded-xl shadow p-5">


                    <h2 className="font-bold mb-4">
                        🏆 Top người dùng
                    </h2>



                    {
                        topUsers.map(
                            (x:any,index:number)=>(

                            <div
                                key={x.name}
                                className="flex justify-between py-3 border-b"
                            >

                                <span>
                                    {index+1}. {x.name}
                                </span>

                                <b>
                                    {x.count}
                                </b>

                            </div>

                            )
                        )
                    }


                </div>







                {/* HISTORY */}

                <div className="col-span-2 bg-white rounded-xl shadow p-5">


                    <h2 className="font-bold mb-4">
                        📋 Lịch sử sử dụng
                    </h2>



                    <table className="w-full text-sm">


                        <thead>

                            <tr className="border-b text-left">

                                <th className="py-2">
                                    Tool
                                </th>

                                <th>
                                    Nhân sự
                                </th>

                                <th>
                                    SHĐ
                                </th>

                                <th>
                                    Thời gian
                                </th>

                            </tr>

                        </thead>



                        <tbody>


                        {
                            filteredHistory
                            .slice(0,15)
                            .map(
                                (x:any,index:number)=>(

                                <tr
                                    key={index}
                                    className="border-b"
                                >

                                    <td className="py-2">
                                        {x.tool}
                                    </td>

                                    <td>
                                        {x.userName}
                                    </td>

                                    <td>
                                        {x.shd}
                                    </td>

                                    <td>
                                        {x.time}
                                    </td>


                                </tr>

                                )
                            )
                        }


                        </tbody>


                    </table>


                </div>


            </div>



        </div>

    );

}
