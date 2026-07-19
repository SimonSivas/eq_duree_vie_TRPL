# Simulation de la photoluminescence résolue en temps (TRPL) dans un semi-conducteur

## Description 

Ce projet modélise la dynamique de recombinaison des porteurs générés par une impulsion laser dans un semi-conducteur III-V dopé. L'objectif est d'étudier l'influence des différents mécanismes de recombinaison, et de la forte ou faible injection sur le signal de photoluminescence résolue en temps (TRPL).

## Contexte physique

Laser pulsé sur le semi conducteur dopé 

      │
      ▼
      
Création de porteurs (paire éectron-trou)

      │
      ▼
Recombinaisons 
 ├── SRH
 ├── Radiative
 └── Auger
 
      │
      ▼
Photoluminescence

## Contexte physique

La photoluminescence résolue en temps (**Time-Resolved Photoluminescence – TRPL**) est une technique permettant d'étudier la dynamique des porteurs de charge dans un semi-conducteur après une excitation par une impulsion laser.

Lorsque l'énergie des photons incidents est supérieure à la largeur de bande interdite du matériau ((E_{ph} > E_g)), des paires électron-trou sont créées. Après l'impulsion laser, ces porteurs se recombinent progressivement selon différents mécanismes : la recombinaison **Shockley-Read-Hall (SRH)**, la recombinaison **radiative** et la recombinaison **Auger**.

L'objectif de ce projet est de modéliser numériquement l'évolution temporelle de la densité de porteurs photogénérés afin de simuler le signal de photoluminescence et d'étudier l'influence des différents mécanismes de recombinaison sur la durée de vie effective des porteurs.

## Modèle physique

