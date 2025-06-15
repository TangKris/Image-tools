# hook-cv2.py
from PyInstaller.utils.hooks import collect_data_files, collect_dynamic_libs

# 收集所有 OpenCV 数据文件
datas = collect_data_files("cv2", include_py_files=True)
# 收集动态链接库
binaries = collect_dynamic_libs("cv2")