


def get_username():
    username= input("Username:")

    return username


def get_password():

    return input("Password")

def auth(username, password):

    if len(username) < 3:
        print("le suername est trop cour")
        return

    print("conect successfull")


username = get_username()
password  =get_password()

auth(username, password)





"""

« Voici comment git flow permet de gérer proprement un cycle de release :

Je démarre la release avec git flow release start nom_release, ce qui fige les changements en attente.

Je travaille uniquement sur des bugs ou des améliorations mineures, en préparant le livrable.

Une fois prêt, je finalise avec git flow release finish, qui automatise les merges vers master et develop, crée un tag, et supprime la branche de release.

Je pousse les changements et le tag, pour que toute l’équipe et CI/CD les reçoivent.

Cela structure le cycle de version, évite les conflits et garantit que ce qui part en production est bien validé. »"""