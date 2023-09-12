@echo off

pip show discord.py > nul 2>&1
if %errorlevel% neq 0 (
    echo Requerimentos não encontrados. Por favor, execute o "instalar.bat" para instalar as bibliotecas necessárias.
    pause
    exit /b 1
)

pip show pylast > nul 2>&1
if %errorlevel% neq 0 (
    echo Requerimentos não encontrados. Por favor, execute o "instalar.bat" para instalar as bibliotecas necessárias.
    pause
    exit /b 1
)


python dzn.py

pause
