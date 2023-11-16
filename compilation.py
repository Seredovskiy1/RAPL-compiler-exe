# compilation.py

import subprocess
import os
import shutil

if __name__ == "__main__":
    # Compile compiler.py using PyInstaller and include all files in the current directory
    subprocess.run([
        'pyinstaller', '--onefile', '--distpath', 'dist', '--specpath', 'dist',
        '--add-data', f'{os.getcwd()}{os.pathsep}.',
        'compiler.py'
    ])

    # Compiled executable is in the 'dist' directory
    compiled_exe = os.path.join('dist', 'compiler')

    # Uncomment the line below if you want to run the compiled executable immediately
    # subprocess.run([compiled_exe])
    
    
    build_folder = 'build'
    try:
        shutil.rmtree(build_folder)
        print("Directory removed successfully")
    except OSError as o:
        print(f"Error, {o.strerror}: {build_folder}")
        
        
    print("Compilation completed. To use the compiler, run the generated 'dist/compiler' executable in cmd or terminal")
