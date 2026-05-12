param(
    [string]$givenName,
    [string]$surname,
    [string]$name,
    [string]$samAccountName,
    [string]$ou
)

$domain = (Get-ADDomain).DistinguishedName
$ouPath = "$ou,$domain"

$password = ConvertTo-SecureString "qwerty123!" -AsPlainText -Force
 
New-ADUser `
    -GivenName $givenName `
    -Surname $surname `
    -Name $name `
    -DisplayName $name `
    -SamAccountName $samAccountName `
    -Path $ouPath `
    -AccountPassword $password `
    -Enabled $true