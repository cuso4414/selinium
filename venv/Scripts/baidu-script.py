#!C:\Users\18729\PycharmProjects\test\venv\Scripts\python.exe
# EASY-INSTALL-ENTRY-SCRIPT: 'baidu==0.2','console_scripts','baidu'
__requires__ = 'baidu==0.2'
import re
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(
        load_entry_point('baidu==0.2', 'console_scripts', 'baidu')()
    )
