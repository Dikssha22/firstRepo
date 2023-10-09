def CreateFile():
    file=open("wonder.txt","w")
    data=input("Enter data:")
    file.write(data)
    file.close()

CreateFile()