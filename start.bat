@echo off
cd /d "%~dp0"
set IPYTHONDIR=%~dp0.ipython
set PYTHONPATH=%~dp0
git -C ..\course pull --quiet
uv run jupyter lab --ServerApp.jpserver_extensions=tutor=True --LabApp.extra_labextensions_path="%~dp0labextensions"
