.PHONY=install test

setup:  # initial install
	chmod +x ./scripts/setup.sh && ./scripts/setup.sh
	chmod +x ./scripts/setenv.sh && ./scripts/setenv.sh

install:  # install project dependencies
	pip3 install -r requirements.txt
	@echo "installled dependencies"

appium:  # Run the appium server
	chmod +x ./scripts/appium.sh
	./scripts/appium.sh

test:  # run sample tests
	pytest ./tests
