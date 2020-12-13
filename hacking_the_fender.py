import csv

compromised_users = []

#reading the pw file / storing in list
with open("passwords.csv") as password_file:
  password_csv = csv.DictReader(password_file)
  password_row = ""
  for row in password_csv:
    password_row = row
    compromised_users.append(password_row["Username"])
    #checking out pws
    #print(row["Password"])
    #noice

#storing list of users in file
with open("compromised_users.txt", "w") as compromised_user_file:
  for user in compromised_users:
    csv.DictWriter(compromised_user_file, user)

#informing boss
import json
with open("boss_message.json", "w") as boss_message:
  boss_message_dict = {"recipient":"The Boss", "message":"Mission Success"}
  json.dump(boss_message_dict, boss_message)

#creating new pw file
with open("new_passwords.csv", "w") as new_passwords_obj:
  slash_null_sig = """ _  _     ___   __  ____             
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
  new_passwords_obj.write(slash_null_sig)

#checking if file was written
#with open("new_passwords.csv") as file:
 # print(file.read())

