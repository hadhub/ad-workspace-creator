import os
import argparse

Parser = argparse.ArgumentParser()
Parser.add_argument('-bn', '--boxname', help="Specify name of the CTF", required=True)
Args = Parser.parse_args()

box_name = Args.boxname
print(f"Workspace for {box_name} is ready")

smb_out     = box_name+"/"+"smb_out"
bloodhound  = box_name+"/"+"bloodhound"
nmap_folder = box_name+"/"+"nmap"

# Répertoires 
os.makedirs(box_name)
os.makedirs(smb_out)
os.makedirs(bloodhound)
os.makedirs(nmap_folder)

# Chemin
path = box_name
file_note = "notes.txt"
file_usernames = "usernames.lst"
file_passwords = "passwords.lst"
file_user_pass = "user_pass.lst"

# Fichier
completePath = os.path.join(path,file_note)
with open(completePath,'w') as file:
    file.write('')

completePath = os.path.join(path,file_usernames)
with open(completePath,'w') as file:
    file.write('')

completePath = os.path.join(path,file_passwords)
with open(completePath,'w') as file:
    file.write('')

completePath = os.path.join(path,file_user_pass)
with open(completePath,'w') as file:
    file.write('')
