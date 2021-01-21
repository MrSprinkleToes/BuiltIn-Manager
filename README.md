# BuiltIn Manager
An easy to use tool to manage BuiltIn plugins.
## Questions
### How do I use this tool?
Using this tool is easy! To get started,
1. Open the tool.
2. When prompted, select your Roblox installation. By default, the file selection window should open in Appdata > Local. From there, find the folder named `Roblox` and press it once. Click on select folder on the bottom right.
3. If done correctly, you should see a list of model files appear. This means it is working!
- Adding plugins
  To add a plugin, simply press the "Add plugin" button on the bottom left. Navigate to where you stored the plugin a developer provided you, then select it! It will automatically be added.
- Removing plugins
  To remove a plugin, select it from the list of installed BuiltIns and press the "Remove plugin" button. Remember, plugins created by Roblox cannot be removed!
## Building
This section is for people wanting to build the plugin to an exe themself. If you want to easily get started, just navigate to the [releases](https://github.com/MrSprinkleToes/BuiltIn-Manager/releases) page and download the exe from the latest release.
Alternatively, you can also download and run the python script if you have python installed.
### To build this tool
1. Install [python](https://python.org). (make sure you choose to install pip!)
2. Install the PyInstaller module using command prompt: `pip install pyinstaller`
3. Install all the modules imported in `builtinmanager.py` from command prompt: `pip install <module>`
4. Download the repository as a zip, extract it, and navigate to the extracted folder in command prompt: `cd <extracted file location>`
5. Run this command in command prompt: `pyinstaller builtinmanager.py --clean --onefile`
- This results in a few folders being created in your extracted folder. Open the folder named "dist". There is your exe!
## Contributing
To contribute, simply create a pull request with changes you believe are best. These can be anywhere from making the code more pythonic to adding features and fixing bugs. (Fixing bugs is greatly appreciated!)
