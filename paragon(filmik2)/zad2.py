def generate_filename(id): #id - całkowitoliczbowy identyfikator 
	s1 = str(id)
	s1 = s1.ljust(4)
	s =  f'{s1} -> data_{id:04}.txt'
	print(s)
	
generate_filename(3)
generate_filename(33)
generate_filename(333)
generate_filename(3333)

