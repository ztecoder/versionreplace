import sys
from ftplib import FTP

host, port = '127.0.0.1', 21
user, passwd = 'admin', 'admin123'
filename, filepath = sys.argv[1:]
if not filepath.endswith('/'):
    filepath += '/'

ftp = FTP()
try:
    ftp.connect(host, port)
    ftp.login(user, passwd)
    print(ftp.getwelcome())
    if filename in ftp.nlst():
        print('%s is exist, you can download' % filename)
        ftp.retrbinary('RETR ' + filename, open(filepath+filename, 'wb').write)
    else:
        print('%s is not exist' % filename)
except:
    print('Fail to connect server %s:%d' % (host,port))
finally:
    ftp.quit()
