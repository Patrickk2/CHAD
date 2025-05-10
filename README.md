# CHAD
CHAD is just a CHATBOT made by a newbie


## 🔍 **CHAD V1 – État actuel**

### ✅ **Ce qu’il sait faire (et il le fait bien)**

* **Réagir à des commandes simples** :

  * `"bonjour"` → te salue
  * `"test"` → répond s’il est vivant
  * `"aide"` → te liste toutes les commandes dispo
  * `"version"` → affiche sa version actuelle
  * `"bye"`, `"rien"` → quitte proprement avec `sys.exit()`
  * `"nettoie"` → efface l’écran (optionnel selon l’OS)

* **Boucle de dialogue** :

  * Il reste actif tant que tu lui parles.
  * Il comprend ce que tu tapes ligne par ligne.

* **Structure propre** :

  * Utilisation d’un **dictionnaire de commandes** pour centraliser la logique.
  * Facile à maintenir et à agrandir.

---

### 🧱 **Ce qui lui manque (et ce qu’on va booster dans V2)**

| Manque                         | Pourquoi c’est important                                                     |
| ------------------------------ | ---------------------------------------------------------------------------- |
| ❌ Pas de vraie "compréhension" | Il ne comprend pas les phrases libres (ex: "Quel temps fait-il à Conakry ?") |
| ❌ Pas de mémoire               | Il oublie tout à chaque exécution                                            |
| ❌ Pas connecté à Internet      | Impossible d’aller chercher des infos fraîches                               |
| ❌ Réponses rigides             | Il répond toujours la même chose, sans humour ni style                       |
| ❌ Aucune personnalité          | C’est un bot neutre, sans âme (snif 😢)                                      |

---

### 🧪 **Résumé de CHAD V1**

> 💬 **"Je suis CHAD, un petit bot simple mais prêt à évoluer."**
> Il a les bases solides. Il est propre, organisé, minimaliste.
> C’est le **squelette d’un futur assistant IA**, et avec un peu de code, il va devenir un GigaCHAD. 🧠⚡



# 🤖 Objectifs de CHAD V2

Version next-gen du chatbot CHAD – plus smart, plus connecté, plus vivant.  
Une IA minimaliste mais ambitieuse. Voici la roadmap :

---

## 🧠 1. IA Légère Intégrée
- [ ] Utiliser un mini-modèle NLP (`DialoGPT-small`, logique maison…)
- [ ] Réponses naturelles et un peu contextuelles
- [ ] Ajouter une personnalité (drôle, calme, curieux…)

---

## 🌍 2. Connexion à Internet
- [ ] Accès à Wikipedia pour répondre à des questions
- [ ] Intégration d’APIs (actualités, météo, etc.)
- [ ] Commande spéciale : `cherche [terme]`

---

## 🧠💾 3. Mémoire
### a) Mémoire Temporaire
- [ ] Dictionnaire en session

### b) Mémoire Persistante
- [ ] Sauvegarde dans un fichier `.json`
- [ ] Commandes :
  - `souviens-toi [clé] : [valeur]`
  - `rappelle-moi [clé]`
  - `oublie [clé]`

---

## 🛠️ 4. Système de Commandes Avancé
- [ ] Commandes centralisées dans un dictionnaire dynamique
- [ ] `help` pour afficher toutes les commandes
- [ ] Réponses stylées aux erreurs ou commandes inconnues

---

## 🎭 5. Personnalité et Style
- [ ] Ton personnalisable (fun, formel, sage, etc.)
- [ ] Réactions expressives (emojis, citations, blagues…)
- [ ] Changement de mode à la volée : `mode thug`, `mode philosophe`...

---

## 💡 6. Modularité
- [ ] Organisation du code en fonctions/fichiers propres
- [ ] Fichier `config.json` pour options de personnalisation
- [ ] Prévoir des updates faciles (plugin, add-ons…)
