"use client";

import { useState } from "react";
import { employees } from "@/data/kpi";
import { summary } from "@/data/summary";
import { cllDetail } from "@/data/cll-detail";


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
const [selectedCLLEmployee,setSelectedCLLEmployee] = useState<any>(null);
const [showCLL,setShowCLL]=useState(false);


const [keyword,setKeyword]=useState("");
const [status,setStatus]=useState("Tất cả");
const [blocksSelected,setBlocksSelected]=useState<string[]>([]);
const [employeesSelected,setEmployeesSelected]=useState<string[]>([]);
const [showBlock,setShowBlock]=useState(false);
const [showEmployee,setShowEmployee]=useState(false);



const blocks = [
  ...Array.from(new Set(employees.map(emp => emp.block)))
];

const filteredEmployeeOptions = employees.filter(emp =>
  blocksSelected.length === 0 ||
  blocksSelected.includes(emp.block)
);



const cllByEmployee = Object.values(
  cllDetail.reduce((acc:any,item:any)=>{

    const key=item.employee;

    if(!acc[key]){
      acc[key]={
        employee:key,
        count:0,
        details:[]
      };
    }

    acc[key].count++;
    acc[key].details.push(item);

    return acc;

  },{})
);



const selectedCLLDetails =
selectedCLLEmployee
?
cllDetail.filter(
x =>
x.employee.toUpperCase()
===
selectedCLLEmployee.name.toUpperCase()
)
:
[];

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
blocksSelected.length === 0
||
blocksSelected.includes(emp.block)
)

&&

(
employeesSelected.length === 0
||
employeesSelected.includes(emp.name)
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
onClick={()=>setShowCLL(true)}
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


<div className="relative">

<button
className="border rounded p-2 w-56 text-left bg-white"
onClick={()=>setShowBlock(!showBlock)}
>
{
blocksSelected.length===0
?
"Block: Tất cả"
:
`Block (${blocksSelected.length})`
}
</button>


{
showBlock &&
<div className="absolute bg-white border shadow rounded p-3 w-64 z-20">


<label className="block mb-2">

<input
type="checkbox"
checked={blocksSelected.length===0}
onChange={()=>{
setBlocksSelected([]);
setEmployeesSelected([]);
}}
/>

<span className="ml-2">
Tất cả
</span>

</label>


{
blocks.map(b=>(

<label
key={b}
className="block mb-2"
>

<input
type="checkbox"
checked={blocksSelected.includes(b)}
onChange={()=>{

if(blocksSelected.includes(b))
{
setBlocksSelected(
blocksSelected.filter(x=>x!==b)
)
}
else
{
setBlocksSelected(
[...blocksSelected,b]
)
}

setEmployeesSelected([]);

}}
/>

<span className="ml-2">
{b}
</span>

</label>

))
}


</div>
}


</div>



<div className="relative">


<button
className="border rounded p-2 w-56 text-left bg-white"
onClick={()=>setShowEmployee(!showEmployee)}
>

{
employeesSelected.length===0
?
"Nhân viên: Tất cả"
:
`Nhân viên (${employeesSelected.length})`
}

</button>



{
showEmployee &&

<div className="absolute bg-white border shadow rounded p-3 w-64 max-h-80 overflow-auto z-20">


<label className="block mb-2">

<input
type="checkbox"
checked={employeesSelected.length===0}
onChange={()=>{
setEmployeesSelected([]);
}}
/>

<span className="ml-2">
Tất cả
</span>

</label>



{
filteredEmployeeOptions.map(emp=>(

<label
key={emp.name}
className="block mb-2"
>


<input
type="checkbox"
checked={employeesSelected.includes(emp.name)}
onChange={()=>{

if(employeesSelected.includes(emp.name))
{
setEmployeesSelected(
employeesSelected.filter(x=>x!==emp.name)
)
}
else
{
setEmployeesSelected(
[...employeesSelected,emp.name]
)
}

}}
/>


<span className="ml-2">
{emp.name}
</span>


</label>

))
}



</div>

}



</div>




<select
className="border rounded p-2"
value={status}
onChange={(e)=>setStatus(e.target.value)}
>

<option>Tất cả</option>
<option>Tốt</option>
<option>Cảnh báo</option>

</select>


</div>





<table className="w-full table-fixed">


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


<td className="w-[18%] p-3">
{emp.block}
</td>


<td className="w-[8%] text-center">
{emp.team}
</td>


<td className="w-[10%] text-center">
{emp.correct.toFixed(2)}%
</td>


<td
className="w-[10%] text-center cursor-pointer text-blue-600 font-bold hover:underline"
onClick={(e)=>{

e.stopPropagation();

setSelectedCLLEmployee(emp);

}}
>
{emp.cll.toFixed(2)}%
</td>


<td className="w-[10%] text-center">
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
showCLL &&

<div className="fixed inset-0 bg-black/40 flex items-center justify-center">

<div className="bg-white rounded-xl p-8 w-[700px] shadow">

<h2 className="text-2xl font-bold mb-5">
Chi tiết CLL
</h2>


<p className="mb-4">
Tổng phiếu CLL: {cllDetail.length}
</p>


<table className="w-full border">

<thead>
<tr className="border-b">

<th className="p-2 text-left">
Nhân sự
</th>

<th>
Số phiếu
</th>

</tr>
</thead>


<tbody>

{
cllByEmployee.map((x:any)=>(

<tr key={x.employee} className="border-b">

<td className="p-2">
{x.employee}
</td>

<td className="text-center">
{x.count}
</td>

</tr>

))
}

</tbody>

</table>


<button
className="mt-5 bg-black text-white px-5 py-2 rounded"
onClick={()=>setShowCLL(false)}
>
Đóng
</button>


</div>

</div>

}



{
selectedCLLEmployee &&

<div className="fixed inset-0 bg-black/40 flex items-center justify-center">

<div className="bg-white rounded-xl p-8 w-[900px] shadow">


<h2 className="text-2xl font-bold mb-5">
Chi tiết CLL - {selectedCLLEmployee.name}
</h2>


<p className="mb-4">
Số phiếu CLL: {selectedCLLDetails.length}
</p>


<table className="w-full border">

<thead>

<tr className="border-b">

<th className="p-2 text-left">
Số HĐ
</th>

<th>
Khách hàng
</th>

<th>
Tạo CL
</th>

<th>
Hoàn tất
</th>

</tr>

</thead>


<tbody>

{
selectedCLLDetails.map((x:any)=>(

<tr
key={x.contract}
className="border-b"
>

<td className="p-2">
{x.contract}
</td>

<td>
{x.customer}
</td>

<td>
{x.createTime}
</td>

<td>
{x.finishTime}
</td>

</tr>

))
}

</tbody>

</table>


<button
className="mt-5 bg-black text-white px-5 py-2 rounded"
onClick={()=>setSelectedCLLEmployee(null)}
>
Đóng
</button>


</div>

</div>

}


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
color="text-black",
onClick
}:any){

return (

<div
className="bg-white rounded-xl p-6 shadow cursor-pointer hover:bg-gray-50"
onClick={onClick}
>

<p className="text-gray-500">
{title}
</p>


<h2 className={`text-4xl font-bold ${color}`}>
{value}
</h2>

</div>

)

}
