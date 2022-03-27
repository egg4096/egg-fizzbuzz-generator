from itertools import combinations

keywords = {
}

while True:
	i = input('Assign keywords and what a number should be divisible by to get this keyword (Example syntax: fizz 3). Leave a blank line when done. \n: ')
	if i == '':
		break
	i = i.split(' ')
	keywords[i[0]] = i[1]
	
print('for i in range(1, 101):')

for i in list(keywords):
	print(f'  {i} = i % {keywords[i]} == 0')

sus = ''
generated = ''
print('')
for i in range(len(keywords), 0, -1):
	for j in list(combinations(list(keywords), i)):
		generated += f"'{sus.join(j)}' if {' and '.join(j)} else "
print(f'  print({generated} i)')


