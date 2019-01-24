def reverse(text):
	return text[::-1]

def is_palindrome(text):
	return text == reverse(text)
	
def removeSigns(text):
	signList = [r".",r"?",r"!",r":",r";",r"-",r"_",r"(",r")",r"{",r"}",r"[",r"]",r"'",r'"',"/",","," "]
	for sign in signList:
		text = text.replace(sign,"")
	return text
	
something = raw_input("Enter text:")
aux = removeSigns(something)
if is_palindrome(aux):
	print("Yes, it is a palindrome ({})".format(aux))
else:
	print("No, it is not a palindrome ({})".format(aux))