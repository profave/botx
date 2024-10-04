import requests
import json
import os
import re
import random
from getuseragent import UserAgent
import os
import re
import sys
import time
import json
import random
import datetime
import requests
from rich import print as rich_print
import sys
import os
import requests
import threading
import time

__AUTHOR__ = 'Pham Dinh Quoc '
__CONTACT__ = 'fb.com/PhDinhQuoc '
def jovan(): 
    print("""\033[1;31m
          ██╗██╗   ██╗██████╗ ███████╗
          ██║██║   ██║██╔══██╗██╔════╝
          ██║██║   ██║██║  ██║█████╗  
    ██   ██║██║   ██║██║  ██║██╔══╝  
    ╚█████╔╝╚██████╔╝██████╔╝███████╗
      ╚════╝  ╚═════╝ ╚═════╝ ╚══════╝
                                 

\033[1;37m──────────────────────────────────────────────────────────────\033[1;37m
          \033[1;31mOWNER    \033[1;32m: \033[1;37mJUDE POGI 
          \033[1;31mCODED IN \033[1;32m: \033[1;37mPYTHON
          \033[1;31mVERSION  \033[1;32m: \033[1;37m4.1
          \033[1;31mTOOL     \033[1;32m: \033[1;37mAUTO BOOST FACEBOOK
\033[1;37m──────────────────────────────────────────────────────────────\033[1;37m""")




def ban():
   print("""
\033[1;38;2;255;105;180m   

╔═╗╦ ╦╔╦╗╔═╗  ╔═╗╦ ╦╔═╗╦═╗╔═╗
╠═╣║ ║ ║ ║ ║  ╚═╗╠═╣╠═╣╠╦╝║╣ 
╩ ╩╚═╝ ╩ ╚═╝  ╚═╝╩ ╩╩ ╩╩╚═╚═╝

\x1b[38;2;173;255;47m════════════════════════════════════\x1b[38;2;233;233;233m
Coded By: Jovan
Programming Language use: Python
 Multithread: NO
\x1b[38;2;173;255;47m════════════════════════════════════\x1b[38;2;233;233;233m
\033[0m""")

def clear():
    if(sys.platform.startswith('win')):
        os.system('cls')
    else:
        os.system('clear')

gome_token = []

def tokz(input_cookies):
    for cookie in input_cookies:
        header_ = {
            'authority': 'business.facebook.com',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
            'cache-control': 'max-age=0',
            'cookie': cookie,
            'referer': 'https://www.facebook.com/',
            'sec-ch-ua': '".Not/A)Brand";v="99", "Google Chrome";v="103", "Chromium";v="103"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Linux"',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'same-origin',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1',
        }
        try:
            home_business = requests.get('https://business.facebook.com/content_management', headers=header_).text
            token = home_business.split('EAAG')[1].split('","')[0]
            cookie_token = f'{cookie}|EAAG{token}'
            gome_token.append(cookie_token)
        except:
            pass
    return gome_token

def share(tach, id_share):
    cookie = tach.split('|')[0]
    token = tach.split('|')[1]
    he = {
        'accept': '*/*',
        'accept-encoding': 'gzip, deflate',
        'connection': 'keep-alive',
        'content-length': '0',
        'cookie': cookie,
        'host': 'graph.facebook.com'
    }
    try:
        res = requests.post(f'https://graph.facebook.com/me/feed?link=https://m.facebook.com/{id_share}&published=0&access_token={token}', headers=he).json()
    except:
        pass
    
def shar():
    input_cookies = input("\x1b[38;2;173;255;47mEnter Cookie:  \x1b[38;2;233;233;233m").split(',')
    id_share = input("\x1b[38;2;173;255;47mEnter Post ID: \x1b[38;2;233;233;233m")
    total_share = int(input("\x1b[38;2;173;255;47mHow Many Share: \x1b[38;2;233;233;233m"))
    delay = int(input("\x1b[38;2;173;255;47m Delay Share: \x1b[38;2;233;233;233m"))
    print('\x1b[38;2;173;255;47m════════════════════════════════════\x1b[38;2;233;233;233m')
    print('\x1b[38;2;173;255;47m[*] \x1b[38;2;233;233;233mwaiting...', end='\r')

    all = tokz(input_cookies)
    total_live = len(all)
    print(f'\x1b[38;2;173;255;47mLive: \x1b[38;2;233;233;233m{total_live} \x1b[38;2;173;255;47mCookies')
    
    if total_live == 0:
        sys.exit()

    print('\x1b[38;2;173;255;47m════════════════════════════════════\x1b[38;2;233;233;233m')
    stt = 0
    while True:
        for tach in all:
            stt = stt + 1
            threa = threading.Thread(target=share, args=(tach, id_share))
            threa.start()
            print(f'\x1b[38;2;173;255;47mShare: + \x1b[38;2;233;233;233m{stt}', end='\r')
            time.sleep(delay)
        if stt > total_share:
            break

    gome_token.clear()
    input('\x1b[38;2;173;255;47m[*] \x1b[38;2;233;233;233mEnter^^\033[0m')


    

def Load_data_alot():
    """Load data from a JSON file."""
    try:
        with open('Eaau.json', 'r') as file:
            data = file.read()
            if data:
                return json.loads(data)
            else:
                return {"access_tokens": []}  # Assuming only personal account tokens are stored
    except FileNotFoundError:
        return {"access_tokens": []}
    except json.decoder.JSONDecodeError:
        print("Error: Failed to decode JSON from Eaau.json. File might be corrupted.")
        return {"access_tokens": []}

def saving_data(data):
    """Save data to a JSON file."""
    with open('Eaau.json', 'w') as file:
        json.dump(data, file, indent=4)
import requests
from concurrent.futures import ThreadPoolExecutor, as_completed

def Auto_react_comment_fast(post_id, reaction_type, reactor_type, num_reactions):
    """Perform reactions on a Facebook post/comment."""
    access_tokens_data = Load_data_alot()
    access_tokens = access_tokens_data.get("access_tokens", [])

    total_reactions_sent = 0

    def react_with_token(access_token, reactor_type):
        nonlocal total_reactions_sent  # Allows modifying total_reactions_sent inside the inner function
        
        if access_token.startswith("EA") or access_token.startswith("EAA"):
            if reactor_type == "PAGE":
                pages = token_info.get("pages", [])
                for page in pages:
                    page_access_token = page.get("access_token", "")
                    page_name = page.get("name", "")
                    try:
                        if not has_reacted(post_id, page_access_token):
                            url = f'https://graph.facebook.com/v18.0/{post_id}/reactions'
                            params = {'access_token': page_access_token, 'type': reaction_type}
                            response = requests.post(url, params=params)

                            if response.status_code == 200:
                                total_reactions_sent += 1
                                print(f"Successfully reacted using Page '{page_name}' ✅")
                                if total_reactions_sent >= num_reactions:
                                    return True
                            else:
                                print(f"Failed to react using Page '{page_name}'. Status code: {response.status_code}, Response: {response.text}")
                    except requests.exceptions.RequestException as error:
                        print(f"Exception occurred while reacting using Page '{page_name}': {error}")

            elif reactor_type == "ACCOUNT":
                try:
                    if not has_reacted(post_id, access_token):
                        url = f'https://graph.facebook.com/v18.0/{post_id}/reactions'
                        params = {'access_token': access_token, 'type': reaction_type}
                        response = requests.post(url, params=params)

                        if response.status_code == 200:
                            total_reactions_sent += 1
                            print("Successfully reacted using Personal Profile ✅")
                            if total_reactions_sent >= num_reactions:
                                return True
                        else:
                            print(f"Failed to react using Personal Profile. Status code: {response.status_code}, Response: {response.text}")
                except requests.exceptions.RequestException as error:
                    print(f"Exception occurred while reacting using Personal Profile: {error}")

            elif reactor_type == "BOTH":
                try:
                    if not has_reacted(post_id, access_token):
                        url = f'https://graph.facebook.com/v18.0/{post_id}/reactions'
                        params = {'access_token': access_token, 'type': reaction_type}
                        response = requests.post(url, params=params)

                        if response.status_code == 200:
                            total_reactions_sent += 1
                            print("Successfully reacted using both methods ✅")
                            if total_reactions_sent >= num_reactions:
                                return True
                        else:
                            print(f"Failed to react. Status code: {response.status_code}, Response: {response.text}")
                except requests.exceptions.RequestException as error:
                    print(f"Exception occurred while reacting: {error}")

        else:
            print("Invalid access token format")
        
        return False

    with ThreadPoolExecutor(max_workers=2000) as executor:
        futures = []
        for token_info in access_tokens:
            access_token = token_info.get("access_token", "")
            futures.append(executor.submit(react_with_token, access_token, reactor_type))

        for future in as_completed(futures):
            if total_reactions_sent >= num_reactions:
                print(f"Reached the limit of {num_reactions} reactions.")
                break

    print(f"Total reactions sent: {total_reactions_sent}")

# Example usage
# Auto_react_comment('123456789', 'LIKE', 'BOTH', 10)

def Auto_react_comment(post_id, reaction_type, reactor_type, num_reactions):
    """Perform reactions on a Facebook post/comment."""
    access_tokens_data = Load_data_alot()
    access_tokens = access_tokens_data.get("access_tokens", [])

    reactions_count = 0
    total_reactions_sent = 0

    for token_info in access_tokens:
        access_token = token_info.get("access_token", "")
        
        try:
            if access_token.startswith("EA") or access_token.startswith("EAA"):
                if reactor_type == "PAGE":
                    # Use only pages as reactors
                    pages = token_info.get("pages", [])
                    for page in pages:
                        page_access_token = page.get("access_token", "")
                        page_name = page.get("name", "")
                        try:
                            if not has_reacted(post_id, page_access_token):
                                url = f'https://graph.facebook.com/v18.0/{post_id}/reactions'
                                params = {'access_token': page_access_token, 'type': reaction_type}
                                response = requests.post(url, params=params)
                                
                                if response.status_code == 200:
                                    reactions_count += 1
                                    total_reactions_sent += 1
                                    print("\033[1m\033[92mSuccessfully\033[0m\033[1m\033[92m✅\033[0m")

                                    if total_reactions_sent >= num_reactions:
                                        print(f"Reached the limit of {num_reactions} reactions.")
                                        return
                                else:
                                    print(f"Failed to react using Page '{page_name}'. Status code: {response.status_code}, Response: {response.text}")
                        except requests.exceptions.RequestException as error:
                            print(f"Exception occurred while reacting using Page '{page_name}': {error}")
                        
                elif reactor_type == "ACCOUNT":
                    # Use only personal account as reactor
                    try:
                        if not has_reacted(post_id, access_token):
                            url = f'https://graph.facebook.com/v18.0/{post_id}/reactions'
                            params = {'access_token': access_token, 'type': reaction_type}
                            response = requests.post(url, params=params)
                            
                            if response.status_code == 200:
                                reactions_count += 1
                                total_reactions_sent += 1
                                print("\033[1m\033[92m[Successfully\033[0m\033[1m\033[92m✅\033[0m\033[1m\033[92m]")

                                if total_reactions_sent >= num_reactions:
                                    print(f"\033[1m\033[92mReached the limit of {num_reactions} reactions✅.\033[0m")

                                    return
                            else:
                                print(f"Failed to react using Personal Profile. Status code: {response.status_code}, Response: {response.text}")
                    except requests.exceptions.RequestException as error:
                        print(f"Exception occurred while reacting using Personal Profile: {error}")
                    
                elif reactor_type == "BOTH":
                    # Use both pages and personal account as reactors
                    try:
                        if not has_reacted(post_id, access_token):
                            url = f'https://graph.facebook.com/v18.0/{post_id}/reactions'
                            params = {'access_token': access_token, 'type': reaction_type}
                            response = requests.post(url, params=params)
                            
                            if response.status_code == 200:
                                reactions_count += 1
                                total_reactions_sent += 1
                                if "pages" in token_info:  # Check if pages are available
                                    print("\033[1m\033[92mSuccessfully\033[0m\033[1m\033[92m✅\033[0m")

                                else:
                                    print("Successfully reacted using Personal Profile")
                                
                                if total_reactions_sent >= num_reactions:
                                    print(f"Reached the limit of {num_reactions} reactions.")
                                    return
                            else:
                                if "pages" in token_info:
                                    print(f"Failed to react using Page '{page_name}'. Status code: {response.status_code}, Response: {response.text}")
                                else:
                                    print(f"Failed to react using Personal Profile. Status code: {response.status_code}, Response: {response.text}")
                    except requests.exceptions.RequestException as error:
                        if "pages" in token_info:
                            print(f"Exception occurred while reacting using Page '{page_name}': {error}")
                        else:
                            print(f"Exception occurred while reacting using Personal Profile: {error}")
            else:
                print("Invalid access token format")
        except requests.exceptions.RequestException as error:
            print(f"Exception occurred: {error}")

    print(f"Total reactions sent: {total_reactions_sent}")

def has_reacted(post_id, access_token):
    """Check if the user has already reacted to the post."""
    try:
        url = f'https://graph.facebook.com/v18.0/{post_id}/reactions'
        params = {'access_token': access_token}
        response = requests.get(url, params=params)
        
        if response.status_code == 200:
            data = response.json()
            for reaction in data.get("data", []):
                if reaction.get("id") == access_token:  # Check if user ID matches access_token (simplified check)
                    return True
            return False
        else:
            print(f"Failed to check reactions. Status code: {response.status_code}, Response: {response.text}")
            return False
    except requests.exceptions.RequestException as error:
        print(f"Exception occurred while checking reactions: {error}")
        return False

MONTHS = {
    '1': 'januari', '2': 'februari', '3': 'maret', '4': 'april', '5': 'mei', '6': 'juni', 
    '7': 'juli', '8': 'agustus', '9': 'september', '10': 'oktober', '11': 'november', '12': 'desember'
}
DAYS = {
    'Sunday': 'Minggu', 'Monday': 'Senin', 'Tuesday': 'Selasa', 'Wednesday': 'Rabu', 
    'Thursday': 'Kamis', 'Friday': 'Jumat', 'Saturday': 'Sabtu'
}
COMMENTS = ['Semangat Bang', 'Keren Bang', 'Gokil Suhu', 'Panutanku', 'Semangat Terus']

# Session
ses = requests.Session()

# Helper functions
def get_current_date():
    now = datetime.datetime.now()
    return f"{now.day} {MONTHS[str(now.month)]} {now.year}"

def clear_screen():
    os.system('clear')

def login():
    clear_screen()
    cookie = input('</> 🥵Cookie🥵 : ')
    try:
        response = requests.get(
            "https://business.facebook.com/business_locations",
            headers={
                "user-agent": "Mozilla/5.0 (Linux; Android 8.1.0; MI 8 Build/OPM1.171019.011) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.86 Mobile Safari/537.36",
                "cookie": cookie
            }
        )
        token = re.search(r"(EAAG\w+)", response.text).group(1)
        if token:
            with open('cookie.txt', 'w') as f:
                f.write(cookie)
            with open('token.txt', 'w') as f:
                f.write(token)
            rich_print("</> 🚭Login Successful🔞 !!! ")
            bot(cookie)
        else:
            raise AttributeError
    except AttributeError:
        rich_print("</> 😭Cookie Expired😓 !!")
        time.sleep(4)
        login()
    except requests.exceptions.ConnectionError:
        sys.exit("</> Internet Connection ERROR !!!")

def bot(cookie):
    current_time = datetime.datetime.now().strftime('%H:%M:%S')
    current_day = DAYS[datetime.datetime.now().strftime("%A")]
    date_str = get_current_date()
    token = open("token.txt", "r").read()
    response_message = random.choice(COMMENTS)
    comment = f"\n\nhttps://www.facebook.com/100089033379675/posts/139149639062815/?app=fbl\n\nKomentar Ini Ditulis Oleh Bot"
    
    post_url = f"https://graph.facebook.com/100089033379675_139149639062815/comments"
    post_data = {
        "message": f"{response_message} {comment}\n[ Pukul {current_time} WIB ] \n- {current_day}, {date_str} -",
        "access_token": token
    }
    headers = {"cookie": cookie}
    requests.post(post_url, data=post_data, headers=headers)
    
    share_post()

def share_post():
    clear_screen()
    header = {
        "authority": "graph.facebook.com",
        "cache-control": "max-age=0",
        "sec-ch-ua-mobile": "?0",
        "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.66 Safari/537.36"
    }
    post_link = input("</> 😘Your Fucking Post Link🥵 : ")
    share_limit = int(input("</> 🔰Share Limit🔰 : "))
    rich_print('</> Post Share Started...')
    
    cookie = open('cookie.txt', 'r').read()
    token = open('token.txt', 'r').read()
    cookies = {"cookie": cookie}
    
    try:
        for i in range(share_limit):
            response = ses.post(
                f"https://graph.facebook.com/me/feed?link={post_link}&published=0&access_token={token}",
                headers=header,
                cookies=cookies
            ).json()
            
            if "id" in response:
                rich_print(f"</> Post Shared : {response['id']}")
                sys.stdout.flush()
            else:
                sys.exit('</> ERROR DATA\n')
                
        rich_print("</> All Shares Complete !!! ")
        input("</> Press Enter To Back")
        share_post()
    except requests.exceptions.ConnectionError:
        sys.exit('</> Server Error !!! \n')
def load_data():
    try:
        with open('Eaau.json', 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return {"accounts": [], "access_tokens": []}
    except json.decoder.JSONDecodeError:
        return {"accounts": [], "access_tokens": []}
def load_data_rpw():
    try:
        with open('Rpw.json', 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return {"accounts": [], "access_tokens": []}
    except json.decoder.JSONDecodeError:
        return {"accounts": [], "access_tokens": []}

def save_data(data):
    print("Saving data:", data)  
    with open('data.json', 'w') as f:
        if isinstance(data, dict):
            json.dump(data, f, indent=4)
        else:
            json.dump({"access_tokens": data}, f, indent=4)

def count_accounts_and_pages(data):
    if isinstance(data, list):
        access_tokens = data
    else:
        access_tokens = data.get("access_tokens", [])
    
    total_accounts = len(access_tokens)
    total_pages = sum(len(token.get("pages", [])) for token in access_tokens)
    
    return total_accounts, total_pages
class color:
    END = '\033[0m'
    BOLD = '\033[1m'
    RED = '\033[91m'

def add_token():
    data = load_data()
    
    if isinstance(data, list):
        access_tokens = data
    else:
        access_tokens = data.get("access_tokens", [])
    
    while True:
        access_token = input('Enter your access token (if done just leave this blank): ')
        if not access_token:
            save_data(data)  
            main()  
            break
        
        
        
        if any(token.get("access_token") == access_token for token in access_tokens):
            print("Token already exists.")
            continue

        
        try:
            response = requests.get(f'https://graph.facebook.com/me?access_token={access_token}')
            if response.status_code == 200:
                is_valid_token = True
                
                pages_response = requests.get(f'https://graph.facebook.com/me/accounts?access_token={access_token}')
                if pages_response.status_code == 200:
                    pages_data = pages_response.json().get("data", [])
                   
                    account_data = {"access_token": access_token}
                    account_pages = [page for page in pages_data]
                    account_data["pages"] = account_pages
                    access_tokens.append(account_data)
                    if isinstance(data, list):
                        data = access_tokens  # Update data if it was initially a list
                    else:
                        data["access_tokens"] = access_tokens  # Update the access_tokens in the data structure
                        
                    print("\033[91mSuccessfully added Account\033[0m")  # Successfully added message in red
            else:
                is_valid_token = False
        except requests.exceptions.RequestException:
            is_valid_token = False

        if not is_valid_token:
            print("Invalid token. Please enter a valid token.")

        # Add this line for debugging
        save_data(data)

def Video_Extractid(url):
    group_pattern = r'groups/(\d+)/permalink/(\d+)/'
    post_pattern = r'(\d+)/posts/(\d+)/'
    photo_pattern = r'fbid=(\d+)'
    video_pattern = r'videos/(\d+)/'

    group_match = re.search(group_pattern, url)
    post_match = re.search(post_pattern, url)
    photo_match = re.search(photo_pattern, url)
    video_match = re.search(video_pattern, url)

    if group_match:
        group_id, post_id = group_match.groups()
        return f"{group_id}_{post_id}"
    elif post_match:
        group_id, post_id = post_match.groups()
        return f"{group_id}_{post_id}"
    elif photo_match:
        photo_id = photo_match.group(1)
        return photo_id
    elif video_match:
        video_id = video_match.group(1)
        return video_id
    else:
        return None
def perform_reaction_video(url, reaction_type, reactor_type, num_reactions):
    
    post_id = url
    if not post_id:
        print("[ERROR] Invalid URL or unable to extract post ID.")
        return

    access_tokens_data = load_data()
    access_tokens = access_tokens_data if isinstance(access_tokens_data, list) else access_tokens_data.get("access_tokens", [])
    
    reactions_count = 0

    for token_info in access_tokens:
        access_token = token_info.get("access_token", "") if isinstance(token_info, dict) else token_info
        try:
            if access_token.startswith("EA") or access_token.startswith("EAA"):
                if reactor_type == "PAGE":
                    # Use only pages as reactors
                    response = requests.get(f'https://graph.facebook.com/me/accounts', headers={'Authorization': f'Bearer {access_token}'}).json()
                    
                    for page in response.get('data', []):
                        page_access_token = page.get('access_token', '')
                        page_name = page.get('name', '')
                        try:
                            if not has_reacted(post_id, page_access_token):
                                url = f'https://graph.facebook.com/v18.0/{post_id}/reactions'
                                params = {'access_token': page_access_token, 'type': reaction_type}
                                response = requests.post(url, params=params)
                                
                                if response.status_code == 200:
                                    reactions_count += 1
                                    print("\033[0m\033[1m[\033[91mSUCCESS\033[0m\033[1m] SUCCESSFULLY REACTED |\033[91m {}\033[0m \033[1m|\033[91m {}\033[0m \033[1m|\033[90m {}\033[0m".format(page_name, post_id, str(response.json())))
                                    if reactions_count >= num_reactions:
                                        print("Reached the limit of {} reactions.".format(num_reactions))
                                        return
                                else:
                                    print("\033[1;91m[ERROR]\033[0;1m FAILED TO POST REACTION | \033[91m{}\033[0m".format(post_id))
                        except requests.exceptions.RequestException as error:
                            print("\033[1;91m[EXCEPTION]\033[0;1m {}\033[0m".format(error))
                        
                elif reactor_type == "ACCOUNT":
                    # Use only accounts as reactors
                    try:
                        if not has_reacted(post_id, access_token):
                            url = f'https://graph.facebook.com/v18.0/{post_id}/reactions'
                            params = {'access_token': access_token, 'type': reaction_type}
                            response = requests.post(url, params=params)
                            
                            if response.status_code == 200:
                                reactions_count += 1
                                print("\033[0m\033[1m[\033[91mSUCCESS\033[0m\033[1m] SUCCESSFULLY REACTED |\033[91m Personal Profile\033[0m \033[1m|\033[91m {}\033[0m \033[1m|\033[90m {}\033[0m".format(post_id, str(response.json())))
                                if reactions_count >= num_reactions:
                                    print("Reached the limit of {} reactions.".format(num_reactions))
                                    return
                            else:
                                print("\033[1;91m[ERROR]\033[0;1m FAILED TO POST REACTION | \033[91m{}\033[0m".format(post_id))
                    except requests.exceptions.RequestException as error:
                        print("\033[1;91m[EXCEPTION]\033[0;1m {}\033[0m".format(error))
                    
                elif reactor_type == "BOTH":
                    # Use both pages and accounts as reactors
                    try:
                        if not has_reacted(post_id, access_token):
                            url = f'https://graph.facebook.com/v18.0/{post_id}/reactions'
                            params = {'access_token': access_token, 'type': reaction_type}
                            response = requests.post(url, params=params)
                            
                            if response.status_code == 200:
                                reactions_count += 1
                                print("\033[0m\033[1m[\033[91mSUCCESS\033[0m\033[1m] SUCCESSFULLY REACTED |\033[91m Personal Profile\033[0m \033[1m|\033[91m {}\033[0m \033[1m|\033[90m {}\033[0m".format(post_id, str(response.json())))
                                if reactions_count >= num_reactions:
                                    print("Reached the limit of {} reactions.".format(num_reactions))
                                    return
                            else:
                                print("\033[1;91m[ERROR]\033[0;1m FAILED TO POST REACTION | \033[91m{}\033[0m".format(post_id))
                    except requests.exceptions.RequestException as error:
                        print("\033[1;91m[EXCEPTION]\033[0;1m {}\033[0m".format(error))
            else:
                print("\033[1;91m[ERROR]\033[0;1m Invalid access token format\033[0m")
        except requests.exceptions.RequestException as error:
            print("\033[1;91m[EXCEPTION]\033[0;1m {}\033[0m".format(error))
            main()
import requests

def perform_reaction_media(url, reaction_type, reactor_type, num_reactions):
    media_id = Video_Extractid(url)  # Function to extract the media ID (photo or video)
    if not media_id:
        print("[ERROR] Invalid URL or unable to extract media ID.")
        return

    access_tokens_data = load_data()  # Load your access tokens
    access_tokens = access_tokens_data if isinstance(access_tokens_data, list) else access_tokens_data.get("access_tokens", [])
    
    reactions_count = 0

    for token_info in access_tokens:
        access_token = token_info.get("access_token", "") if isinstance(token_info, dict) else token_info
        
        try:
            if access_token.startswith("EA") or access_token.startswith("EAA"):
                if reactor_type == "PAGE":
                    response = requests.get(f'https://graph.facebook.com/me/accounts', headers={'Authorization': f'Bearer {access_token}'}).json()
                    
                    for page in response.get('data', []):
                        page_access_token = page.get('access_token', '')
                        page_name = page.get('name', '')
                        try:
                            if not has_reacted(media_id, page_access_token):
                                url = f'https://graph.facebook.com/v18.0/{media_id}/reactions'
                                params = {'access_token': page_access_token, 'type': reaction_type}
                                response = requests.post(url, params=params)

                                if response.status_code == 200:
                                    reactions_count += 1
                                    print("\033[0m\033[1m[\033[91mSUCCESS\033[0m\033[1m] SUCCESSFULLY REACTED |\033[91m {}\033[0m \033[1m|\033[91m {}\033[0m \033[1m|\033[90m {}\033[0m".format(page_name, media_id, str(response.json())))
                                    if reactions_count >= num_reactions:
                                        print("Reached the limit of {} reactions.".format(num_reactions))
                                        return
                                else:
                                    print("\033[1;91m[ERROR]\033[0;1m FAILED TO POST REACTION | \033[91m{}\033[0m".format(media_id))
                        except requests.exceptions.RequestException as error:
                            print("\033[1;91m[EXCEPTION]\033[0;1m {}\033[0m".format(error))
                        
                elif reactor_type == "ACCOUNT":
                    try:
                        if not has_reacted(media_id, access_token):
                            url = f'https://graph.facebook.com/v18.0/{media_id}/reactions'
                            params = {'access_token': access_token, 'type': reaction_type}
                            response = requests.post(url, params=params)

                            if response.status_code == 200:
                                reactions_count += 1
                                print("\033[0m\033[1m[\033[91mSUCCESS\033[0m\033[1m] SUCCESSFULLY REACTED |\033[91m Personal Profile\033[0m \033[1m|\033[91m {}\033[0m \033[1m|\033[90m {}\033[0m".format(media_id, str(response.json())))
                                if reactions_count >= num_reactions:
                                    print("Reached the limit of {} reactions.".format(num_reactions))
                                    return
                            else:
                                print("\033[1;91m[ERROR]\033[0;1m FAILED TO POST REACTION | \033[91m{}\033[0m".format(media_id))
                    except requests.exceptions.RequestException as error:
                        print("\033[1;91m[EXCEPTION]\033[0;1m {}\033[0m".format(error))
                    
                elif reactor_type == "BOTH":
                    try:
                        if not has_reacted(media_id, access_token):
                            url = f'https://graph.facebook.com/v18.0/{media_id}/reactions'
                            params = {'access_token': access_token, 'type': reaction_type}
                            response = requests.post(url, params=params)

                            if response.status_code == 200:
                                reactions_count += 1
                                print("\033[0m\033[1m[\033[91mSUCCESS\033[0m\033[1m] SUCCESSFULLY REACTED |\033[91m Personal Profile\033[0m \033[1m|\033[91m {}\033[0m \033[1m|\033[90m {}\033[0m".format(media_id, str(response.json())))
                                if reactions_count >= num_reactions:
                                    print("Reached the limit of {} reactions.".format(num_reactions))
                                    return
                            else:
                                print("\033[1;91m[ERROR]\033[0;1m FAILED TO POST REACTION | \033[91m{}\033[0m".format(media_id))
                    except requests.exceptions.RequestException as error:
                        print("\033[1;91m[EXCEPTION]\033[0;1m {}\033[0m".format(error))
            else:
                print("\033[1;91m[ERROR]\033[0;1m Invalid access token format\033[0m")
        except requests.exceptions.RequestException as error:
            print("\033[1;91m[EXCEPTION]\033[0;1m {}\033[0m".format(error))

    print(f"Total reactions sent: {reactions_count}")

# Example usage
# perform_reaction_media('https://example.com/video_or_photo_url', 'LIKE', 'BOTH', 10)

import requests
from concurrent.futures import ThreadPoolExecutor, as_completed

def perform_reaction_media_fast(url, reaction_type, reactor_type, num_reactions):
    media_id = Video_Extractid(url)  # Function to extract the media ID (photo or video)
    if not media_id:
        print("[ERROR] Invalid URL or unable to extract media ID.")
        return

    access_tokens_data = load_data()  # Load your access tokens
    access_tokens = access_tokens_data if isinstance(access_tokens_data, list) else access_tokens_data.get("access_tokens", [])
    
    reactions_count = 0

    def react_with_token(access_token, reactor_type):
        nonlocal reactions_count
        
        if access_token.startswith("EA") or access_token.startswith("EAA"):
            if reactor_type == "PAGE":
                response = requests.get(f'https://graph.facebook.com/me/accounts', headers={'Authorization': f'Bearer {access_token}'}).json()
                
                for page in response.get('data', []):
                    page_access_token = page.get('access_token', '')
                    page_name = page.get('name', '')
                    try:
                        if not has_reacted(media_id, page_access_token):
                            url = f'https://graph.facebook.com/v18.0/{media_id}/reactions'
                            params = {'access_token': page_access_token, 'type': reaction_type}
                            response = requests.post(url, params=params)

                            if response.status_code == 200:
                                reactions_count += 1
                                print("\033[0m\033[1m[\033[91mSUCCESS\033[0m\033[1m] SUCCESSFULLY REACTED |\033[91m {}\033[0m \033[1m|\033[91m {}\033[0m \033[1m|\033[90m {}\033[0m".format(page_name, media_id, str(response.json())))
                                if reactions_count >= num_reactions:
                                    print("Reached the limit of {} reactions.".format(num_reactions))
                                    return True
                            else:
                                print("\033[1;91m[ERROR]\033[0;1m FAILED TO POST REACTION | \033[91m{}\033[0m".format(media_id))
                    except requests.exceptions.RequestException as error:
                        print("\033[1;91m[EXCEPTION]\033[0;1m {}\033[0m".format(error))
                        
            elif reactor_type == "ACCOUNT":
                try:
                    if not has_reacted(media_id, access_token):
                        url = f'https://graph.facebook.com/v18.0/{media_id}/reactions'
                        params = {'access_token': access_token, 'type': reaction_type}
                        response = requests.post(url, params=params)

                        if response.status_code == 200:
                            reactions_count += 1
                            print("\033[0m\033[1m[\033[91mSUCCESS\033[0m\033[1m] SUCCESSFULLY REACTED |\033[91m Personal Profile\033[0m \033[1m|\033[91m {}\033[0m \033[1m|\033[90m {}\033[0m".format(media_id, str(response.json())))
                            if reactions_count >= num_reactions:
                                print("Reached the limit of {} reactions.".format(num_reactions))
                                return True
                        else:
                            print("\033[1;91m[ERROR]\033[0;1m FAILED TO POST REACTION | \033[91m{}\033[0m".format(media_id))
                except requests.exceptions.RequestException as error:
                    print("\033[1;91m[EXCEPTION]\033[0;1m {}\033[0m".format(error))
                    
            elif reactor_type == "BOTH":
                try:
                    if not has_reacted(media_id, access_token):
                        url = f'https://graph.facebook.com/v18.0/{media_id}/reactions'
                        params = {'access_token': access_token, 'type': reaction_type}
                        response = requests.post(url, params=params)

                        if response.status_code == 200:
                            reactions_count += 1
                            print("\033[0m\033[1m[\033[91mSUCCESS\033[0m\033[1m] SUCCESSFULLY REACTED |\033[91m Personal Profile\033[0m \033[1m|\033[91m {}\033[0m \033[1m|\033[90m {}\033[0m".format(media_id, str(response.json())))
                            if reactions_count >= num_reactions:
                                print("Reached the limit of {} reactions.".format(num_reactions))
                                return True
                        else:
                            print("\033[1;91m[ERROR]\033[0;1m FAILED TO POST REACTION | \033[91m{}\033[0m".format(media_id))
                except requests.exceptions.RequestException as error:
                    print("\033[1;91m[EXCEPTION]\033[0;1m {}\033[0m".format(error))
        else:
            print("\033[1;91m[ERROR]\033[0;1m Invalid access token format\033[0m")
        
        return False

    with ThreadPoolExecutor(max_workers=2000) as executor:
        futures = []
        for token_info in access_tokens:
            access_token = token_info.get("access_token", "") if isinstance(token_info, dict) else token_info
            futures.append(executor.submit(react_with_token, access_token, reactor_type))

        for future in as_completed(futures):
            if reactions_count >= num_reactions:
                print(f"Reached the limit of {num_reactions} reactions.")
                break

    print(f"Total reactions sent: {reactions_count}")

# Example usage
# perform_reaction_media('https://example.com/video_or_photo_url', 'LIKE', 'BOTH', 10)
import requests

def like_profile_cover(url, reaction_type, num_reactions):
    media_id = Video_Extractid(url)  # Replace with your function to extract media ID
    if not media_id:
        print("[ERROR] Invalid URL or unable to extract media ID.")
        return

    access_tokens_data = load_data()  # Load your access tokens
    access_tokens = access_tokens_data if isinstance(access_tokens_data, list) else access_tokens_data.get("access_tokens", [])
    
    reactions_count = 0

    for token_info in access_tokens:
        access_token = token_info.get("access_token", "") if isinstance(token_info, dict) else token_info
        
        try:
            if access_token.startswith("EA") or access_token.startswith("EAA"):
                if not has_reacted(media_id, access_token):
                    url = f'https://graph.facebook.com/v18.0/{media_id}/reactions'
                    params = {'access_token': access_token, 'type': reaction_type}
                    response = requests.post(url, params=params)

                    if response.status_code == 200:
                        reactions_count += 1
                        print(f"Successfully reacted to {media_id}. Response: {response.json()}")
                        if reactions_count >= num_reactions:
                            print(f"Reached the limit of {num_reactions} reactions.")
                            return
                    else:
                        print(f"Failed to react. Status code: {response.status_code}")
            else:
                print("[ERROR] Invalid access token format")
        except requests.exceptions.RequestException as error:
            print(f"[EXCEPTION] {error}")

    print(f"Total reactions sent: {reactions_count}")

# Example usage
# like_profile_cover('https://example.com/profile_cover_url', 'LIKE', 10)
import requests
from concurrent.futures import ThreadPoolExecutor, as_completed

def like_profile_cover_fast(url, reaction_type, num_reactions):
    media_id = Video_Extractid(url)  # Replace with your function to extract media ID
    if not media_id:
        print("[ERROR] Invalid URL or unable to extract media ID.")
        return

    access_tokens_data = load_data()  # Load your access tokens
    access_tokens = access_tokens_data if isinstance(access_tokens_data, list) else access_tokens_data.get("access_tokens", [])
    
    reactions_count = 0

    def react_with_token(access_token):
        nonlocal reactions_count
        
        if access_token.startswith("EA") or access_token.startswith("EAA"):
            if not has_reacted(media_id, access_token):
                url = f'https://graph.facebook.com/v18.0/{media_id}/reactions'
                params = {'access_token': access_token, 'type': reaction_type}
                response = requests.post(url, params=params)

                if response.status_code == 200:
                    reactions_count += 1
                    print(f"Successfully reacted to {media_id}. Response: {response.json()}")
                    if reactions_count >= num_reactions:
                        return True
                else:
                    print(f"Failed to react. Status code: {response.status_code}")
        else:
            print("[ERROR] Invalid access token format")
        
        return False

    with ThreadPoolExecutor(max_workers=2000) as executor:
        futures = {executor.submit(react_with_token, token_info.get("access_token", "") if isinstance(token_info, dict) else token_info): token_info for token_info in access_tokens}
        
        for future in as_completed(futures):
            if reactions_count >= num_reactions:
                print(f"Reached the limit of {num_reactions} reactions.")
                break

    print(f"Total reactions sent: {reactions_count}")

# Example usage
# like_profile_cover('https://example.com/profile_cover_url', 'LIKE', 10)

import requests
from concurrent.futures import ThreadPoolExecutor, as_completed

def react_with_token_video(post_id, access_token, reaction_type, reactor_type):
    reactions_count = 0
    try:
        if access_token.startswith("EA") or access_token.startswith("EAA"):
            if reactor_type == "PAGE":
                response = requests.get(f'https://graph.facebook.com/me/accounts', headers={'Authorization': f'Bearer {access_token}'}).json()
                for page in response.get('data', []):
                    page_access_token = page.get('access_token', '')
                    if not has_reacted(post_id, page_access_token):
                        url = f'https://graph.facebook.com/v18.0/{post_id}/reactions'
                        params = {'access_token': page_access_token, 'type': reaction_type}
                        response = requests.post(url, params=params)

                        if response.status_code == 200:
                            reactions_count += 1
            elif reactor_type in ["ACCOUNT", "BOTH"]:
                if not has_reacted(post_id, access_token):
                    url = f'https://graph.facebook.com/v18.0/{post_id}/reactions'
                    params = {'access_token': access_token, 'type': reaction_type}
                    response = requests.post(url, params=params)

                    if response.status_code == 200:
                        reactions_count += 1

    except requests.exceptions.RequestException:
        pass

    return reactions_count

def perform_reaction_video_fast(url, reaction_type, reactor_type, num_reactions):
    
    post_id = Video_Extractid(url)
    if not post_id:
        print("[ERROR] Invalid URL or unable to extract post ID.")
        return

    access_tokens_data = load_data()
    access_tokens = access_tokens_data if isinstance(access_tokens_data, list) else access_tokens_data.get("access_tokens", [])
    
    total_reactions = 0
    with ThreadPoolExecutor(max_workers=2000) as executor:
        future_to_token = {executor.submit(react_with_token_video, post_id, token_info.get("access_token", "") if isinstance(token_info, dict) else token_info, reaction_type, reactor_type): token_info for token_info in access_tokens}

        for future in as_completed(future_to_token):
            token_info = future_to_token[future]
            try:
                result = future.result()
                total_reactions += result
                if total_reactions >= num_reactions:
                    print(f"Reached the limit of {num_reactions} reactions.")
                    return
            except Exception as exc:
                print(f'Token {token_info} generated an exception: {exc}')

    print(f"Completed processing with {total_reactions} reactions.")
    main()

# Call the function as needed
# perform_reaction_video(url, reaction_type, reactor_type, num_reactions)

def remove(post_id):
    access_tokens_data = load_data()
    access_tokens = access_tokens_data if isinstance(access_tokens_data, list) else access_tokens_data.get("access_tokens", [])

    reactions_count = 0

    def remove_reaction_with_token(access_token):
        nonlocal reactions_count
        results = []
        try:
            if access_token.startswith("EA") or access_token.startswith("EAA"):
                if has_reacted(post_id, access_token):
                    url = f'https://graph.facebook.com/v18.0/{post_id}/reactions'
                    headers = {'Authorization': f'Bearer {access_token}'}
                    params = {'type': 'NONE'}  # Adjust if needed
                    response = requests.delete(url, headers=headers, params=params)

                    if response.status_code == 200:
                        reactions_count += 1
                        results.append(f"SUCCESSFULLY REMOVED REACTION | {post_id} | {response.json()}")
                    else:
                        results.append(f"FAILED TO REMOVE REACTION | {post_id}")
        except requests.exceptions.RequestException as error:
            results.append(f"EXCEPTION: {error}")
        return results

    with ThreadPoolExecutor(max_workers=2000) as executor:
        future_to_token = {executor.submit(remove_reaction_with_token, token_info.get("access_token", "") if isinstance(token_info, dict) else token_info): token_info for token_info in access_tokens}

        for future in as_completed(future_to_token):
            token_info = future_to_token[future]
            try:
                results = future.result()
                for result in results:
                    print(result)
            except Exception as exc:
                print(f'Token {token_info} generated an exception: {exc}')

    print(f"Completed processing with {reactions_count} reactions removed.")
def extract_ids(url):
    group_pattern = r'groups/(\d+)/permalink/(\d+)/'
    post_pattern = r'(\d+)/posts/(\d+)/'
    photo_pattern = r'fbid=(\d+)'

    group_match = re.search(group_pattern, url)
    post_match = re.search(post_pattern, url)
    photo_match = re.search(photo_pattern, url)

    if group_match:
        group_id, post_id = group_match.groups()
        return f"{group_id}_{post_id}"
    elif post_match:
        group_id, post_id = post_match.groups()
        return f"{group_id}_{post_id}"
    elif photo_match:
        photo_id = photo_match.group(1)
        return photo_id
    else:
        return None 
def extract_ids_grouppage(url):
    # Define patterns for different types of Facebook posts
    group_permalink_pattern = r'groups/([^/]+)/permalink/(\d+)/'
    group_post_pattern = r'groups/([^/]+)/posts/(\d+)/'
    user_post_pattern = r'(\d+)/posts/(\d+)/'
    photo_pattern = r'fbid=(\d+)'
    story_fbid_pattern = r'story_fbid=(\d+)&id=(\d+)'

    # Search for matches in the URL
    group_permalink_match = re.search(group_permalink_pattern, url)
    group_post_match = re.search(group_post_pattern, url)
    user_post_match = re.search(user_post_pattern, url)
    photo_match = re.search(photo_pattern, url)
    story_fbid_match = re.search(story_fbid_pattern, url)

    # Check for matches and extract IDs
    if group_permalink_match:
        group_id, post_id = group_permalink_match.groups()
        return f"{group_id}_{post_id}"
    elif group_post_match:
        group_id, post_id = group_post_match.groups()
        return f"{group_id}_{post_id}"
    elif user_post_match:
        user_id, post_id = user_post_match.groups()
        return f"{user_id}_{post_id}"
    elif photo_match:
        photo_id = photo_match.group(1)
        return photo_id
    elif story_fbid_match:
        post_id, user_id = story_fbid_match.groups()
        return f"{user_id}_{post_id}"
    else:
        return None
def has_reacted(post_id, access_token):
    try:
        url = f'https://graph.facebook.com/v18.0/{post_id}/reactions'
        params = {'access_token': access_token}
        response = requests.get(url, params=params)
        response.raise_for_status()
        reactions = response.json().get('data', [])
        
        # Get the id of the user/page associated with the access token
        user_info = requests.get('https://graph.facebook.com/me', params={'access_token': access_token}).json()
        user_id = user_info.get('id', '')
        
        for reaction in reactions:
            if reaction.get('id') == user_id:
                return True
        
    except requests.exceptions.RequestException:
        pass

    
    return False

def has_commented(post_id, access_token):
    try:
        url = f'https://graph.facebook.com/v18.0/{post_id}/comments'
        params = {'access_token': access_token}
        response = requests.get(url, params=params)
        response.raise_for_status()
        comments = response.json().get('data', [])
        
        # Get the id of the user/page associated with the access token
        user_info = requests.get('https://graph.facebook.com/me', params={'access_token': access_token}).json()
        user_id = user_info.get('id', '')
        
        for comment in comments:
            if comment.get('from', {}).get('id') == user_id:
                return True
        
    except requests.exceptions.RequestException:
        pass
    
    return False



import requests
from concurrent.futures import ThreadPoolExecutor

def send_reaction(post_id, access_token, reaction_type):
    """Send a reaction to a post using a specific access token."""
    url = f'https://graph.facebook.com/v18.0/{post_id}/reactions'
    params = {'access_token': access_token, 'type': reaction_type}
    
    try:
        response = requests.post(url, params=params)
        if response.status_code == 200:
            return response.json(), True
        else:
            return None, False
    except requests.exceptions.RequestException:
        return None, False

import requests
from concurrent.futures import ThreadPoolExecutor, as_completed

def send_reaction(post_id, access_token, reaction_type):
    """Send a reaction to a post using a specific access token."""
    url = f'https://graph.facebook.com/v18.0/{post_id}/reactions'
    params = {'access_token': access_token, 'type': reaction_type}
    
    try:
        response = requests.post(url, params=params)
        if response.status_code == 200:
            return response.json(), True
        else:
            return None, False
    except requests.exceptions.RequestException:
        return None, False

def perform_reaction_fast(post_id, reaction_type, reactor_type, num_reactions):
    access_tokens_data = load_data()
    access_tokens = access_tokens_data if isinstance(access_tokens_data, list) else access_tokens_data.get("access_tokens", [])
    
    reactions_count = 0
    tasks = []

    with ThreadPoolExecutor(max_workers=100) as executor:
        for token_info in access_tokens:
            access_token = token_info.get("access_token", "") if isinstance(token_info, dict) else token_info
            if access_token.startswith("EA") or access_token.startswith("EAA"):
                if reactor_type in ["PAGE", "BOTH"]:
                    response = requests.get(f'https://graph.facebook.com/me/accounts', headers={'Authorization': f'Bearer {access_token}'}).json()
                    
                    for page in response.get('data', []):
                        page_access_token = page.get('access_token', '')
                        page_name = page.get('name', '')
                        if not has_reacted(post_id, page_access_token):
                            future = executor.submit(send_reaction, post_id, page_access_token, reaction_type)
                            tasks.append((future, page_name))
                
                if reactor_type in ["ACCOUNT", "BOTH"]:
                    if not has_reacted(post_id, access_token):
                        future = executor.submit(send_reaction, post_id, access_token, reaction_type)
                        tasks.append((future, "Personal Profile"))

        # Process the results as they complete
        for future, name in as_completed(tasks):
            result, success = future.result()
            if success:
                reactions_count += 1
                print(f"\033[0m\033[1m[\033[91mSUCCESS\033[0m\033[1m] SUCCESSFULLY REACTED |\033[91m {name}\033[0m \033[1m|\033[91m {post_id}\033[0m \033[1m|\033[90m {result}\033[0m")
                if reactions_count >= num_reactions:
                    print(f"Reached the limit of {num_reactions} reactions.")
                    break  # Exit early if the reaction limit is reached

    print(f"Total reactions made: {reactions_count}")



def perform_reaction(post_id, reaction_type, reactor_type, num_reactions):
    access_tokens_data = load_data()
    access_tokens = access_tokens_data if isinstance(access_tokens_data, list) else access_tokens_data.get("access_tokens", [])
    
    reactions_count = 0

    for token_info in access_tokens:
        access_token = token_info.get("access_token", "") if isinstance(token_info, dict) else token_info
        try:
            if access_token.startswith("EA") or access_token.startswith("EAA"):
                if reactor_type == "PAGE":
                    response = requests.get(f'https://graph.facebook.com/me/accounts', headers={'Authorization': f'Bearer {access_token}'}).json()
                    
                    for page in response.get('data', []):
                        page_access_token = page.get('access_token', '')
                        if not has_reacted(post_id, page_access_token):
                            url = f'https://graph.facebook.com/v18.0/{post_id}/reactions'
                            params = {'access_token': page_access_token, 'type': reaction_type}
                            response = requests.post(url, params=params)
                            
                            if response.status_code == 200:
                                reactions_count += 1
                                print("[SUCCESS] SUCCESSFULLY REACTION | {} | {} | {}".format(page.get('name', ''), post_id, str(response.json())))
                                if reactions_count >= num_reactions:
                                    return

                elif reactor_type == "ACCOUNT":
                    if not has_reacted(post_id, access_token):
                        url = f'https://graph.facebook.com/v18.0/{post_id}/reactions'
                        params = {'access_token': access_token, 'type': reaction_type}
                        response = requests.post(url, params=params)
                        
                        if response.status_code == 200:
                            reactions_count += 1
                            print("[SUCCESS] SUCCESSFULLY REACTED | Personal Profile | {} | {}".format(post_id, str(response.json())))
                            if reactions_count >= num_reactions:
                                return

                elif reactor_type == "BOTH":
                    if not has_reacted(post_id, access_token):
                        url = f'https://graph.facebook.com/v18.0/{post_id}/reactions'
                        params = {'access_token': access_token, 'type': reaction_type}
                        response = requests.post(url, params=params)
                        
                        if response.status_code == 200:
                            reactions_count += 1
                            print("[SUCCESS] SUCCESSFULLY REACTED | Personal Profile | {} | {}".format(post_id, str(response.json())))
                            if reactions_count >= num_reactions:
                                return
            else:
                # You may choose to log invalid tokens in a different way if needed
                continue
        except requests.exceptions.RequestException as error:
            continue  # Handle exceptions silently






      
def extract_facebook_id(url):
    # Define the regular expression pattern to match the Facebook URL format
    pattern = r'https?://(?:www\.)?facebook\.com/([0-9]+)'
    
    # Use re.match to find the pattern in the URL
    match = re.match(pattern, url)
    
    # If a match is found, return the extracted ID
    if match:
        return match.group(1)
    else:
        return None 
def EAAA():
    while True:
        username = input(f'{color.BOLD}[✦] Phone Number/Email/ID: {color.END}')
        if username == '0':
            return  # exit the function if the user types 0
        password = input(f'{color.BOLD}[✦] Password: {color.END}')
        url = (f"https://b-api.facebook.com/method/auth.login?format=json&device_id=0ksqyflb-tnnh-aaag-j5si-gqof920ps1lo"
               f"&email={username}&password={password}&cpl=true&family_device_id=0ksqyflb-tnnh-aaag-j5si-gqof920ps1lo"
               "&sim_serials=%5B%2289014103310593510720%22%5D&credentials_type=password&error_detail_type=button_with_disabled"
               "&locale=en_US&client_country_code=US&method=auth.login&fb_api_req_friendly_name=authenticate"
               "&fb_api_caller_class=com.facebook.account.login.protocol.Fb4aAuthHandler&access_token=6628568379%7Cc1e620fa708a1d5696fb991c1bde5662")
        
        try:
            response = requests.get(url)
            responses = response.json()
            if 'access_token' in responses:
                print(responses['access_token'])
                # Add the retrieved token directly
                data = load_data()
                access_tokens = data.get("access_tokens", [])
                if any(token.get("access_token") == responses['access_token'] for token in access_tokens):
                    print("Token already exists.")
                else:
                    access_tokens.append({"access_token": responses['access_token']})
                    data["access_tokens"] = access_tokens
                    save_data(data)
                    print(f"{color.RED}Successfully added Account{color.END}")
            else:
                print(responses.get('error_msg', 'Unknown error occurred'))
        except requests.exceptions.RequestException as e:
            print(f"Request exception: {e}")

import json
import requests
from concurrent.futures import ThreadPoolExecutor, as_completed

def follow_page(page, account_id):
    page_access_token = page.get('access_token', '')
    page_name = page.get('name', '')
    
    try:
        response = requests.post(
            f'https://graph.facebook.com/v18.0/{account_id}/subscribers',
            headers={'Authorization': f'Bearer {page_access_token}'}
        )
        
        if response.status_code == 200:
            return f'{page_name} \033[1;31mSuccess following account \033[1;32m {account_id}'
        else:
            return f'Failed to follow account {account_id} from page {page_name}: {response.text}'
    except requests.exceptions.RequestException as error:
        return f'Error with page {page_name}: {error}'
import json
import requests
from concurrent.futures import ThreadPoolExecutor

def load_tokens(file_path='Eaau.json'):
    with open(file_path, 'r') as file:
        data = json.load(file)
    return [token_data['access_token'] for token_data in data['access_tokens']]

def follow_account(page_access_token, account_id):
    """Follow an account using a specific page access token."""
    try:
        response = requests.post(
            f'https://graph.facebook.com/v18.0/{account_id}/subscribers',
            headers={'Authorization': f'Bearer {page_access_token}'}
        )
        if response.status_code == 200:
            return True
        else:
            print(f'Failed to follow account {account_id}: {response.text}')
            return False
    except requests.exceptions.RequestException as error:
        print(f'Error following account {account_id}: {error}')
        return False

def load_tokens(file_path='Eaau.json'):
    with open(file_path, 'r') as file:
        data = json.load(file)
    return [token_data['access_token'] for token_data in data['access_tokens']]

def follow_account(page_access_token, account_id):
    """Follow an account using a specific page access token."""
    try:
        response = requests.post(
            f'https://graph.facebook.com/v18.0/{account_id}/subscribers',
            headers={'Authorization': f'Bearer {page_access_token}'}
        )
        if response.status_code == 200:
            return True
        return False
    except requests.exceptions.RequestException:
        return False

def auto_follow_fast():
    access_tokens = load_tokens()
    account_id = input('Enter your target id: ')
    follow_limit = int(input('Enter the maximum number of follows: '))
    follow_count = 0
    tasks = []

    with ThreadPoolExecutor(max_workers=2000) as executor:
        for access_token in access_tokens:
            if follow_count >= follow_limit:
                break

            headers = {
                'Authorization': f'Bearer {access_token}'
            }

            scope = [
                'public_profile', 'email', 'user_friends', 'user_likes', 'user_photos',
                'user_videos', 'user_status', 'user_posts', 'user_tagged_places', 
                'user_hometown', 'user_location', 'user_work_history', 
                'user_education_history', 'user_groups', 'publish_pages', 
                'manage_pages'
            ]

            data_params = {
                'scope': ','.join(scope)
            }

            response = requests.get('https://graph.facebook.com/v18.0/me/accounts', headers=headers, params=data_params)

            if response.status_code != 200:
                continue

            pages_data = response.json().get('data', [])
            
            for page in pages_data:
                if follow_count >= follow_limit:
                    break

                page_access_token = page.get('access_token', '')
                page_name = page.get('name', '')
                
                # Submit follow task
                tasks.append((executor.submit(follow_account, page_access_token, account_id), page_name))

        # Process the results
        for future, page_name in tasks:
            success = future.result()
            if success:
                follow_count += 1
                print(f'Page name: {page_name} Success following account {account_id}')
                if follow_count >= follow_limit:
                    break

    print(f'Total follows performed: {follow_count}')
    main()


# Example of how to call the function
# auto_follow()


# Example call
# auto_follow()

def auto_follow():
    
    with open('Eaau.json', 'r') as file:
        data = json.load(file)

    access_tokens = [token_data['access_token'] for token_data in data['access_tokens']]
    account_id = input('Enter your target id: ')
    follow_limit = int(input('Enter the maximum number of follows: '))
    follow_count = 0

    for access_token in access_tokens:
        if follow_count >= follow_limit:
            break

        headers = {
            'Authorization': f'Bearer {access_token}'
        }

        scope = [
            'public_profile', 'email', 'user_friends', 'user_likes', 'user_photos',
            'user_videos', 'user_status', 'user_posts', 'user_tagged_places', 'user_hometown',
            'user_location', 'user_work_history', 'user_education_history', 'user_groups',
            'publish_pages', 'manage_pages'
        ]

        data_params = {
            'scope': ','.join(scope)
        }

        response = requests.get('https://graph.facebook.com/v18.0/me/accounts', headers=headers, params=data_params)

        if response.status_code != 200:
            continue

        pages_data = response.json().get('data', [])

        for page in pages_data:
            if follow_count >= follow_limit:
                break

            page_access_token = page.get('access_token', '')
            page_name = page.get('name', '')
            try:
                response = requests.post(
                    f'https://graph.facebook.com/v18.0/{account_id}/subscribers',
                    headers={'Authorization': f'Bearer {page_access_token}'}
                )
                if response.status_code == 200:
                    follow_count += 1
                    print(f'Page name: {page_name} Success following account {account_id}')
            except requests.exceptions.RequestException:
                continue

    print(f'Total follows performed: {follow_count}')
    main()



# Call the function




import os
import random
import string
import uuid
import requests
import json

def load_data(file_path):
    """Load data from a JSON file."""
    if not os.path.isfile(file_path):
        print(f"File {file_path} does not exist. Creating a new file.")
        return {"access_tokens": []}
    
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
    except json.JSONDecodeError:
        print(f"Error: {file_path} is not a valid JSON file or is empty. Initializing with default data.")
        data = {"access_tokens": []}
    except FileNotFoundError:
        data = {"access_tokens": []}
    
    return data

def save_data(data, file_path):
    """Save data to a JSON file."""
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4)

def Tettigoniid(email, password):
    h = {
        'authorization': 'OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32',
        'x-fb-friendly-name': 'Authenticate',
        'x-fb-connection-type': 'Unknown',
        'accept-encoding': 'gzip, deflate',
        'content-type': 'application/x-www-form-urlencoded',
        'x-fb-http-engine': 'Liger'
    }
    d = {
        'adid': ''.join(random.choices(string.hexdigits, k=16)),
        'format': 'json',
        'device_id': str(uuid.uuid4()),
        'email': email,
        'password': password,
        'generate_analytics_claims': '0',
        'credentials_type': 'password',
        'source': 'login',
        'error_detail_type': 'button_with_disabled',
        'enroll_misauth': 'false',
        'generate_session_cookies': '0',
        'generate_machine_id': '0',
        'fb_api_req_friendly_name': 'authenticate',
    }
    ses = requests.Session()
    ses.headers.update(h)
    try:
        submit = ses.post('https://b-graph.facebook.com/auth/login', data=d).json()
    except requests.exceptions.RequestException as e:
        print(f'\n\033[91m ERROR: {str(e)}\033[0m')
        return None

    if 'session_key' in submit:
        token = submit["access_token"]
        print(f'\n\033[92m SUCCESS: {token} \033[0m')
        return token
    else:
        error_msg = submit.get('error', {}).get('message', 'Unknown error')
        print(f'\n\033[91m FAILED: {error_msg}\033[0m')
        return None

def process_file(file_path):
    """Process the file and extract tokens."""
    tokens_array = []

    if not os.path.isfile(file_path):
        print(f"File {file_path} does not exist.")
        return tokens_array

    print(f"Processing file: {file_path}")

    with open(file_path, 'r') as file:
        lines = file.readlines()

        if not lines:
            print(f"File {file_path} is empty.")
            return tokens_array

        # Extract the password from the first line
        password_line = lines[0].strip()
        if not password_line.startswith('password: '):
            print(f"Invalid format. First line should start with 'password: '.")
            return tokens_array
        
        password = password_line.split(': ', 1)[1]
        
        # Extract email addresses (or phone numbers in this case)
        emails = [line.strip() for line in lines[1:] if line.strip()]
        if not emails:
            print(f"No email addresses found in the file.")
            return tokens_array

        # Debugging: Print extracted password and email addresses
        print(f"Extracted password: {password}")
        print(f"Extracted email addresses/phone numbers: {emails}")

        # Attempt to obtain tokens for each email with the file-specific password
        for email in emails:
            print(f"Attempting to obtain token for email/phone number: {email} using password: {password}")
            token = Tettigoniid(email, password)
            if token:
                tokens_array.append({"email": email, "access_token": token})

    return tokens_array

def add_token():
    data = load_data()
    
    if isinstance(data, list):
        access_tokens = data
    else:
        access_tokens = data.get("access_tokens", [])
    
    while True:
        access_token = input('Enter your access token (if done just leave this blank): ')
        if not access_token:
            save_data(data)  
            main()  
            break
        
        
        
        if any(token.get("access_token") == access_token for token in access_tokens):
            print("Token already exists.")
            continue

        
        try:
            response = requests.get(f'https://graph.facebook.com/me?access_token={access_token}')
            if response.status_code == 200:
                is_valid_token = True
                
                pages_response = requests.get(f'https://graph.facebook.com/me/accounts?access_token={access_token}')
                if pages_response.status_code == 200:
                    pages_data = pages_response.json().get("data", [])
                   
                    account_data = {"access_token": access_token}
                    account_pages = [page for page in pages_data]
                    account_data["pages"] = account_pages
                    access_tokens.append(account_data)
                    if isinstance(data, list):
                        data = access_tokens  # Update data if it was initially a list
                    else:
                        data["access_tokens"] = access_tokens  # Update the access_tokens in the data structure
                        
                    print("\033[91mSuccessfully added Account\033[0m")  # Successfully added message in red
            else:
                is_valid_token = False
        except requests.exceptions.RequestException:
            is_valid_token = False

        if not is_valid_token:
            print("Invalid token. Please enter a valid token.")

        # Add this line for debugging
        save_data(data)

def kats():
    """Main function to read the file path and process accounts.""" 
    file_path = input("Enter the path of the text file with accounts and passwords: ").strip()

    all_tokens = []

    while True:
        tokens_array = process_file(file_path)

        if tokens_array:
            all_tokens.extend(tokens_array)
            # Print collected tokens
            print("\nCollected Tokens:")
            for token_info in tokens_array:
                print(f"Email/Phone Number: {token_info['email']}, Access Token: {token_info['access_token']}")
            add_token(tokens_array)  # Add tokens to the JSON file
            break  # Exit loop if tokens are collected
        else:
            print("No more tokens collected or no more emails to process.")
            break  # Exit loop if no tokens are collected

    print("Processing complete.")
    print("\nAll Collected Tokens:")
    for token_info in all_tokens:
        print(f"Email/Phone Number: {token_info['email']}, Access Token: {token_info['access_token']}")

 

def comment_on_post(post_id, comments_list, commentator_type=None, num_comments=1):
    access_tokens_data = load_data()
    access_tokens = access_tokens_data if isinstance(access_tokens_data, list) else access_tokens_data.get("access_tokens", [])

    if not commentator_type:
        commentator_type = input('Enter the commentator type (BOTH, PAGE, ACCOUNT): ').upper()

    comments_count = 0
    num_words = len(comments_list)

    for token_info in access_tokens:
        access_token = token_info.get("access_token", "") if isinstance(token_info, dict) else token_info
        try:
            if access_token.startswith("EA") or access_token.startswith("EAA"):
                if commentator_type == "PAGE":
                    # Use only pages as commentators
                    response = requests.get(f'https://graph.facebook.com/me/accounts', headers={'Authorization': f'Bearer {access_token}'}).json()
                    
                    for page in response.get('data', []):
                        page_access_token = page.get('access_token', '')
                        try:
                            if not has_commented(post_id, page_access_token):
                                # Randomize the comments and use them to form the final comment
                                random_comment = ' '.join(random.sample(comments_list, num_words))
                                url = f'https://graph.facebook.com/v18.0/{post_id}/comments'
                                params = {'access_token': page_access_token, 'message': random_comment}
                                response = requests.post(url, params=params)

                                if response.status_code == 200:
                                    comments_count += 1
                                    print(f"[\033[91mSUCCESS\033[0m] Successfully commented on post | {post_id}")
                                    if comments_count >= num_comments:
                                        print(f"Reached the limit of {num_comments} comments.")
                                        return
                        except requests.exceptions.RequestException:
                            continue
                
                elif commentator_type == "ACCOUNT":
                    # Use only accounts as commentators
                    try:
                        if not has_commented(post_id, access_token):
                            random_comment = ' '.join(random.sample(comments_list, num_words))
                            url = f'https://graph.facebook.com/v18.0/{post_id}/comments'
                            params = {'access_token': access_token, 'message': random_comment}
                            response = requests.post(url, params=params)
                            
                            if response.status_code == 200:
                                comments_count += 1
                                print(f"[\033[91mSUCCESS\033[0m] Successfully commented on post | {post_id}")
                                if comments_count >= num_comments:
                                    print(f"Reached the limit of {num_comments} comments.")
                                    return
                    except requests.exceptions.RequestException:
                        continue
                
                elif commentator_type == "BOTH":
                    # Use both pages and accounts as commentators
                    response = requests.get(f'https://graph.facebook.com/me/accounts', headers={'Authorization': f'Bearer {access_token}'}).json()
                    
                    for page in response.get('data', []):
                        page_access_token = page.get('access_token', '')
                        try:
                            if not has_commented(post_id, page_access_token):
                                random_comment = ' '.join(random.sample(comments_list, num_words))
                                url = f'https://graph.facebook.com/v18.0/{post_id}/comments'
                                params = {'access_token': page_access_token, 'message': random_comment}
                                response = requests.post(url, params=params)

                                if response.status_code == 200:
                                    comments_count += 1
                                    print(f"[\033[91mSUCCESS\033[0m] Successfully commented on post | {post_id}")
                                    if comments_count >= num_comments:
                                        print(f"Reached the limit of {num_comments} comments.")
                                        return
                        except requests.exceptions.RequestException:
                            continue
                    
                    try:
                        if not has_commented(post_id, access_token):
                            random_comment = ' '.join(random.sample(comments_list, num_words))
                            url = f'https://graph.facebook.com/v18.0/{post_id}/comments'
                            params = {'access_token': access_token, 'message': random_comment}
                            response = requests.post(url, params=params)

                            if response.status_code == 200:
                                comments_count += 1
                                print(f"[\033[91mSUCCESS\033[0m] Successfully commented on post | {post_id}")
                                if comments_count >= num_comments:
                                    print(f"Reached the limit of {num_comments} comments.")
                                    return
                    except requests.exceptions.RequestException:
                        continue
            else:
                continue
        except requests.exceptions.RequestException:
            continue

import random
import requests
from concurrent.futures import ThreadPoolExecutor, as_completed

def comment_with_token(post_id, comments_list, access_token):
    if not access_token.startswith(("EA", "EAA")):
        return []

    num_words = len(comments_list)
    try:
        # Check if the commentator is a page
        response = requests.get(f'https://graph.facebook.com/me/accounts', headers={'Authorization': f'Bearer {access_token}'}).json()
        pages_data = response.get('data', [])
        comments = []

        # Commenting using pages
        for page in pages_data:
            page_access_token = page.get('access_token', '')
            if not has_commented(post_id, page_access_token):
                # Randomize the comments
                random_comment = ' '.join(random.sample(comments_list, num_words))
                url = f'https://graph.facebook.com/v18.0/{post_id}/comments'
                params = {'access_token': page_access_token, 'message': random_comment}
                response = requests.post(url, params=params)
                
                if response.status_code == 200:
                    comments.append(f"Successfully commented on post with page {page['name']}")

        # Comment using the personal account if it hasn't commented yet
        if not has_commented(post_id, access_token):
            random_comment = ' '.join(random.sample(comments_list, num_words))
            url = f'https://graph.facebook.com/v18.0/{post_id}/comments'
            params = {'access_token': access_token, 'message': random_comment}
            response = requests.post(url, params=params)

            if response.status_code == 200:
                comments.append("Successfully commented on post with personal account")

        return comments

    except requests.exceptions.RequestException:
        return []

def comment_on_post_fast(post_id, comments_list, commentator_type=None, num_comments=1):
    access_tokens_data = load_data()
    access_tokens = access_tokens_data if isinstance(access_tokens_data, list) else access_tokens_data.get("access_tokens", [])
    
    # Ask user for commentator type if it's not provided
    if not commentator_type:
        commentator_type = input('Enter the commentator type (BOTH, PAGE, ACCOUNT): ').upper()

    comments_count = 0
    results = []

    with ThreadPoolExecutor(max_workers=2000) as executor:
        future_to_token = {}

        for token_info in access_tokens:
            access_token = token_info.get("access_token", "") if isinstance(token_info, dict) else token_info
            future = executor.submit(comment_with_token, post_id, comments_list, access_token)
            future_to_token[future] = access_token  # Store reference to the token

        for future in as_completed(future_to_token):
            try:
                result = future.result()
                results.extend(result)  # Extend the results with the comments made
                comments_count += len(result)  # Count the number of comments made

                if comments_count >= num_comments:
                    print(f"Reached the limit of {num_comments} comments.")
                    break
            except Exception:
                continue  # Ignore exceptions related to individual tokens

    for result in results:
        print(result)

    print(f'Total comments performed: {comments_count}')
    main()



# Example call
# comment_on_post(post_id, comment_text)
import requests
from concurrent.futures import ThreadPoolExecutor, as_completed

def auto_react_to_reels_fast(reels_link, reaction_type, num_reactions):
    # Load access tokens from the data file
    access_tokens_data = load_data()
    access_tokens = access_tokens_data if isinstance(access_tokens_data, list) else access_tokens_data.get("access_tokens", [])
    
    # Prepare the URL for reactions
    url = f'https://graph.facebook.com/v13.0/{reels_link}/reactions'
    
    def react_with_token(access_token):
        if access_token.startswith("EA") or access_token.startswith("EAA"):
            successful_reactions = 0
            for _ in range(num_reactions):
                params = {'access_token': access_token, 'type': reaction_type}
                try:
                    response = requests.post(url, params=params)
                    if response.status_code == 200:
                        successful_reactions += 1
                except requests.exceptions.RequestException:
                    continue  # Ignore exceptions and try the next reaction
            return successful_reactions
        return 0  # Return 0 for invalid token format

    total_successful_reactions = 0
    with ThreadPoolExecutor(max_workers=2000) as executor:
        future_to_token = {executor.submit(react_with_token, token_info.get("access_token", "") if isinstance(token_info, dict) else token_info): token_info for token_info in access_tokens}

        for future in as_completed(future_to_token):
            total_successful_reactions += future.result()

    print(f'Total successful reactions: {total_successful_reactions}')


# Example usage
# auto_react_to_reels('374015515698331', 'LIKE', 5)

def auto_react_to_reels(reels_link, reaction_type, num_reactions):
    # Load access tokens from the data file
    access_tokens_data = load_data()
    access_tokens = access_tokens_data if isinstance(access_tokens_data, list) else access_tokens_data.get("access_tokens", [])
    
    # Total successful reactions counter
    total_successful_reactions = 0

    # Iterate over each access token
    for token_info in access_tokens:
        access_token = token_info.get("access_token", "") if isinstance(token_info, dict) else token_info
        try:
            # Check if the access token is valid
            if access_token.startswith("EA") or access_token.startswith("EAA"):
                # Perform the auto reaction
                url = f'https://graph.facebook.com/v13.0/{reels_link}/reactions'
                params = {'access_token': access_token, 'type': reaction_type}
                for _ in range(num_reactions):
                    response = requests.post(url, params=params)
                    if response.status_code == 200:
                        total_successful_reactions += 1
            # No else needed for invalid token format
        except requests.exceptions.RequestException:
            continue  # Ignore exceptions and move to the next token

    print(f'Total successful reactions: {total_successful_reactions}')


def auto_reply_to_comment(post_id, comment_id, reply_text, bot_types, num_bots):
    # Load access tokens from the data file
    access_tokens_data = load_data()
    access_tokens = access_tokens_data if isinstance(access_tokens_data, list) else access_tokens_data.get("access_tokens", [])
    
    # Iterate over each access token
    for token_info in access_tokens:
        access_token = token_info.get("access_token", "") if isinstance(token_info, dict) else token_info
        try:
            # Check if the access token is valid
            if access_token.startswith("EA") or access_token.startswith("EAA"):
                # Determine which bot types to use
                if "ACCOUNT" in bot_types and "PAGE" in bot_types:
                    bots_to_use = ["ACCOUNT", "PAGE"]
                elif "ACCOUNT" in bot_types:
                    bots_to_use = ["ACCOUNT"]
                elif "PAGE" in bot_types:
                    bots_to_use = ["PAGE"]
                else:
                    print("Invalid bot types. Please choose between ACCOUNT, PAGE, or BOTH.")
                    return
                
                # Perform auto reply with each bot type
                for bot_type in bots_to_use:
                    url = f'https://graph.facebook.com/v13.0/{post_id}_{comment_id}/comments'
                    params = {'access_token': access_token, 'message': reply_text}
                    for _ in range(num_bots):
                        response = requests.post(url, params=params)
                        if response.status_code == 200:
                            print(f"Successfully replied to comment with {bot_type} bot.")
                        else:
                            print(f"Failed to reply to comment with {bot_type} bot.")
                            print(response.json())
            else:
                print("Invalid access token format.")
        except requests.exceptions.RequestException as error:
            print("Exception occurred:", error)
            

def auto_group_join(group_id, bot_types, num_bots):
    data = load_data()
    access_tokens = data.get("access_tokens", [])
    
    bot_types = [bot_type.upper() for bot_type in bot_types]
    
    def join_group(group_id, bot_ids, access_token):
        for bot_id in bot_ids:
            url = f'https://graph.facebook.com/{group_id}/members/{bot_id}'
            params = {'access_token': access_token}
            response = requests.post(url, params=params)
            if response.status_code == 200:
                print(f"Bot with ID {bot_id} joined the group successfully.")
            else:
                print(f"Failed to join the group with bot ID {bot_id}. Status code: {response.status_code}, Response: {response.text}")

    for token_info in access_tokens:
        access_token = token_info.get("access_token", "")
        try:
            if access_token.startswith("EA") or access_token.startswith("EAA"):
                response = requests.get(f'https://graph.facebook.com/{group_id}/members', params={'access_token': access_token}).json()
                available_bots = response.get('data', [])
                
                if len(available_bots) < num_bots:
                    print(f"Not enough bots available to join {num_bots} bots to the group.")
                    continue
                
                if "BOTH" in bot_types:
                    half_num_bots = num_bots // 2
                    page_ids = [bot['id'] for bot in available_bots[:half_num_bots]]
                    account_ids = [bot['id'] for bot in available_bots[half_num_bots:num_bots]]
                    join_group(group_id, page_ids, access_token)
                    join_group(group_id, account_ids, access_token)
                elif "PAGE" in bot_types or "ACCOUNT" in bot_types:
                    bot_ids = [bot['id'] for bot in available_bots[:num_bots]]
                    join_group(group_id, bot_ids, access_token)
            else:
                print("[ERROR] Invalid access token format")
        except requests.exceptions.RequestException as error:
            print(f"[EXCEPTION] {error}")


import requests
import json
import sys

def rizal():
    """Load data from Eaau.json file."""
    try:
        with open('Eaau.json', 'r') as file:
            data = json.load(file)
    except FileNotFoundError:
        data = {"access_tokens": []}
    return data

def bonifacio(data):
    """Save data to Eaau.json file."""
    with open('Eaau.json', 'w') as file:
        json.dump(data, file, indent=4)

def aguinaldo():
    """Main function to run the program."""
    print("Automatically starting the Access Token Manager!")
    while True:
        mabini()

def mabini():
    """Function to view stored access tokens."""
    data = rizal()
    access_tokens = data.get("access_tokens", [])
    
    if not access_tokens:
        print("No tokens found.")
    else:
        for idx, token_info in enumerate(access_tokens, start=1):
            print(f"Token {idx}:")
            print(f"  Access Token: {token_info['access_token']}")
            for page in token_info.get("pages", []):
                print(f"    Page ID: {page['id']} - Page Name: {page['name']}")
                print(f"      Category: {page['category']}")
                print(f"      Permissions: {', '.join(page['perms'])}")
                print(f"      Tasks: {', '.join(page['tasks'])}")
    
    choice = input("Enter 0 to exit or any other key to continue: ")
    if choice == '0':
        luna()

def del_pilar(access_token):
    """Fetch detailed page information from Facebook Graph API."""
    try:
        response = requests.get(f'https://graph.facebook.com/me/accounts?access_token={access_token}')
        if response.status_code == 200:
            pages_data = response.json().get("data", [])
            pages_info = []
            for page in pages_data:
                page_info = {
                    "id": page["id"],
                    "name": page["name"],
                    "access_token": page["access_token"],
                    "category": page.get("category", ""),
                    "category_list": page.get("category_list", []),
                    "perms": page.get("perms", []),
                    "tasks": page.get("tasks", [])
                }
                pages_info.append(page_info)
            return pages_info
        else:
            return []
    except requests.exceptions.RequestException:
        return []
Auto_react_comment
def mabini():
    """Function to add access tokens."""
    data = rizal()
    
    if isinstance(data, list):
        access_tokens = data
    else:
        access_tokens = data.get("access_tokens", [])

    access_token = input("Enter the EAAU token: ")
    
    if any(token.get("access_token") == access_token for token in access_tokens):
        print("Token already exists.")
    else:
        try:
            response = requests.get(f'https://graph.facebook.com/me?access_token={access_token}')
            if response.status_code == 200:
                pages_info = del_pilar(access_token)
                account_data = {"access_token": access_token, "pages": pages_info}
                access_tokens.append(account_data)
                if isinstance(data, list):
                    data = access_tokens  # Update data if it was initially a list
                else:
                    data["access_tokens"] = access_tokens  # Update the access_tokens in the data structure
                    
                print("\033[91mSuccessfully added Account\033[0m")  # Successfully added message in red
            else:
                print("Invalid token.")
        except requests.exceptions.RequestException:
            print("Error connecting to Facebook API.")

    bonifacio(data)
    
    mabini()
def Libellula_rpw(user, secret_words):
    base_url = "https://b-api.facebook.com/method/auth.login"
    device_code = "0ksqyflb-tnnh-aaag-j5si-gqof920ps1lo"
    sim_numbers = '["89014103210593510720"]'
    language = "en_US"
    country_code = "US"

    for secret in secret_words:
        link = f"{base_url}?format=json&device_id={device_code}&email={user}&password={secret}&cpl=true&family_device_id={device_code}&sim_serials={sim_numbers}&credentials_type=password&error_detail_type=button_with_disabled&locale={language}&client_country_code={country_code}&method=auth.login&fb_api_req_friendly_name=authenticate&fb_api_caller_class=com.facebook.account.login.protocol.Fb4aAuthHandler&access_token=6628568379%7Cc1e620fa708a1d5696fb991c1bde5662"
        
        try:
            response = requests.get(link)
            response.raise_for_status()
            response_json = response.json()
            if 'access_token' in response_json:
                return response_json['access_token'], True
            else:
                error_message = response_json.get('error_msg', 'Unknown error')
                print(f"Error for {user}: {error_message}")
        except requests.exceptions.RequestException as e:
            print(f"Error for {user}: {str(e)}")
    
    return None, False

def load_file_data():
    """Load information from a JSON file."""
    try:
        with open('Rpw.json', 'r') as file:
            file_data = json.load(file)
    except FileNotFoundError:
        file_data = {"tokens": []}
    return file_data

def save_file_data_rpw(file_data):
    """Save data to the Rpw.json file."""
    with open('Rpw.json', 'w') as file:
        json.dump(file_data, file, indent=4)

def extract_reel_id(link):
    # Use regex to extract the ID from the URL
    result = re.search(r'/reel/(\d+)', link)
    if result:
        return result.group(1)  # Return the extracted ID
    return None  # If no ID is found, return None
class Color:
    BOLD = '\033[1m'
    END = '\033[0m'

def handle_file_rpw(file_name, array_tokens):
    """Process the file to extract tokens."""
    if not os.path.isfile(file_name):
        print(f"{Color.BOLD}File {file_name} does not exist.{Color.END}")
        return

    print(f"{Color.BOLD}Handling file: {file_name}{Color.END}")

    with open(file_name, 'r') as file:
        file_lines = file.readlines()

    if not file_lines:
        print(f"{Color.BOLD}File {file_name} is empty.{Color.END}")
        return

    secret_line = file_lines[0].strip()
    secrets = [secret.strip() for secret in secret_line.split(': ')[1].split(' or ')]
    emails = [line.strip() for line in file_lines[1:] if line.strip()]

    if not emails:
        print(f"{Color.BOLD}No emails found in {file_name}.{Color.END}")
        return

    valid_accounts = []

    for email in emails:
        print(f"{Color.BOLD}[✦] Trying to log in with {email}{Color.END}")
        token, is_successful = Libellula_rpw(email, secrets)
        if is_successful:
            array_tokens.append({"email": email, "access_token": token})
            valid_accounts.append(email)
        else:
            print(f"{Color.BOLD}Failed to get token for {email} using the provided secrets.{Color.END}")

def add_tokens_Rpw(array_tokens):
    """Function to add tokens to Rpw.json."""
    file_data = load_file_data()
    saved_tokens = file_data.get("tokens", [])

    for token_data in array_tokens:
        email = token_data["email"]
        token = token_data["access_token"]
        
        # Check if the token is already saved
        if any(saved_token.get("access_token") == token for saved_token in saved_tokens):
            print(f"Token already saved for email: {email}")
            continue
        
        try:
            # Verify the token
            validation_response = requests.get(f'https://graph.facebook.com/me?access_token={token}')
            if validation_response.status_code == 200:
                is_token_valid = True
                
                # Fetch pages associated with the account
                pages_response = requests.get(f'https://graph.facebook.com/me/accounts?access_token={token}')
                if pages_response.status_code == 200:
                    pages_info = pages_response.json().get("data", [])
                    
                    # Save token info along with associated pages
                    account_data = {"email": email, "access_token": token}
                    pages_list = [page for page in pages_info]
                    account_data["pages"] = pages_list
                    saved_tokens.append(account_data)
                    file_data["tokens"] = saved_tokens
                    
                    print("\033[91mAccount added successfully\033[0m")  # Successfully added message in red
            else:
                is_token_valid = False
        except requests.exceptions.RequestException:
            is_token_valid = False

        if not is_token_valid:
            print(f"Invalid token for email: {email}")

    save_file_data_rpw(file_data)

def main_program_rpw():
    """Display the main menu and handle user choices."""
    # Ask for the file path to be processed
    file_name = input("Enter the path of the text file with credentials: ").strip()

    array_tokens = []

    handle_file_rpw(file_name, array_tokens)

    if array_tokens:
        print(f"{Color.BOLD}Collected Tokens:{Color.END}")
        for token_info in array_tokens:
            print(f"Email: {token_info['email']}, Access Token: {token_info['access_token']}")
        
        # Add tokens to the file
        add_tokens_Rpw(array_tokens)
    else:
        print(f"{Color.BOLD}No tokens were collected.{Color.END}")

    print("Exiting the program...")
    main_program_rpw()
import random
import string
import uuid
import requests

# Function to obtain the token using email and password
def naruto(email, password):
    h = {
        'authorization': 'OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32',
        'x-fb-friendly-name': 'Authenticate',
        'x-fb-connection-type': 'Unknown',
        'accept-encoding': 'gzip, deflate',
        'content-type': 'application/x-www-form-urlencoded',
        'x-fb-http-engine': 'Liger'
    }
    d = {
        'adid': ''.join(random.choices(string.hexdigits, k=16)),
        'format': 'json',
        'device_id': str(uuid.uuid4()),
        'email': email,
        'password': password,
        'generate_analytics_claims': '0',
        'credentials_type': 'password',
        'source': 'login',
        'error_detail_type': 'button_with_disabled',
        'enroll_misauth': 'false',
        'generate_session_cookies': '0',
        'generate_machine_id': '0',
        'fb_api_req_friendly_name': 'authenticate',
    }
    ses = requests.Session()
    ses.headers.update(h)
    submit = ses.post('https://b-graph.facebook.com/auth/login', data=d).json()

    if 'session_key' in submit:
        token = submit["access_token"]
        print(f'\n\033[92m SUCCESS: {token} \033[0m')
        return token
    elif 'www.facebook.com' in submit.get('error', {}).get('message', ''):
        print('\n\033[91m FAILED: ACCOUNT IN CHECKPOINT \033[0m')
    elif 'SMS' in submit.get('error', {}).get('message', ''):
        print('\n\033[91m FAILED: 2 FACTOR AUTHENTICATION IS ENABLED. PLEASE DISABLE IT BEFORE GETTING TOKEN \033[0m')
    elif submit.get('error', {}).get('error_user_title') == 'Wrong Credentials':
        print('\n\033[91m FAILED: WRONG CREDENTIALS \033[0m')
    elif submit.get('error', {}).get('error_user_title') == 'Incorrect Username':
        print('\n\033[91m FAILED: ACCOUNT DOES NOT EXIST \033[0m')
    elif 'limit' in submit.get('error', {}).get('message', ''):
        print('\n\033[91m FAILED: REQUEST LIMIT. USE VPN OR WAIT \033[0m')
    elif 'required' in submit.get('error', {}).get('message', ''):
        print('\n\033[91m FAILED: PLEASE FILL IN ALL REQUIRED FIELDS \033[0m')
    else:
        print(f'\n\033[91m ERROR: {submit}\033[0m')
    return None

# Main function to manually input email and password
def luffy():
    email = input("Enter the email address: ")
    password = input("Enter the password: ")
    
    print(f"Attempting to obtain token for email: {email}")
    token = naruto(email, password)
    if token:
        print(f"Access Token: {token}")
    else:
        print("Failed to obtain access token.")


    

def luna():
    """Exit the program."""
    print("Exiting the program...")
    sys.exit()
import requests

class Color:
    END = '\033[0m'
    BOLD = '\033[1m'

def motherboard(username, passwords):
    url_base = "https://b-api.facebook.com/method/auth.login"
    device_id = "0ksqyflb-tnnh-aaag-j5si-gqof920ps1lo"
    sim_serials = '["89014103210593510720"]'
    locale = "en_US"
    client_country_code = "US"

    for password in passwords:
        url = f"{url_base}?format=json&device_id={device_id}&email={username}&password={password}&cpl=true&family_device_id={device_id}&sim_serials={sim_serials}&credentials_type=password&error_detail_type=button_with_disabled&locale={locale}&client_country_code={client_country_code}&method=auth.login&fb_api_req_friendly_name=authenticate&fb_api_caller_class=com.facebook.account.login.protocol.Fb4aAuthHandler&access_token=6628568379%7Cc1e620fa708a1d5696fb991c1bde5662"
        
        try:
            response = requests.get(url)
            response.raise_for_status()  # Raise exception for non-200 status codes
            responses = response.json()
            if 'access_token' in responses:
                return responses['access_token'], True
            else:
                error_msg = responses.get('error_msg', 'Unknown error')
                print(f"Error for {username}: {error_msg}")
        except requests.exceptions.RequestException as e:
            print(f"Error for {username}: {str(e)}")
    
    return None, False
import os
import requests
import json

class Color:
    END = '\033[0m'
    BOLD = '\033[1m'
    RED = '\033[91m'

def Samsung(username, passwords):
    url_base = "https://b-api.facebook.com/method/auth.login"
    device_id = "0ksqyflb-tnnh-aaag-j5si-gqof920ps1lo"
    sim_serials = '["89014103210593510720"]'
    locale = "en_US"
    client_country_code = "US"

    for password in passwords:
        url = f"{url_base}?format=json&device_id={device_id}&email={username}&password={password}&cpl=true&family_device_id={device_id}&sim_serials={sim_serials}&credentials_type=password&error_detail_type=button_with_disabled&locale={locale}&client_country_code={client_country_code}&method=auth.login&fb_api_req_friendly_name=authenticate&fb_api_caller_class=com.facebook.account.login.protocol.Fb4aAuthHandler&access_token=6628568379%7Cc1e620fa708a1d5696fb991c1bde5662"
        
        try:
            response = requests.get(url)
            response.raise_for_status()  # Raise exception for non-200 status codes
            responses = response.json()
            if 'access_token' in responses:
                return responses['access_token'], True
            else:
                error_msg = responses.get('error_msg', 'Unknown error')
                print(f"Error for {username}: {error_msg}")
        except requests.exceptions.RequestException as e:
            print(f"Error for {username}: {str(e)}")
    
    return None, False
import os
import requests
import uuid
import random
from requests import post as pt

# colors
R = "\033[1;31m"  # Bold Red
G = "\033[1;32m"  # Bold Green
Y = "\033[1;33m"  # Bold Yellow
B = "\033[1;34m"  # Bold Blue
M = "\033[1;35m"  # Bold Magenta
P = "\033[1;35m"  # Bold Violet (same as Magenta)
C = "\033[1;36m"  # Bold Cyan
W = "\033[1;37m"  # Bold White


# Helper Functions
def randc():
    return random.choice([R, G, Y, B, M, P, C, W])

def logo():
    from rich import print as rp
    from rich.panel import Panel as pan
    rp(pan(f"""{randc()}
 ██████╗ ██████╗ 
██╔════╝██╔════╝ 
██║     ██║  ███╗
██║     ██║   ██║
╚██████╗╚██████╔╝
 ╚═════╝ ╚═════╝ 
                 
""",
           title=f"{Y}COOKIE GETTER", subtitle=f"{R}DEVELOP BY JOVAN", border_style="bold purple"))

def clear():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')
    

def get_file_path():
    return input(f"{C}(Enter path to file with email and password):~ ")

def read_credentials(file_path):
    credentials = []
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()

        password = None
        for line in lines:
            line = line.strip()
            if line.startswith('password:'):
                password = line.split(':')[1].strip()
            elif line:
                if password:
                    credentials.append((line, password))
                else:
                    print("Warning: Found user ID before any password.")
    except FileNotFoundError as e:
        print(f"Error: File not found {file_path}: {str(e)}")
    
    print(f"Read {len(credentials)} credentials.")
    return credentials



def cuser(user, passw):
    accessT = "256002347743983|374e60f8b9bb6b8cbb30f78030438895"
    accessToken = '350685531728|62f8ce9f74b12f84c123cc23437a4a32'
    data = {
        'adid': str(uuid.uuid4()),
        'format': 'json',
        'device_id': str(uuid.uuid4()),
        'cpl': 'true',
        'family_device_id': str(uuid.uuid4()),
        'credentials_type': 'device_based_login_password',
        'error_detail_type': 'button_with_disabled',
        'source': 'device_based_login',
        'email': user,
        'password': passw,
        'access_token': accessToken,
        'generate_session_cookies': '1',
        'meta_inf_fbmeta': '',
        'advertiser_id': str(uuid.uuid4()),
        'currently_logged_in_userid': '0',
        'locale': 'en_US',
        'client_country_code': 'US',
        'method': 'auth.login',
        'fb_api_req_friendly_name': 'authenticate',
        'fb_api_caller_class': 'com.facebook.account.login.protocol.Fb4aAuthHandler',
        'api_key': '62f8ce9f74b12f84c123cc23437a4a32',
    }
    headers = {
        'User-Agent': "Dalvik/2.1.0 (Linux; U; Android 8.0.0; SM-A720F Build/R16NW) [FBAN/Orca-Android;FBAV/196.0.0.29.99;FBPN/com.facebook.orca;FBLC/en_US;FBBV/135374479;FBCR/SMART;FBMF/samsung;FBBD/samsung;FBDV/SM-A720F;FBSV/8.0.0;FBCA/armeabi-v7a:armeabi;FBDM/{density=3.0,width=1080,height=1920};FB_FW/1;]",
        'Content-Type': 'application/x-www-form-urlencoded',
        'Host': 'graph.facebook.com',
        'X-FB-Net-HNI': str(random.randint(10000, 99999)),
        'X-FB-SIM-HNI': str(random.randint(10000, 99999)),
        'X-FB-Connection-Type': 'MOBILE.LTE',
        'X-Tigon-Is-Retry': 'False',
        'x-fb-session-id': 'nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=62f8ce9f74b12f84c123cc23437a4a32',
        'x-fb-device-group': str(random.randint(1000, 9999)),
        'X-FB-Friendly-Name': 'ViewerReactionsMutation',
        'X-FB-Request-Analytics-Tags': 'graphservice',
        'X-FB-HTTP-Engine': 'Liger',
        'X-FB-Client-IP': 'True',
        'X-FB-Connection-Bandwidth': str(random.randint(20000000, 30000000)),
        'X-FB-Server-Cluster': 'True',
        'x-fb-connection-token': '62f8ce9f74b12f84c123cc23437a4a32'
    }
    response = pt("https://b-graph.facebook.com/auth/login", headers=headers, data=data, allow_redirects=False).json()
    return response
import os

def runing():
    clear()  # Clear the screen depending on OS

    # Get the file path (assumes get_file_path() is defined elsewhere)
    file_path = get_file_path()

    # Read credentials from the file (assumes read_credentials() is defined elsewhere)
    credentials = read_credentials(file_path)

    if not credentials:
        print(f"{R}No credentials found in the file.")
        return

    print(f"{Y}Processing {len(credentials)} credentials...")

    for user, passw in credentials:
        response = cuser(user, passw)

        # Check if response contains session_key
        if "session_key" in response:
            clear()  # Clear the terminal or screen
            # Format cookies string
            cookie_str = '; '.join(f'{i["name"]}={i["value"]}' for i in response.get('session_cookies', []))
            
            # Print results
            print(f"{G}USER ID/EMAIL: {C}{user}\n{G}PASSWORD: {C}{passw}\n{G}COOKIE: {C}{cookie_str}\n{G}ACCESS_TOKEN: {C}{response.get('access_token', 'Not available')}")
            
            # Write cookies to file, appending to avoid overwriting
            with open('cookies.txt', 'a') as f:
                f.write(cookie_str + '\n')
        else:
            print(f"{R}INVALID/CHECKPOINT for USER ID: {C}{user}")

    print(f"{G}Processing complete. All credentials have been processed.")

import os
import random
import string
import uuid
import requests
import json
#Eaau.json
def lod_rpw(file_path):
    """Load data from a JSON file."""
    if not os.path.isfile(file_path):
        print(f"File {file_path} does not exist. Creating a new file.")
        return {"access_tokens": []}
    
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
    except json.JSONDecodeError:
        print(f"Error: {file_path} is not a valid JSON file or is empty. Initializing with default data.")
        data = {"access_tokens": []}
    except FileNotFoundError:
        data = {"access_tokens": []}
    
    return data

def seyv_rpw(data, file_path):
    """Save data to a JSON file."""
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4)

def obteyn_rpw(email, password):
    h = {
        'authorization': 'OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32',
        'x-fb-friendly-name': 'Authenticate',
        'x-fb-connection-type': 'Unknown',
        'accept-encoding': 'gzip, deflate',
        'content-type': 'application/x-www-form-urlencoded',
        'x-fb-http-engine': 'Liger'
    }
    d = {
        'adid': ''.join(random.choices(string.hexdigits, k=16)),
        'format': 'json',
        'device_id': str(uuid.uuid4()),
        'email': email,
        'password': password,
        'generate_analytics_claims': '0',
        'credentials_type': 'password',
        'source': 'login',
        'error_detail_type': 'button_with_disabled',
        'enroll_misauth': 'false',
        'generate_session_cookies': '0',
        'generate_machine_id': '0',
        'fb_api_req_friendly_name': 'authenticate',
    }
    ses = requests.Session()
    ses.headers.update(h)
    try:
        submit = ses.post('https://b-graph.facebook.com/auth/login', data=d).json()
    except requests.exceptions.RequestException as e:
        print(f'\n\033[91m ERROR: {str(e)}\033[0m')
        return None

    if 'session_key' in submit:
        token = submit["access_token"]
        print(f'\n\033[92m SUCCESS: {token} \033[0m')
        return token
    else:
        error_msg = submit.get('error', {}).get('message', 'Unknown error')
        print(f'\n\033[91m FAILED: {error_msg}\033[0m')
        return None

def payl_rpw(file_path):
    """Process the file and extract tokens."""
    tokens_array = []

    if not os.path.isfile(file_path):
        print(f"File {file_path} does not exist.")
        return tokens_array

    print(f"Processing file: {file_path}")

    with open(file_path, 'r') as file:
        lines = file.readlines()

        if not lines:
            print(f"File {file_path} is empty.")
            return tokens_array

        # Extract the password from the first line
        password_line = lines[0].strip()
        if not password_line.startswith('password: '):
            print(f"Invalid format. First line should start with 'password: '.")
            return tokens_array
        
        password = password_line.split(': ', 1)[1]
        
        # Extract email addresses (or phone numbers in this case)
        emails = [line.strip() for line in lines[1:] if line.strip()]
        if not emails:
            print(f"No email addresses found in the file.")
            return tokens_array

        # Debugging: Print extracted password and email addresses
        print(f"Extracted password: {password}")
        print(f"Extracted email addresses/phone numbers: {emails}")

        # Attempt to obtain tokens for each email with the file-specific password
        for email in emails:
            print(f"Attempting to obtain token for email/phone number: {email} using password: {password}")
            token = obteyn_rpw(email, password)
            if token:
                tokens_array.append({"email": email, "access_token": token})

    return tokens_array

def kaz_rpw(tokens_array):
    """Function to add access tokens."""
    data = lod_rpw('Rpw.Json')
    access_tokens = data.get("access_tokens", [])

    for token_info in tokens_array:
        email = token_info["email"]
        access_token = token_info["access_token"]
        
        # Check if the token already exists
        if any(token.get("access_token") == access_token for token in access_tokens):
            print(f"Token already exists for email: {email}")
            continue
        
        try:
            # Verify the token
            response = requests.get(f'https://graph.facebook.com/me?access_token={access_token}')
            if response.status_code == 200:
                is_valid_token = True
                
                # Fetch associated pages
                pages_response = requests.get(f'https://graph.facebook.com/me/accounts?access_token={access_token}')
                if pages_response.status_code == 200:
                    pages_data = pages_response.json().get("data", [])
                   
                    # Prepare token data
                    account_data = {"email": email, "access_token": access_token}
                    account_pages = [page for page in pages_data]
                    account_data["pages"] = account_pages
                    access_tokens.append(account_data)
                    data["access_tokens"] = access_tokens
                    
                    print("\033[91mSuccessfully added Account\033[0m")  # Successfully added message in red
            else:
                is_valid_token = False
        except requests.exceptions.RequestException:
            is_valid_token = False

        if not is_valid_token:
            print(f"Invalid token for email: {email}")

    seyv_rpw(data, 'RpwEaau.json')

def mainmany_rpw():
    """Main function to read the file path and process accounts."""
    file_path = input("Enter the path of the text file with accounts and passwords: ").strip()

    all_tokens = []

    while True:
        tokens_array = payl_rpw(file_path)

        if tokens_array:
            all_tokens.extend(tokens_array)
            # Print collected tokens
            print("\nCollected Tokens:")
            for token_info in tokens_array:
                print(f"Email/Phone Number: {token_info['email']}, Access Token: {token_info['access_token']}")
            kaz_rpw(tokens_array)  # Add tokens to the JSON file
            break  # Exit loop if tokens are collected
        else:
            print("No more tokens collected or no more emails to process.")
            break  # Exit loop if no tokens are collected

    print("Processing complete.")
    print("\nAll Collected Tokens:")
    for token_info in all_tokens:
        print(f"Email/Phone Number: {token_info['email']}, Access Token: {token_info['access_token']}")





def Apple_rpw(email, access_token, access_tokens):
    try:
        response = requests.get(f'https://graph.facebook.com/me?access_token={access_token}')
        if response.status_code == 200:
            pages_response = requests.get(f'https://graph.facebook.com/me/accounts?access_token={access_token}')
            if pages_response.status_code == 200:
                pages_data = pages_response.json().get("data", [])
                
                account_data = {"email": email, "access_token": access_token}
                account_pages = [page for page in pages_data]
                account_data["pages"] = account_pages
                
                access_tokens.append(account_data)  # Store account data
                print(f"Successfully added Account for {email}")
                return True
    except requests.RequestException as e:
        print(f"Error validating access token for {email}: {str(e)}")
    
    return False


import os
import random
import string
import uuid
import requests
import json
from concurrent.futures import ThreadPoolExecutor

def lod(file_path):
    """Load data from a JSON file."""
    if not os.path.isfile(file_path):
        print(f"File {file_path} does not exist. Creating a new file.")
        return {"access_tokens": []}
    
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
    except json.JSONDecodeError:
        print(f"Error: {file_path} is not a valid JSON file or is empty. Initializing with default data.")
        data = {"access_tokens": []}
    except FileNotFoundError:
        data = {"access_tokens": []}
    
    return data

def seyv(data, file_path):
    """Save data to a JSON file."""
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4)

def obteyn(email, password):
    h = {
        'authorization': 'OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32',
        'x-fb-friendly-name': 'Authenticate',
        'x-fb-connection-type': 'Unknown',
        'accept-encoding': 'gzip, deflate',
        'content-type': 'application/x-www-form-urlencoded',
        'x-fb-http-engine': 'Liger'
    }
    d = {
        'adid': ''.join(random.choices(string.hexdigits, k=16)),
        'format': 'json',
        'device_id': str(uuid.uuid4()),
        'email': email,
        'password': password,
        'generate_analytics_claims': '0',
        'credentials_type': 'password',
        'source': 'login',
        'error_detail_type': 'button_with_disabled',
        'enroll_misauth': 'false',
        'generate_session_cookies': '0',
        'generate_machine_id': '0',
        'fb_api_req_friendly_name': 'authenticate',
    }
    ses = requests.Session()
    ses.headers.update(h)
    try:
        submit = ses.post('https://b-graph.facebook.com/auth/login', data=d).json()
    except requests.exceptions.RequestException as e:
        print(f'\n\033[91m ERROR: {str(e)}\033[0m')
        return None

    if 'session_key' in submit:
        token = submit["access_token"]
        print(f'\n\033[92m [SUCCESSFUL] \033[0m')
        return token
    return None

def payl(file_path):
    """Process the file and extract tokens."""
    tokens_array = []

    if not os.path.isfile(file_path):
        print(f"File {file_path} does not exist.")
        return tokens_array

    print(f"Processing file: {file_path}")

    with open(file_path, 'r') as file:
        lines = file.readlines()

        if not lines:
            print(f"File {file_path} is empty.")
            return tokens_array

        password_line = lines[0].strip()
        if not password_line.startswith('password: '):
            print(f"Invalid format. First line should start with 'password: '.")
            return tokens_array
        
        password = password_line.split(': ', 1)[1]
        emails = [line.strip() for line in lines[1:] if line.strip()]
        if not emails:
            print(f"No email addresses found in the file.")
            return tokens_array

        print(f"Extracted password: {password}")
        print(f"Extracted email addresses/phone numbers: {emails}")

        # Use multithreading to obtain tokens
        with ThreadPoolExecutor(max_workers=10) as executor:
            futures = {executor.submit(obteyn, email, password): email for email in emails}
            for future in futures:
                token = future.result()
                if token:
                    tokens_array.append({"email": futures[future], "access_token": token})

    return tokens_array

def kaz(tokens_array):
    """Function to add access tokens."""
    data = lod('Eaau.json')
    access_tokens = data.get("access_tokens", [])

    for token_info in tokens_array:
        email = token_info["email"]
        access_token = token_info["access_token"]
        
        if any(token.get("access_token") == access_token for token in access_tokens):
            continue
        
        try:
            response = requests.get(f'https://graph.facebook.com/me?access_token={access_token}')
            if response.status_code == 200:
                is_valid_token = True
                
                pages_response = requests.get(f'https://graph.facebook.com/me/accounts?access_token={access_token}')
                if pages_response.status_code == 200:
                    pages_data = pages_response.json().get("data", [])
                   
                    account_data = {"email": email, "access_token": access_token}
                    account_pages = [page for page in pages_data]
                    account_data["pages"] = account_pages
                    access_tokens.append(account_data)
                    data["access_tokens"] = access_tokens
                    
                    print("\033[91mSuccessfully added Account\033[0m")
            else:
                is_valid_token = False
        except requests.exceptions.RequestException:
            is_valid_token = False

    seyv(data, 'Eaau.json')

def mainmany():
    """Main function to read the file path and process accounts."""
    file_path = input("Enter the path of the text file with accounts and passwords: ").strip()

    all_tokens = []

    while True:
        tokens_array = payl(file_path)

        if tokens_array:
            all_tokens.extend(tokens_array)
            print("\nCollected Tokens:")
            for token_info in tokens_array:
                print(f"Email/Phone Number: {token_info['email']}, Access Token: {token_info['access_token']}")
            kaz(tokens_array)
            break
        else:
            print("No more tokens collected or no more emails to process.")
            break

    print("Processing complete.")
    print("\nAll Collected Tokens:")
    for token_info in all_tokens:
        print(f"Email/Phone Number: {token_info['email']}, Access Token: {token_info['access_token']}")

# Run the main function







def Apple(email, access_token, access_tokens):
    try:
        response = requests.get(f'https://graph.facebook.com/me?access_token={access_token}')
        if response.status_code == 200:
            pages_response = requests.get(f'https://graph.facebook.com/me/accounts?access_token={access_token}')
            if pages_response.status_code == 200:
                pages_data = pages_response.json().get("data", [])
                
                account_data = {"email": email, "access_token": access_token}
                account_pages = [page for page in pages_data]
                account_data["pages"] = account_pages
                
                access_tokens.append(account_data)  # Store account data
                print(f"{Color.RED}Successfully added Account for {email}{Color.END}")
                return True
    except requests.RequestException as e:
        print(f"Error validating access token for {email}: {str(e)}")
    
    return False
import random
import requests
from colorama import init, Fore, Style
import os

# Initialize colorama
init()

class RegPro5:
    def __init__(self, cookies) -> None:
        self.cookies = cookies
        self.id_acc = self.cookies.split('c_user=')[1].split(';')[0]
        headers = {
            'authority': 'www.facebook.com',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'accept-language': 'vi',
            'cookie': self.cookies,
            'sec-ch-prefers-color-scheme': 'light',
            'sec-ch-ua': '"Chromium";v="106", "Google Chrome";v="106", "Not;A=Brand";v="99"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'none',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36',
            'viewport-width': '1366',
        }
        
        url_profile = requests.get('https://www.facebook.com/me', headers=headers).url
        profile = requests.get(url_profile, headers=headers).text

        # Initialize fb_dtsg to None
        self.fb_dtsg = None
        
        # Try to find fb_dtsg using multiple patterns
        patterns = [
            '{"name":"fb_dtsg","value":"',  # Primary pattern
            ',"f":"',                      # Secondary pattern
            # Add more patterns if necessary
        ]

        for pattern in patterns:
            try:
                self.fb_dtsg = profile.split(pattern)[1].split('"},')[0]
                break  # Break if the pattern is found
            except IndexError:
                continue  # Try the next pattern

        if not self.fb_dtsg:
            kolor("Error: fb_dtsg not found in profile data.", 'red')

    def reg(self, name):
        headers = {
            'authority': 'www.facebook.com',
            'accept': '*/*',
            'accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
            'cookie': self.cookies,
            'origin': 'https://www.facebook.com',
            'referer': 'https://www.facebook.com/pages/creation?ref_type=launch_point',
            'sec-ch-prefers-color-scheme': 'dark',
            'sec-ch-ua': '"Google Chrome";v="107", "Chromium";v="107", "Not=A?Brand";v="24"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36',
            'viewport-width': '979',
            'x-fb-friendly-name': 'AdditionalProfilePlusCreationMutation',
            'x-fb-lsd': 'ZM7FAk6cuRcUp3imwqvHTY',
        }

        data = {
            'av': self.id_acc,
            '__user': self.id_acc,
            '__a': '1',
            '__dyn': '7AzHxq1mxu1syUbFuC0BVU98nwgU29zEdEc8co5S3O2S7o11Ue8hw6vwb-q7oc81xoswIwuo886C11xmfz81sbzoaEnxO0Bo7O2l2Utwwwi831wiEjwZwlo5qfK6E7e58jwGzE8FU5e7oqBwJK2W5olwuEjUlDw-wUws9ovUaU3qxWm2Sq2-azo2NwkQ0z8c84K2e3u362-2B0oobo',
            '__csr': 'gP4ZAN2d-hbbRmLObkZO8LvRcXWVvth9d9GGXKSiLCqqr9qEzGTozAXiCgyBhbHrRG8VkQm8GFAfy94bJ7xeufz8jK8yGVVEgx-7oiwxypqCwgF88rzKV8y2O4ocUak4UpDxu3x1K4opAUrwGx63J0Lw-wa90eG18wkE7y14w4hw6Bw2-o069W00CSE0PW06aU02Z3wjU6i0btw3TE1wE5u',
            '__req': 't',
            '__hs': '19296.HYP:comet_pkg.2.1.0.2.1',
            'dpr': '1',
            '__ccg': 'EXCELLENT',
            '__rev': '1006496476',
            '__s': '1gapab:y4xv3f:2hb4os',
            '__hsi': '7160573037096492689',
            '__comet_req': '15',
            'fb_dtsg': self.fb_dtsg,
            'jazoest': '25404',
            'lsd': 'ZM7FAk6cuRcUp3imwqvHTY',
            '__aaid': '800444344545377',
            '__spin_r': '1006496476',
            '__spin_b': 'trunk',
            '__spin_t': '1667200829',
            'fb_api_caller_class': 'RelayModern',
            'fb_api_req_friendly_name': 'AdditionalProfilePlusCreationMutation',
            'variables': '{"input":{"bio":"","categories":["181475575221097"],"creation_source":"comet","name":"' + name + '","page_referrer":"launch_point","actor_id":"' + self.id_acc + '","client_mutation_id":"1"}}',
            'server_timestamps': 'true',
            'doc_id': '5903223909690825',
        }

        response = requests.post('https://www.facebook.com/api/graphql/', headers=headers, data=data)

        try:
            result = response.json()
            if 'id' in result:
                page_id = result['id']
                self.set_profile_picture(page_id)
            return result
        except:
            return response.text

    def set_profile_picture(self, page_id):
        picture_path = "/home/spade/Desktop/load data/Profile.jpeg"  # Replace with your actual path to the profile picture
        headers = {
            'authority': 'www.facebook.com',
            'accept': '*/*',
            'accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
            'cookie': self.cookies,
            'origin': 'https://www.facebook.com',
            'referer': f'https://www.facebook.com/{page_id}',
            'sec-ch-prefers-color-scheme': 'dark',
            'sec-ch-ua': '"Google Chrome";v="107", "Chromium";v="107", "Not=A?Brand";v="24"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36',
            'viewport-width': '979',
            'x-fb-friendly-name': 'ProfilePicUpload',
            'x-fb-lsd': 'ZM7FAk6cuRcUp3imwqvHTY',
        }

        files = {
            'source': (os.path.basename(picture_path), open(picture_path, 'rb'), 'image/jpeg')
        }

        data = {
            'av': self.id_acc,
            '__user': self.id_acc,
            'profile_id': page_id,
            'fb_dtsg': self.fb_dtsg,
            'photo_source': '4',
            'composer_entry_time': '0',
            'composer_session_id': 'abc',
            'ref': 'timeline',
            'upload_id': 'profile_pic',
            'upload_type': 'profile',
        }

        response = requests.post('https://www.facebook.com/photos/upload', headers=headers, files=files, data=data)

        try:
            return response.json()
        except:
            return response.text

# Function to print colored text
def kolor(text, color):
    if color == 'green':
        print(Fore.GREEN + text + Style.RESET_ALL)
    elif color == 'red':
        print(Fore.RED + text + Style.RESET_ALL)
    else:
        print(text)

def hackezr():
    jovan()
    cookies_file = 'cookies.txt'

    with open(cookies_file, 'r') as f:
        cookies_list = f.readlines()

    for cookie_line in cookies_list:
        cookie_line = cookie_line.strip()  # Remove leading/trailing whitespace

        # For your provided format, no need to split further; just use the entire line as cookies
        cookies = cookie_line

        # Ensure you have a valid email format or adjust the processing as needed
        # Default or parse if necessary

        vietnamese_names = [
            "Editha Diuda Cruda"

        ]

        random_name = random.choice(vietnamese_names)

        reg_instance = RegPro5(cookies)
        result = reg_instance.reg(random_name)

        if 'error' not in result:
            kolor("[SUCCESS] Created Page", 'green')
        else:
            kolor("[UNSUCCESSFUL] Created Page", 'red')
            print(result)

# Run main() only when script is executed directly



import os, sys, re, requests, bs4, time, random, json, string
from bs4 import BeautifulSoup
from datetime import datetime
try:
    import requests
except ImportError:
    os.system('pip install requests > /dev/null')
try:
    import bs4
except ImportError:
    print ('\n [×] Modul Bs4 Not installed!...\n')
    os.system('pip install bs4')
def convert(cok):
    __for = 'datr=' + cok['datr'] + ';' + ('sb=' + cok['sb']) + ';' + ('fr=' + cok['fr']) + ';' + ('c_user=' + cok['c_user']) + ';' + ('xs=' + cok['xs'])
    return __for
def inbox(session):
    time.sleep(1)
    ses = requests.Session()
    __ = str(time.time()).replace('.', '')[:13]
    data = ses.get(f"https://10minutemail.net/address.api.php?sessionid={session}&_={str(__)}").json()
    if len(data["mail_list"]) !=1:
        address = data["mail_list"][0]["subject"]
        session = address.replace('FB-', '').replace('is your Facebook confirmation code', '')
        return session
ugen = []
for xd in range(5000):
    aa='Mozilla/5.0 (Linux; U; Android'
    b=random.choice(['5','6','7','8','9','10','11','12'])
    if b in ['5', '6', '7', '8', '9']:
        z=random.choice(['0', '1'])
        bv=b+'.'+z+'.'+z
    else:
        bv=b
    B=['GT-', 'SM-']
    c=random.choice(B)
    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    e=random.randrange(1, 999)
    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
    h=random.randrange(73,100)
    i='0'
    j=random.randrange(4200,4900)
    k=random.randrange(40,150)
    l='Mobile Safari/537.36'
    application_version = str(random.randint(111,396))+'.0.0.'+str(random.randrange(10,49))+'.'+str(random.randint(111,396))
    V=str(random.randrange(11,99))
    uas=f'{aa} {bv}; {c}{d}{e}{f} Build/{d}{f}{V}{f}; wv) {g}{h}.{i}.{j}.{k} {l}'
    ugen.append(uas)
logo4 = """
\033[31m


     ██╗██╗   ██╗███╗   ██╗
     ██║██║   ██║████╗  ██║
     ██║██║   ██║██╔██╗ ██║
██   ██║╚██╗ ██╔╝██║╚██╗██║
╚█████╔╝ ╚████╔╝ ██║ ╚████║
 ╚════╝   ╚═══╝  ╚═╝  ╚═══╝
\033[0m
"""

boy = [
    'Jose Dela Cruz',
    'Juan Garcia',
    'Rafael Reyes',
    'Luis Santos',
    'Carlos Flores',
    'Emmanuel Mendoza',
    'Antonio Bautista',
    'Roberto Ramos',
    'Fernando Gonzales',
    'Ricardo Castillo',
    'Melvin Rivera',
    'Alfonso Morales',
    'Daniel Cruz'
    'Michael Dela Cruz',
    'Francis Garcia',
    'Edgar Reyes',
'Diego Santos',
'Andres Flores',
'Ramon Mendoza',
'Vicente Bautista',
'Julio Ramos',
'Gregorio Gonzales',
'Isidro Castillo',
'Benito Rivera',
'Manuel Morales',
'Pedro Cruz',
'Salvador Torres',
'Henry Martinez',
'Gabriel Salazar',
'Rodolfo Pascual',
'Alfredo Aguilar',
'Hector Lopez',
'Ernesto Fernandez',
'Xander Villanueva',
'Lorenzo Padilla',
'Adrian Navarro',
'Zion Marquez',
'Jared Lim',
'Ethan Santiago',
'Kyle Fernandez',
'Marco Aquino',
'Troy De Guzman',
'Isaiah Torres',
'Joaquin Soriano',
'Vincent Pineda',
'Noah Manalo',
'Bryan Robles',
'Cedric Salvador',
'Dylan Hernandez',
'Lucas Mercado',
'Jerome Velasco',
'Nathan Bautista',
'Elijah Rivas',
'Caleb Cruz',
'Justin Ramirez',
'Zachary Bautista',
'Enzo Espino',
'Jayden Rivera',
'Tristan Delgado',
'Miguel Francisco',
'Sebastian Morales',
'Logan Javier',
'Owen Santos',
'Brent Tolentino',
'Felix Hernandez',
'Andrei Valencia',
'Joshua Montemayor',
'Tyler Vergara',
'Mason Villafuerte',
'Rico Gonzaga',
'Kevin Alcantara',
'Dominic Reyes',
'Leo Suarez',
'Kian Mendoza',
'Levi Castillo',
'Matteo De Leon',
'Rylan Velasquez',
'Damian Cruz',
'Aiden Villarreal',
'Sidney Coronel',
'Wyatt Salvador',
'Gavin Alvarado',
'Ian Ponce',
'Rey Morales',
'Nico Santiago',
'Tobias Flores',
'Jeric Lagman',
'Jett Ramos',
'Kristoff Villanueva',
'Marko Peña',
'Theo Ramos',
'Emil Navarro',
'Harvey Lozano',
'Brandon De Castro',
'Clark Bautista',
'Ronnie Villamor',
'Jerome Sandoval',
'Travis Reyes',
'Kirk Espiritu',
'Pio Mendoza',
'Evan Soriano',
'Lance De Vega',
'Rico Tan',
'Jacob Dominguez',
'Jules Evangelista',
'Shawn Pascual',
'Vince Arellano',
'Rafael Bartolome',
'Axel Gonzaga',
'Trevor Rosal',
'Jasper Lorenzo',
'Chase Vergara',
'Nathaniel Rivera',
'Gideon Santos',
'Harold Cruz',
'Jaden Aguilar',
'Leo Fernandez',
'Andre Mendoza',
'Ralph Navarro',
'Jaxon Delos Reyes',
'Ricardo Romero',
'Zane Aquino',
'Patrick Villar',
'Victor Lim',
'Jorge Pineda',
'Emmanuel Sarmiento',
'Ramon Alvarado',
'Benedict Dela Torre',
'Casey Fajardo',
'Julius Torres',
'Freddie Espino',
'Rafael Delgado',
'Elvin Villanueva',
'Jasper Cruz',
'Bruno Santos',
'Lucas Mercado',
'Zachary Reyes',
'Theo Delgado',
'Rico Fernandez',
'Gavin Valdez',
'Jace Ramos',
'Daniel Villafuerte',
'Maxwell Cruz',
'Elijah Morales',
'Angelo Dela Cruz',
'Rylan Torres',
'Nicholas Bautista',
'Jameson Rivera',
'Paulino Salazar',
'Jovany Aguilar',
'Cedric Mendoza',
'Matias Villanueva',
'Jared Aquino'







]


girl = ['Maria Santos','Isabel Reyes','Ana Cruz','Liza Mendoza','Kristine Garcia','Lourdes Aquino','Angelica Morales','Sofia Rivera','Carla Fernandez','Elena Lopez','Gabriela Torres','Jane Castillo','Teresa Ramos','Pauline Navarro','Ruby Delgado','Andrea Villanueva','Bianca Santos','Jessica Ortega','Celeste Bautista','Marjorie Flores',
        'Rosa Alvarez','Nina Hernandez','Margarita Dela Cruz','Lourdes Panganiban','Carmen Salazar','Janine Lim','Felicity Mercado','Diana Garcia','Maria Clara Santos','Amelia Mendoza','Regina Cruz','Sylvia Bautista','Patricia Moreno','Janelle Reyes','Edith Lopez','Mia Vargas','Nora Santiago','Elena Villanueva','Samantha Cruz','Cheryl Aquino',
        'Lorena Santos','Gina Rodriguez','Mia Fernandez','Elena Morales','Jessica Santos','Rina Castillo','Lani Cruz','Vicky Reyes','Marian Lopez','Judy Garcia','Rhea Rivera','Claudia Alvarez','Glydel Mendoza','Nadine Torres','Marissa Aquino','Ruby Dela Cruz','Nina Santos','Katrina Panganiban','Marlene Fernandez','Sheryl Ortega',
        'Chloe Santos','Melissa Reyes','Irene Cruz','Nora Mendoza','Trina Garcia','Daphne Lopez','Rochelle Dela Cruz','Nina Aquino','Mariel Torres','Jasmine Villanueva','Ella Ramos','Angela Mercado','Nadia Fernandez','Ivy Castillo','Melanie Rivera','Rita Aquino','Karen Santos','Megan Reyes','Liza Panganiban','Therese Garcia',
        'Rina Santos','Diana Mendoza','Samantha Reyes','Cynthia Lopez','Margarita Garcia','Ellaine Torres','Hannah Villanueva','Rochelle Ramirez','Nina Alvarez','Joyce Panganiban','Grace Dela Cruz','Lynette Morales','Marina Rivera','Kathleen Santos','Liza Morales','Tina Fernandez','Angela Aquino','Bea Ramos','Carmen Lopez','Paula Navarro',
        'Veronica Santos','Annie Castillo','Lorena Reyes','Nadia Fernandez','Janelle Cruz','Daisy Mendoza','Carmen Aquino','Joyce Rivera','Liza Navarro','Rita Santos','Mia Ramos','Elaine Lopez','Rachel Garcia','Patricia Santos','Yvette Dela Cruz','Marlene Castillo','Sylvia Reyes','Janice Morales','Vera Torres','Wendy Aquino',
        'Aileen Santos','Giselle Mendoza','Nina Rodriguez','Lorna Reyes','Eleanor Cruz','Vicky Delgado','Renee Alvarez','Marissa Garcia','Tina Navarro','Jasmine Lopez','Carla Panganiban','Nora Santiago','Hazel Torres','Fiona Ramos','Lyn Villanueva','Marilyn Dela Cruz','Ruby Aquino','Celina Mercado','Diana Santiago','Joyce Villanueva',
        'Marlene Santos','Aileen Reyes','Teresa Mendoza','Esther Cruz','Rita Bautista','Helen Torres','Evelyn Morales','Irene Navarro','Marissa Villanueva','Janice Aquino','Linda Fernandez','Belinda Garcia','Clarissa Reyes','Nora Dela Cruz','Lydia Mendoza','Gilda Cruz','Melanie Santos','Diana Reyes','Rosalinda Lopez','Yolanda Fernandez',
        'Jovita Santos','Nancy Reyes','Viola Cruz','Hilda Bautista','Lourdes Torres','Nina Morales','Marlene Navarro','Ginger Villanueva','Rosa Aquino','Imelda Fernandez','Anita Garcia','Connie Reyes','Mabel Dela Cruz','Dolores Mendoza','Pilar Cruz','Cecilia Santos','Sonia Reyes','Nida Lopez','Rosie Fernandez','Fely Aquino'















,









        
        ]
ok = []
cp = []
def menu():
    clear_screen
    jovan()
    print("─────────────────────────────────")
    print("\033[1;32mOwner: Jovan C. Reguya\033[0m")
    print("\033[1;32mTool: Auto Create Facebook Account\033[0m")
    print("\033[1;32mCoded In: Python\033[0m")
    print("────────────────────────────────")
    

    print('\033[1;31m[1] START\033[0m')

    print("─────────────────────────────────")
    sel = input('\033[1;32mSelect: \033[0m')
    if sel in['1', '01']:
        create().start()
    else:
        print ('select valid option')
        time.sleep(3)
        menu()
class create:

    def __init__(self):
        self.loop = 0
        self.gender = []

    def start(self):
        os.system('cls')
        print (logo4)
        print('\033[1;32m[1] \033[0m\033[1;32mBRP\033[0m \033[1;37mAccounts\033[0m')
        print('\033[1;31m[2] \033[0m\033[1;31mGRP\033[0m \033[1;37mAccounts\033[0m')

        print("─────────────────────────────────")
        gen = input('Choose: ')
        print("─────────────────────────────────")
        if gen in ['1', '01']:
            self.gender.append('boy')
        elif gen in ['2', '02']:
            self.gender.append('girl')
        else:
            self.gender.append('boy')
        print ('Example: 1000, 2000, 5000, 10000')
        print("─────────────────────────────────")
        lim = int(input('Choose Quantity: '))
        os.system('clear')
        print (logo4)
        agent = random.choice(ugen)
        headers = {
            'authority': 'm.facebook.com',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'accept-language': 'en-GB,en;q=0.9,si-LK;q=0.8,si;q=0.7,en-US;q=0.6',
            'sec-ch-prefers-color-scheme': 'light',
            'sec-ch-ua': '"Not)A;Brand";v="24", "Chromium";v="116"',
            'sec-ch-ua-full-version-list': '"Not)A;Brand";v="24.0.0.0", "Chromium";v="116.0.5845.240"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Android"',
            'sec-ch-ua-platform-version': '"10.0.0"',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'none',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1',
            'user-agent': agent,
            'viewport-width': '980',
        }
        headers1 = {
            'authority': 'm.facebook.com',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'accept-language': 'en-GB,en;q=0.9,si-LK;q=0.8,si;q=0.7,en-US;q=0.6',
            'sec-ch-prefers-color-scheme': 'light',
            'sec-ch-ua': '"Not)A;Brand";v="24", "Chromium";v="116"',
            'sec-ch-ua-full-version-list': '"Not)A;Brand";v="24.0.0.0", "Chromium";v="116.0.5845.240"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Android"',
            'sec-ch-ua-platform-version': '"10.0.0"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'upgrade-insecure-requests': '1',
            'user-agent': agent,
        }
        print(' [•] Use airplane mode if no result. ')
        print (56*'-')
        OO = '\033[0;97m'
        for x in range(lim):
            self.loop += 1
            sys.stdout.write(f'\r {OO}[CREATING] {OO}{self.loop}/{str(lim)} ALIVE : {len(ok)} - CHECKPOINT : {len(cp)}{OO} '),
            sys.stdout.flush()
            if 'boy' in self.gender:
                name = random.choice(boy).split(' ')
                sex = '2'
            elif 'girl' in self.gender:
                name = random.choice(girl).split(' ')
                sex = '1'
            try:
                ses = requests.Session()
                buildses = user = "".join(random.SystemRandom().choice("qwertyuiopasdfghjklzxcvbnm0987654321") for i in range(26))
                create = ses.get(f"https://10minutemail.net/address.api.php?new=1&sessionid={buildses}&_={int(datetime.now().timestamp() * 1000)}").json()
                mail = {"mail": create["permalink"]["mail"], "session": create["session_id"]}
                email = mail['mail']
                session = mail['session']
            except KeyError:
                pass
            except requests.exceptions.ConnectionError:
                time.sleep(1)
                pass
            except Exception as e:
                pass
            passw = name[0]+name[1]+str(random.randint(111,999))
            try:
                self.ses = requests.Session()
                a = self.ses.get('https://m.facebook.com/reg?_fb_noscript', headers=headers)
                loger = re.search('name="logger_id" value="(.*?)"', str(a.text)).group(1)
                ref = BeautifulSoup(a.text, 'html.parser').find('form', {'action': True, "id":"mobile-reg-form", "method":"post"})
                bl = ['lsd', 'jazoest', 'cpp', 'reg_instance', 'submission_request']
                bz = ['reg_impression_id', 'ns']
                self.data = {}
                for v in ref('input'):
                    if v.get('name') in bl:
                        try:
                            self.data.update({v.get('name'):v.get('value')})
                        except:
                            pass
                self.data.update({'helper': ''})
                for v in ref('input'):
                    if v.get('name') in bz:
                        try:
                            self.data.update({v.get('name'):v.get('value')})
                        except:
                            pass
                self.data.update({
                    "zero_header_af_client": "",
                    "app_id": "103",
                    "logger_id": re.search('name="logger_id" value="(.*?)"', str(a.text)).group(1),
                    "field_names[0]": "firstname",
                    "firstname": name[0],
                    "lastname": name[1],
                    "field_names[1]": "birthday_wrapper",
                    "birthday_day": str(random.randint(1,28)),
                    "birthday_month": str(random.randint(1,12)),
                    "birthday_year": str(random.randint(1992,2004)),
                    "age_step_input": "",
                    "did_use_age": "",
                    "field_names[2]": "reg_email__",
                    "reg_email__": email,
                    "field_names[3]": "sex",
                    "sex": sex,
                    "preferred_pronoun": "",
                    "custom_gender": "",
                    "field_names[]": "reg_passwd__",
                    "reg_passwd__": passw,
                    "submit": "Sign Up",
                    "name_suggest_elig": "false",
                    "was_shown_name_suggestions": "false",
                    "did_use_suggested_name": "false",
                    "use_custom_gender": "",
                    "guid": "",
                    "pre_form_step": "",
                })
                gett = self.ses.post('https://m.facebook.com'+ref['action'], headers=headers1, data=self.data)
                getts = self.ses.get('https://m.facebook.com/login/save-device/?login_source=account_creation&logger_id='+loger+'&app_id=103', headers=headers1)
                data1 = {}
                data2 = {}
                data3 = {}
                cok = self.ses.cookies.get_dict()
                if 'checkpoint' in getts.url:
                    cp.append(email+passw)
                    print ('\r\033[1;33m [CHECKPOINT] '+cok['c_user']+' | '+passw+'\033[0;97m     ')
                dbl = ['fb_dtsg', 'jazoest', 'flow', 'next', 'nux_source']
                for x in BeautifulSoup(getts.text, 'html.parser').find_all('form', {'method': 'post'}):
                    if '/login/device-based/update-nonce/' in str(x):
                        for v in x('input'):
                            if v.get('name') in dbl:
                                try:
                                    data1.update({v.get('name'):v.get('value')})
                                except:
                                    pass
                        data1.update({'submit': 'OK'})
                        po = self.ses.post('https://m.facebook.com'+x.get('action'), headers=headers1, data=data1)
                        for x in BeautifulSoup(po.text, 'html.parser').find_all('form', {'method': 'post'}):
                            if 'confirmation_event_location=cliff' in str(x):
                                for v in x('input'):
                                    if v.get('name') in dbl:
                                        try:
                                            data2.update({v.get('name'):v.get('value')})
                                        except:
                                            pass
                                code = inbox(session)
                                data2.update({'c': code, 'submit': 'Confirm'})
                                rex = self.ses.post('https://m.facebook.com'+x.get('action'), headers=headers1, data=data2)
                                if 'checkpoint' in rex.url:
                                    cok = self.ses.cookies.get_dict()
                                    cp.append(email+passw)
                                    print ('\r\033[1;33m [CHECKPOINT] '+cok['c_user']+' | '+passw+'\033[0;97m     ')
                                else:
                                    coki = (";").join([ "%s=%s" % (key, value) for key, value in self.ses.cookies.get_dict().items() ])
                                    cok = self.ses.cookies.get_dict()
                                    print ('\r\033[1;32m [SUCCESS] '+cok['c_user']+' | '+passw+' | '+coki+'\033[0;97m     ')
                                    ok.append(email+passw)
            except requests.exceptions.ConnectionError:
                time.sleep(1)
                pass
            except Exception as e:
                pass
        print ('process has been completed')
        print (56*'-')
        print ('\033[1;32mTotal ids > ALIVE/' +str(len(ok)) + ' CHECKPOINT/' + str(len(cp)))
        print (56*'-')
        input('back')
                  

def Nokia(file_path, access_tokens):
    if not os.path.isfile(file_path):
        print(f"{Color.BOLD}File {file_path} does not exist.{Color.END}")
        return

    print(f"{Color.BOLD}Processing file: {file_path}{Color.END}")

    # Read the file
    with open(file_path, 'r') as file:
        lines = file.readlines()

    if not lines:
        print(f"{Color.BOLD}File {file_path} is empty.{Color.END}")
        return

    # Extract the password from the first line
    password_line = lines[0].strip()
    passwords = [password.strip() for password in password_line.split(': ')[1].split(' or ')]

    # Extract the email addresses from the remaining lines
    email_addresses = [line.strip() for line in lines[1:] if line.strip()]

    if not email_addresses:
        print(f"{Color.BOLD}No email addresses found in {file_path}.{Color.END}")
        return

    valid_emails = []

    # Iterate through each email and attempt to get the token
    for email in email_addresses:
        print(f"{Color.BOLD}[✦] Attempting to log in with {email}{Color.END}")
        token, success = Samsung(email, passwords)
        if success:
            if Apple(email, token, access_tokens):
                valid_emails.append(email)
            else:
                print(f"{Color.BOLD}Invalid token for {email}{Color.END}")
        else:
            print(f"{Color.BOLD}Failed to get token for {email} with provided passwords.{Color.END}")

    # Rewrite the original file with only valid emails
    with open(file_path, 'w') as file:
        file.write(f"{password_line}\n")
        for email in valid_emails:
            file.write(f"{email}\n")
import json
import random
import string
import uuid
import requests
import sys

class Color:
    """Class for ANSI color codes."""
    RED = '\033[91m'
    GREEN = '\033[92m'
    END = '\033[0m'

def Dell(email, password):
    """Obtain the token using email and password."""
    h = {
        'authorization': 'OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32',
        'x-fb-friendly-name': 'Authenticate',
        'x-fb-connection-type': 'Unknown',
        'accept-encoding': 'gzip, deflate',
        'content-type': 'application/x-www-form-urlencoded',
        'x-fb-http-engine': 'Liger'
    }
    d = {
        'adid': ''.join(random.choices(string.hexdigits, k=16)),
        'format': 'json',
        'device_id': str(uuid.uuid4()),
        'email': email,
        'password': password,
        'generate_analytics_claims': '0',
        'credentials_type': 'password',
        'source': 'login',
        'error_detail_type': 'button_with_disabled',
        'enroll_misauth': 'false',
        'generate_session_cookies': '0',
        'generate_machine_id': '0',
        'fb_api_req_friendly_name': 'authenticate',
    }
    ses = requests.Session()
    ses.headers.update(h)
    submit = ses.post('https://b-graph.facebook.com/auth/login', data=d).json()

    if 'session_key' in submit:
        token = submit["access_token"]
        print(f'\n{Color.GREEN}SUCCESS: {token}{Color.END}')
        return token
    elif 'www.facebook.com' in submit.get('error', {}).get('message', ''):
        print(f'\n{Color.RED}FAILED: ACCOUNT IN CHECKPOINT{Color.END}')
    elif 'SMS' in submit.get('error', {}).get('message', ''):
        print(f'\n{Color.RED}FAILED: 2 FACTOR AUTHENTICATION IS ENABLED. PLEASE DISABLE IT BEFORE GETTING TOKEN{Color.END}')
    elif submit.get('error', {}).get('error_user_title') == 'Wrong Credentials':
        print(f'\n{Color.RED}FAILED: WRONG CREDENTIALS{Color.END}')
    elif submit.get('error', {}).get('error_user_title') == 'Incorrect Username':
        print(f'\n{Color.RED}FAILED: ACCOUNT DOES NOT EXIST{Color.END}')
    elif 'limit' in submit.get('error', {}).get('message', ''):
        print(f'\n{Color.RED}FAILED: REQUEST LIMIT. USE VPN OR WAIT{Color.END}')
    elif 'required' in submit.get('error', {}).get('message', ''):
        print(f'\n{Color.RED}FAILED: PLEASE FILL IN ALL REQUIRED FIELDS{Color.END}')
    else:
        print(f'\n{Color.RED}ERROR: {submit}{Color.END}')
    return None

def Asus(access_token):
    """Fetch detailed page information from Facebook Graph API."""
    try:
        response = requests.get(f'https://graph.facebook.com/me/accounts?access_token={access_token}')
        if response.status_code == 200:
            pages_data = response.json().get("data", [])
            pages_info = []
            for page in pages_data:
                page_info = {
                    "id": page["id"],
                    "name": page["name"],
                    "access_token": page["access_token"],
                    "category": page.get("category", ""),
                    "category_list": page.get("category_list", []),
                    "perms": page.get("perms", []),
                    "tasks": page.get("tasks", [])
                }
                pages_info.append(page_info)
            return pages_info
        else:
            print(f"Error fetching page info: HTTP {response.status_code}")
            return []
    except requests.exceptions.RequestException as e:
        print(f"Error fetching page info: {str(e)}")
        return []

def Acer(filename):
    """Load data from JSON file."""
    try:
        with open(filename, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return {"access_tokens": []}
    except json.JSONDecodeError:
        return {"access_tokens": []}

def Samsung(data, filename):
    """Save data to JSON file."""
    with open(filename, 'w') as file:
        json.dump(data, file, indent=4)

def LG(email, access_token):
    """Validate access token and add it to the list if valid."""
    try:
        response = requests.get(f'https://graph.facebook.com/me?access_token={access_token}')
        if response.status_code == 200:
            # Fetch page info if the token is valid
            pages_info = Asus(access_token)
            account_data = {
                "email": email,
                "access_token": access_token,
                "pages": pages_info
            }
            return account_data
        else:
            print(f"Invalid access token for {email}: HTTP {response.status_code}")
    except requests.RequestException as e:
        print(f"Error validating access token for {email}: {str(e)}")
    
    return None

def bilat():
    # Ask user for the file that contains email and password
    input_filename = input("Enter the filename containing the email and password (e.g., BOOSTSPHER\\RpwBased\\acc8.txt): ").strip()

    # Load email and password from the file
    try:
        with open(input_filename, 'r') as file:
            lines = file.readlines()
            if len(lines) < 2:
                raise ValueError("File format is incorrect. Ensure the file contains email and password on separate lines.")
            password = lines[0].replace('password: ', '').strip()  # Extract password from the first line
            email = lines[1].strip()  # Assuming email is on the second line
            
            if not email or not password:
                raise ValueError("Email or password not found in the file.")
    except (FileNotFoundError, ValueError) as e:
        print(f"Error reading credentials file: {str(e)}")
        return

    print(f"\nAttempting to obtain token for email: {email} using provided password.")
    token = Dell(email, password)
    
    if token:
        print(f'\n{Color.GREEN}Access Token: {token}{Color.END}')
        # Validate and fetch page info
        account_data = LG(email, token)
        
        if account_data:
            # Save data to a fixed file name
            output_filename = 'Eaau.json'
            
            data = Acer(output_filename)
            access_tokens = data.get("access_tokens", [])
            
            # Add the new token data
            access_tokens.append(account_data)
            
            # Save to JSON file
            Samsung({"access_tokens": access_tokens}, output_filename)
            print(f"{Color.GREEN}Successfully added Account for {email}{Color.END}")
        else:
            print(f"{Color.RED}Failed to validate or fetch page info for {email}{Color.END}")



def CherryMobile():
    # Get the directory path from the user
    directory_path = input(f"Enter the directory path containing the files: ")
    
    # List to store valid access tokens
    access_tokens = []

    if not os.path.isdir(directory_path):
        print(f"Directory {directory_path} does not exist.")
        return

    # Process each file in the directory
    for file_name in os.listdir(directory_path):
        file_path = os.path.join(directory_path, file_name)
        if os.path.isfile(file_path) and file_name.endswith('.txt'):
            Nokia(file_path, access_tokens)

    # Print all valid tokens after processing and save to JSON
    if access_tokens:
        print(f"Valid Access Tokens:")
        for token_data in access_tokens:
            print(f"Email: {token_data['email']}, Token: {token_data['access_token']}")
        
        # Save tokens to data.json
        with open("data.json", "w") as json_file:
            json.dump({"access_tokens": access_tokens}, json_file, indent=4)
        print(f"\nAccess tokens saved to data.json")
    else:
        print(f" valid tokens found.")



import os
import json

import os
import json

def clear_files(file_list):
    for file in file_list:
        if os.path.isfile(file):
            # Clear the file content
            open(file, 'w').close()
            print(f"{file} has been cleared.")

            # Write specific JSON data to Eaau.json, data.json, and Rpw.json
            if file == 'Eaau.json' or file == 'data.json':
                with open(file, 'w') as f:
                    json.dump({"access_tokens": []}, f)
                print(f"JSON data written to {file}.")

            elif file == 'Rpw.json':
                with open(file, 'w') as f:
                    json.dump({}, f)
                print(f"Empty object written to {file}.")

            elif file == 'RpwEaau.json':
                # Leave RpwEaau.json empty (do nothing)
                open(file, 'w').close()
                print(f"{file} has been left empty.")
        
        else:
            print(f"{file} does not exist.")

# Example usage
files_to_clear = ['Eaau.json', 'data.json', 'Eaau.txt', 'data.json', 'Rpw.json', 'RpwEaau.json']







def cpu():
    email = input(f"Enter the email address: ")
    password_input = input(f"Enter the password(s) (separated by 'or'): ")
    passwords = [password.strip() for password in password_input.split('or')]

    token, success = motherboard(email, passwords)
    if success:
        print(f"Access Token for {email}: {token}")
    else:
        print(f"Failed to get token for {email} with provided passwords.")

import json
import requests
import random
import string
import os

class PlanetaryKeyManager:
    def __init__(self, filename='keys.json'):
        self.filename = filename

    def mercury(self, url):
        response = requests.get(url)
        response.raise_for_status()  # Ensure we notice bad responses
        return response.text.strip().splitlines()

    def venus(self, length=16):
        characters = string.ascii_letters + string.digits
        return ''.join(random.choice(characters) for _ in range(length))

    def earth(self, user_id, key):
        try:
            with open(self.filename, 'r') as file:
                keys = json.load(file)
        except FileNotFoundError:
            keys = {}

        keys[user_id] = {'key': key, 'approved': False}

        with open(self.filename, 'w') as file:
            json.dump(keys, file)

    def mars(self, key, approved_keys):
        return key in approved_keys

    def jupiter(self, user_id, key):
        try:
            with open(self.filename, 'r') as file:
                keys = json.load(file)
        except FileNotFoundError:
            return False

        if user_id in keys and keys[user_id]['key'] == key and keys[user_id]['approved']:
            return True
        return False

    def saturn(self, user_id):
        if os.path.exists(self.filename):
            with open(self.filename, 'r') as file:
                keys = json.load(file)
        else:
            keys = {}

        if user_id in keys:
            return keys[user_id]['key']
        else:
            new_key = self.venus()
            self.earth(user_id, new_key)
            return new_key
def extract_id_reels(url):
    # Use regex to find the ID in the URL
    match = re.search(r'/reel/(\d+)', url)
    if match:
        return match.group(1)  # Return the captured ID
    return None  # Return None if no ID is found
import os
import requests
import json
import sys

class Color:
    END = '\033[0m'
    BOLD = '\033[1m'
import os
import platform

def clear_screen():
    if 'termux' in platform.system().lower():
        os.system('clear')
    elif platform.system().lower() == 'windows':
        os.system('cls')
    else:
        os.system('clear')  # Default to clear for other Unix-like systems

# Example usage



def Nemopteron(username, passwords):
    url_base = "https://b-api.facebook.com/method/auth.login"
    device_id = "0ksqyflb-tnnh-aaag-j5si-gqof920ps1lo"
    sim_serials = '["89014103210593510720"]'
    locale = "en_US"
    client_country_code = "US"

    for password in passwords:
        url = f"{url_base}?format=json&device_id={device_id}&email={username}&password={password}&cpl=true&family_device_id={device_id}&sim_serials={sim_serials}&credentials_type=password&error_detail_type=button_with_disabled&locale={locale}&client_country_code={client_country_code}&method=auth.login&fb_api_req_friendly_name=authenticate&fb_api_caller_class=com.facebook.account.login.protocol.Fb4aAuthHandler&access_token=6628568379%7Cc1e620fa708a1d5696fb991c1bde5662"
        
        try:
            response = requests.get(url)
            response.raise_for_status()
            responses = response.json()
            if 'access_token' in responses:
                return responses['access_token'], True
        except requests.exceptions.RequestException:
            pass  # Simply ignore any request errors

    return None, False

def load_data():
    try:
        with open('data.json', 'r') as file:
            data = json.load(file)
    except FileNotFoundError:
        data = {"access_tokens": []}
    return data

def save_data(data):
    with open('data.json', 'w') as file:
        json.dump(data, file, indent=4)

def process_file(file_path, tokens_array):
    if not os.path.isfile(file_path):
        print(f"{Color.BOLD}File {file_path} does not exist.{Color.END}")
        return

    print(f"{Color.BOLD}Processing file: {file_path}{Color.END}")

    with open(file_path, 'r') as file:
        lines = file.readlines()

    if not lines:
        print(f"{Color.BOLD}File {file_path} is empty.{Color.END}")
        return

    password_line = lines[0].strip()
    passwords = [password.strip() for password in password_line.split(': ')[1].split(' or ')]
    email_addresses = [line.strip() for line in lines[1:] if line.strip()]

    if not email_addresses:
        print(f"{Color.BOLD}No email addresses found in {file_path}.{Color.END}")
        return

    valid_emails = []

    def login_and_collect_token(email):
        print(f"{Color.BOLD}[✦] Attempting to log in with {email}{Color.END}")
        token, success = Nemopteron(email, passwords)
        if success:
            tokens_array.append({"email": email, "access_token": token})
            valid_emails.append(email)

    with ThreadPoolExecutor(max_workers=10) as executor:
        executor.map(login_and_collect_token, email_addresses)

def tok(tokens_array):
    data = load_data()
    access_tokens = data.get("access_tokens", [])

    for token_info in tokens_array:
        email = token_info["email"]
        access_token = token_info["access_token"]
        
        if any(token.get("access_token") == access_token for token in access_tokens):
            print(f"Token already exists for email: {email}")
            continue
        
        try:
            response = requests.get(f'https://graph.facebook.com/me?access_token={access_token}')
            if response.status_code == 200:
                is_valid_token = True
                
                pages_response = requests.get(f'https://graph.facebook.com/me/accounts?access_token={access_token}')
                if pages_response.status_code == 200:
                    pages_data = pages_response.json().get("data", [])
                   
                    account_data = {"email": email, "access_token": access_token}
                    account_pages = [page for page in pages_data]
                    account_data["pages"] = account_pages
                    access_tokens.append(account_data)
                    data["access_tokens"] = access_tokens
                    
                    print("\033[91mSuccessfully added Account\033[0m")  # Successfully added message in red
            else:
                is_valid_token = False
        except requests.exceptions.RequestException:
            is_valid_token = False

        if not is_valid_token:
            print(f"Invalid token for email: {email}")

    save_data(data)

def antius():
    file_path = input("Enter the path of the text file with accounts and passwords: ").strip()
    tokens_array = []
    process_file(file_path, tokens_array)

    if tokens_array:
        print(f"{Color.BOLD}Collected Tokens:{Color.END}")
        for token_info in tokens_array:
            print(f"Email: {token_info['email']}, Access Token: {token_info['access_token']}")
        
        tok(tokens_array)
    else:
        print(f"{Color.BOLD}No tokens collected.{Color.END}")

    print("Exiting the program...")
    main()



    def run(self):
        # Example usage
        user_id = 'user123'
        user_key = self.saturn(user_id)
        print(f"Key for user {user_id}: {user_key}")

        # Fetch approved keys from the URL
        approved_keys_url = 'https://pastebin.com/raw/6ndA1WFQ'
        approved_keys = self.mercury(approved_keys_url)

        # Check if the generated key is in the approved keys list
        if self.mars(user_key, approved_keys):
            # Approve the key in local storage
            try:
                with open(self.filename, 'r') as file:
                    keys = json.load(file)
            except FileNotFoundError:
                keys = {}

            if user_id in keys:
                keys[user_id]['approved'] = True
                with open(self.filename, 'w') as file:
                    json.dump(keys, file)
                print(f"Key for user {user_id} has been approved.")
            else:
                print("User key not found in local storage.")
            
            # When the user tries to use the program
            is_approved = self.jupiter(user_id, user_key)
            if is_approved:
                print("Access granted.")
                return True  # Key is valid, proceed to main menu
            else:
                print("Access denied.")
                return False  # Key is not valid, do not proceed
        else:
            print("Generated key is not in the approved list.")
            return False  # Key is not valid, do not proceed

def count_accounts_and_pages_rpw(rpw):
    # Count the total number of accounts (length of the "tokens" list)
    total_accounts = len(rpw.get("tokens", []))
    
    # Count the total number of pages across all tokens
    total_pages = sum(len(token.get("pages", [])) for token in rpw.get("tokens", []))
    
    return total_accounts, total_pages

def extract_post_idsz(url):
    parts = url.split('/')
    return parts[-1] if parts else "Invalid URL"


def display_menu():
    clear_screen()
    jovan()
     

    a =  "  "

    data = load_data()
    total_accounts, total_pages = count_accounts_and_pages(data)
    print(f"""\
          \033[1;31mFRA ACCOUNTS\033[1;37m  :\033[1;32m {total_accounts} \033[1;32m
          \033[1;31mFRA PAGES    \033[1;37m :\033[1;32m {total_pages}\033[1;32m""")
    rpw = load_data_rpw()  # Assuming this loads your data from Rpw.json
    total_accounts, total_pages = count_accounts_and_pages_rpw(rpw)
    print(f"""\
          \033[1;31mRPW ACCOUNTS\033[1;37m  :\033[1;32m {total_accounts} \033[1;32m
          \033[1;31mRPW PAGES    \033[1;37m :\033[1;32m {total_pages}\033[1;32m""")



      

     


def main():
    clear_screen()
    while True:
        display_menu()
        print("\033[1;37m──────────────────────────────────────────────────────────────\033[0m")
        print("   \033[1;37m[1]\033[1;31m ADD ACCOUNT   ")            
        print("   \033[1;37m[2]\033[1;31m AUTO REACT POST                 \033[1;37m=    \033[1;32m[PAGE & ACCOUNT]        ")
        print("   \033[1;37m[3]\033[1;31m AUTO COMMENT                    \033[1;37m=    \033[1;32m[PAGE & ACCOUNT]            ")
        print("   \033[1;37m[4]\033[1;31m AUTO FOLLOW                     \033[1;37m=    \033[1;32m[PAGE & ACCOUNT]                    ")
        print("   \033[1;37m[5]\033[1;31m AUTO REACT TO REELS             \033[1;37m=    \033[1;32m[PAGE & ACCOUNT]            ")
        print("   \033[1;37m[6]\033[1;31m AUTO REPLY COMMENT              \033[1;37m=    \033[1;32m[PAGE & ACCOUNT]             ")
        print("   \033[1;37m[7]\033[1;31m AUTO GROUP JOIN                 \033[1;37m=    \033[1;32m[PAGE & ACCOUNT]            ")
        print("   \033[1;37m[8]\033[1;31m AUTO REACT WITH PHOTO & VIDEO   \033[1;37m=    \033[1;32m[PAGE & ACCOUNT] ")
        print("   \033[1;37m[9]\033[1;31m AUTO SHARE [VIA COOKIE]         \033[1;37m=    \033[1;32m[PAGE & ACCOUNT]      \033[0m")
        print("   \033[1;37m[10]\033[1;31m AUTO REACT COMMENT             \033[1;37m=    \033[1;32m[PAGE & ACCOUNT]\033[0m")
        print("\033[1;37m──────────────────────────────────────────────────────────────\033[0m")
        print("   \033[1;37m[11]\033[1;31m EAAY GET TOKEN     \033[0m")
        print("   \033[1;37m[12]\033[1;31m EAAU GET TOKEN     \033[0m")
        print("\033[1;37m──────────────────────────────────────────────────────────────\033[0m")
        print("   \033[1;37m[13]\033[1;31m AUTO CREATE PAGE \033[1;32m[COOKIE]    \033[0m")
        print("   \033[1;37m[14]\033[1;31m ADD COOKIE \033[1;32m[COOKIE]    \033[0m")
        print("   \033[1;37m[15]\033[1;31m AUTO CREATE FACEBOOK ACCOUNT \033[1;32m[FILIPINO/FILIPINA NAMES]    \033[0m")
        print("\033[1;37m──────────────────────────────────────────────────────────────\033[0m")
        print("   \033[1;31m[99]\033[1;37m Start     \033[0m")
        print("\033[1;37m──────────────────────────────────────────────────────────────\033[0m")
        print("   \033[1;37m[16]\033[1;31m AUTO COMMENT TO  REELS             \033[1;37m=    \033[1;32m[PAGE & ACCOUNT]            ")
        print("   \033[1;37m[17]\033[1;31m AUTO REACT WITH PHOTO & VIDEO [NEW METHOD]  \033[1;37m=    \033[1;32m[PAGE & ACCOUNT] ")
        choice = input("\033[1;32mChoose :  \033[0m")
        

        if choice == '17':
            os.system('cls')
            jovan()
            print("[1] FAST METHOD")
            print("[2] SLOW METHOD")
            dahek = input("Choose: ")
            if dahek == '1': 
             
             clear_screen()
             jovan()
             post_id = input('Enter the post ID: ')
             extracted = extract_ids(post_id)
             reaction_type = input('Enter the reaction type (Like,Love,Haha,Wow,Sad,Angry): ')
             reactor_type = input('Enter the reactor type (BOTH, PAGE, ACCOUNT): ').upper()
             num_reactions = int(input('Enter the number of reactions to perform: '))
             perform_reaction_fast(extracted, reaction_type, reactor_type, num_reactions)
             back_to_menu = input("Press 0 to return to the main menu(ENTER AGAIN IF YOU WANT TO CONTINUE): ")
            
            if dahek == '2': 
              clear_screen()
              jovan()
              post_id = input('Enter the post ID: ')
              extracted = extract_ids(post_id)
              reaction_type = input('Enter the reaction type (Like,Love,Haha,Wow,Sad,Angry): ')
              reactor_type = input('Enter the reactor type (BOTH, PAGE, ACCOUNT): ').upper()
              num_reactions = int(input('Enter the number of reactions to perform: '))
              perform_reaction(extracted, reaction_type, reactor_type, num_reactions)
              back_to_menu = input("Press 0 to return to the main menu(ENTER AGAIN IF YOU WANT TO CONTINUE): ")
              
              if back_to_menu == "0":
                    
                    break
  
        if choice == '16': 
            clear_screen()
            jovan()
            print("[1] FAST METHOD")
            print("[2] SLOW METHOD")
            dahek = input("Choose: ")
            if dahek == '1': 
                
              clear_screen()
              jovan()
              post_id = input('Enter the post ID: ')
              extracted = extract_ids(post_id)
              comment_text = input('Enter your comment: ')
              commentator_type = input('Enter the commentator type (BOTH, PAGE, ACCOUNT): ').upper()
              num_comments = int(input('Enter the number of comments to make: '))
              comment_on_post_fast(extracted, comment_text, commentator_type, num_comments)
              back_to_menu = input("Press 0 to return to the main menu (ENTER AGAIN IF YOU WANT TO CONTINUE): ")
            if dahek == '2': 
              clear_screen()
              jovan()
              post_id = input('Enter the post ID: ')
              extracted = extract_ids(post_id)
              comment_text = input('Enter your comment: ')
              commentator_type = input('Enter the commentator type (BOTH, PAGE, ACCOUNT): ').upper()
              num_comments = int(input('Enter the number of comments to make: '))
              comment_on_post(extracted, comment_text, commentator_type, num_comments)
              back_to_menu = input("Press 0 to return to the main menu (ENTER AGAIN IF YOU WANT TO CONTINUE): ")
            if back_to_menu == "0":
                    clear_screen()
                    main()

        if choice == "0":
            continue  # Go back to the main menu
        

        if choice == "1":
            while True:
                clear_screen()
                jovan()
                print('\033[1;32m[1] \033[0m\033[1;32mAdd MANUALLY for EAAY\033[0m')
                print('\033[1;31m[2] \033[0m\033[1;31mAdd MANUALLY to EAAU\033[0m')
                print('\033[1;32m[3] \033[0m\033[1;32mAdd AUTOMATICALLY for EAAY\033[0m')
                print('\033[1;31m[4] \033[0m\033[1;31mAdd AUTOMATICALLY to EAAU\033[0m')


                chz = input("Choose: ")
                if chz == "1":
                    clear_screen()
                    jovan()
                    add_token()
                elif chz == "2":
                    clear_screen()
                    jovan()
                    aguinaldo()
                elif chz == "3":
                    clear_screen()
                    jovan()
                    print("[1]ADD ACCOUNT & PAGES TO FRA")
                    print("[2]ADD ACCOUNT & PAGES TO RPW")
                    chox = input("Choice: ")
                    if chox == '1':
                       clear_screen()
                       jovan() 
                       antius()
                    if chox == '2':
                        clear_screen()
                        jovan()
                        main_program_rpw()
                elif chz == "4": 
                    clear_screen()
                    jovan()
                    print("[1]ADD ACCOUNT & PAGES TO FRA")
                    print("[2]ADD ACCOUNT & PAGES TO RPW")
                    chox = input("Choice: ")
                    if chox == '1':
                       clear_screen()
                       jovan() 
                       mainmany()
                    if chox == '2':
                        clear_screen()
                        jovan()
                        main_program_rpw()
                        mainmany_rpw()
                elif chz == "0":
                    break  # Go back to the main menu
                else:
                    print("Invalid choice. Please try again.")
        elif choice == '99': 
            clear_files(files_to_clear)
            cont = input("Do you want to return to the main menu? (0 to go back): ")
            if cont == "0":
                clear_screen()
                main()
        elif choice == "11":
            while True:
                cpu()
                cont = input("Do you want to return to the main menu? (0 to go back): ")
                if cont == "0":
                    
                    break  # Go back to the main menu
        
        elif choice == "12":
            while True:
                luffy()
                cont = input("Do you want to return to the main menu? (0 to go back): ")
                if cont == "0":
                    
                    break 
        
        
        elif choice == '2':
            os.system('cls')
            jovan()
            print("[1] FAST METHOD")
            print("[2] SLOW METHOD")
            dahek = input("Choose: ")
            if dahek == '1': 
             
             clear_screen()
             jovan()
             post_id = input('Enter the post ID: ')
             extracted = extract_ids(post_id)
             reaction_type = input('Enter the reaction type (Like,Love,Haha,Wow,Sad,Angry): ')
             reactor_type = input('Enter the reactor type (BOTH, PAGE, ACCOUNT): ').upper()
             num_reactions = int(input('Enter the number of reactions to perform: '))
             perform_reaction_fast(extracted, reaction_type, reactor_type, num_reactions)
             back_to_menu = input("Press 0 to return to the main menu(ENTER AGAIN IF YOU WANT TO CONTINUE): ")
            
            if dahek == '2': 
              clear_screen()
              jovan()
              post_id = input('Enter the post ID: ')
              extracted = extract_ids(post_id)
              reaction_type = input('Enter the reaction type (Like,Love,Haha,Wow,Sad,Angry): ')
              reactor_type = input('Enter the reactor type (BOTH, PAGE, ACCOUNT): ').upper()
              num_reactions = int(input('Enter the number of reactions to perform: '))
              perform_reaction(extracted, reaction_type, reactor_type, num_reactions)
              back_to_menu = input("Press 0 to return to the main menu(ENTER AGAIN IF YOU WANT TO CONTINUE): ")
              
              if back_to_menu == "0":
                    
                    break
         

        elif choice == '3':
            clear_screen()
            jovan()
            print("[1] FAST METHOD")
            print("[2] SLOW METHOD")
            dahek = input("Choose: ")
            if dahek == '1': 
                
              clear_screen()
              jovan()
              
              post_id = input('Enter the post ID: ')
              extracted = extract_ids(post_id)
              num_words = int(input("How many words would you like for the comment? "))
              comments_list = []
              for i in range(1, num_words + 1):
                  comment_input = input(f"Enter comment {i}: ")
                  comments_list.append(comment_input)

              commentator_type = input('Enter the commentator type (BOTH, PAGE, ACCOUNT): ').upper()
              num_comments = int(input('Enter the number of comments to make: '))
              comment_on_post_fast(extracted, comments_list, commentator_type, num_comments)
              back_to_menu = input("Press 0 to return to the main menu (ENTER AGAIN IF YOU WANT TO CONTINUE): ")
            if dahek == '2': 
              clear_screen()
              jovan()
              
              post_id = input('Enter the post ID: ')
              extracted = extract_ids(post_id)
              num_words = int(input("How many words would you like for the comment? "))
              comments_list = []
              for i in range(1, num_words + 1):
                  comment_input = input(f"Enter comment {i}: ")
                  comments_list.append(comment_input)

              commentator_type = input('Enter the commentator type (BOTH, PAGE, ACCOUNT): ').upper()
              num_comments = int(input('Enter the number of comments to make: '))
              comment_on_post(extracted, comments_list, commentator_type, num_comments)
              back_to_menu = input("Press 0 to return to the main menu (ENTER AGAIN IF YOU WANT TO CONTINUE): ")
            if back_to_menu == "0":
                    clear_screen()
                    main()
              
        elif choice == '4':
            clear_screen()
            jovan()
            print("[1] FAST METHOD")
            print("[2] SLOW METHOD")
            dahek = input("Choose: ")
            if dahek == '1':
               
               auto_follow_fast()
            if dahek == '2':
                
                auto_follow()
                
            back_to_menu = input("Press 0 to return to the main menu (ENTER AGAIN IF YOU WANT TO CONTINUE): ")
            if back_to_menu == "0":
                    main()
                    b
            
            
        elif choice =='122':
            post_id = input("Please enter the Post ID: ").strip()
            remove(post_id)
            
        elif choice == '5':
            clear_screen()
            jovan()
            print("[1] FAST METHOD")
            print("[2] SLOW METHOD")
            dahek = input("Choose: ")
            if dahek == '1':
                clear_screen()
                jovan()
                reels_link = input('Enter the reels link: ')
                reels = extract_id_reels(reels_link)
                reaction_type = input('Enter the reaction type (Like,Love,Haha,Wow,Sad,Angry): ')
                num_reactions = int(input('Enter the number of reactions to reels: '))
                auto_react_to_reels_fast(reels, reaction_type, num_reactions)
                back_to_menu = input("Press 0 to return to the main menu (ENTER AGAIN IF YOU WANT TO CONTINUE): ")
            if dahek == '2':
                clear_screen()
                jovan()
                reels_link = input('Enter the reels link: ')
                reels = extract_id_reels(reels_link)
                reaction_type = input('Enter the reaction type (Like,Love,Haha,Wow,Sad,Angry): ')
                num_reactions = int(input('Enter the number of reactions to reels: '))
                auto_react_to_reels(reels, reaction_type, num_reactions)
                back_to_menu = input("Press 0 to return to the main menu (ENTER AGAIN IF YOU WANT TO CONTINUE): ")
            
            if back_to_menu == "0":
                main()
        
        elif choice == '6':
            clear_screen()
            jovan()
            print("[1] FAST METHOD")
            print("[2] SLOW METHOD")
            dahek = input("Choose: ")
            if dahek == '1':
               post_id = input('Enter the post ID: ')
               comment_id = input('Enter the comment ID: ')
               reply_text = input('Enter the reply text: ')
               bot_types = input('Enter bot types (comma-separated, e.g., ACCOUNT,PAGE): ').upper().split(',')
               num_bots = int(input('Enter the number of bots to use: '))
               auto_reply_to_comment(post_id, comment_id, reply_text, bot_types, num_bots)
               back_to_menu = input("Press 0 to return to the main menu (ENTER AGAIN IF YOU WANT TO CONTINUE): ")
            if dahek == '2': 
               post_id = input('Enter the post ID: ')
               comment_id = input('Enter the comment ID: ')
               reply_text = input('Enter the reply text: ')
               bot_types = input('Enter bot types (comma-separated, e.g., ACCOUNT,PAGE): ').upper().split(',')
               num_bots = int(input('Enter the number of bots to use: '))
               auto_reply_to_comment(post_id, comment_id, reply_text, bot_types, num_bots)
               back_to_menu = input("Press 0 to return to the main menu (ENTER AGAIN IF YOU WANT TO CONTINUE): ")
            if back_to_menu == "0":
                break
        elif choice == '7':
            group_id = input('Enter the Facebook group ID: ')
            bot_types = input('Enter the bot types (ACCOUNT, PAGE, BOTH): ').split(',')
            num_bots = int(input('Enter the number of bots to join: '))
            auto_group_join(group_id, bot_types, num_bots)
        elif choice == '8':
            clear_screen()
            jovan()
            print("[1] FAST METHOD")
            print("[2] SLOW METHOD")
            dahek = input("Choose: ")
            if dahek == '1': 
             clear_screen()
             jovan()
             
             post_id = input('Enter the post ID: ')
             Video_Extractid = extract_ids(post_id)
             reaction_type = input('Enter the reaction type (Like,Love,Haha,Wow,Sad,Angry): ')
             reactor_type = input('Enter the reactor type (BOTH, PAGE, ACCOUNT): ').upper()
             num_reactions = int(input('Enter the number of reactions to perform: '))
             perform_reaction_video_fast(Video_Extractid, reaction_type, reactor_type, num_reactions)
             back_to_menu = input("Press 0 to return to the main menu(ENTER AGAIN IF YOU WANT TO CONTINUE): ")
            if dahek == '2': 
             clear_screen()
             jovan()
             post_id = input('Enter the post ID: ')
             
             reaction_type = input('Enter the reaction type (Like,Love,Haha,Wow,Sad,Angry): ')
             reactor_type = input('Enter the reactor type (BOTH, PAGE, ACCOUNT): ').upper()
             num_reactions = int(input('Enter the number of reactions to perform: '))
             perform_reaction_video(post_id, reaction_type, reactor_type, num_reactions)
             back_to_menu = input("Press 0 to return to the main menu(ENTER AGAIN IF YOU WANT TO CONTINUE): ")
              
            
            
        elif choice == '9':
            clear_screen()
            jovan()
            shar()
        elif choice == '10': 
            clear_screen()
            jovan()
            print("[1] FAST METHOD")
            print("[2] SLOW METHOD")
            dahek = input("Choose: ")
            if dahek == '1': 
                clear_screen()
                jovan()
                post_id = input("Enter the post ID where you want to react: ")
                reaction_type = input("Enter the type of reaction (LIKE, LOVE, WOW, SAD, ANGRY): ").upper()
                reactor_type = input("Enter the reactor type (PAGE, ACCOUNT, BOTH): ").upper()
                num_reactions = int(input("Enter the number of reactions you want to send: "))
                Auto_react_comment_fast(post_id, reaction_type, reactor_type, num_reactions)
            
            if dahek == '2':
               clear_screen()
               jovan() 
               post_id = input("Enter the post ID where you want to react: ")
               reaction_type = input("Enter the type of reaction (LIKE, LOVE, WOW, SAD, ANGRY): ").upper()
               reactor_type = input("Enter the reactor type (PAGE, ACCOUNT, BOTH): ").upper()
               num_reactions = int(input("Enter the number of reactions you want to send: "))
     
               Auto_react_comment(post_id, reaction_type, reactor_type, num_reactions)
        elif choice == '13': 
            hackezr()
        elif choice == '14': 
            runing()
        elif choice == '15': 
            menu()
        else: 
        
        
            print("Invalid option. Please try again.")

if __name__ == "__main__":
   
        main()