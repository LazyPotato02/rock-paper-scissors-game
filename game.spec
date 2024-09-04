# -*- mode: python ; coding: utf-8 -*-

import os
from PyInstaller.building.build_main import Analysis, PYZ, EXE

# Paths to the image files
image_files = [
    'rock.png',
    'paper.png',
    'scissors.png'
]


# Create datas list for PyInstaller
datas = [(os.path.abspath(image), '.') for image in image_files]

block_cipher = None

a = Analysis(
    ['game.py'],
    pathex=['.'],
    binaries=[],
    datas=datas,
    hiddenimports=['pygame'],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    cipher=block_cipher,
    noarchive=False
)

pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)
exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.zipfiles,
    a.datas,
    name='RockPaperScissors',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=False,  # Set this to False to avoid the console window
)
