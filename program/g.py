


f = open('centre_matrix_out.txt', 'r')

a = f.readline()
a = f.readline()
a = f.readline()
a = f.readline()	
	
	
b = float(a[18:-6])

a = f.readline()
a = f.readline()
a = f.readline()

err = float(a[18:-10])

f.close()

print('Acceleratia gravitationala este: ' + str(b*2.0))
print('Eroarea este: +/- ' + str(err*2.0))