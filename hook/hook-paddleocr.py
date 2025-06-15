# hook-paddleocr.py
from PyInstaller.utils.hooks import collect_data_files, collect_submodules, collect_dynamic_libs

hiddenimports = collect_submodules('paddleocr')
hiddenimports += ['paddleocr.ppocr.data.imaug.text_image_aug', 'paddleocr.ppocr.postprocess.pse_postprocess.pse']

# 包含所有数据文件和模型
datas = collect_data_files('paddleocr', include_py_files=True)
datas += collect_data_files('paddleocr/ppocr/utils/dict', includes=['*.txt'])
datas += collect_data_files('paddleocr/ppocr/utils', includes=['*.txt', '*.json'])

# 强制包含PaddlePaddle的DLL
binaries = collect_dynamic_libs('paddleocr')
binaries += collect_dynamic_libs('paddle')
