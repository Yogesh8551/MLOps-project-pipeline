@echo off

echo =============================
echo 🚀 STARTING LOCAL PIPELINE
echo =============================

echo.
echo Step 1: Simulating code change...
echo main.py > changed_files.txt

echo.
echo Step 2: Running ML model...
python ml/predict.py

echo.
echo Step 3: Selected tests:
type tests_to_run.txt

echo.
echo Step 4: Running tests...

for /f %%i in (tests_to_run.txt) do (
    echo Running %%i
    python -m pytest tests/%%i
)

echo.
echo ✅ PIPELINE COMPLETED