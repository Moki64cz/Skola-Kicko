from PIL import Image

image = Image.open("D:/png/raid.jpg").convert("L") # .covert("L") to proste hodí do sivej
pixels = image.load()
width, height = image.size

# 2D zoznam(tabulka) všetkych pixelov v čislach- na desatine
pixelo_matrix = ([[pixels[x, y] for x in range(width)] for y in range(height)])

for y in range(height):
    for x in range(width):
        old = pixelo_matrix[y][x]
        new = 0 if old < 128 else 255 # porovnávame či je pixel bližšie k hodnote black/0 alebo white/255
        pixels[x, y] = new #zapísanie nového pixelu
        rozdiel = old - new # získanie rozdielu pre temnú mágiu

# temná mágia- náš zámer je znížiť celkový počet farieb na obrázku- pomocou Floyd zabezpečíme že image vyzerá dobre aj
# po znížení farieb-farebný rozadiel posunie na susedné pixly-"pravidelne" rozmiestny rozdiel do priestoru-optický klam

        if x + 1 < width: # temná mágia
            pixelo_matrix[y][x+1] += rozdiel * 7 / 16
        if x - 1 >= 0 and y + 1 < height:
            pixelo_matrix[y + 1][x - 1] += rozdiel * 3 / 16
        if y + 1 < height:
            pixelo_matrix[y + 1][x] += rozdiel * 5 / 16
        if x + 1 < width and y + 1 < height:
            pixelo_matrix[y + 1][x + 1] += rozdiel * 1 / 16

image.save("D:/png/raid2.jpg") # uložíme

