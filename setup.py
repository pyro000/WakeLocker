import sys
from cx_Freeze import setup, Executable

base = "Win32GUI" if sys.platform == "win32" else None
base_c = None

includefiles = ['lib'] #'lib'
packages = []
build_exe_options = {'build_exe': {'include_files': includefiles, 'packages': packages}}

cr = """Copyright (c) 2023 Vantablack

        All rights reserved."""

exe = Executable("main.py", target_name='WakeLocker.exe', icon="lib/icon.ico", base=base, copyright=cr)

setup(
    name="WakeLocker",
    version="1.0",
    license=cr,
    description="WakeLocker by Vantablack",
    options=build_exe_options,
    executables=[exe]
)
