@ECHO OFF

: Sets the proper date and time stamp with 24Hr Time for log file naming
: convention

SET HOUR=%time:~0,2%
SET dtStamp9=%date:~-4%%date:~4,2%%date:~7,2%_0%time:~1,1%%time:~3,2%%time:~6,2%
SET dtStamp24=%date:~-4%%date:~4,2%%date:~7,2%_%time:~0,2%%time:~3,2%%time:~6,2%

if "%HOUR:~0,1%" == " " (SET dtStamp=%dtStamp9%) else (SET dtStamp=%dtStamp24%)

docker-compose exec db pg_dumpall -h localhost -c -U admin > D:\DatabaseFiles\analytics_project\analytics_project_backup-%dtStamp%.sql
ECHO Backup Process Completed!
PAUSE