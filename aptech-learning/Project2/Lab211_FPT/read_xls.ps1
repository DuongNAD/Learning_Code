$path='e:\aptech-learning\Project2\Lab211_FPT\src\main\java\Day1\Lab211_ Checklist_Code Review.xls'
$bytes = [System.IO.File]::ReadAllBytes($path)
$text = [System.Text.Encoding]::ASCII.GetString($bytes)
$text -replace '[^\x20-\x7E]+', ' '
