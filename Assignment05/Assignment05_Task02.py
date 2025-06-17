# Create a list of numbers from 1 to 10
mylist = [i for i in range(1,11)]
print("Original list: {}".format(mylist))

# Extract the first five elements
extractedlist = mylist[:5]
print("Extracted first five elements: {}".format(extractedlist))

# Reverse the extracted elements
extractedlist.reverse()
print("Reversed extracted elements: {}".format(extractedlist))


