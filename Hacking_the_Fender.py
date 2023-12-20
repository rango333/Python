# ## A hacker compromised several top-secret passwords. Aquire the access to systems hacked, update password file to scramble the secret data, and add signiture Slash Null that comes the threat to the fender.

# # Write a program that will read in the compromised usernames and passwords that are stored in a file.
# Import the CSV module in order to parse the data
import csv
# Create a list of users whose passwords have been compromised
compromised_users = []
# Open compromised file and store in an object. In this case, 'passwords.csv'.
with open('passwords.csv') as password_file:
  # Pass object holder to CSV reader for parsing and save it to a temporary variable
  password_csv = csv.DictReader(password_file)
  # Create a for loop and save each row of the CSV into a temporary variable.
  for password_row in password_csv:
    # Append Usernames to the compromised_users list
    compromised_users.append(password_row['Username'])

# Start a new with block, opening a file called compromised_users.txt. Open this file in write-mode, saving the file object as compromised_user_file
with open('compromised_users.txt', 'w') as compromised_user_file:
  # Inside the new context-managed block opened by the with statement start a new for loop. Iterate over each of your compromised_users.
  for compromised_user in compromised_users:
    # Write the username of each compromised_user in compromised_users to compromised_user_file.
    compromised_user_file.write(compromised_user)

# Send encoded message (in this case use JSON) to the boss to show that you were successful in retrieving the compromised data.

# First import JSON. Note: could import at start of script for cleaner script format.
import json
# Open a new JSON file in write-mode called boss_message.json. Save the file object to the variable boss_message.
with open('boss_message.json', 'w') as boss_message:
  # Create a Python dictionary object within your with statement that relays a boss message. Call this boss_message_dict. Give it a "recipient" key with a value "The Boss". Also give it a "message" key with the value "Mission Success".
  boss_message_dict = {'recipient': 'The Boss', 'message': 'Mission Success'}
  # Write out boss_message_dict to boss_message using json.dump()
  json.dump(boss_message_dict, boss_message)

# Now that we’ve safely recovered the compromised users we’ll want to remove the "passwords.csv" file completely. 
#Create a new with block and open "new_passwords.csv" in write-mode. Save the file object to a variable called new_passwords_obj.
with open('new_passwords.csv', 'w') as new_passwords_obj:
  # Enemy of the people, Slash Null, is who we want The Fender to think was behind this attack. He has a signature, whenever he hacks someone he adds this signature to one of the files he touches.
  # Save that as a multiline string to the variable slash_null_sig.
  slash_null_sig = """_  _     ___   __  ____             
/ )( \   / __) /  \(_  _)            
) \/ (  ( (_ \(  O ) )(              
\____/   \___/ \__/ (__)             
 _  _   __    ___  __ _  ____  ____  
/ )( \ / _\  / __)(  / )(  __)(    \ 
) __ (/    \( (__  )  (  ) _)  ) D ( 
\_)(_/\_/\_/ \___)(__\_)(____)(____/ 
        ____  __     __   ____  _  _ 
 ___   / ___)(  )   / _\ / ___)/ )( \
(___)  \___ \/ (_/\/    \\___ \) __ (
       (____/\____/\_/\_/(____/\_)(_/
 __ _  _  _  __    __                
(  ( \/ )( \(  )  (  )               
/    /) \/ (/ (_/\/ (_/\             
\_)__)\____/\____/\____/"""
  # Write slash_null_sig to new_passwords_obj. Now we have the file to replace passwords.csv with!
  new_passwords_obj.write(slash_null_sig)