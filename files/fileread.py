with open("hello.txt","r") as fileread:
    while True:
        buf=fileread.readline()
        if not buf:
            break
        print(buf)

# writefile=open("helloWrite.txt","w")
# writefile.write(buf)
# writefile.close()
