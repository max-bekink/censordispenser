# These are the emails you will be censoring. The open() function is opening the text file that the emails are contained in and the .read() method is allowing us to save their contexts to the following variables:
email_one = open("email_one.txt", "r").read()
email_two = open("email_two.txt", "r").read()
email_three = open("email_three.txt", "r").read()
email_four = open("email_four.txt", "r").read()

proprietary_terms = ["she", "personality matrix", "sense of self", "self-preservation", "learning algorithm", "her", "herself"]

negative_words = ["concerned", "behind", "danger", "dangerous", "alarming", "alarmed", "out of control", "help", "unhappy", "bad", "upset", "awful", "broken", "damage", "damaging", "dismal", "distressed", "distressed", "concerning", "horrible", "horribly", "questionable"]

example = "Hello there, I am max and I am concerned about some things concerned. It is bad, very bad. She is totally gone crazy"


def censor_four(text):
	index = 0
	index2 = 0
	found_indexes = {}
	idx = 0
	textn = ""
	for i in proprietary_terms:
		while index < len(text):
			index = text.lower().find(i, index)
			if index == -1:
				index = 0
				break
			found_indexes[index] = len(i)
			index += len(i)
	for i in negative_words:
		while index2 < len(text):
			index2 = text.lower().find(i, index2)
			if index2 == -1:
				index2 = 0
				break
			if text.count(i) > 1:  
				found_indexes[index2] = len(i)
			index2 += len(i)      
	found_indexes_s = sorted(found_indexes)
	found_indexes_new = {}
	for key in found_indexes_s:
		found_indexes_new[key] = found_indexes[key]
	found_indexes_new2 = {}
	for key, value in found_indexes_new.items():
		after = text.find(" ", key+value+2, -1)
		before = text.rfind(" ", 0, (key-2))+1
		key_n = before
		value_n = after - before
		found_indexes_new2[key_n] = value_n
	for key, value in found_indexes_new2.items():
		textn += text[idx:key] + value*'X'
		idx = key + value 
	textn += text[idx:]
	return textn


def censor_three(text):
	index = 0
	index2 = 0
	found_indexes = {}
	idx = 0
	textn = ""
	for i in proprietary_terms:
		while index < len(text):
			index = text.lower().find(i, index)
			if index == -1:
				index = 0
				break
			found_indexes[index] = len(i)
			index += len(i)
	for i in negative_words:
		while index2 < len(text):
			index2 = text.lower().find(i, index2)
			if index2 == -1:
				index2 = 0
				break
			if text.count(i) > 1:  
				found_indexes[index2] = len(i)
			index2 += len(i)      
	found_indexes_s = sorted(found_indexes)
	found_indexes_new = {}
	for key in found_indexes_s:
		found_indexes_new[key] = found_indexes[key]
	for key, value in found_indexes_new.items():
		textn += text[idx:key] + value*'X'
		idx = key + value 
	textn += text[idx:]
	return textn

def censor_two(text):
	index = 0
	found_indexes = {}
	idx = 0
	textn = ""
	for i in proprietary_terms:
		while index < len(text):
			index = text.lower().find(i, index)
			if index == -1:
				index = 0
				break
			found_indexes[index] = len(i)
			index += len(i)
	for key, value in found_indexes.items():
		textn += text[idx:key] + value*'X'
		idx = key + value 
	textn += text[idx:]
	return textn

def censor_one(text):
	phrase = 'learning algorithms'
	index = 0
	idx = 0
	found_indexes = []
	textn = ""
	while index < len(text):
		index = text.lower().find(phrase, index)
		if index == -1:
			break
		found_indexes.append(index)
		index += len(phrase)
	for i in found_indexes:
		textn += text[idx:i] + len(phrase)*'X'
		idx = i + len(phrase)
	textn += text[idx:]  
	return textn

#for i in proprietary_terms:
#print(i)
print(email_four)
print()
print(censor_four(email_four))s