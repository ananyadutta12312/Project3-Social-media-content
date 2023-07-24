import pytube as p
#from pytube import YouTube

link = input("Enter youtube link: ")
youtube = p.YouTube(link)

#get the title of the video
print(youtube.title)

#get the link of the video thumbnail
print(youtube.thumbnail_url)

# #For user to choose resolution of the video
# videos = youtube.streams.all()
# vid = list(enumerate(videos))

# for i in vid:
#     print(i)
# print()

# strm = int(input("Enter stream: "))
# videos[strm].download()



#directly download the highest resolution video
videos = youtube.streams.get_highest_resolution()
videos.download()

print("Download successfully")


