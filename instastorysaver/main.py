from .auth import get_credentials
from instagrapi import Client
from instagrapi.exceptions import LoginRequired
import os

def login_user(username, password):

    print("Logging in user...")

    # Setup client session and delay to avoid suspicion
    cl = Client()
    cl.delay_range = [1, 3]
    SESSION_PATH = os.path.expanduser("~/.igsave_session.json")

    session = cl.load_settings(SESSION_PATH)
    login_via_session = False
    login_via_pw = False

    if session:
        try:
            cl.set_settings(session)
            cl.login(username, password)

            # Check if session is valid
            try:
                cl.get_timeline_feed()
            except LoginRequired:
                print("Session is invalid, need to login via username and password")

                # Use the same device uuids across logins
                old_session = cl.get_settings()
                cl.set_settings({})
                cl.set_uuids(old_session["uuids"])

                cl.login(username, password)

            login_via_session = True
            cl.dump_settings(SESSION_PATH)
            print("✅ Login via session successful")

        except Exception as e:
            print("Couldn't login user using session information: %s" % e)

    if not login_via_session:
        try:
            print("Attempting to login via username and password. username: %s" % username)
            if cl.login(username, password):
                login_via_pw = True
                cl.dump_settings(SESSION_PATH)
                print("✅ Login via passoword is successful")

        except Exception as e:
            print("Couldn't login user using username and password: %s" % e)

    if not login_via_pw and not login_via_session:
        raise Exception("Couldn't login user with either password or session")

    return cl

def save_story(cl, username):
    
    # Get UserID from username
    user_info = cl.user_info_by_username_v1(username).model_dump()
    userid = user_info["pk"]
    # userid = cl.user_id_from_username(username)
    print("Found user ID: "+userid)
    
    
    # Get story count
    stories = cl.user_stories(userid)
    print("User story count: "+str(len(stories)))

    # Save story if not exists
    for s in stories:
        storid = s.pk
        if not os.path.exists("stories"):
            os.makedirs("stories")
        if not (os.path.isfile(f"stories/{username}_{storid}.mp4") or os.path.isfile(f"stories/{username}_{storid}.jpg")):
            cl.story_download(storid, f"{username}_{storid}", "./stories")
            print(f"Story {storid} successfully downloaded!")
        else:
            print(f"Story {storid} already exists, skipping...")

def main():
    print("💾 Instastorysaver")
    username, password = get_credentials()
    cl = login_user(username, password)
    print("ℹ️ To save multiple users, simply seperate each user by a whitespace (e.g.: foo bar etc)")
    print("ℹ️ To quit the program, simply input: exit")
    while True:
        users = input("Input usernames to save: ")
        if users == "exit":
            quit()
        for username in users.split():
            save_story(cl, username)

if __name__ == "__main__":
    main()
