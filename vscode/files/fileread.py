fileread=open("hello.txt","r")
buf=fileread.read()
fileread.close()
print(buf)