@echo off
REM BVA Flooring - automated blog post (run twice/week via Task Scheduler).
REM Requires ANTHROPIC_API_KEY in the environment (same key as Triangle).
cd /d "%~dp0"
set PYTHONIOENCODING=utf-8
py automation\run.py >> automation\run.log 2>&1
