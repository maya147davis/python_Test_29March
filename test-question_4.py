str_list = []
duplicate = False

while True:
    x = input("Enter string (or 'quit' to stop): ").lower()
    if x == "quit":
        break
    if x in str_list:
        duplicate = True
    str_list.append(x)

if duplicate:
    print("There were duplicates")
else:
    print("There were no duplicates")