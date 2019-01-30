#! python3
#password manager for users
import sys, pyperclip

db={'Meri':'abcdef', 'Vishaal':'vishaaliii', 'Deepika':'nani'}

if len(sys.argv)<2:
    print("Please enter program name followed by account username")
    SystemExit

#first argument is the program name. second argument is the user
user=sys.argv[1]

if user in db:
    pyperclip.copy(db[user])    #copy key value from dict
    print('Password for '+user+ ' is copied')
else:
    print('Sorry no such account')

