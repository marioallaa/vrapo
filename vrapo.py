
import sys, os, magic
fileToRun = ''
for l in sys.argv[1:]:
    fileToRun+= ' ' + l
try:
    t = magic.from_file(fileToRun[1:], mime=True)
except Exception as e:
    t = ''
if t == 'text/x-python':
    os.system('python3' + fileToRun)
elif t == 'text/plain':
    t = fileToRun.split('.')[-1]
    if t == 'py':
        os.system('python3' + fileToRun)
    elif t == 'js' or t == 'ts':
        os.system('node' + fileToRun)
elif os.path.isfile('./package.json'):
    os.system('npm run' + fileToRun)
else:
    try:
        os.system('xdg-open' + fileToRun)
    except Exception as e:
        print('filetype ', t, 'unsupported')




