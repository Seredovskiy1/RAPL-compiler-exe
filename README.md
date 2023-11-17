
# RAPL Compiler

EXE Compiler for Riskuap - a programming language for instructions.


## Authors

- [@Seredovskiy1](https://www.github.com/Seredovskiy1) - Creator of EXE Compiler.

- [@risknu](https://github.com/risknu) - Creator of Riskuap.
## Documentation

Get Riskuap from `https://github.com/risknu/riskuap`.

Get files from this repo.

Unzip `riskuap-main`

Extract `compiler.py` and `compilator.py` to unziped folder with replacing.

Install requirements from `requirements.txt` of `riskuap` repo: `pip install -r requirements.txt`.  (Linux: `pip3`)

Install `pyinstaller`: `pip install pyinstaller` (Windows)

Install `pyinstaller`: `pip3 install pyinstaller` (Linux)

Launch `compilation.py`: `python compilation.py`.  (Windows)

Launch `compilation.py`: `python3 compilation.py`.  (Linux)

Wait for compilation.

After that, in `distro` folder, you can find `compiler.exe / compiler (Linux)` file.

You can move the `compiler` file anywhere you want, everything will work!

Done!
## USAGE

usage: `compiler.exe [-h] [-mode {normal,gui}] [-file [FILE_PATH]]`

RAPL Compiler script.

options:

  `-h, --help` - show this help message and exit

  `-mode {normal,gui}` - Mode for script execution: normal or gui

  `-file [FILE_PATH]` - Path to the file to compile

