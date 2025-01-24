from instagrapi import Client
import config

if __name__ == '__main__':
    print("Logging in...")
    cl = Client()
    cl.login(config.ACCOUNT_USERNAME, config.ACCOUNT_PASSWORD)
    print(f"Login as {config.ACCOUNT_USERNAME} successful!")

    while True:
        users = input("Input ig usernames to save: ")

        for username in users.split():
            try:
                userid = cl.user_id_from_username(username)
                print("Found user ID: "+userid)
            except ValueError:
                pass
            
            stories = cl.user_stories(userid)
            print("User story count: "+str(len(stories)))

            import os

            for s in stories:
                storid = s.pk
                if not os.path.exists("stories"):
                    os.makedirs("stories")
                cl.story_download(storid, f"{username}_{storid}", "./stories")
                print(f"Story {storid} successfully downloaded")
