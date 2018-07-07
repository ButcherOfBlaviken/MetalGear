from cx_Freeze import setup, Executable
import sys
base = 'WIN32GUI' if sys.platform == "win32" else None


executables = [Executable("main.py", base=base)]
py_modules = ['main','MainWindow_Business','MG_MainWindow']

packages = []
include_files=[]
options = {
    'build_exe': {
        'packages':packages,
        'include_files': include_files
    },

}

setup(
    name = "prog",
    options = options,
    version = "1.0",
    description = 'desc of program',
    executables = executables
)
