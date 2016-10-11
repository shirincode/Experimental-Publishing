keyword = "";

json searchquery = json.load(googleapistuff.getsearchquery(keyword))



poem = []

lastsentence = ""
for result in searchquery :
	if lastsentence == "": # look if sentence is empty (that would be the first)
		lastsentence = result
		poem.add(result) # add result to array
	else:
		if(rhymeswith(lastword(lastsentence),lastword(result):
			poem.add(result)

def lastword(sentence):
	return #google how to get last word of sentence

def rhymeswith(one,two):
	json rhymes = json.load(http://rhymebrain.com/talk?function=getRhymes&word=one)
	for word in rhymes:
		if two.equals(word): # you could also check if only the last part of the word equals
			return true
	return false

print poem