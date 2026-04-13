@echo off
@set VSCODE_ROOT=%ProgramFiles%\Microsoft VS Code
@set ANACONDA_ROOT=C:\Anaconda3
call "%ANACONDA_ROOT%\Scripts\activate.bat" %ANACONDA_ROOT%
@set PATH=%VSCODE_ROOT%;%PATH%
start "" Code .