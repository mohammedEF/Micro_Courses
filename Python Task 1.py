import datetime 
import os

while True:    # the loop is to give the user option to enter multiple times
    filename = 'diary.txt'
    user_input = input("What did you do today? ")
    # Adding the current date for each entry
    current_date = datetime.datetime.now().strftime("%Y-%m-%d")
    with open(filename, 'a') as file:
        file.write(f"{current_date}: {user_input}\n")
    
    with open(filename, 'r') as file:
        print("\nYour diary entries so far:")
        print(file.read())
    # giving the user an option to add more entries if they want
    add_more = input("do you want to add more stuff? (yes/no): ").strip().lower()
    if add_more != "yes":
        print("your Diray has been updated")
        break
# giving option to download the file after entring all what they want (the file will be stored local)
download = input("\nWould you like to download your diary file? (yes/no): ").strip().lower()
if download == 'yes':
    download_path = os.path.abspath(filename)
    print(f"\nYour diary file is ready for download: {download_path}")