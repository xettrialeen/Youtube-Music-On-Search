# This is a youtube search programm
import pywhatkit as kit

user = input("Enter your name: ")
print(f" Hello {user} This is a tool you can search google, play youtube Music and search wikepedia \n")

# ? adding if else statement
print(" 1) Play Youtube")
print(" 2) Search Google")
print(" 3) Search Wikepedia")
print(" 4) Show Search History \n \n")

search_directory = input("Type Here The Following... ")


if search_directory == "1":
    youtube_data = input("Hi i can play you a music ! Search for..? \n ")
    kit.playonyt(youtube_data)
elif search_directory == "2":
    google_data = input("What to search in Google? \n")
    kit.search(google_data)
elif search_directory == "3":
    wikepedia_data = input(
        "what do you wanna learn today i can search ypu from wikepedia?... \n")
    kit.info(wikepedia_data)
elif search_directory == "4":
    kit.showHistory()
