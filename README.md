# Polyglot File Security Demo

## Overview
This project demonstrates how a polyglot file can exploit improper file upload validation.

## Features
- Generates image + HTML polyglot
- Executes JavaScript payload
- Demonstrates XSS
- Displays cookies
- Sends data to local server

## Usage

1. Run:
   python polyglot_tool.py

2. Enter image path

3. Upload generated polyglot.jpg to vulnerable site

4. Observe:
   - Alert popup
   - Cookies displayed
   - Terminal logs data



## Docker Usage

### Build
docker build -t polyglot-demo .

### Run
docker run -it -p 5000:5000 -v ${PWD}:/app polyglot-demo

## Disclaimer
This project is for educational purposes only.