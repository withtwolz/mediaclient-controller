#!/bin/bash
# Shared functions and constants

# Colors
RED='\033[37;41m'
BLACK='\033[1;31;40m'
GREEN='\033[1;30;42m'
GRAY='\033[37;100m'
NC='\033[0m'

# Helper functions
info() { printf "${BLACK}[$(basename "$0")][INFO]:${NC}${GRAY} %s ${NC}\n" "$1"; }
success() { printf "${BLACK}[$(basename "$0")][SUCCESS]:${NC}${GREEN} %s ${NC}\n" "$1"; }
error() { printf "${BLACK}[$(basename "$0")][ERROR]:${NC}${RED} %s ${NC}\n" "$1"; }

check_command() {
    command -v "$1" >/dev/null 2>&1
}

check_env_var() {
    [ -n "${!1}" ] && [ -d "${!1}" ]
}