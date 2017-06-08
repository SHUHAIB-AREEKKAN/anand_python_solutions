#anand python problem 2:36
#Problem 36: Write a program to find anagrams in a given list of words.

def anagram(words):
	anagram_dict={}
	for word in words:
		
		sorted_word=''.join(sorted(list(word)))
		
		if sorted_word not in anagram_dict:
			
			anagram_dict[sorted_word]=[]
			
		anagram_dict[sorted_word].append(word)
		
	return anagram_dict
 		 	
if __name__ == '__main__':

	a=anagram(['eat', 'ate', 'done', 'tea', 'soup', 'node'])			
	print a.values()		
				 
