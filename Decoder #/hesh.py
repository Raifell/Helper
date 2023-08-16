import struct
import sys

cod = struct.pack('I3c', 123, b'a', b'b', b'c')
print(cod)
ucod = struct.unpack('I3c', b'{\x00\x00\x00abc')
print(ucod)
urd = 'ITStep'
print(urd, sys.byteorder)
