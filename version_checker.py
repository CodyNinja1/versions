import requests
import ctypes

def check_for_updates():
    version_url = 'https://raw.githubusercontent.com/Stuntlover-TM/versions/main/example_vc.txt' # This URL should stay the same in all versions of the program
    newest_release_url = requests.get(version_url).text.split("\n") # Splits the URL for each newline, newest_release_url[0] being the download URL and newest_release_url[1] being the version
    current_release_url = "https://github.com/Stuntlover-TM/versions/releases/download/example-v1.0.0/version-checker.exe" # The "example-v1.1.0" would change if you made a new release
    file_name = f"Program Name v{newest_release_url[1]}.exe"
    update_bool = None

    if newest_release_url[0] != current_release_url:
        update_bool = ctypes.windll.user32.MessageBoxW(0, f"New update available ({newest_release_url[1]})! Would you like to install the newest version?", "New update available!", 1) # Show a message box asking if the user wants to update
        # update_bool is 1 if Yes is pressed and 2 if Cancel is pressed
    
    if update_bool == 1:
        newest_release_file = requests.get(newest_release_url[0]) # Gets the first line which should be the URL to the newest version
        open(file_name, 'wb').write(newest_release_file.content) # Names the file with your program name and version number with .exe at the end
        exit()

check_for_updates()
