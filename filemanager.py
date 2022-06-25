import os
import argparse
import wget

Parser = argparse.ArgumentParser()
Parser.add_argument('-bn', '--boxname', help="Specify name of the CTF", required=True)
Args = Parser.parse_args()

box_name = Args.boxname

# Paths
smb_out     = box_name+"/"+"smb_out"
bloodhound  = box_name+"/"+"bloodhound"
nmap_folder = box_name+"/"+"enumeration"
privesc_folder = box_name+"/"+"privesc"

path = box_name

file_note = "notes.txt"
file_usernames = "usernames.lst"
file_passwords = "passwords.lst"
file_user_pass = "user_pass.lst"

web_site_power_view = 'https://raw.githubusercontent.com/PowerShellMafia/PowerSploit/master/Recon/PowerView.ps1'
web_site_power_up   = 'https://raw.githubusercontent.com/PowerShellMafia/PowerSploit/master/Privesc/PowerUp.ps1'

# Folders 
os.makedirs(box_name)
os.makedirs(smb_out)
os.makedirs(bloodhound)
os.makedirs(nmap_folder)
os.makedirs(privesc_folder)

# lst & txt files
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

# wget powerview and mooving it in privesc folder
wget.download(web_site_power_view)
print(" Downloading PowerView...")
os.replace("PowerView.ps1", privesc_folder+"/"+"PowerView.ps1")

# wget powerup and mooving it in privesc folder
wget.download(web_site_power_up)
print(" Downloading PowerUp...")
os.replace("PowerUp.ps1", privesc_folder+"/"+"PowerUp.ps1")

print(f"Workspace for {box_name} is ready")
