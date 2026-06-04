param(
    [string]$indentity
    [string]$userPrincipalName
)

Add-ADGroupMember `
    -Indentity $indentity
    -Members $userPrincipalName
    -Confirm $false