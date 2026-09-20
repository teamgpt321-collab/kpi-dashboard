from pathlib import Path

p = Path("app/tool-usage/page.tsx")

s = p.read_text(encoding="utf-8")

s = s.replace(
    "min-h-screen bg-slate-50 p-8",
    "min-h-screen bg-[#f5f8ff] p-8"
)

s = s.replace(
    "bg-white rounded-2xl shadow p-6",
    "bg-white rounded-2xl border border-slate-100 shadow-sm p-6 hover:shadow-md transition"
)

s = s.replace(
    "bg-white rounded-2xl shadow p-5 mb-8 grid grid-cols-4 gap-4",
    "bg-white rounded-2xl border border-slate-100 shadow-sm p-6 mb-8 grid grid-cols-4 gap-5"
)

s = s.replace(
    "bg-slate-100 text-slate-600 text-sm",
    "bg-slate-50 text-slate-500 text-sm uppercase"
)

s = s.replace(
    "border-b hover:bg-blue-50 transition text-sm",
    "border-b border-slate-100 hover:bg-blue-50/50 transition text-sm"
)

p.write_text(s, encoding="utf-8")

print("UI DONE")
