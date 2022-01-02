@echo off
:menu
cls
echo      ----------------------------------------------------------------------
echo     \                                 MENU                                 \
echo     /                                                                      /
echo     \                                                                      \
echo     /                             1. Start                                 /
echo     \                             2. Informacje                            \
echo     /                             3. Backup                                /
echo     \                             4. Wyjscie                               \
echo     /                                                                      /
echo     \                                                                      \
echo      ----------------------------------------------------------------------
echo.
set /p choice=Wybierz opcje: 
if %choice%==1 ( goto start )
if %choice%==2 ( goto info )
if %choice%==3 ( goto backup )
if %choice%==4 ( goto exit 
) else ( 
echo Nie ma takiej opcji, sprobuj ponownie!
pause
goto menu ) 

:start
cls
call program.py
echo Program zostal pomyslnie wykonany
if exist index.html (
echo Uruchomiono raport w postaci strony www 
call index.html 

 ) 
pause
goto menu

:info
cls
echo      ----------------------------------------------------------------------
echo     \                               INFORMACJE                             \
echo     /                                                                      /
echo     \                         Alicja Gruca "Podpisy"                       \
echo     /                                                                      /
echo     \      W Urzedzie Ochrony Bajtocji zatrudnieni sa urzednicy oraz       \
echo     /   dowodcy. W archiwum UOB znajduja sie teczki kazdego urzednika.     /
echo     \   W kazdej teczce znajduja sie podpisy poreczajace za lojalnosc      \
echo     /   danego pracownika. UOB dowiedzial sie ze do grona dowodcow         /
echo     \   przeniknal szpieg wrogiej Mikromieklandii oraz, ze kolejni         \
echo     /   szpiedzy byli wprowadzani na stanowsiska urzednicze. Dowodztwo     /
echo     \   UOB chce zobaczyc liste takich urzednikow, i to jak najszybciej!   \
echo     /                                                                      /
echo     \       Ostrzezenie!                                                   \
echo     /           Program przeznaczony tylko i wylacznie dla dowodcow!       /
echo     \                                                                      \
echo      ----------------------------------------------------------------------
pause
goto menu

:backup
cls
if not exist backup\ ( 
mkdir backup
)
if exist backup\%date% ( 
echo Kopia zapasowa zostala juz dzisiaj wykonana
pause
) else (
mkdir backup\%date%
copy *.* backup\%date%
echo Kopia zapasowa zostala utworzona pomyslnie
pause
)
goto menu

:exit
exit





