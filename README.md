# Instagram Story Saver
A simple python script to save all currently available stories based on the given ig usernames.

## Installation
Installation is done using pip
```sh
pip install igsave
```

## Usage
To use the script simply run the application
```
igsave
```

When running the application for the first time, it would ask for your instagram username and password to be used for the instagram api.  
Subsequent runs will utilize locally saved sessions to avoid suspicion from instagram.  
After successfully logging in, you can start inputting usernames of the users that you wanted to save.  
  
Example run  
```
✅ Login via session successful
ℹ️ To save multiple users, simply seperate each user by a whitespace (e.g.: foo bar etc)
ℹ️ To quit the program, simply input: exit
Input usernames to save: instagram  
Found user ID: 25025320
User story count: 1
Story 3556539556155674170 successfully downloaded!
```

## Alternate Usage
I have also provided an alternate script made in Jupyter Notebook, which can be used with Google Colab for cloud integration.

## Disclaimer
*This Project utilizes subzeroid's unofficial [Instagram API](https://github.com/subzeroid/instagrapi) and is not affiliated with Meta. Use at your own risk*
