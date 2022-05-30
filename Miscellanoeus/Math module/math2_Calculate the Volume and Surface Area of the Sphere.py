#Python Program to Calculate the Volume and Surface Area of the Sphere

PI = 3.14

# Take the Input from the User
radius = float(input("Enter the Radius of a Sphere: "))

# Calculate the Surface Area
sa =  4 * PI * radius * radius

# Calculate the Volume
Volume = (4 / 3) * PI * radius * radius * radius

# Print the Output
print("\nThe Surface area of a Sphere = %.2f" %sa)
print("\nThe Volume of a Sphere = %.2f" %Volume)
