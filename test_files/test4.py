def word_frequency(words):
	frequency={}
	for w in words:
		frequency[w]=frequency.get(w,0) + 1 
	return frequency

def read_words(filename):
	return open(filename).read().split()


if __name__ == '__main__':
	frequency= word_frequency(read_words('she.txt'))
	sec=[ [x,k] for x,k in frequency.items()]
	sec=sorted(sec,key=lambda x: x[1] ,reverse=True)
	for k in sec:
		print k
		
	

