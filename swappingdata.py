def swapfiledata():
    file1=input("enter file 1 name")
    file2=input("enter file 2 name")
    with open(file1,'r')as a:
        dataa =a.read ()
    with open(file2,'r')as b:
        datab =b.read ()
    with open(file1,'w')as a:
        a.write(datab)
    with open(file2,'w')as b:
       b.write(dataa)
swapfiledata()  