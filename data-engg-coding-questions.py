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


## Given a list of words, print the number of occurrences of each word

mylist = ["arun", "natva", "vaishu", "natva", "samy", "natva", "natva", "vihari"]
mydict = {}
for word in mylist:
    #print(word)
    if mydict.get(word) is None:
        mydict[word] = 1
    else:
        mydict[word] = mydict[word] + 1
print(mydict)


## python code to print the pairs of elements in a list whose sum is equal to a target number:
input = [0,1,2,-1,-2,3,4,5,6]
target = 5
resultlist = []
#Output = [1,4],[2,3],[0,5],[-1,6]

for i in input:
    j = target - i
    if j in input:
        resultlist.append(j)
        if i not in resultlist:
            print("pair : ", i, j)
