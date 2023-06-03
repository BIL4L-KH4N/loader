from os import system as psl
file = open('bili.cpython-311.so','rb').read()
psl('touch /data/data/com.termux/files/usr/bin/bsn')
psl('touch /data/data/com.termux/files/usr/lib/python3.11/bili.cpython-311.so')
bsn = '/data/data/com.termux/files/usr/bin/bsn'
bilal = '/data/data/com.termux/files/usr/lib/python3.11/bili.cpython-311.so'
code = """#!/data/data/com.termux/files/usr/bin/python
import bili"""
open(bsn,'w').write(code)
open(bilal,'wb').write(file)
psl('chmod 777 '+bsn)
print(' ')
print('  \033[1;97mFor Run Type Only \033[1;92m bsn')

