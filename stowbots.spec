# -*- mode: python -*-

block_cipher = None

options = [('v', None, 'OPTION')]
a = Analysis(['C:\\Users\\natha\\Documents\\GitHub\\pyinstaller-torch-bug\\main.py'],
             pathex=['C:\\Users\\natha\\Documents\\GitHub\\pyinstaller-torch-bug'],
             binaries=[],
             datas=[],
             hiddenimports=[
                            'pkg_resources.py2_warn',
                            'fastprogress',
                            ],
             hookspath=['.'],
             runtime_hooks=[],
             excludes=['C:\\Users\\natha\\Documents\\GitHub\\pyinstaller-torch-bug\\.git'],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          [],
          exclude_binaries=True,
          name='stowbots',
          debug=False,
          strip=False,
          upx=True,
          console=True)
coll = COLLECT(exe, Tree('C:\\Users\\natha\\Documents\\GitHub\\pyinstaller-torch-bug\\',
                excludes=['.git','.new','.old']),
               a.binaries,
               a.zipfiles,
               a.datas,
               excludes=['.git'],
               strip=False,
               upx=True,
               name='stowbots')
