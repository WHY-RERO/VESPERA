# VESPERA
A powerful, modern, cross-platform Python automation & cybersecurity utility.

![Python](https://img.shields.io/badge/Python-3.8%2B-blue?style=for-the-badge)
![Platform](https://img.shields.io/badge/Platform-Windows%20%7C%20macOS%20%7C%20Linux%20%7C%20Termux-success?style=for-the-badge)
![License](https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Active-brightgreen?style=for-the-badge)





## Features
- Fully cross-platform
- Minimal dependencies
- Fast & lightweight
- Works on Termux
- Supports Python 3.8+
- Beginner-friendly
- Open-source and free

## Pre-Requirements
### Windows
- Python 3.8+
- pip

### Linux (Ubuntu / Debian / Kali)
```bash
sudo apt update
sudo apt install python3 python3-pip git -y
```
### macOS
```bash
brew install python git
```
### Termux  
```bash
pkg update -y
pkg install python git pip -y
termux-setup-storage
pkg install git -y
pkg install python -y
git clone https://github.com/WHY-RERO/VESPERA
cd VESPERA
pip install -r requirements.txt
python app.py
```


## Installation
```bash
git clone https://github.com/WHY-RERO/VESPERA
cd VESPERA
pip install -r requirements.txt
python app.py
```

## Usage Examples
```bash
python app.py
python app.py --scan target.com
python app.py --output report.txt
```

## Project Structure
```bash
rero-project/
├── app.py
├── requirements.txt
├── README.md
├── LICENSE
└── .gitignore
```

## Troubleshooting
pip: command not found -> sudo apt install python3-pip
Permission denied -> chmod +x app.py
ModuleNotFoundError -> pip install -r requirements.txt
Python not recognized -> Add Python to PATH

## Contributing
Pull requests are welcome.

## Support the Project
Crypto Donation Address:
Bitcoin: bc1qjaez9qsadhxecup7lctwtvreqxklvv9c8e5ux9


<p align="center">
  <img src="banner/vespera.jpg" width="%100">
</p>
