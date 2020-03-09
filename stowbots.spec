from kivy_deps import sdl2, glew
# -*- mode: python -*-

block_cipher = None

options = [('v', None, 'OPTION')]
a = Analysis(['C:\\Users\\natha\\Documents\\GitHub\\stowbots-v2\\main.py'],
             pathex=['C:\\Users\\natha\\Documents\\GitHub\\stowbots-v2'],
             binaries=[('C:\\Users\\natha\\Anaconda3\\envs\\stowbotsv2\\Lib\\site-packages\\torch\\_C.cp37-win_amd64.pyd','torch'),
                       ('C:\\Users\\natha\\Anaconda3\\envs\\stowbotsv2\\Lib\\site-packages\\torch\\lib', 'torch\\lib')],
             datas=[('C:\\Users\\natha\\Documents\\GitHub\\stowbots-v2\\assets','assets')],
             hiddenimports=['torch',
                            'torch._C',
                            'torch._C.*',
                            'win32file',
                            'win32timezone',
                            'pkg_resources.py2_warn',
                            'fastprogress',
                            ],
             hookspath=['.'],
             runtime_hooks=[],
             excludes=['C:\\Users\\natha\\Documents\\GitHub\\stowbots-v2\\.git'],
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
          console=True, icon='C:\\Users\\natha\\Documents\\GitHub\\stowbots-v2\\stowbots_icon.ico')
coll = COLLECT(exe, Tree('C:\\Users\\natha\\Documents\\GitHub\\stowbots-v2\\',
                excludes=['.git','.new','.old']),
               a.binaries,
               a.zipfiles,
               a.datas,
               *[Tree(p) for p in (sdl2.dep_bins + glew.dep_bins)],
               excludes=['.git'],
               strip=False,
               upx=True,
               name='stowbots')
