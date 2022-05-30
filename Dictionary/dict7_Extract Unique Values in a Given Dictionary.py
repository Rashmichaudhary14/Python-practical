#Extract Unique Values in a Given Dictionary
#In a dictionary, the keys have to be unique, whereas the values can be duplicated. So, given a dictionary as shown below, how can you print all the unique values it has?

D1 = {'list1': [4, 7, 10, 20], 
      'list2': [7, 16, 9, 10], 
      'list3': [13, 10, 4, 8], 
      'list4': [7, 20, 6, 11]}
Output = [4, 6, 7, 8, 9, 10, 11, 13, 16, 20]
 
#Extract unique values in dictionary
#Initializing Dictionary
D1 = {'list1': [4, 7, 10, 20], 
      'list2': [7, 16, 9, 10], 
      'list3': [13, 10, 4, 8], 
      'list4': [7, 20, 6, 11]}
 
#Actual dictionary
print("The given dictionary is:", str(D1))
 
#Extract the sorted unique values using set_comprehension + values() + sorted()
uniqueVals = list(sorted({val2 for val1 in D1.values() for val2 in val1 }))
 
#list of unique values
print("The unique values of the given dictionary are:", uniqueVals)
