# Efrei-TP3-Devops

## L'API
J'ai juste récupéré l'API du TP précédent.

## Github Action
1. J'ai d'abord lu la documentation pour comprendre comment je pourrais mettre en place la github action. 
2. Ensuite j'ai récupéré le code qui était proposé par Microsoft. Après je l'ai essayé de comprendre le fichier.
3. Une fois fait, j'ai modifié le nom de l'image en lui donnait le bon format de nom proposé dans l'énoncé du TP, ce qui a bien fonctionné.

## Azure
A cette étape s'est posé un problème. L'action Github fonctionnait bien néanmoins lors du test j'avais une erreur.
Je vous ai contacté et vous m'avez suggeré de faire des recherches et vous avez donné l'indice que le problème serait au niveau du réseau.
J'ai fait d'inombrables recherches où j'ai découvert des possibilités comme:
* Un problème avec le dns
* Une mauvaise configuration de authLevel
* etc..
Et finalement j'ai compris que ce serait un problème de port. J'ai alors fait des recherches pour modifier le port d'écoute sur Azure et je n'ai pas eu de réponse.
Ensuite un camarade de classe a suggéré de changer le port dans mon API plutôt, ce qui était une solution viable.
Après il y avait le problème sur la variable d'environnement, et j'ai trouvé le paramètre qui me permettait d'en ajouter dans mon fichier YAML.
Enfin, tout a bien fonctionné.

Malheureusement je n'ai pas pu attaquer la partie bonus car je ne pouvais pas tester 

Saisissez plutôt la commande ```curl "http://devops-20180532.francecentral.azurecontainer.io/echo?lat=9.32&lon=102.75"``` si vous voulez avoir une sortie directe des données
