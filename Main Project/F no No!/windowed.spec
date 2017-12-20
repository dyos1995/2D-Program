# -*- mode: python -*-

block_cipher = None


a = Analysis(['windowed', 'mygame.py'],
             pathex=['C:\\Users\\Administrator\\Desktop\\한국산업기술대학교 학생\\2학년 2학기\\2D 프로그램\\2Dprogram\\2D-Program\\Main Project\\F no No!'],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name='windowed',
          debug=False,
          strip=False,
          upx=True,
          runtime_tmpdir=None,
          console=True )
