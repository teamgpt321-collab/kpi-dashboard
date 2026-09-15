
"use client";

export default function DesktopDashboard({
  employees,
  setSelectedEmployee,
  setSelectedCLLEmployee
}:any){

return (

<div className="hidden md:block">

<table className="w-full table-fixed">

<colgroup>
<col className="w-[25%]" />
<col className="w-[18%]" />
<col className="w-[8%]" />
<col className="w-[10%]" />
<col className="w-[10%]" />
<col className="w-[10%]" />
<col className="w-[12%]" />
</colgroup>


<thead>

<tr className="border-b">

<th className="p-3 text-left">
Nhân sự
</th>

<th className="p-3 text-left">
Block
</th>

<th className="p-3 text-center">
Đội
</th>

<th className="p-3 text-center">
Đúng hẹn
</th>

<th className="p-3 text-center">
CLL
</th>

<th className="p-3 text-center">
7N
</th>

<th className="p-3 text-center">
Trạng thái
</th>

</tr>

</thead>


<tbody>

{
employees.map((emp:any)=>(

<tr
key={emp.name}
className="border-b hover:bg-gray-50 cursor-pointer"
onClick={()=>setSelectedEmployee(emp)}
>


<td className="p-3 font-bold">
{emp.name}
</td>


<td className="p-3">
{emp.block}
</td>


<td className="text-center">
{emp.team}
</td>


<td className="text-center">
{emp.correct.toFixed(2)}%
</td>


<td
className="text-center text-blue-600 font-bold cursor-pointer"
onClick={(e)=>{
e.stopPropagation();
setSelectedCLLEmployee(emp);
}}
>
{emp.cll.toFixed(2)}%
</td>


<td className="text-center">
{emp.sevenDay.toFixed(2)}%
</td>


<td className="text-center">

<span
className={
emp.status==="Tốt"
?
"text-green-600 font-bold"
:
"text-red-600 font-bold"
}
>

{emp.status}

</span>

</td>


</tr>

))

}

</tbody>

</table>

</div>

)

}
