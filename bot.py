#!/usr/bin/env python3
import os
import sys

"""
Mini chatbot CHAD - version 0.1 alpha
Commandes disponibles :
- test      : vérifie le chat
- bonjour   : salutation de CHAD
- aide      : affiche ce message d'aide
- rien      : termine la discussion
- bye       : termine la discussion
- version   : affiche la version du bot
- nettoie   : nettoie l'écran
"""

def cmd_test():
    print("Bonjour, je suis CHAD. Je suis encore en développement, donc pas la peine d’insister.")
    sys.exit()

def cmd_bonjour():
    print("Salut ! Tu tombes bien, j’étais en train de réfléchir à l’univers.")

def cmd_aide():
    # Affiche l'aide avec le dictionnaire des commandes
    print("\n=== Aide CHAD ===")
    print("Voici les commandes que tu peux utiliser :")
    for cmd in commands:
        print(f"- {cmd}")
    print("=================\n")

def cmd_rien():
    print("D'accord, je vais retourner dormir alors...")
    sys.exit()

def cmd_bye():
    print("À plus dans le bus !")
    sys.exit()

def cmd_version():
    print("CHAD est actuellement à la version 0.1 alpha.")

def cmd_nettoie():
    os.system('clear')

def cmd_unknown():
    print("Frero, j’ai pas capté, tu peux répéter ?")

# Mapping des commandes vers les fonctions
commands = {
    "test": cmd_test,
    "bonjour": cmd_bonjour,
    "aide": cmd_aide,
    "rien": cmd_rien,
    "bye": cmd_bye,
    "version": cmd_version,
    "nettoie": cmd_nettoie,
}

def main():
    os.system('clear')
    user = input("C'est quoi ton blaze ? ")

    while True:
        prompt = input(f"{user} : ")
        key = prompt.lower().strip()
        # Exécute la commande si elle existe, sinon la fonction unknown
        commands.get(key, cmd_unknown)()

if __name__ == "__main__":
    main()

