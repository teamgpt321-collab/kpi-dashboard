"use client";

export default function MobileDashboard({
  employees,
  setSelectedEmployee,
  setSelectedCLLEmployee
}: any) {

  return (

    <div className="md:hidden space-y-4">

      {employees.map((emp:any)=>{

        const warning =
          emp.correct < 97 ||
          emp.cll >= 7 ||
          emp.sevenDay > 0;


        return (

          <div
            key={emp.name}
            onClick={()=>setSelectedEmployee(emp)}
            className="
              bg-white
              rounded-3xl
              p-5
              shadow-sm
              border
              border-gray-100
            "
          >


            {/* Header */}

            <div className="
              flex
              justify-between
              items-start
            ">


              <div>

                <h3
                className="
                  text-base
                  font-bold
                  text-gray-900
                "
                >
                  {emp.name}
                </h3>


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
                font-semibold

                ${
                  warning
                  ?
                  "bg-red-50 text-red-600"
                  :
                  "bg-green-50 text-green-600"
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


              <KPI
              title="Đúng hẹn"
              value={`${emp.correct.toFixed(2)}%`}
              />


              <KPI
              title="CLL"
              value={`${emp.cll.toFixed(2)}%`}
              danger={emp.cll>=7}
              onClick={(e:any)=>{
                e.stopPropagation();
                setSelectedCLLEmployee(emp);
              }}
              />


              <KPI
              title="7N"
              value={`${emp.sevenDay.toFixed(2)}%`}
              danger={emp.sevenDay>0}
              />


            </div>



            {/* Progress */}

            <div className="mt-5">


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
                  {warning ? "Cần cải thiện":"Đạt"}
                </span>

              </div>


              <div
              className="
                h-2
                bg-gray-100
                rounded-full
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



            <div
            className="
              text-center
              text-blue-600
              text-sm
              font-medium
              mt-4
            "
            >
              Xem chi tiết →
            </div>


          </div>

        )

      })}


    </div>

  )

}



function KPI({
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
