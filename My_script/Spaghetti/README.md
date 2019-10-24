## Spaghetti - Web Application Security Scanner
![build](https://img.shields.io/badge/build-passing-green.svg) ![python](https://img.shields.io/badge/python-2.7-green.svg)  ![license](https://img.shields.io/badge/License-GPLv3-brightgreen.svg)

![logo](https://github.com/m4ll0k/Spaghetti/blob/master/screenshots/logo.png)

## Description
Spaghetti is a web application security scanner tool. It is designed to find various default and insecure files, configurations and misconfigurations. Spaghetti is built on python2.7 and can run on any platform which has a Python environment.

## Installation
```
$ git clone https://github.com/m4ll0k/Spaghetti.git
$ cd Spaghetti 
$ pip install -r doc/requirements.txt
$ python spaghetti.py -h 
```

## Features
- Fingerprints
  - Server
  - Frameworks (CakePHP,CherryPy,Django,...)
  - Firewall (Cloudflare,AWS,Barracuda,...)
  - CMS (Drupal,Joomla,Wordpress)
  - OS (Linux,Unix,Windows,...)
  - Language (PHP,Ruby,Python,ASP,...)

- Discovery:
  - Admin Panel
  - Apache Enumeration Users
  - Apache XSS
  - Apache ModStatus
  - Backdoors
  - Backup
  - Captcha
  - Common Directories
  - Common Files
  - Cookie Security
  - Multiple Index
  - Information Disclosure (Emails and Private IP)

## Screenshots
![screen1](https://github.com/m4ll0k/Spaghetti/blob/master/screenshots/screenshot_1.png)
![screen2](https://github.com/m4ll0k/Spaghetti/blob/master/screenshots/screenshot_2.png)
![screen3](https://github.com/m4ll0k/Spaghetti/blob/master/screenshots/screenshot_3.png)
