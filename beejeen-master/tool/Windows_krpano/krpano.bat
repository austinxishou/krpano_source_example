@Echo off&SetLocal EnableExtensions EnableDelayedExpansion

echo delete old data...
For /d /r %1\ %%d in (vtour) do @if exist "%%d" rd /s /q "%%d"

echo init...
Set /a i=0
For /d /r %1\ %%A in (.) Do (
  Set "Files="
  If Exist "%%~fA\*.jpg" For /f "delims=" %%B in ('dir /S /B "%%~fA\*.jpg"') Do Set Files=!Files! "%%~fB"
  If defined Files (
	Set target[!i!]=!Files!
	Set /a i=i+1
  )
)

Set /a i=i-1
For /l %%n in (0,1,!i!) do (call here.bat !target[%%n]!)

pause


:::::::::::::::::::: How to use ::::::::::::::::::::::

:: krpano
::   |-----subdirs
::   |-----krpano.bat
::   |-----here.bat

:: drag and drop subdirs on krpano.bat
:: If you want to process directory out of the directory krpano, meaning that subdirs and krpano.bat are not at the same directory, please replace here.bat above (line 18) with its absolute path.