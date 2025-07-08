# Test Technique : Opérations sur les matrices

## Sommaire
- [Instructions](#instructions)
- [Restrictions](#restrictions)
- [Structure du projet](#structure-du-projet)
- [Rappel : Formule du déterminant d'une matrice](#rappel--formule-du-déterminant-dune-matrice)


## Instructions

1. Cloner ce dépôt.
2. Implémenter les opérations de base sur des matrices : addition, soustraction, multiplication.
3. Implémenter le calcul du déterminant d'une matrice.
4. Ajouter tout autre élément que vous jugerez pertinent à ce dépôt.
5. Pousser votre fork sur un dépôt public.

## Restrictions

- Interdiction d’utiliser l’IA, la complétion automatique ou toute recherche Internet.
- Aucun recours à des bibliothèques externes.
- Un seul écran et partagé durant tout le test.

## Structure du projet

- `matrix.py` : Contient la classe `Matrix` et les opérations demandées
- `README.md` : Ce fichier d'instructions

## Rappel : Formule du déterminant d'une matrice

Pour une matrice carrée $A = (a_{ij})$ de taille $n \times n$ :

$$
\det(A) = \sum_{j=1}^{n} (-1)^{1+j} \; a_{1j} \; \det(A_{1j})
$$

avec $A_{1j}$ la matrice obtenue en supprimant la première ligne et la $j$-ème colonne de $A$ (développement de Laplace).

Plus généralement, pour toute ligne $i$ :

$$
\det(A) = \sum_{j=1}^{n} (-1)^{i+j} \; a_{ij} \; \det(A_{ij})
$$

où $A_{ij}$ est la matrice obtenue en supprimant la ligne $i$ et la colonne $j$.

