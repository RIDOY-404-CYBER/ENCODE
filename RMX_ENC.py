import os,platform
os.system('clear')

os.system('git pull')
bit = platform.architecture()[0]
if bit=='64bit':

    os.system('xdg-open https://facebook.com/groups/770617227293870/')
    import ENC
else:
    exit('\033[1;31m[×] Sorry Device Not Support')
