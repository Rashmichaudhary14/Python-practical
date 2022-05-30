#Write a python progran to shuffle a list.
# import the random module
import random
#declare a list
sample_list=[1,2,3,4,5]
print("original list:")
print(sample_list)
#first shuffle
random.shuffle(sample_list)
print("\nafter the first shuffle:")
print(sample_list)
#second shuffle
random.shuffle(sample_list)
print("\nafter the second shuffle:")
print(sample_list)
