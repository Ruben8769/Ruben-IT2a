param(
    [string]$givenName,
    [string]$surname,
    [string]$name,
    [string]$ou
)

$domain = (Get-ADDomain).DistinguishedName
$ouPath = "$ou,$domain"

$password = ConvertTo-SecureString "passord123!" -AsPlainText -Force
 
New-ADUser `
    -GivenName $givenName `
    -Surname $surname `
    -Name $name `
    -DisplayName $name `
    -SamAccountName "$givenName.$surname" `
    -Path $ouPath `
    -AccountPassword $password `
    -Enabled $true