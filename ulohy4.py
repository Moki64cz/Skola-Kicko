from PIL import Image

image = Image.open("D:/png/test.png") # obrazok musí byť v rovnakom priečinku, musí byť Image nie image- lebo ano
pixel = image.load() # načítanie obrázku
width, height = image.size # zistim si veľkosti

msg = "Biely papier/" # 13 znakov - výsledok musí byť 104 bitov

binary_string = '' # spravenie prázdneho reťazcu
for znak in msg: # po poradí každý znak v správe
    ascii_value = ord(znak) # ord vracia Ascii hodnotu znaku
    binary_znak = format(ascii_value, '08b') # 8 bitová hodnota binary
    binary_string += binary_znak # pridanie znakov do stringu


print(f"Test- Binary reťazec- (({len(binary_string)} bitov): {binary_string}") # (f" formátovaný reťazec- nech mi ide zátvorky


bit_index = 0 # index- poradie


for y in range (height):
    for x in range (width): # double cyklus prejdem obe osi x y
        if bit_index >= len(binary_string): # ukončenie keď sa dĺžky rovnajú- keď sme hotovy
            break

        r, g, b = pixel[x, y]
        bit = int(binary_string[bit_index]) # zoberem bit z binary reťazca a dameho na číslo

        if bit == 0: # keď je nula, tak b musi byť párne
            if b % 2 != 0:
                b -= 1

        else: # keď je 1 tak musí byť nepárne
            if b % 2 == 0:
                b += 1


        pixel[x, y] = (r, g, b) # prepísanie nových hodnôť
        bit_index += 1 # posunieme sa na ďalší bit


    if bit_index >= len(binary_string): # keď prejdem cely cyklus koniec
        break

image.save("D:/png/test5.png") # uložený obrázok s novym nazvom, ako nový súbor
