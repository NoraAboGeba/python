#removing vowel charachters from input of a user
def vowel_rem(name):
	name=input("enter name")
	vowel=['a','e','i','o','u','a','E','I','O','U']
	for i in name:
	   if(i in vowel):
	       name=name.replace(i,"")
	return( name)
#word=vowel_rem('mobile')
#print(word)

# python
