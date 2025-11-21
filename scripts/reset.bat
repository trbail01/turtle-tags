@echo off
REM Reset repository to last committed state (Windows)
cd /d %~dp0
cd ..
git restore --source=HEAD --worktree --staged -S .
git clean -fdx
echo Repo reset to last commit. Press any key to close.
pause >nul
