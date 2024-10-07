import math

def word_count(numb):
    return len(str(abs(numb))) #abs- absolútna hodnota, len na dĺžku

def middle_word(numb):
    mid_numb = str(numb)
    length_word = word_count(numb)
    if length_word % 2 == 1:
        stredo = length_word // 2
        return int(mid_numb[stredo])
    else:
        stredo1 = length_word // 2 -1
        stredo2 = length_word // 2
        stredo_oboje = ((int(mid_numb[stredo1])) + (int(mid_numb[stredo2]))) / 2 # priemer stredu
        return stredo_oboje


def decimal_to_binary(numb):
    if numb == 0:
        return "0"

    dvojkove = ""
    while numb > 0:
        zvysok = numb % 2
        dvojkove = (str(zvysok)) + dvojkove
        numb = numb // 2
    return dvojkove


def binary_to_decimal(binare):
    decimal = 0
    lenght = len(binare)
    for i in range(lenght):
        hodnota = int(binare[i])
        mocnina = lenght - i - 1
        decimal += hodnota * (2 ** mocnina)
    return decimal

binare_numb = "1101"
decimal_numb = binary_to_decimal(binare_numb)

#symetrické číslo- zprava aj zľava to isté
def symetria(cislo_nove):
    str_numb = str(abs(cislo_nove)) #reťazec
    return str_numb == str_numb[::-1]

cislo_symetria = 12321

cislo = 123456


#úloha č 6, stred/priemerný stred
print(middle_word(cislo))

#úloha č 7, zadané číslo v binare
print(decimal_to_binary(cislo))

#úloha č 8, čislo z 2 na 10
print(decimal_numb)

#úloha č 9, symetria
print(symetria(cislo_symetria))