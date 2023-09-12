@echo off
echo Verificando e instalando as bibliotecas necessárias...
pip install discord.py
pip install pylast

pip show discord.py > nul 2>&1
if %errorlevel% neq 0 (
    echo Erro: Falha ao instalar discord.py.
    pause
    exit /b 1
)

pip show pylast > nul 2>&1
if %errorlevel% neq 0 (
    echo Erro: Falha ao instalar pylast.
    pause
    exit /b 1
)

echo Todas as bibliotecas foram instaladas com sucesso.

echo Iniciando dzn.py...
python dzn.py

pause
