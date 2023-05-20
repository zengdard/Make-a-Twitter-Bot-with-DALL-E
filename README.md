# Make-a-Twitter-Bot-with-DALL-E
# Bot Twitter utilisant OpenAI pour générer des images

Ce dépôt contient le code d'un bot Twitter qui utilise l'API OpenAI pour générer des images en réponse aux mentions sur Twitter. Le bot est construit avec Python, en utilisant les bibliothèques openai, tweepy, requests et json.

## Fonctionnalités

- Ecoute les mentions Twitter en temps réel.
- Génère une image en utilisant le modèle `image-alpha-001` d'OpenAI en réponse à chaque mention.
- Publie l'image générée en réponse à la mention originale.

## Comment l'utiliser

1. Clonez ce dépôt sur votre machine locale.
2. Installez les dépendances requises en utilisant pip:
   ```bash
   pip install openai tweepy requests
   ```
3. Ajoutez vos clés d'API Twitter et OpenAI aux variables appropriées dans le script Python. Ces clés sont nécessaires pour que le bot puisse accéder à Twitter et à OpenAI. Ne partagez jamais ces clés publiquement.

## Structure du code

Le script Python principal est un script qui tourne en boucle, vérifiant constamment les nouvelles mentions sur Twitter.

Pour chaque mention, le bot génère une image en utilisant OpenAI, la sauvegarde localement, puis répond à la mention avec l'image générée.

Le script utilise également un fichier `last_mention_id.json` pour garder une trace de la dernière mention traitée, afin de ne pas traiter les mêmes mentions plusieurs fois.

## Limitations

Le bot vérifie les nouvelles mentions toutes les 5 secondes. Ceci peut être ajusté, mais faites attention à ne pas violer les limites de l'API de Twitter.

## Contribuer

Les contributions à ce projet sont les bienvenues. Vous pouvez ouvrir une issue pour discuter d'un bug ou proposer une amélioration, ou ouvrir une pull request pour proposer des changements directement.

## Licence

Ce projet est sous licence MIT. Voir le fichier `CC.4` pour plus de détails.
