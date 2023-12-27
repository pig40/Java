import ftplib


def anonLogin(hostname):
    try:
        ftp = ftplib.FTP(hostname)
        ftp.login('anonymous', 'password')
        print('\n(*) ' + str(hostname) + ' FTP Anonymous Logon Succeeded.')
        ftp.quit()
        return True
    except Exception as e:
        print('[*]' + str(e))
        print('\n[-]' + str(hostname) + 'FTP Anonymous Logon Failed.')
        return False


host = '119.114.189.244'
anonLogin(host)
