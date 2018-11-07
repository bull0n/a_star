# Questions

## L’utilisation des différentes heuristiques a-t-elle une influence sur l’efficacité de la recherche ? (en termes du nombres de noeuds visités)

Oui plus l'heuristique est proche du résultat réel, moins l'algorithme fera d'itérations.  C'est pour cela qu'il faut préférer une bonne heuristique.

## Pouvez-vous trouver des exemples où l’utilisation de différentes heuristiques donne des résultats différents en termes de chemin trouvé ?

Les heuristiques de la différence en x, différence en y, 0 et distance à vol d'oiseau sont admissibles. Donc les chemins retournés seront toujours identiques.

Par contre manhattan n'est pas admissible et il est donc possible de trouver un chemin qui n'est pas optimal. Par exemple de Paris à Prague

## Dans un cas réel, quelle heuristique utiliseriez-vous ?

La distance à vol d'oiseau me semble la plus optimale. L'heuristique est admissible (si une route va tout droit, elle sera égale, sinon toujours plus petit).

Le problème de l'heuristique 0 est qu'elle est identique à tous les chemins et l'algorithme ne fera pas de préférences entre les différentes routes.

La différence en x et en y n'est pas très adapté aussi car deux villes peuvent avoir une valeur en x très petite mais une distance en y très grande.

Et l'heuristique de manhattan n'est pas admissible et ne trouvera pas toujours le chemin optimal.
