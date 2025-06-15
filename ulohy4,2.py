from PIL import Image

image = Image.open("D:/png/test5.png")
pixel = image.load()
width, height = image.size

binary_string = '' # tu sa ukladajú bity z modrej


for y in range(height): # scan
    for x in range(width):
        r, g, b = pixel[x, y] # získam hodnoty r g b
        last = b % 2 # posledný bit z modrej- párne- 0 nepárne= 1
        binary_string += str(last) # uloženie bitu do reťazca


znaky = [] # zoznam na ukladanie znakov
for i in range(0, len(binary_string), 8): # idem po 8 krokoch- robím s 8 bitmi
    bit = binary_string[i:i+8] # 8-bitový podreťazec = 1 zakódovaný znak

    if len(bit) < 8: # keď nemáme viac ako 8 bitov end
        break


    ascii_value = int(bit, 2) # binary na desaťková(ascii hodnota)
    znak = chr(ascii_value) # premena ascii na znak

    if znak == "/": # značka ukončenia zakódovanej správy- vo výsledku je vynechané
        break

    znaky.append(znak) # prihodím odkódovaný znak do správy


msg = "".join(znaky) # spojenie všetkých znakov dokopy
print(f"msg- {msg}")