from random import *
Matrice = [[], [], [], []]
Mat = [[], [], [], []]

for i in range(4):
	for j in range(4):
		Matrice[i].append(randint(1,10))
		Mat[i].append(randint(1,10))
	#riempimento matrici
	
print(f'Matrice: {Matrice}')
print(f'Mat: {Mat}')

cont=0
for i in range(4):
	for j in range(4):
		if Mat[i][j]==Matrice[i][j]:
			cont=cont+1

print(f'ci sono {cont} elementi uguali che corrispondono')
