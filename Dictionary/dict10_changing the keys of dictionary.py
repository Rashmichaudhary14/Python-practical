#changing the keys of dictionary
 
D1 = {'jim': 23, 'sam': 29, 'dean': 33, 'micheal': 40}
 
#print the original dictionary
print("The original dictionary is =", D1)
 
#using assignment (basic technique)
#changing key 'jim' to 'sam'
D1['sam'] = D1['jim']
del D1['jim']
# printing result
print ("Dictionary D1 after changing key 'jim'=", str(D1))
 
#using pop() function
#changing key 'sam' to 'anni'
D1['anni'] = D1.pop('sam')
# printing result
print ("Dictionary D1 after changing key 'sam'=", str(D1))
 
#To change all the keys
#use zip()
new_keyslist = ['tom', 'simon', 'tony', 'roy']
final_D1 = dict(zip(new_keyslist, list(D1.values())))
# printing result
print ("Dictionary D1 after changing all keys=", str(final_D1))
