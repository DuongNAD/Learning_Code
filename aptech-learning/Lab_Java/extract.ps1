[xml]$xml = Get-Content -Path "extracted_docx/word/document.xml" -Raw
$ns = New-Object System.Xml.XmlNamespaceManager($xml.NameTable)
$ns.AddNamespace("w", "http://schemas.openxmlformats.org/wordprocessingml/2006/main")
$paragraphs = $xml.SelectNodes("//w:p", $ns)
$text = foreach ($p in $paragraphs) {
    $runs = $p.SelectNodes(".//w:t", $ns)
    if ($runs) {
        -join $runs.InnerText
    } else {
        ""
    }
}
$text | Out-File -FilePath "coding_rules.txt" -Encoding utf8
Write-Output "Successfully extracted to coding_rules.txt"
