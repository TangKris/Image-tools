# hook-paddle.py
from PyInstaller.utils.hooks import collect_dynamic_libs, collect_data_files

binaries = collect_dynamic_libs('paddle')
datas = collect_data_files('paddle', include_py_files=True)