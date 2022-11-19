import os,platform

os.system('clear')


os.system('git pull')

bit = platform.architecture()[0]

if bit=='64bit':


    import PY3

else:

    exit('\033[1;31m[×] Sorry Device Not Support')
