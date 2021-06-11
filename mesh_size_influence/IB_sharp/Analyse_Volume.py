#Analyse de l'effet de la taille du domaine sur les Resultats
#Les fichier sont placé dans les méthode conforme ou IB_sharp
#Les dossier sont nommée avec r=? pour indiqué la puissance. serie géométrique raison 1.1 init (22,10,10)

import os
from numpy import pi
from pylab import *

###################---FONCTION---##############################################

def drag_data(Pow,dossier): #Renvoie la liste des donnée de force 
    with open(os.getcwd()+"/"+dossier+"/r="+str(Pow)+"/force.00.dat", "r") as f:
        x = list()
        y = list()
        for line in f:
            data = line.split()
            x.append(data[1])
    x.pop(0)
    x=[float(i) for i in x]
    return x

def drag_pow(pow,dossier): #Renvoie la force de trainé à la convergence associé à sont Re
        v=drag_data(pow,dossier)
        return v[len(v)-1]

def power_liste(dossier): #renvoie la liste triée des Reynolds basé sur les nom de dossier
    liste_dir=folders_id(dossier)
    liste_pow=list()

    for nom in liste_dir:
        liste_pow.append(nom[2:])

    liste_pow=[int(i) for i in liste_pow]
    liste_pow.sort()
    return liste_pow

def folders_id(dossier): #renvoie la liste des dossier
    with os.scandir(os.getcwd()+"/"+dossier) as entries:
        liste_dir=list()
        for entry in entries:
            if entry.is_dir():
                liste_dir.append(entry.name)
    return liste_dir


#################################---Main---###########################################

dossier=list() #initialisation de la liste dossier Resultats
dossier=folders_id("") #liste des dossiers Resultats
q=1.1 #raison de la suite géométrique

Volume_eq=list()
Fd=list()
pow_list=list()
for namefold in dossier:
    Pow_temp=power_liste(namefold) 
    Fd_temp=list()
    Volume_temp=list()
    for k in Pow_temp:
        v=drag_pow(k,namefold)
        Fd_temp.append(v)
        Volume_temp.append(round(pow(q,3*k),3))
    pow_list.append(Pow_temp)
    Fd.append(Fd_temp)
    Volume_eq.append(Volume_temp)

print(Volume_eq)


#################################---Affichage---###########################################

fig, ax = plt.subplots()
line1=plot(Volume_eq[0][:], Fd[0][:],'-x')
plt.title('Influence de la taille du domaine de simulation sur la force de trainée')
ax.legend(dossier, loc='best')
ax.set_xlabel('Nombre de volume équivalent')
ax.set_ylabel('Force de trainée Fd')
plt.show() 
 