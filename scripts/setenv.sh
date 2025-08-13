#!/bin/bash
# .env variable setup
source ./scripts/helpers.sh

info "=============================="
info "  Setup Appium .env file....  "
info "=============================="

# Essential capabilities only
echo -e "${BLACK}Instructions: Enter a value or hit Return to use default${NC}"
echo -e "${GRAY}App Package [default > com.netflix.mediaclient]:${NC}"
read -r app_package
app_package=${app_package:-com.netflix.mediaclient}

echo -e "${GRAY}Device Name [default > LG508]:${NC}"
read -r device_name  
device_name=${device_name:-LG508}

echo -e "${GRAY}Platform Name Android/iOS [default > Android]:${NC}"
read -r platform_name
platform_name=${platform_name:-Android}

# Generate minimal .env file
cat > .env << EOF
# Appium Desired Capabilities
PLATFORM_NAME=$platform_name
DEVICE_NAME=$device_name
APP_PACKAGE=$app_package
EOF

success ".env file created!"
info "Other configurations can be viewed in pydantic settings.py"