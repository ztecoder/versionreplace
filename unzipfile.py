import sys
import zipfile

filename, filepath = sys.argv[1:]
if not filepath.endswith('/'):
    filepath += '/'

try:
    zipFile = zipfile.ZipFile(filepath+filename)
    zipFile.extractall(filepath)
except:
    print('Fail to unzip %s' % filepath+filename)