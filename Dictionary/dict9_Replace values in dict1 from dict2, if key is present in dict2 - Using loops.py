#Replace values in dict1 from dict2, if key is present in dict2 - Using loops
 
# initializing D1 - first dictionary
D1 = {'first_name' : 'Jim', 'age' : 23, 'height' : 6.0 , 'job' : 'developer', 'company': 'XYZ'}
 
# initializing D2 - - first dictionary
D2 = {'age' : 35, 'job' : 'senior data analyst'}
 
for key in D1:
 
  # checking if key present in dict2
  if key in D2:
    D1[key] = D2[key]
 
# printing the details
print("The original dictionary: " + str(D1))
print("The updated dictionary: " + str(D2))
