num = eval(input("Enter an integer from 1 to 15: "))

def as_str(i):
    s = ""
    if i <10: s = " "
    return s + str(i)


#num = 15

allrows = ""
for j in range(1,num+2):

    #leading spaces
    row = " "*3*(num-j+1)

    #backward
    for i in range(j-1,1,-1):
        s = as_str(i)
        row+=s + " "

    #forward
    for i in range(1,j):
        s = as_str(i)
        row+=s + " "


    row +="\n"
    allrows +=row

print (allrows)
