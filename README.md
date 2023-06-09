# Run Python With Power Automate

## Step to do:
- Create HelloWorld.py
- HelloWorld.py is run properly.
- Use Power Automate desktop app to create new flow Run Hello World Python

![image](https://user-images.githubusercontent.com/79841341/226110682-d22653e5-7c28-43fe-8e3a-d80972dcb7d2.png)

- However, I have the error with PowerAutomate due to company policy to not allow to run Python script or any scripts with Power Automate.
- Therefore, I do not use Power Automate for my case and switch to running PowerShell from a Windows shortcut

## Run Python with PowerShell
- Background:
  - PowerShell is available in all Windows system
  - In my laptop, my company is still limitting to run script in PowerShell. Therefore, I received warning message everything running PowerShell scriptting file with the extension of ps1.

![image](https://user-images.githubusercontent.com/79841341/226164152-d94c852c-7c52-4d52-83fc-1b7d0e3d6377.png)

  - To go around, I created a shortcut to run my ps1 file, which is stored in another ps1 file. Following is the PowerShell script to create the shortcut.

```powershell
$WshShell = New-Object -comObject WScript.Shell
$Shortcut = $WshShell.CreateShortcut("C:\development\RunPythonWithPowerAutomate\PowerShell.lnk")
$Shortcut.TargetPath = "C:\Windows\System32\WindowsPowerShell\v1.0\powershell.exe"
$Shortcut.Arguments = "-ExecutionPolicy Bypass -File C:\development\RunPythonWithPowerAutomate\script.ps1"
$Shortcut.Save()
```

- The shortcut will run the PowerShell file script.ps1, which is run the monitor_folder.py. Below is the content of script.ps1

```powershell
python C:\development\RunPythonWithPowerAutomate\monitor_folder.py
```

- monitor.py is an python program to monitor a folder and execute some commands when new file(s) are added into that folder.
