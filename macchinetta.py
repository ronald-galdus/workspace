def macchinetta(resto):
	
	due = resto/2
	resto=resto-(int(due)*2)	#2 euro

	uno = int(resto)/1
	resto=resto-(int(uno)*1)	#1 euro

	resto=round(resto,2)	#arrotonda, usato spesso causa imprecisioni

	fifty = resto/0.50
	resto = resto - (int(fifty)*0.50)	#50 cent

	resto=round(resto,2)

	twenty = resto/0.20
	resto=resto - (int(twenty)*0.20)	#20 cent

	resto=round(resto,2)

	ten = resto/0.10
	resto=resto - (int(ten)*0.10)	#10 cent
	
	resto=round(resto,2) 

	five = resto/0.05
	resto=resto - (int(five)*0.05)		#5 cent

	resto=round(resto,2)

	two = resto/0.02
	resto=resto - (int(two)*0.02)		#2 cent

	resto=round(resto,2)

	one = resto/0.02
	resto=resto - (int(one)*0.02)		#1 cent

	if(due>=1):
		print(f"Serviranno {int(due)} moneta/e da 2 euro")

	if(uno>=1):
		print(f"Serviranno {int(uno)} moneta/e da 1 euro")

	if(fifty>=1):
		print(f"Serviranno {int(fifty)} moneta/e da 50 centesimi")

	if(twenty>=1):
		print(f"Serviranno {int(twenty)} moneta/e da 20 centesimi")

	if(ten>=1):
		print(f"Serviranno {int(ten)} moneta/e da 10 centesimi")

	if(five>=1):
		print(f"Serviranno {int(five)} moneta/e da 5 centesimi")

	if(two>=1):
		print(f"Serviranno {int(two)} moneta/e da 2 centesimi") 

	if(one>=1):
		print(f"Serviranno {int(one)} moneta/e da 1 centesimi") 


resto=float(input('inserire una cifra nella macchinetta: '))
macchinetta(resto)


