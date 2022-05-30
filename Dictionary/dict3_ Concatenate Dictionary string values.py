#Write a python program to Concatenate Dictionary string values.
Ans.  
test_dict1 = {'SC' : 'a', 'is' : 'b', 'best' : 'c'}
test_dict2 = {'SC' : '1', 'is' : '2', 'best' : '3'}
 
print("The original dictionary 1 : " + str(test_dict1))
print("The original dictionary 2 : " + str(test_dict2))
 
res = {key: test_dict1[key] + test_dict2.get(key, '') for key in test_dict1.keys()}
 
print("The string concatenation of dictionary is : " + str(res))
