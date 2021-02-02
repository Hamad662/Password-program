password = "williams"
for i in range(3):
    pwd = input("enter the password: ")
    j = 2
    if (pwd == password):
        print("welcome")
        break
    else:
        print("please try again, chances",j-i)
        continue
print("try next time!")
