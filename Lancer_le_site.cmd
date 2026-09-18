@echo off
setlocal
pushd "%~dp0"
where py >nul 2>nul
if not errorlevel 1 (
  py -3 serveur_local.py
  goto fin
)
where python >nul 2>nul
if not errorlevel 1 (
  python serveur_local.py
  goto fin
)
echo Python 3 est necessaire pour ce lanceur local.
echo Sinon, ouvre la version du parcours publiee sur un site web.
:fin
popd
pause
