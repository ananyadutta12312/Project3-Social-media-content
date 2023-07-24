import instaloader

ig = instaloader.Instaloader()

user = input("Enter username: ")
post_url = input("Instagram Post link: ")

#download profile pic
ig.download_profile(user,profile_pic_only=True)


#download all post
#ig.download_profile(user,profile_pic_only=False)

