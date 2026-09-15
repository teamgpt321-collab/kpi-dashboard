"use client";

import { useState } from "react";
import { employees } from "@/data/kpi";
import { summary } from "@/data/summary";


function checkKPI(emp:any){

  const issues:string[] = [];

  if(emp.correct < 97)
    issues.push(`Đúng hẹn ${emp.correct.toFixed(2)}% < 97%`);

  if(emp.cll >= 7)
    issues.push(`CLL ${emp.cll.toFixed(2)}% >= 7%`);

  if(emp.cll3 >= 0.5)
    issues.push(`CLL3 ${emp.cll3.toFixed(2)}% >= 0.5%`);

  if(emp.sevenDay > 0)
    issues.push(`7N ${emp.sevenDay.toFixed(2)}% > 0%`);

  if(emp.responseTK >= 18)
    issues.push(`Response TK ${emp.responseTK.toFixed(2)}h >= 18h`);

  if(emp.responseBT >= 9)
    issues.push(`Response BT ${emp.responseBT.toFixed(2)}h >= 9h`);

  return issues;

}

export default function Home(){

const [selectedEmployee,setSelectedEmployee] = useState<any>(null);


const [keyword,setKeyword]=useState("");
const [status,setStatus]=useState("Tất cả");
const [block,setBlock]=useState("Tất cả");



const blocks = [
  "Tất cả",
  ...Array.from(new Set(employees.map(emp => emp.block)))
];


const filteredEmployees = employees.filter(emp=>{

return (

emp.name
.toLowerCase()
.includes(keyword.toLowerCase())

&&

(
status==="Tất cả"
||
emp.status===status
)

&&

(
block==="Tất cả"
||
emp.block===block
)

)

});




return (

<main className="min-h-screen bg-gray-100 p-8">


<h1 className="text-3xl font-bold mb-8">
KPI Performance Dashboard
</h1>



<div className="grid grid-cols-4 gap-5">


<Card title="Tổng nhân sự" value={summary.totalEmployees}/>


<Card title="Đúng hẹn" value={`${summary.correct}%`}/>


<Card
title="CLL"
value={`${summary.cll}%`}
color="text-red-600"
/>


<Card
title="Cảnh báo"
value={summary.warning}
color="text-orange-600"
/>


</div>




<div className="bg-white rounded-xl shadow mt-8 p-6">


<h2 className="text-xl font-bold mb-5">
Chi tiết KPI nhân sự
</h2>



<div className="flex gap-4 mb-5">


<input
className="border rounded p-2 flex-1"
placeholder="Tìm nhân sự..."
value={keyword}
onChange={(e)=>setKeyword(e.target.value)}
/>



<select
className="border rounded p-2"
value={block}
onChange={(e)=>setBlock(e.target.value)}
>

{blocks.map(b=>(
<option key={b}>
{b}
</option>
))}

</select>


<select
className="border rounded p-2"
value={block}
onChange={(e)=>setBlock(e.target.value)}
>
{blocks.map(b=>(
<option key={b}>
{b}
</option>
))}
</select>


<select
className="border rounded p-2"
value={status}
onChange={(e)=>setStatus(e.target.value)}
>

<option>
Tất cả
</option>

<option>
Tốt
</option>

<option>
Cảnh báo
</option>

</select>


</div>




<table className="w-full">


<thead>

<tr className="border-b">

<th className="text-left p-3">
Nhân sự
</th>

<th>
Block
</th>

<th>
Đội
</th>

<th>
Đúng hẹn
</th>

<th>
CLL
</th>

<th>
7N
</th>

<th>
Trạng thái
</th>

</tr>

</thead>



<tbody>


{
filteredEmployees.map(emp=>(


<tr
key={emp.name}
className="border-b hover:bg-gray-100 cursor-pointer"
onClick={()=>setSelectedEmployee(emp)}
>


<td className="p-3 font-bold">
{emp.name}
</td>


<td>
{emp.block}
</td>


<td>
{emp.team}
</td>


<td>
{emp.correct.toFixed(2)}%
</td>


<td>
{emp.cll.toFixed(2)}%
</td>


<td>
{emp.sevenDay.toFixed(2)}%
</td>


<td>

{
emp.status === "Cảnh báo"

?

<span className="text-red-600 font-bold">
Cảnh báo
</span>

:

<span className="text-green-600 font-bold">
Tốt
</span>

}

</td>


</tr>


))
}


</tbody>


</table>


</div>





{
selectedEmployee &&


<div className="fixed inset-0 bg-black/40 flex items-center justify-center">


<div className="bg-white rounded-xl p-8 w-[500px] shadow">


<h2 className="text-2xl font-bold mb-4">
{selectedEmployee.name}
</h2>


<p>
<b>Block:</b> {selectedEmployee.block}
</p>


<p>
<b>Đội:</b> {selectedEmployee.team}
</p>



<hr className="my-4"/>



<h3 className="font-bold text-lg">
Đánh giá KPI
</h3>



{

selectedEmployee.kpiFailCount === 0

?

<p className="text-green-600 font-bold mt-3">
✅ Đạt KPI
</p>


:


<div className="bg-red-50 p-3 rounded mt-3">

<p className="text-red-600 font-bold">
⚠ Cảnh báo
</p>


<ul className="list-disc ml-5">

<li>
Số KPI chưa đạt: {selectedEmployee.kpiFailCount}
</li>

</ul>


</div>


}




<hr className="my-4"/>



<p>
Đúng hẹn: {selectedEmployee.correct.toFixed(2)}%
</p>

<p>
CLL: {selectedEmployee.cll.toFixed(2)}%
</p>

<p>
CLL3: {selectedEmployee.cll3.toFixed(2)}%
</p>

<p>
7N: {selectedEmployee.sevenDay.toFixed(2)}%
</p>

<p>
Response TK: {selectedEmployee.responseTK.toFixed(2)}h
</p>

<p>
Response BT: {selectedEmployee.responseBT.toFixed(2)}h
</p>

<p>
TK quá 72H: {selectedEmployee.over72h}
</p>

<p>
BT quá 24H: {selectedEmployee.over24h}
</p>



<button
className="mt-5 bg-black text-white px-5 py-2 rounded"
onClick={()=>setSelectedEmployee(null)}
>
Đóng
</button>



</div>


</div>


}



</main>

)

}




function Card({
title,
value,
color="text-black"
}:any){

return (

<div className="bg-white rounded-xl p-6 shadow">

<p className="text-gray-500">
{title}
</p>


<h2 className={`text-4xl font-bold ${color}`}>
{value}
</h2>

</div>

)

}
