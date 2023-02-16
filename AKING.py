import os,time
import struct
size = struct.calcsize("P")

if size == 8:
    print("\033[1;31m YOUR DEVICE SUPPORT TOOL: 64BIT")
    time.sleep(1)
    from AKING import menu
    menu()
elif size == 4:
    print("\033[1;31m OPPPS YOUR DEVICE 32 BIT")
    sys.exit()
else:
    print("your system not support TOOL")
