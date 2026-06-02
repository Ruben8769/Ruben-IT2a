import subprocess
subprocess.run([
    "powershell",
    "-ExecutionPolicy", "Bypass",
    "-File", "Python/Test/pstest.ps1"
])