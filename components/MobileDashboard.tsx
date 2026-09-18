"use client";

export default function MobileDashboard({
  employees,
  setSelectedEmployee,
  setSelectedCLLEmployee
}: any) {


  return (

    <div className="md:hidden space-y-4">


      {
        employees.map((emp:any)=>{


          const isGood =
            emp.correct >= 97 &&
            emp.cll < 7 &&
            emp.sevenDay <= 0;


          return (

          <div
            key={emp.name}
            onClick={()=>setSelectedEmployee(emp)}
            className="
              bg-white
              rounded-3xl
              p-5
              shadow-sm
              active:scale-[0.98]
              transition
              cursor-pointer
            "
          >


            {/* Header */}

            <div className="flex justify-between items-start">


              <div>

                <h2 className="
                  font-bold
                  text-base
                  text-gray-900
                ">
                  {emp.name}
                </h2>


                <p className="
                  text-xs
                  text-gray-500
                  mt-1
                ">
                  {emp.block}
                </p>


                <p className="
                  text-xs
                  text-gray-400
                  mt-1
                ">
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
                  isGood
                  ?
                  "bg-green-100 text-green-700"
                  :
                  "bg-red-100 text-red-700"
                }
              `}
              >

              {
                isGood
                ?
                "Tốt"
                :
                "Cảnh báo"
              }

              </span>


            </div>



            {/* KPI */}

            <div className="
              grid
              grid-cols-3
              gap-3
              mt-5
            ">


              <KpiBox
                title="Đúng hẹn"
                value={`${emp.correct.toFixed(0)}%`}
                good={emp.correct>=97}
              />


              <KpiBox
                title="CLL"
                value={`${emp.cll.toFixed(2)}%`}
                good={emp.cll<7}
                onClick={(e:any)=>{
                  e.stopPropagation();
                  setSelectedCLLEmployee(emp);
                }}
              />


              <KpiBox
                title="7N"
                value={`${emp.sevenDay.toFixed(2)}%`}
                good={emp.sevenDay<=0}
              />


            </div>



            {/* Progress */}

            <div className="mt-5">


              <div className="
                flex
                justify-between
                text-xs
                text-gray-500
                mb-2
              ">

                <span>
                  Hiệu suất KPI
                </span>

                <span>
                  {
                    isGood
                    ?
                    "100%"
                    :
                    "Cần cải thiện"
                  }
                </span>

              </div>



              <div className="
                h-2
                rounded-full
                bg-gray-100
                overflow-hidden
              ">

                <div
                  className={`
                    h-full
                    rounded-full
                    ${
                      isGood
                      ?
                      "bg-green-500"
                      :
                      "bg-red-500"
                    }
                  `}
                  style={{
                    width:
                    isGood
                    ?
                    "100%"
                    :
                    "65%"
                  }}
                />

              </div>


            </div>



            <div className="
              mt-4
              text-center
              text-blue-600
              text-sm
              font-medium
            ">
              Xem chi tiết →
            </div>



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
  good,
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

<p className="
text-xs
text-gray-500
">
{title}
</p>


<p
className={`
mt-1
font-bold
text-lg
${
good
?
"text-gray-900"
:
"text-red-600"
}
`}
>
{value}
</p>


</div>

)

}
