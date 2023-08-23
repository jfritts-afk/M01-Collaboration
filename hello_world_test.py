#____________________________________________________________________________________________________________________________________________
#|       ::::::::::: :::::::::: :::::::::  ::::::::::: ::::::::::: ::::::::::: ::::::::                    :::     :::::::::: :::    :::    /
#|          :+:     :+:        :+:    :+:     :+:         :+:         :+:    :+:    :+:                 :+: :+:   :+:        :+:   :+:     /
#|         +:+     +:+        +:+    +:+     +:+         +:+         +:+    +:+                       +:+   +:+  +:+        +:+  +:+      /
#|        +#+     :#::+::#   +#++:++#:      +#+         +#+         +#+    +#++:++#++ +#++:++#++:++ +#++:++#++: :#::+::#   +#++:++       /
#|       +#+     +#+        +#+    +#+     +#+         +#+         +#+           +#+               +#+     +#+ +#+        +#+  +#+      / 
#|  #+# #+#     #+#        #+#    #+#     #+#         #+#         #+#    #+#    #+#               #+#     #+# #+#        #+#   #+#     /  
#|  #####      ###        ###    ### ###########     ###         ###     ########                ###     ### ###        ###    ###    /
#------------------------------------------------------------------------------------------------------------------------------------/
import os
import time
import sys
import select
import msvcrt

def wait_for_keypress_or_timeout(timeout_seconds):
    print("Press any key within {} seconds or the program will close.".format(timeout_seconds))
    
    start_time = time.time()
    while True:
        if msvcrt.kbhit():
            msvcrt.getch()  # Register the keypress
            print("Key pressed! Restarting...")
            return True  # Signal that a key was pressed
        
        if sys.platform != 'win32':
            # On non-Windows platforms, use select
            rlist, _, _ = select.select([sys.stdin], [], [], 0)
            if rlist:
                # Something is ready to be read on stdin
                print("Key pressed! Restarting...")
                return True  # Signal that a key was pressed
        
        if time.time() - start_time >= timeout_seconds:
            # Timeout reached
            os.system('cls' if sys.platform == 'win32' else 'clear')
            print("Timeout reached. Exiting. Have a good day! ")
            time.sleep(2)
            os.system('cls' if sys.platform == 'win32' else 'clear')
            return False  # Signal that the timeout occurred

def animate_text(text, delay):
    for i in range(len(text)):
        os.system('cls' if sys.platform == 'win32' else 'clear')
        print(" " * i + text)
        time.sleep(delay)

def animate_text2(text, delay):
    for i in range(len(text)):
        os.system('cls' if sys.platform == 'win32' else 'clear')
        print(" " * i + text)
        time.sleep(delay)

def animate_text3(text, delay):
    for i in range(len(text)):
        os.system('cls' if sys.platform == 'win32' else 'clear')
        print(" " * i + text)
        time.sleep(delay)
        
if __name__ == "__main__":
    timeout_seconds = 10  # Adjust this to set the timeout duration in seconds
    
    while True:
        os.system('cls' if sys.platform == 'win32' else 'clear')  # Clear console based on OS
        
        print("Hello, this is my first file using Git!")
        time.sleep(2)
        os.system('cls' if sys.platform == 'win32' else 'clear')  
        
        print("Hello World!")
        time.sleep(2)
        os.system('cls' if sys.platform == 'win32' else 'clear')  
        
        animate_text("Wanna run it again?", 0.1)  
        
        animate_text2("-----------------", 0.1)  
        
        animate_text3("Then you better:", 0.01)
        
        if not wait_for_keypress_or_timeout(timeout_seconds):
            break  # Exit the loop if the timeout occurs
