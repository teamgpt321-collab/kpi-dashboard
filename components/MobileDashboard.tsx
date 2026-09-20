"use client";


export default function MobileDashboard({
  employees,
  setSelectedEmployee,
  setSelectedCLLEmployee
}:any){


return (

<div className="md:hidden space-y-4">


{
employees.map((emp:any)=>{


const warning =
emp.correct < 97 ||
emp.cll >= 7 ||
emp.sevenDay > 0;



return (

<div
key={emp.name}
className="
bg-white
rounded-3xl
p-5
shadow-sm
border
border-gray-100
"
>


{/* HEADER */}

<div
className="
flex
justify-between
items-start
"
onClick={()=>setSelectedEmployee(emp)}
>


<div>


<h2
className="
font-bold
text-base
text-gray-900
"
>
{emp.name}
</h2>


<p
className="
text-sm
text-gray-500
mt-1
"
>
{emp.block}
</p>


<p
className="
text-xs
text-gray-400
mt-1
"
>
Đội {emp.team}
</p>


</div>



<span
className={`
px-3
py-1
rounded-full
text-xs
font-bold

${
warning
?
"bg-red-100 text-red-600"
:
"bg-green-100 text-green-600"
}

`}
>

{
warning
?
"Cảnh báo"
:
"Tốt"
}

</span>


</div>





{/* KPI */}

<div
className="
grid
grid-cols-3
gap-3
mt-5
"
>


<KpiBox

title="Đúng hẹn"

value={`${emp.correct.toFixed(2)}%`}

/>



<KpiBox

title="CLL"

value={`${emp.cll.toFixed(2)}%`}

danger={emp.cll>=7}

onClick={(e:any)=>{

e.stopPropagation();

setSelectedCLLEmployee(emp);

}}

/>



<KpiBox

title="7N"

value={`${emp.sevenDay.toFixed(2)}%`}

danger={emp.sevenDay>0}

/>



</div>





{/* PROGRESS */}

<div
className="
mt-5
"
>


<div
className="
flex
justify-between
text-xs
text-gray-500
mb-2
"
>

<span>
Hiệu suất KPI
</span>


<span>

{
warning
?
"Cần cải thiện"
:
"Đạt"
}

</span>


</div>



<div
className="
h-2
rounded-full
bg-gray-100
overflow-hidden
"
>


<div

className={`
h-full
rounded-full

${
warning
?
"bg-red-500 w-[65%]"
:
"bg-green-500 w-full"
}

`}

/>


</div>


</div>





<button

className="
w-full
mt-4
text-blue-600
text-sm
font-medium
"

onClick={()=>setSelectedEmployee(emp)}

>

Xem chi tiết →

</button>



</div>


)


})

}


</div>

)

}





function KpiBox({
title,
value,
danger,
onClick
}:any){


return (

<div

onClick={onClick}

className="
bg-gray-50
rounded-2xl
p-3
text-center
cursor-pointer
active:scale-95
transition
"

>


<p
className="
text-xs
text-gray-500
"
>
{title}
</p>


<p
className={`
font-bold
text-lg
mt-1

${
danger
?
"text-red-600"
:
"text-gray-900"
}

`}
>

{value}

</p>


</div>


)

}
