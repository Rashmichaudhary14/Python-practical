#Print the Sum of Key Value Pairs in a Given Dictionary
 
D1 = {2: 8, 5: 20, 3: 15}
res_sumList = []
 
# Traverse the dictionary
for key in D1:
  res_sumList.append(key + D1[key])
 
# Print the list
print("Sum of Key-value pairs is =",list(res_sumList))
