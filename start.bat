@echo off
cd /d "%~dp0"
git -C ..\course pull --quiet
uv run jupyter lab
