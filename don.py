def ReadFile():
    file=open("wonder.txt","r")
    data=file.read()
    v=0
    for ch in "AEIOUaeiou":
        v+=1
    print("Total vowels in file=",v)
    file.close()
    
ReadFile()
        