@echo off
echo MAKE VTOUR (NORMAL) droplet

IF "%~1" == "" GOTO ERROR
IF NOT EXIST "%~1" GOTO ERROR

set KRPANOTOOLSEXE=krpanotools64.exe
if "%PROCESSOR_ARCHITECTURE%" == "x86" set KRPANOTOOLSEXE=krpanotools32.exe

"%~dp0\%KRPANOTOOLSEXE%" makepano "%~dp0\templates\vtour-normal.config" %*
GOTO DONE

:ERROR
echo.
echo Drag and drop several panoramic images on this droplet to create 
echo automatically a simple virtual tour with normal panos from it.

:DONE
echo.
::pause





:: This bat comes from krpano/MAKE VTOUR (NORMAL) droplet.bat. The only difference is this bat comment the last line (pause) so that it won't pause after processing one directory containing panorama photos.