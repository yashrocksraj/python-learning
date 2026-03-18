def greeting():
    return "hello"

# print(greeting(),"Glenn")
# print(greeting(),"sally")

def greet(lang):
    if lang == 'es':
        return "Hola"
    elif lang == 'fr':
        return "Bonjour"
    else:
        return "Hello"
    

print(greet('es'),'Yash')
print(greet('fr'),'Siya')
print(greet('eer'),"harshit")