import sys
import fileinput

filename, filepath = sys.argv[1:]
if not filepath.endswith('/'):
    filepath += '/'

try:
    for line in fileinput.input(files = filepath+filename, inplace=True):
        if 'CMAKE_C_FLAGS' in line:
            print(line.rstrip() + ' -Werror')
        else:
            print(line.rstrip())
finally:
    fileinput.close()