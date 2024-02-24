# Simultanous assignments in Python, used twice
print("Simultanous assignments")
a, b = 0, 1
while(a < 10):
    print(a)
    a, b = b, a+b
   
# Not skipping line with end, since print statement prints in new line
print("Not skipping line with end")
a, b = 0, 1
while(a < 10):
    print(a , end=",")
    a, b = b, a+b

# Getting used to input and if condition, no checks for non integer value ( for now)
# print("\nInput and if condition")
# x = int(input("Please enter an interger: "))
# if(x < 0):
#     x=0
#     print('Negative value changed to zero')
# elif x == 0:
#     print('Zero')
# elif x == 1:
#     print('Single')
# else:
#     print('More')

# For loop while measuring strings length
print('\nFor loops measuring strings length\n')
words = ['Tea', 'Peacock', 'Bugs']
for eachWord in words:
    print(eachWord, len(eachWord))

#Changing a value in an object can be tricky, so there are two ways: 
    #1: make a copy of object, and the change the value in it,
    #2: make a new object to store the updated data
users = {'alizaib': 'active', 'aslam': 'inactive', 'atif': 'active' }
print('interating over a copy')
for user, status in users.copy().items():

    if status=='inactive':
        del users[user]
print('update users', users , '\n')

print('making a new object, but achieving same results')
active_users= {}
for user, status in users.items():
    if status == 'active':
        active_users[user] = status
print('new collection', active_users)