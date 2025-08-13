#!/bin/bash
# Appium Python Environment Setup Script
set -e
source ./scripts/helpers.sh

info "Setting up Appium Python environment..."
sleep 2

# Python virtual environment check
if [ ! -d ".venv" ]; then
    info "Creating Python virtual environment @ ./.venv"
    python3 -m venv .venv
fi

source .venv/bin/activate
success "Venv ready, installing python dependencies and commit hooks..."

if [ -f "requirements.txt" ]; then
    pip install -r requirements.txt
    pre-commit install
fi

# Java check
check_command java || error "Java not found. Install Java JDK and ensure it's in \$PATH."
check_env_var JAVA_HOME || error "JAVA_HOME not set. Add 'export JAVA_HOME=/path/to/jdk' to your shell profile or session"

# Android SDK check  
check_env_var ANDROID_HOME || error "ANDROID_HOME not set. Install Android Studio and add 'export ANDROID_HOME=/path/to/android/sdk' to your shell profile."
check_command adb || error "Android Debug Bridge unavailable, symlink android sdk/platform-tools or brew install --cask android-platform-tools"

# Node.js and Appium
check_command node || error "Node.js not found. Install from https://nodejs.org/"
check_command npm || error "npm not found. Install Node.js with npm included."

info "Installing Appium drivers and plugins"
npm install -g appium
appium driver install uiautomator2 || info "drivers already installed"
appium plugin install --source=npm appium-inspector-plugin || info "plugins already installed"
# TODO: add iOS/Xcode work and optional installs, bonus
# appium driver install xcuitest

info "=============================="
success "Environment setup complete!"
info "=============================="
info "Java > $(java -version 2>&1 | head -n1)"
info "JAVA_HOME > $JAVA_HOME"  
info "ANDROID_HOME > $ANDROID_HOME"
info "Node > $(node --version)"
info "Appium > $(appium --version)"
info "=============================="
