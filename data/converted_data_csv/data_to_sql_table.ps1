$server = "DESKTOP-HTQ5LV8"
$database = "data_base"
$folderPath = "D:\python_data\projekt\products_management\sellers-data-engineering\data\converted_data_csv"

$csvFiles = Get-ChildItem -Path $folderPath -Filter *.csv

foreach ($file in $csvFiles) {
    $filePath = $file.FullName
    $tableName = $file.BaseName -replace '_converted$', ''
    $query = "BULK INSERT $tableName FROM '$filePath' WITH (FIELDTERMINATOR = ';', ROWTERMINATOR = '\n', FIRSTROW = 2)"
    $command = "sqlcmd -S $server -d $database -Q `"$query`" -E"
    Invoke-Expression $command
    Write-Host "Zaimportowano $filePath do tabeli $tableName."
}
