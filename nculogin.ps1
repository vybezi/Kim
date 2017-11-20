$username='26120512' 
$password='uhoh'

$ie = New-Object -ComObject 'internetExplorer.Application'
$ie.Visible= $true
$ie.fullscreen = $true
$ie.Navigate("https://aeorion.ncu.edu.jm/")

while ($ie.Busy -eq $true){Start-Sleep -seconds 1;}   

$usernamefield = $ie.Document.getElementByID('ctl00_ContentPlaceHolder1_wucLogin1_UserName')
$usernamefield.value = $username

$passwordfield = $ie.Document.getElementByID('ctl00_ContentPlaceHolder1_wucLogin1_Password')
$passwordfield.value = $password

$Link=$ie.Document.getElementsByTagName("input") | where-object {$_.className -eq "btn btn-large btn-block btn-primary"}
$Link.click()