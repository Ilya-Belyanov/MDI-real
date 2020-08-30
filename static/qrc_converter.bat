@echo off
 
set source_path=%1
set destination_path=%2

IF "%source_path%"=="" (
   set source_path=%CD%
)

IF NOT EXIST %source_path% (
   set source_path=%CD%
)

IF "%destination_path%"=="" (
   set destination_path=qrc_generated
)

IF NOT EXIST %destination_path% (
   MD %destination_path%
)


FOR /R %source_path% %%f IN (*.qrc) DO  (
   pyrcc5 -o %destination_path%\%%~nf.py %%f
)