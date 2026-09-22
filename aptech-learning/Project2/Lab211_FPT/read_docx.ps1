$path='e:\aptech-learning\Project2\Lab211_FPT\src\main\java\Day1\Bubble sort algorithm.docx'
Add-Type -AssemblyName System.IO.Compression.FileSystem
$zip = [System.IO.Compression.ZipFile]::OpenRead($path)
$entry = $zip.GetEntry('word/document.xml')
$stream = $entry.Open()
$reader = New-Object System.IO.StreamReader($stream)
$xml = $reader.ReadToEnd()
$reader.Close()
$stream.Close()
$zip.Dispose()
$xmlDoc = [xml]$xml
$texts = $xmlDoc.SelectNodes('//*[local-name()=''t'']') | Select-Object -ExpandProperty '#text'
$texts -join ' '
