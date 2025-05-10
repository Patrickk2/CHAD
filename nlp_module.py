#Version : v0.1-RainyBot
def preprocess():
    text = text.lower()
    tokens = text.split()
    return tokens 

intents = {
    "Salutation": ["Yo", "salut", "Bonjour"],
    "Aide": ["Info", "aide", "commande", "help"],
    "merci": ["Thanks", "merci"]
}