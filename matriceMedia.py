from random import *

Matrice = [[], [], [], []]

i=0
j=0
while i<len(Matrice):
	j=0
	while j<len(Matrice):
		Matrice[i].append(randint(1,10))  #riempio matrce
		j=j+1
	i=i+1
	

print(f'Matrice: {Matrice}') #stampo matrice

Medie=[]
m=0
i=0
j=0
while i<len(Matrice):
	j=0
	m=0
	while j<len(Matrice):
		m=m+Matrice[i][j]  #calcolo media per riga
		j=j+1
	Medie.append(m/len(Matrice))
	i=i+1

i=0
while i<len(Matrice):
	print(f'Media {Matrice[i]} : {Medie[i]}')  #stampo medie
	i=i+1
