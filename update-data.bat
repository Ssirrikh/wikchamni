@echo off
setlocal enabledelayedexpansion

REM 9.5 hrs

REM Change to this script's folder (assumed repo root)
pushd "%~dp0"

REM Google Sheets exports .tsv only, while Excel exports .txt only
set "FILE=data\spreadsheet.tsv"
set "FILE_SHORT=spreadsheet.tsv"
set "FILE_ALT=data\spreadsheet.txt"

REM 
set "UPSTREAM=origin/main"



REM === Basic Checks ===

where git >nul 2>&1
if errorlevel 1 (
  echo Can't access Git commands.
  echo Install Git if you haven't already. Otherwise, ask Kat to add it to PATH.
  goto :done
)

git rev-parse --is-inside-work-tree >nul 2>&1
if errorlevel 1 (
  echo Script isn't in a Git repository folder.
  echo It must be run from the original folder it came in.
  goto :done
)



REM === Sync with Upstream ===

echo.
echo === Step 1 of 3 ===
echo.
echo Checking for updates to project files...
echo.

REM If the file is tracked, restore it to HEAD (discarding local edits).
REM If it's untracked but exists (e.g., copied early), delete it so pull won't be blocked.
git ls-files --error-unmatch "%FILE%" >nul 2>&1
if errorlevel 1 (
  if exist "%FILE%" del /f /q "%FILE%"
) else (
  git restore --staged --worktree -- "%FILE%" 2>nul
  if errorlevel 1 git checkout -- "%FILE%" >nul 2>&1
)

REM Fast forward to get changes
git pull --ff-only
if errorlevel 1 (
  echo Pull failed. Check your internet connection, then run this script again.
  echo If your internet is fine and it fails again, poke Kat about it.
  goto :done
)

echo.
echo Sync complete.

rem rem REM Check for local commits that didn't get pushed yet
rem rem set "UPSTREAM="
rem rem for /f "delims=" %%U in ('git rev-parse --abbrev-ref --symbolic-full-name @{u} 2^>nul') do set "UPSTREAM=%%U"

rem echo Checking against upstream %UPSTREAM%
rem set "BEHIND=0"
rem set "AHEAD=0"
rem for /f "tokens=1,2" %%A in ('git rev-list --left-right --count "!UPSTREAM!"...HEAD 2^>nul') do (
rem   set "BEHIND=%%A"
rem   set "AHEAD=%%B"
rem )
rem echo Local is !BEHIND! commits behind and !AHEAD! ahead.

rem if not "!AHEAD!"=="0" (
rem   rem
rem )




REM === User Updates Database ===

echo.
echo === Step 2 of 3 ===
echo.
echo Now here's the part where you do stuff:
echo.
echo Please copy the updated spreadsheet into the \data folder (replace the old version).
echo  - For Google Sheets: use `File ^> Download ^> Tab Separated Values` and save as "spreadsheet.tsv".
echo  - For Excel: use `File ^> Save As ^> Text (Tab Delimited)` and save as "spreadsheet.txt".
echo.
echo The filepath will be [main folder]\data\spreadsheet.tsv, or [main folder]\data\spreadsheet.txt respectively.
echo.
REM echo When that's done, press Enter to continue...
REM set /p "dummy= "
set /p "=When that's done, press Enter to continue... "



REM === Save Changes and Upload ===

echo.
echo === Step 3 of 3 ===
echo.
echo Scanning for changes...
echo.

REM Make sure file wasn't deleted or named wrong
REM If alternate file extension was found, change it to primary extension
if not exist "%FILE%" (
  if not exist "%FILE_ALT%" (
    echo Couldn't find "%FILE%" or "%FILE_ALT%".
    echo Make sure you used the correct name and file extension.
    goto :done
  ) else (
    echo Converting "%FILE_ALT%" to "%FILE%"...
    ren "%FILE_ALT%" "%FILE_SHORT%"
    echo.
  )
)
git add "%FILE%"
if errorlevel 1 (
  echo Couldn't save changes properly. Try running the script one more time.
  echo If it still doesn't work, something got really borked. Poke Kat about it.
  goto :done
)

REM Only commit if file actually changed
git diff --cached --quiet -- "%FILE%"
if %errorlevel%==0 (
  echo No changes detected in "%FILE%" since last update.
  echo Are you sure you replaced it with the newest version?
  goto :done
)

git commit -m "update database" -- "%FILE%"
if errorlevel 1 (
  echo Commit failed. Try running the script one more time.
  echo If it still doesn't work, something got really borked. Poke Kat about it.
  goto :done
)

echo.
echo Changes saved.



:push
echo Pushing changes to server...
echo.
git push
if errorlevel 1 (
  echo.
  echo Push failed. Either your internet is bad, or you got unlucky and Kat made changes just now.
  echo Run the script one more time. If your internet is fine and it fails again, poke Kat about it.
  goto :done
)

echo.
echo === SUCCESS ===
echo.
echo All done^^! Your spreadsheet has been uploaded to the server.
echo Changes will go live in 5-10 minutes.

:done
popd
echo.
pause
