# AnyDesk-Auto-Launcher

## Overview
This project is a batch and python script program that will open a new AnyDesk remote session with a specified host computer, it will close the AnyDesk session and windows to relaunch them at set intervals. This is so the host machine can be monitored over a long time, and will be reconected at set intervals as an automated "refresh" after connection has been lost due to network related issues.

The project requires Windows 11 with a Python install to run.

## Installation
1. Download required software:
    * Python 3.12
2. Install dependencies:
    ```bash
    pip install pywin32
    ```

## Usage
1. Run the Config.py script to set up the path to your AnyDesk install folder and the AnyDesk ID for the host machine.
2. Start the application by running the Launcher.py script

## Issues
    * Does not work correctly on Windows 10 devices