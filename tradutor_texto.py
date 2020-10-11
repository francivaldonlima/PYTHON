from googletrans import Translator
translator = Translator()


with open("texto01.txt") as file_in:
    lines = []
    for line in file_in:

        if line != '':
            lines.append(line)


palavras = []


for i in range(len(lines)):
    separa = lines[i]
    separado = separa.split()
    for i in range(len(separado)):
        x = separado[i].strip()
        z=x.lower()
        k=z.replace(",", "")
        o=k.replace(".", "")
        s=[o]
        z=set()
        

        palavras.append(o)
        print(x)
        




print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")

print(palavras)
print(type(palavras))
print(len(palavras))
print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")

print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
unico = set(palavras)
print(unico)
print(len(unico))
print(type(unico))
lista = []

for d in unico:
	print(d)
	lista.append(d)
	



#lista = [unico]
  
print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
print("****************************************************************")
print("****************************************************************")
print(lista)
print(type(lista))
print(len(lista))
print("****************************************************************")
print("****************************************************************")

translations = translator.translate(lista, dest='pt')
for translation in translations:
    print(translation.origin, ' -> ', translation.text)



print('FIM')


#pip install googletrans
#translations = translator.translate([palavras], dest='pt')
#for translation in translations:
#   print(translation.origin, ' -> ', translation.text)


