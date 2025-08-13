# mediaclient-controller
Python + Appium automation framework for testing Netflix's mobile game controller interface. Currently it can login, triggering controller activity still in progress

# Prerequisites
- [ ] Android Studio - set Android SDK and ANDROID_HOME environment variable
- [ ] Java JDK 8+ - set JAVA_HOME environment variable
- [ ] Node.js & npm - For installing and running Appium server
- [ ] Python 3.11+
- [ ] Netflix mobile app - Installed on target Android device/emulator
- [ ] Android device or emulator plugged in - For running the tests
- [ ] ADB / Android platform-tools for debugging and connectivity

# Setup
This project uses a Makefile and bash scripts to simplify the setup  
1. `make setup` > this will install all the project dependencies  
Next you will use 2 terminals
2. `make appium` > this terminal will run the Appium server
3. `make test` > this terminal will run the `/tests`. Right now only login is covered

# Examples

Project:

Client:

# Future Considerations
- Still in progress at filling out more Pages
- Redo the controller as a Page
- Add a GithubAction CI