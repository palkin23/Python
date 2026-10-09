items = ["apple", "banana", "orange", "apple", "mango"]
for ch in items:
    if(items.count(ch)!=1):
        print("duplicate is: ",ch)
        exit()
    else:
        print("No duplicates in the given list!")

# items = ["apple", "banana", "orange", "apple", "mango"]

# unique_item = set()

# for item in items:
#     if item in unique_item:
#         print("Duplicate: ", item)
#         break
#     unique_item.add(item)