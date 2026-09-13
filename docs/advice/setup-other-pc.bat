@echo off
setlocal

set "ARTIFACT_URL=https://claude.ai/code/artifact/16cabdbd-e00f-40e1-b1cc-1cebc7d30858"
set "STARTUP_DIR=%APPDATA%\Microsoft\Windows\Start Menu\Programs\Startup"

echo Setting up the Claude Advice auto-popup on this computer...
echo (You must be signed in to the same Claude account in your browser to view it.)
echo.

> "%STARTUP_DIR%\ClaudeAdvice.bat" (
    echo @echo off
    echo start "" "%ARTIFACT_URL%"
)

schtasks /create /tn "ClaudeAdvice_Daily8am" /tr "explorer.exe %ARTIFACT_URL%" /sc daily /st 08:00 /f

echo.
echo Done. The advice page will now open automatically:
echo   - every time you log in to Windows
echo   - every day at 8:00 AM
echo.
pause
