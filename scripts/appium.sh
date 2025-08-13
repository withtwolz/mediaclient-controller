#!/bin/bash
# Run appium and pytests
set -e
source ./scripts/helpers.sh

# Start Appium server in background
info "Starting Appium server..."
appium --use-plugins=inspector --allow-cors || read -p "Ctrl + C to close"
APPIUM_PID=$!

# Cleanup - kill Appium server
info "Stopping Appium server..."
kill $APPIUM_PID || true
wait $APPIUM_PID || true

# Exit with test result
exit ${TEST_RESULT:-0}