# Usage: ./save.ps1 "optional message"
$msg = "progress: $(Get-Date -Format 'yyyy-MM-dd')"
if ($args[0]) { $msg += " $($args[0])" }

Set-Location $PSScriptRoot
git add -A
git diff --cached --quiet
if ($LASTEXITCODE -eq 0) {
    Write-Host "Nothing to save."
    exit 0
}
git commit -m $msg
if ($LASTEXITCODE -ne 0) { exit $LASTEXITCODE }
git push
