f=open('tester.bin','wb')
f.write(b'\x00\x01\x02\x03\x04\x05')
f=open('tester.bin','rb')
print(f.read())
f.close()