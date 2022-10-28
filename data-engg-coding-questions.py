## python code to print elements of a list whose indexes sum is 10
mylist = [1,2,3,4,5,6,7,8,9]

ctr = 0
i = 0
while i < 9:
    j = 10 - i
    if j < 9:
        print("pairs whose indexes sum is 10: ", mylist[i], mylist[j], i, j)
    ctr = ctr + 1
    i = i + 1
    
print ("total ctr ", ctr)


