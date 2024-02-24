# range() Function: 
# it is intersting to know that range() looks like a list sometimes, but it is not a list, but it generates a list, only when interating over it, thus
#saving a lot memory. Helpful in huge ranges. 
for i in range(0,5):
    print(i)

# for loop can also be done this way
print(list(range(0,5)))
# run range from 3 to 9 with a differnce of 2
print(list(range(3, 9, 2)))

# interate over a list / sequence : 
nouns =['Chris', 'men', 'hen', 'whatsup']
for i in range(len(nouns)):
    print(i, nouns[i])