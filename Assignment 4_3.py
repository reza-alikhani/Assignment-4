import instaloader
import getpass
print("Instagram new followers finder!")

f = open("followers.txt", "r")
old_followers = []
for line in f:
    old_followers.append(line)
f.close()


L = instaloader.Instaloader()

username = input("username: ")
password = getpass.getpass("password: ")

L.login(username, password)
print ("Successful login!")

profile = instaloader.Profile.from_username(L.context, input("username: "))

new_followers = []
for follower in profile.get_followers():
    new_followers.append(follower)

for new_follower in new_followers:
    if new_follower not in old_followers:
        print("new followers: ", new_follower)

f = open("followers.txt", "w")
for follower in new_followers:
    f.write(follower + "/n")
f.close()
