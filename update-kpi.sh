#!/bin/bash

echo "=============================="
echo "      UPDATE KPI START"
echo "=============================="

cd ~/kpi-dashboard || exit


echo "[1/5] Import Excel -> KPI"

source venv/bin/activate

python scripts/import-kpi.py

if [ $? -ne 0 ]; then
    echo "IMPORT KPI FAILED"
    read -p "Press Enter"
    exit 1
fi


echo "[2/5] Build Local Dashboard"

npm run build

if [ $? -ne 0 ]; then
    echo "BUILD FAILED"
    read -p "Press Enter"
    exit 1
fi


echo "[3/5] Restart Local Dashboard"

pm2 restart kpi-dashboard


echo "[4/5] Commit KPI data"

git add data/kpi.ts data/summary.ts data/cll-detail.ts

git commit -m "update KPI data"


echo "[5/5] Push to GitHub -> Vercel"

git push


echo "=============================="
echo "      UPDATE KPI DONE"
echo "=============================="

read -p "Press Enter to close..."
