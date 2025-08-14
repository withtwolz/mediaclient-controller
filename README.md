# Netflix mediaclient-controller
Python+Appium automation framework for testing Netflix's mobile app and game controller interface. Currently it can complete [login](https://github.com/withtwolz/mediaclient-controller/?tab=readme-ov-file#examples) with full app and Game control planned for the future.  

# Prerequisites
- [ ] Android Studio - set ANDROID_HOME environment variable to the directory path your android sdk is within
- [ ] Java JDK 8+ - set JAVA_HOME environment variable (`which java` can help here)
- [ ] Node.js & npm - For installing and running Appium server 
- [ ] Python 3.11+
- [ ] Netflix mobile app - Installed on target Android device/emulator
- [ ] Android device or emulator plugged in - For running the tests
- [ ] ADB / Android SDK bundled platform-tools for debugging and connectivity  
This [article covers](https://swtestacademy.com/how-to-install-appium-on-mac/) where you may find most of your dependencies; keep in mind you should look for the latest installations from the respective developers site or your CLI.

# Setup
This project uses a Makefile and bash scripts to simplify the setup  
1. `make setup` > this will install all the project dependencies  
Next you will use 2 terminals
2. `make appium` > this terminal will run the Appium server
3. `make test` > this terminal will run the `/tests`. Right now only login is covered

# Running Example

Project running Appium + pytests:  
[Running in Project](https://github.com/user-attachments/assets/e62b523b-4a22-46e3-9051-38cc6ec5b47e)  
Appium Running Client ([test source](https://github.com/withtwolz/mediaclient-controller/blob/main/tests/test_controller.py)):  
[Running on Client](https://github.com/user-attachments/assets/7083ad60-0690-4981-a034-a30772d066f4)  


# Future Considerations
- Still in progress at filling out more Pages
- Redo the controller as a Page
- Add a GithubAction CI
