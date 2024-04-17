list = []
while True:
    a = input("enter anything, type finish when you're done: ")
    if a != "finish":
         list.append(a)
    if a == "finish":
        break
list.reverse()

print(list)

