# hook-cython.py
from PyInstaller.utils.hooks import collect_data_files

datas = collect_data_files('Cython.Utility')
hiddenimports = [
    'Cython.Compiler.Main',
    'Cython.Compiler.Code',
    'Cython.Compiler.Symtab',
    'Cython.Compiler.PyrexTypes',
    'Cython.Utils'
]