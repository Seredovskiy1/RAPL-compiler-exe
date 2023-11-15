# compilation.py

import subprocess
import sys
import os

if __name__ == "__main__":
    # Check if the correct number of command-line arguments is provided
    if len(sys.argv) < 2:
        print('Usage: python compilation.py <file_path>')
        sys.exit(1)

    # Extract the file path from the command-line arguments
    file_path = os.path.abspath(sys.argv[1])

    # Compile compiler.py using PyInstaller and include all files in the current directory
    subprocess.run([
        'pyinstaller', '--onefile', '--distpath', 'dist', '--specpath', 'dist',
        '--add-data', f'{os.getcwd()}{os.pathsep}.',
        'compiler.py', '--', '-normal', file_path
    ])

    # Compiled executable is in the 'dist' directory
    compiled_exe = os.path.join('dist', 'compiler.exe')

    # Run the compiled executable
    subprocess.run([compiled_exe, '-normal', file_path])
