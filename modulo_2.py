# Demostración del método capitalize():
print('aBcD'.capitalize())

print("Alpha".capitalize())
print('ALPHA'.capitalize())
print(' Alpha'.capitalize())
print('123'.capitalize())
print("αβγδ".capitalize())
print()
# Demostración del método center():
print('[' + 'alpha'.center(10) + ']')
print()
print('[' + 'Beta'.center(2) + ']')
print('[' + 'Beta'.center(4) + ']')
print('[' + 'Beta'.center(6) + ']')
print()
print('[' + 'gamma'.center(20, '*') + ']')

print()

# Demostración del método endswith():
if "epsilon".endswith("on"):
    print("si")
else:
    print("no")
  
print()
  
t = "zeta"
print(t.endswith("a"))
print(t.endswith("A"))
print(t.endswith("et"))
print(t.endswith("eta"))

print()

# Demostración del método find():
print("Eta".find("ta"))
print("Eta".find("mma"))
t = 'theta'
print(t.find('eta'))
print(t.find('et'))
print(t.find('the'))
print(t.find('ha'))
print('kappa'.find('a', 2))
print()
print()

the_text = """A variation of the ordinary lorem ipsum
text has been used in typesetting since the 1960s 
or earlier, when it was popularized by advertisements 
for Letraset transfer sheets. It was introduced to 
the Information Age in the mid-1980s by the Aldus Corporation, 
which employed it in graphics and word-processing templates
for its desktop publishing program PageMaker (from Wikipedia)"""

fnd = the_text.find('the')
while fnd != -1:
    print(fnd)
    fnd = the_text.find('the', fnd + 1)

print()
print()

print('kappa'.find('a', 1, 4))
print('kappa'.find('a', 2, 4))

print()
print()

# Demostración del método isalnum():
print('lambda30'.isalnum())
print('lambda'.isalnum())
print('30'.isalnum())
print('@'.isalnum())
print('lambda_30'.isalnum())
print(''.isalnum())

t = 'Six lambdas'
print(t.isalnum())

t = '&Alpha;&beta;&Gamma;&delta;'
print(t.isalnum())

t = '20E1'
print(t.isalnum())

print()
print()

# Ejemplo: Demostración del método isalpha():
print("Moooo".isalpha())
print('Mu40'.isalpha())

print()
print()

# Ejemplo: Demostración del método isdigit():
print('2018'.isdigit())
print("Year2019".isdigit())

print()
print()

# Ejemplo: Demostración del método islower():
print("Moooo".islower())
print('moooo'.islower())

print()
print()

# Ejemplo: Demostración del método isspace():
print(' \n '.isspace())
print(" ".isspace())
print("mooo mooo mooo".isspace())

print()
print()

# Ejemplo: Demostración del método isupper():
print("Moooo".isupper())
print('moooo'.isupper())
print('MOOOO'.isupper())

print()
print()

# Demostración del método join():
print(",".join(["omicron", "pi", "rho"]))

print()
print()

# Demostración del método lower():
print("SiGmA=60".lower())

print()
print()

# Demostración del método lstrip():
print("[" + " tau ".lstrip() + "]")

print()

print("www.cisco.com".lstrip("w."))
print("pythoninstitute.org".lstrip(".org"))

print()
print()

# Demostración del método replace():
print("www.netacad.com".replace("netacad.com", "pythoninstitute.org"))
print("This is it!".replace("is", "are"))
print("Apple juice".replace("juice", ""))
print()
print("This is it!".replace("is", "are", 1))
print("This is it!".replace("is", "are", 2))

print()
print()

# Demostración del método rfind():
print("tau tau tau".rfind("ta"))
print("tau tau tau".rfind("ta", 9))
print("tau tau tau".rfind("ta", 3, 9))
 
print()
print()
 
# Demostración del método rstrip():
print("[" + " upsilon ".rstrip() + "]")
print("cisco.com".rstrip(".com"))

print()
print()

# Demostración del método split():
print("phi       chi\npsi".split())

print()
print()
# Demostración del método startswith():
print("omega".startswith("meg"))
print("omega".startswith("om"))

print()
print()

# Demostración del método strip():
print("[" + "   aleph   ".strip() + "]")

print()
print()

# Demostración del método swapcase():
print("Yo solo sé que no sé nada".swapcase())

print()
print()

# Demostración del método title():
print("Yo solo sé que no sé nada. Parte 1.".title())

print()
print()

# Demostración del método upper():
print("Yo solo sé que no sé nada. Parte 2.".upper())


# 1. Algunos de los métodos que ofrecen las cadenas son:

# capitalize(): cambia todas las letras de la cadena a mayúsculas.
# center(): centra la cadena dentro de una longitud conocida.
# count(): cuenta las ocurrencias de un carácter dado.
# join(): une todos los elementos de una tupla/lista en una cadena.
# lower(): convierte todas las letras de la cadena en minúsculas.
# lstrip(): elimina los caracteres en blanco al principio de la cadena.
# replace(): reemplaza una subcadena dada con otra.
# rfind(): encuentra una subcadena comenzando por el final de la cadena.
# rstrip(): elimina los caracteres en blanco al final de la cadena.
# split(): divide la cadena en una subcadena usando un delimitador dado.
# strip(): elimina los espacios en blanco iniciales y finales.
# swapcase(): intercambia las mayúsculas y minúsculas de las letras.
# title(): hace que la primera letra de cada palabra sea mayúscula.
# upper(): convierte todas las letras de la cadena en mayúsculas.

# 2. El contenido de las cadenas se puede determinar mediante los siguientes métodos (todos devuelven valores booleanos):

# endswith(): ¿La cadena termina con una subcadena determinada?
# isalnum(): ¿La cadena consta solo de letras y dígitos?
# isalpha(): ¿La cadena consta solo de letras?
# islower(): ¿La cadena consta solo de letras minúsculas?
# isspace(): ¿La cadena consta solo de espacios en blanco?
# isupper(): ¿La cadena consta solo de letras mayúsculas?
# startswith(): ¿La cadena consta solo de letras mayúsculas?
       
print()
print()

def mysplit(string):
    # Inicializamos una lista vacía para almacenar las palabras divididas
    words = []
    
    # Verificamos si la cadena está vacía
    if not string:
        return words  # Devolvemos la lista vacía si la cadena está vacía
    
    # Inicializamos un índice para rastrear el inicio de la próxima palabra
    start_index = 0
    
    # Iteramos a través de la cadena
    for i, char in enumerate(string):
        # Si encontramos un espacio en blanco o estamos al final de la cadena
        if char.isspace() or i == len(string) - 1:
            # Agregamos la palabra actual a la lista de palabras
            words.append(string[start_index:i+1].strip())
            
            # Actualizamos el índice de inicio para la próxima palabra
            start_index = i + 1
    
    return words

# Ejemplos de uso
print(mysplit("Hola mundo"))  # Output: ['Hola', 'mundo']
print(mysplit("Esta es una cadena"))  # Output: ['Esta', 'es', 'una', 'cadena']
print(mysplit(""))  # Output: []

print()
print()

'10' == 10
'10' != 10
'10' == 1
'10' != 1
#'10' > 10

print()
print()

# Demostración de la función sorted():
first_greek = ['omega', 'alpha', 'pi', 'gamma']
first_greek_2 = sorted(first_greek)

print(first_greek)
print(first_greek_2)

print()
print()

# Demostración del método sort():
second_greek = ['omega', 'alpha', 'pi', 'gamma']
print(second_greek)

second_greek.sort()
print(second_greek)

print()
print()

itg = 13
flt = 1.3
si = str(itg)
sf = str(flt)

print(si + ' ' + sf)

print()
print()

si = '13'
sf = '1.3'
itg = int(si)
flt = float(sf)

print(itg + flt)


print()
print()

def create_digit_leds():
    # Definimos los patrones de LEDs para cada dígito del 0 al 9
    digits = {
        '0': [" ### ",
              "#   #",
              "#   #",
              "#   #",
              "#   #",
              "#   #",
              " ### "],
        '1': ["    #",
              "    #",
              "    #",
              "    #",
              "    #",
              "    #",
              "    #"],
        '2': [" ### ",
              "#   #",
              "    #",
              " ### ",
              "#    ",
              "#    ",
              " ### "],
        '3': [" ### ",
              "#   #",
              "    #",
              " ### ",
              "    #",
              "#   #",
              " ### "],
        '4': ["#   #",
              "#   #",
              "#   #",
              " ### ",
              "    #",
              "    #",
              "    #"],
        '5': [" ### ",
              "#    ",
              "#    ",
              " ### ",
              "    #",
              "#   #",
              " ### "],
        '6': [" ### ",
              "#    ",
              "#    ",
              " ### ",
              "#   #",
              "#   #",
              " ### "],
        '7': [" ### ",
              "#   #",
              "    #",
              "    #",
              "    #",
              "    #",
              "    #"],
        '8': [" ### ",
              "#   #",
              "#   #",
              " ### ",
              "#   #",
              "#   #",
              " ### "],
        '9': [" ### ",
              "#   #",
              "#   #",
              " ### ",
              "    #",
              "    #",
              " ### "],
    }
    return digits

def display_number(number):
    digits_leds = create_digit_leds()
    number_str = str(number)
    for row in range(7):  # Hay 7 filas de LEDs
        digit_line = ""
        for digit in number_str:
            digit_line += digits_leds[digit][row] + "  "  # Añadimos 2 espacios entre cada dígito
        print(digit_line)

# Ejemplo de uso
display_number(33)

print()
print()

# Cifrado César.
text = input("Ingresa tu mensaje: ")
cipher = ''
for char in text:
    if not char.isalpha():
        continue
    char = char.upper()
    code = ord(char) + 1
    if code > ord('Z'):
        code = ord('A')
    cipher += chr(code)

print(cipher)

print()
print()

# Cifrado César - descifrando un mensaje.
cipher = input('Ingresa tu criptograma: ')
text = ''
for char in cipher:
    if not char.isalpha():
        continue
    char = char.upper()
    code = ord(char) - 1
    if code < ord('A'):
        code = ord('Z')
    text += chr(code)

print(text)

print()
print()

#Procesador de Números.

line = input("Ingresa una línea de números, sepáralos con espacios: ")
strings = line.split()
total = 0
try:
    for substr in strings:
        total += float(substr)
    print("El total es:", total)
except:
    print(substr, "no es un numero.")
    
    
print()
print()

# Validador IBAN.

iban = input("Ingresa un IBAN, por favor: ")
iban = iban.replace(' ','')

if not iban.isalnum():
    print("Has introducido caracteres no válidos.")
elif len(iban) < 15:
    print("El IBAN ingresado es demasiado corto.")
elif len(iban) > 31:
    print("El IBAN ingresado es demasiado largo.")
else:
    iban = (iban[4:] + iban[0:4]).upper()
    iban2 = ''
    for ch in iban:
        if ch.isdigit():
            iban2 += ch
        else:
            iban2 += str(10 + ord(ch) - ord('A'))
    iban = int(iban2)
    if iban % 97 == 1:
        print("El IBAN ingresado es válido.")
    else:
        print("El IBAN ingresado no es válido.")
        
        
    


 
    
