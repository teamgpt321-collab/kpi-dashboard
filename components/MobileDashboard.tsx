
"use client";


export default function MobileDashboard({
  employees,
  setSelectedEmployee,
  setSelectedCLLEmployee
}:any){


return (

<div className="md:hidden space-y-4">


{
employees.map((emp:any)=>(

<div
key={emp.name}
className="
bg-white
rounded-xl
shadow
p-4
border
"
onClick={()=>setSelectedEmployee(emp)}
>


<div className="flex justify-between items-start gap-3">


<div className="min-w-0">

<h2 className="
font-bold 
text-lg
truncate
">
{emp.name}
</h2>


<p className="
text-gray-500 
text-sm
break-words
">
{emp.block}
</p>

</div>



<span
className={
`
px-2
py-1
rounded-full
text-xs
font-bold
whitespace-nowrap
${
emp.status==="Tốt"
?
"bg-green-100 text-green-700"
:
"bg-red-100 text-red-700"
}
`
}
>

{emp.status}

</span>


</div>



<div className="grid grid-cols-2 gap-4 mt-4">


<div>

<p className="text-gray-500 text-sm">
Đội
</p>

<b>
{emp.team}
</b>

</div>



<div>

<p className="text-gray-500 text-sm">
Đúng hẹn
</p>

<b>
{emp.correct.toFixed(2)}%
</b>

</div>



<div
className="cursor-pointer"
onClick={(e)=>{

e.stopPropagation();

setSelectedCLLEmployee(emp);

}}
>

<p className="text-gray-500 text-sm">
CLL
</p>

<b className="text-blue-600">
{emp.cll.toFixed(2)}%
</b>

</div>



<div>

<p className="text-gray-500 text-sm">
7N
</p>

<b>
{emp.sevenDay.toFixed(2)}%
</b>

</div>


</div>



<div className="mt-4">


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


</div>


</div>

))

}


</div>

)

}
