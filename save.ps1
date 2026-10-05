param([string]$msg = "")
$date = Get-Date -Format "yyyy-MM-dd"
git add -A
$changes = git status --porcelain
if (-not $changes) { Write-Host "Nothing to save."; exit 0 }
git commit -m "progress: $date $msg"
git push
