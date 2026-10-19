Set shell = CreateObject("WScript.Shell")
Set fso = CreateObject("Scripting.FileSystemObject")

launcherFolder = fso.GetParentFolderName(WScript.ScriptFullName)
projectFolder = fso.GetParentFolderName(launcherFolder)
desktopFolder = shell.SpecialFolders("Desktop")
shortcutPath = fso.BuildPath(desktopFolder, "Calculator.lnk")
launcherPath = fso.BuildPath(launcherFolder, "open.bat")
calculatorIcon = shell.ExpandEnvironmentStrings("%SystemRoot%\System32\calc.exe")

Set shortcut = shell.CreateShortcut(shortcutPath)
shortcut.TargetPath = launcherPath
shortcut.WorkingDirectory = projectFolder
shortcut.IconLocation = calculatorIcon & ",0"
shortcut.Description = "Open the Calculator project"
shortcut.Save

WScript.Echo "Created the Calculator shortcut on your desktop."
