names = ["Alex","John","Mary","Steve","John", "Steve"]
filtered_names =[]
def remove_duplicate():
    for name in names:
        print(name)
        if name not in filtered_names:
            filtered_names.append(name)
remove_duplicate()
print (filtered_names)
largest = max(names)
print (largest)
smallest =names = min(names)
print (smallest)
