direction = [('direction', 'north'),
				('direction', 'south'),
				('direction', 'east'),
				('direction', 'west'),
				('direction', 'up'),
				('direction', 'down'),
				('direction', 'left'),
				('direction', 'right'),
				('direction', 'back')
]
	
verbs = [('verb', 'go'),
			('verb', 'stop'),
			('verb', 'kill'),
			('verb', 'eat')
]
			
stop_words = [('stop', 'the'),
				('stop', 'in'),
				('stop', 'of'),
				('stop', 'from'),
				('stop', 'at'),
				('stop', 'it')
]
	
nouns = [('noun', 'door'),
			('noun', 'bear'),
			('noun', 'princess'),
			('noun', 'cabinet')
]
	
	
library = tuple(nouns + stop_words + verbs + direction)

def convert_number(x):
	try:
		return int(x)
	except ValueError:
		return None
		

def scan(input):
	#include uppercase input for searching. (Study Drills no.3)
	lowercase = input.lower()
	#element is what i want to search.
	element = lowercase.split()
	#orielement is the original input which have uppercase, for 'error' type
	orielement = input.split()
	#library is tuple of the word types from above. You can replace with your data source.
	data = library
	#i is used to evaluate the position of element
	i = 0
	#z is used to indicate the position of output, which is the data that match what i search, equals to "i".
	z = 0
	#create a place to store my output.
	output = []
	#temp is just a on/off switch. Turn off the switch when i get any match for that particular input.
	temp = True
	#creating a condition which evaluates the total search needed to be done and follows the sequence by +1.
	while not(i == len(element)):
		try:
			#j is used to position the word in the library, eg 'door', 'bear', 'go', etc which exclude the word type.
			j = 0
			while not (j == len(data)):
				#data[j][1] all the single word in library
				matching = data[j][1]
				#when the word match, it will save the match into the output.
				if (matching == element[i]):
					output.append(data[j])
					#print output[z]
					j += 1
					z += 1
					#to switch off the search for else: below and go to next input search. Otherwise they would be considerd 'error'
					temp = False
				#else is everything that is not in the library.
				else:
					while (data[j][1] == data [-1][1]) and (temp == True):
						#refer to convert_number, to test if the input is a number, here i use orielement which includes uppercase
						convert = convert_number(orielement[i])
						#a is used to save number only.
						a = tuple(['number', convert])
						#b is to save everything
						b = tuple(['error', orielement[i]])
						#conver is number a[1] is the access the number inside, if it returns None from number then it wont append.	
						if convert == a[1] and not(convert == None):	
							output.append(a)
							temp = False
						else:
							output.append(b)
							#keep the switch off to escape the while loop!
							temp = False
					#searching in next data
					j += 1
			#next word of input
			i += 1
			temp = True
		except ValueError:
			return output
	else:
		pass
	return output