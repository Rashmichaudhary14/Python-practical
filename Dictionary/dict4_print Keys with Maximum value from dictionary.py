#Write a python program to print Keys with Maximum value from dictionary.
Ans.  
test_dict = {'Simply' : 2, 'Coding' : 1, 'Python' : 3, 'java': 2}
 
print("The original dictionary is : " + str(test_dict))
 
temp = max(test_dict.values())
res = [key for key in test_dict if test_dict[key] == temp]
 
print("Keys with maximum values are : " + str(res))
