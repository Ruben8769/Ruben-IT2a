param(
    [string]$name,
    [string]$samaccountname,
    [string]$ou
)

$domain = (Get-ADDomain).DistinguishedName
$ouPath = "$ou,$domain"

New-ADGroup `
    -Name $name `
    -SamAccountName $samaccountname `
    -GroupScope Global -GroupCategory Security `
    -Path $ouPath