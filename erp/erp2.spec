# -*- mode: python -*-

block_cipher = None


a = Analysis(['erp2.py'],
             pathex=['F:\\���ݷ���\\demo\\venv\\Scripts', 'F:\\���ݷ���\\demo\\venv\\Lib\\site-packages', 'F:\\���ݷ���\\demo'],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          [],
          name='erp2',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          runtime_tmpdir=None,
          console=True )
