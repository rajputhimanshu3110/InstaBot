#pip install instaloader
import instaloader
import speak
import os

x=1
def talk(text):
    print(text)
    speak.speak(text)

def check_dir(username):
    try :
        f = open(f"{username}/check.txt", "w")
        f.write("")
        f.close()
    except:
        create_dir(username)

def create_dir(username):
    # set your local directory
    parent_dir = "E:\Projects\Python\project\insta"
    path = os.path.join(parent_dir, username)
    os.mkdir(path)

def down_follower(profile):
    talk('Saving followers in file')
    for follower in profile.get_followers():
        f = open(f"{profile.username}_follower.txt", "a")
        f.write(f"{follower.username}\n")
        f.close()
    talk('Followers Saved in file')


def down_following(profile):
    talk("Printing Following")
    for followee in profile.get_followees():
        f = open(f"{profile.username}_following.txt", "a")
        f.write(f"{followee.username}\n")
        f.close()

    talk('Followings Saved in file')

def down_post(profile):
    talk("Downloading Posts Wait for a While")
    posts = profile.get_posts()

    for index, post in enumerate(posts, 1):
        bot.download_post(post, target=f"{profile.username}_{index}")

    talk("All Posts Downloaded")


user = input("Name Please : ")

talk(f"Hello {user} Welcome to instagram Scrapping")
# Create an instance of Instaloader class
bot = instaloader.Instaloader()
bot.login(user="__singhhimanshu",passwd="Viraj@1983")

if __name__ == '__main__':
    while x!=0:
        talk("Enter Username for Scrapping ")
        username = input()
        # Load a profile from an Instagram handle
        profile = instaloader.Profile.from_username(bot.context, username)
        speak.speak(f"User {username} have {profile.mediacount} Posts, {profile.followers} Followers and {profile.followees} Following")

        print("Username: ", profile.username)
        print("User ID: ", profile.userid)
        print("Number of Posts: ", profile.mediacount)
        print("Followers: ", profile.followers)
        print("Followees: ", profile.followees)
        print("Bio: ", profile.biography)

        talk("Press\n1 - Download Followers List\n2 - Download Following List\n3 - Download Posts")
        choice = int(input())

        if choice == 1:
            down_follower(profile)
        elif choice == 2:
            down_following(profile)
        elif choice == 3:
            down_post(profile)
        talk("Wanna Search more Profile\nPress 1 for Continue and 0 for Exit.")
        x = int(input())