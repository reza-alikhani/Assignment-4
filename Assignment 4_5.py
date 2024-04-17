list = []
while True:
    a = input("enter anything, type finish when you're done: ")
    if a != "finish":
         list.append(a)
    if a == "finish":
        break
new_list = []

for i in list:
    if i not in new_list:
        new_list.append(i)
print(new_list)