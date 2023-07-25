import instaloader

ig = instaloader.Instaloader()

user = input("Enter username: ")

#check if account is private
profile = instaloader.Profile.from_username(ig.context,user)
private = profile.is_private
print("Is account private:",private)

# #download profile pic
print("Downloading profile picture...")
ig.download_profile(user,profile_pic_only=True)

print("For more account details please login")
print("Do you want to login: y/n")
log = input()
if log == "y":
    username = input("Enter username: ")
    password = input("Enter password: ")
    ig.login(username,password)

    conti = True

    while(conti == True):
        print("choose your options:")
        options = ["List of Follower","List of Followee","Download all Post"]
        for i in range(len(options)):
            print(str(i) + ":" + options[i])
        
        option_input = int(input())

        if option_input == 0:
            #print list of followers
            followers = profile.get_followers()
            for follower in followers:
                print(follower)
            print()

        if option_input == 1:
            #print list of followers
            followees = profile.get_followees()
            for followee in followees:
                print(followee)
            print()

        if option_input == 2:
            # download all post
            print("Downloading all post...")
            ig.download_profile(user,profile_pic_only=False)

            print()

        print("Do you want to continue: y/n")
        choise = input()
        if choise == "y":
            conti = True
        elif choise == "n":
            conti = False