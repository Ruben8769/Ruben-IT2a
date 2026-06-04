param(
    [string]$firstname,
    [string]$surname,
    [string]$username,
    [string]$ou,
    [string]$email,
    [string]$phonenummber,
    [string]$jobtitle,
    [string]$department
)

$ouPath = $ou
$password = ConvertTo-SecureString "qwerty123!" -AsPlainText -Force

New-ADUser `
    -GivenName $firstname `
    -Surname $surname `
    -Name "$firstname $surname" `
    -DisplayName "$firstname $surname" `
    -SamAccountName $username `
    -UserPrincipalName $username `
    -Path $ouPath `
    -AccountPassword $password `
    -Enabled $true `
    -Company "Polar Event Solutions AS" `
    -Department $department `
    -Title $jobtitle `
    -EmailAddress $email `
    -OfficePhone $phonenummber