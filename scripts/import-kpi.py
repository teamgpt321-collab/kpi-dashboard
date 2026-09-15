import pandas as pd
import json


file = "data/Đúng hẹn 22 T04 Q2.xlsx"


def to_number(value):

    if pd.isna(value) or value == "-":
        return 0
    try:
        return float(value)
    except:
        return 0


raw = pd.read_excel(
    file,
    sheet_name="Tong hop",
    header=None
)


# tìm dòng header đầu tiên có Nhân sự
header_row = None

for i, row in raw.iterrows():
    if "Nhân sự" in row.values:
        header_row = i
        break


df = pd.read_excel(
    file,
    sheet_name="Tong hop",
    header=header_row
)


employees = []


for _, row in df.iterrows():

    name = row.get("Nhân sự")


    if pd.isna(name):
        continue


    name = str(name).strip().upper()


    # gặp Tổng đầu tiên thì dừng
    if name == "TỔNG":
        break


    # chỉ lấy mã PNC
    if not name.startswith("PNC"):
        continue



    if name == "PNC01.DUCNH5":
        print("DEBUG DUCNH5")
        print("correct raw:", row["Đúng Hẹn\n(>=97%)"])
        print("cll raw:", row["CLL\n(<7%)"])
        print("cll3 raw:", row["CLL3\n(<0.5%)"])
        print("correct calc:", to_number(row["Đúng Hẹn\n(>=97%)"]) * 100)
        print("cll calc:", to_number(row["CLL\n(<7%)"]) * 100)
        print("cll3 calc:", to_number(row["CLL3\n(<0.5%)"]) * 100)

    employees.append({

        "name": name,
        "block": str(row["Block"]),
        "team": str(row["Đội"]),

        "correct": to_number(row["Đúng Hẹn\n(>=97%)"]) * 100,
        "cll": to_number(row["CLL\n(<7%)"]) * 100,
        "cll3": to_number(row["CLL3\n(<0.5%)"]) * 100,

        "sevenDayTK": to_number(row["7N TK"]) * 100,
        "sevenDayBT": to_number(row["7N BT"]) * 100,
        "sevenDay": to_number(row["7N"]) * 100,

        "csat": to_number(row["CSAT"]),

        "over72h": to_number(row["TK quá 72H"]),
        "over24h": to_number(row["BT quá 24H"]),

        "responseTK": to_number(row["Repontime TK\n(<18H)"]),
        "responseBT": to_number(row["Repontime BT\n(<9h)"]),

        "status": "Cảnh báo" if (
            to_number(row["Đúng Hẹn\n(>=97%)"]) * 100 < 97
            or
            to_number(row["CLL\n(<7%)"]) * 100 >= 7
            or
            to_number(row["CLL3\n(<0.5%)"]) * 100 >= 0.5
        ) else "Tốt"

    })


with open(
    "data/kpi.ts",
    "w",
    encoding="utf-8"
) as f:

    f.write("export const employees = ")
    f.write(json.dumps(
        employees,
        ensure_ascii=False,
        indent=2
    ))



# ===== CREATE SUMMARY.TS =====

total_employees = len(employees)

correct_avg = round(
    sum(x["correct"] for x in employees) / total_employees,
    2
) if total_employees else 0


cll_avg = round(
    sum(x["cll"] for x in employees) / total_employees,
    2
) if total_employees else 0


warning_count = len([
    x for x in employees
    if x["status"] == "Cảnh báo"
])


with open(
    "data/summary.ts",
    "w",
    encoding="utf-8"
) as f:

    f.write(f"""export const summary = {{
  totalEmployees: {total_employees},
  correct: {correct_avg},
  cll: {cll_avg},
  warning: {warning_count},
}};""")


print(
    "Đã tạo summary:",
    total_employees,
    "nhân sự | Cảnh báo:",
    warning_count
)


print("Đã tạo KPI:", len(employees), "nhân sự")
