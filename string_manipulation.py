###Changing case in a string whith Methods
##A method is an action that python can perform on a piece of data.
##The dot(.) after the variable (name)tells python to allow the title()
##method to act on variable (name).
name = "ada lovelace"
print(name.title())  

###string concatenation

first_name = "Zachariah"
last_name = "Aondowase"
full_name = first_name + ' ' + last_name
message = "Hello" + " " + full_name + "!"
print(message) 

###To remove whitespace from a string, use the rstrip(), lstrip(), or strip() methods.
###To remove the whitespaces permanently, you have to assign the stripped value back
##into the variable.
###A syntax error occurs when python encounters code that does not follow the proper
###stuctural rules of the language. 
greetings = "Good morning "
print(greetings.rstrip())