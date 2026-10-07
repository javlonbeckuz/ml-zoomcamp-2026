@echo off
cd /d "%~dp0"
set IPYTHONDIR=%~dp0.ipython
git -C ..\course pull --quiet
uv run jupyter lab
