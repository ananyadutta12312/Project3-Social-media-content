import instaloader

ig = instaloader.Instaloader()

user = input("Enter username: ")

#check if account is private
profile = instaloader.Profile.from_username(ig.context,user)
private = profile.is_private
print("Is account private:",private)

# #download profile pic
ig.download_profile(user,profile_pic_only=True)

print("For more account details please login")
print("Do you want to login: y/n")
log = input()
if log == "y":
    username = input("Enter username: ")
    password = input("Enter password: ")
    ig.login(username,password)

    # download all tagged post
    #ig.download_profile(user,download_tagged = True)

    # download all stories
    #ig.download_profile(user,download_stories=True)

    # download all post
    ig.download_profile(user,profile_pic_only=False)

    print()

    #print a list of followers
    followers = profile.get_followers()
    for follower in followers:
        print(follower)
