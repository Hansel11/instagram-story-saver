import json
import os
import getpass
import argparse

CRED_PATH = os.path.expanduser("~/.igsave_cred.json")

def save_cred(username, password):
    # save user credentials to a JSON file.
    cred = {"username": username, "password": password}
    with open(CRED_PATH, "w") as file:
        json.dump(cred, file, indent=4)
    print("✅ Credentials saved successfully!")

def load_cred():
    # load user credentials if they exist.
    if os.path.exists(CRED_PATH):
        with open(CRED_PATH, "r") as file:
            return json.load(file)
    return None

def logout():
    # delete the stored credentials.
    if os.path.exists(CRED_PATH):
        os.remove(CRED_PATH)
        print("✅ Credentials deleted successfully.")
    else:
        print("⚠️ No stored credentials found.")

def prompt_for_credentials():
    # prompt the user for login credentials.
    username = input("Enter username: ")
    password = getpass.getpass("Enter password: ")
    return username, password

def get_credentials():
    parser = argparse.ArgumentParser(description="💾 Instastorysaver by Hansel11")
    parser.add_argument("--login", action="store_true", help="add or update login credentials")
    parser.add_argument("--logout", action="store_true", help="remove saved sessions and credentials")

    args = parser.parse_args()
    
    if args.logout:
        logout()
        quit()
    elif args.login:
        print("🔄 Resetting login credentials...")
        logout()
        username, password = prompt_for_credentials()
        save_cred(username, password)
        quit()
    else:
        credentials = load_cred()
        if credentials:
            print(f"🔑 Credentials found! username: {credentials['username']}")
            username, password = credentials['username'], credentials['password']
        else:
            print("🔓 No credentials found.")
            username, password = prompt_for_credentials()
            save_cred(username, password)
        return (username, password)
    
    