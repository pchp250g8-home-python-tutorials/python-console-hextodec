@echo off
@set ANACONDA_ROOT=C:\Anaconda3
call "%ANACONDA_ROOT%\Scripts\activate.bat" %ANACONDA_ROOT%

start "" pythonw "%ANACONDA_ROOT%\Scripts\spyder-script.py" %~dp0\OctToDec.py