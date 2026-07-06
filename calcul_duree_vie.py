# -*- coding: utf-8 -*-
"""
Created on Tue Jun 16 07:23:33 2026

@author: sivas
"""

import numpy as np
import matplotlib.pyplot as plt
 
from tkinter import*


fenetre = Tk()
fenetre.geometry('400x400')
fenetre.title('Solveur_guide')
fenetre['bg']='grey'

#creation de la boite de dialogue

Boite=Frame(fenetre, bg='grey', bd=1, relief=SUNKEN)

label=Label(Boite, text='Donner_les_parametres', font=('black',20))
label.grid(row=0, column=0)
#creation de 4 variable pour les paramètres

#points maillage

label_subtitle=Label(Boite, text='nb_point :', font=('black',10))
label_subtitle.grid(row=1, column=0, sticky='w')

EntreNb=Entry(Boite)
EntreNb.grid(row=1, column=0)

#niveau dopage
label_subtitle=Label(Boite, text='dopage :', font=('black',10))
label_subtitle.grid(row=2, column=0, sticky='w')

Entredopage=Entry(Boite)
Entredopage.grid(row=2, column=0)

#puissance injetion
label_subtitle=Label(Boite, text='injection :', font=('black',10))
label_subtitle.grid(row=3, column=0, sticky='w')

Entreinjection=Entry(Boite)
Entreinjection.grid(row=3, column=0)

#Temperature
label_subtitle=Label(Boite, text='echelle_temps:', font=('black',10))
label_subtitle.grid(row=4, column=0, sticky='w')

EntreT=Entry(Boite)
EntreT.grid(row=4, column=0)

#besoin de definir en global pour que ça marche
#dans la fonction voir si on peut pas faire plus propre

def valider_variable():
    nb = EntreNb.get()
    Dopage = Entredopage.get()
    Injection = Entreinjection.get()
    echelle_temps= EntreT.get()
    global Nb
    global dopage
    global injection
    global echelle
    Nb=int(nb)
    dopage=float(Dopage)
    injection=float(Injection)
    echelle=float(echelle_temps)
    print(echelle)
    return(Nb, dopage, injection, echelle)

def valider():
    Boite.destroy()
    fenetre.destroy()

#creation du bouton qui renvoie à la fonction solveur
bouton=Button(Boite, text="valider les 4 variables", command=valider_variable, bg='white', fg='black')
bouton.grid(row=5, column=0, pady='5')

#bouton qui arrête la boucle Tkinter

bouton=Button(Boite, text="quitter", command=valider, bg='red', fg='black')
bouton.grid(row=8, column=0, pady='15')

Boite.pack()
fenetre.mainloop()


#méthode runge kutta 4
temps=np.linspace(0, echelle, Nb)

#parametre et duree de vie pour un semicondcuteur InGaAs dans les telecoms
E_Gap=0.75 #eV
Longueur_onde_coupure=1.65 #micron 
alpha=1e4 #cm-1 longueur d'absorbtion.
Nd=dopage #niveau de dopage de l'InGaAs en cm-3
B=1e-10 #coefficient bi moléculaire cm3/s
sigma=1e-15 #section efficace en cm-2
vth=1e7 #vitesse liée à l'agitation thermique en cm/s
Nt=1e13 #densite de piège en cm-3
ni=1e12 #concentration de porteur intrinseque cm-3
Tau_i= 1e-3 #duree de vie intrinsèque en seconde
Cn=1e-28 #coefficient Auger cm6/S

#nombre de porteur obtenue (porteur crée par lexcitation plus dopage)


Tau_rad=1/(B*Nd)
Tau_SRH = 1/(sigma*vth*Nt)
Tau_auger= 1/(Cn*Nd**2)

Rglobal=(1/Tau_rad)+(1/Tau_SRH)+(1/Tau_auger)
Tau_vie=1/Rglobal
print(Tau_vie)
vect_tau_vie=np.zeros(Nb)

def f(n_porteur):
    return (-n_porteur/Tau_SRH-B*n_porteur**2-Cn*n_porteur**3)

dt=echelle/Nb
delta_n=dopage*np.ones(Nb)
delta_n[0]=injection+delta_n[0]

vect_tau_vie[0]=Tau_vie

for i in range(Nb-1):

    k1 = f(delta_n[i])

    k2 = f(delta_n[i] + dt*k1/2)

    k3 = f(delta_n[i] + dt*k2/2)

    k4 = f(delta_n[i] + dt*k3)

    delta_n[i+1] = delta_n[i] + (dt/6)*(k1 + 2*k2 + 2*k3 + k4)

    Tau_rad=1/(B*delta_n[i])
    Tau_SRH = 1/(sigma*vth*Nt)
    Tau_auger= 1/(Cn*delta_n[i]**2)

    Rglobal=(1/Tau_rad)+(1/Tau_SRH)+(1/Tau_auger)
    Tau_vie=1/Rglobal

plt.figure(0)
plt.semilogy(temps, delta_n)
# plt.plot(t,n_fit, color='red')
plt.xlabel("Temps")
plt.ylabel("delta_n")
plt.title("porteur echelle log")
plt.grid()
plt.show()

plt.figure(1)
plt.plot(temps, delta_n)
# plt.plot(t,n_fit, color='red')
plt.xlabel("Temps")
plt.ylabel("delta_n")
plt.title("porteur echelle lineaire")
plt.grid()
plt.show()

