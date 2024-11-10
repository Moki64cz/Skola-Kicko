
def preklad(vtacik: str) -> str:  # šípka určuje čo je výstup
    samohlasky = "aeiouy"
    výsledok = []
    i = 0


    while i < len(vtacik):
        if vtacik[i] == ' ':
            výsledok.append(' ') #preskočim medzeru inak sa zastavi cyklus
            i += 1

        elif vtacik[i] in samohlasky:
            výsledok.append(vtacik[i]) # pridanie do výsledku
            i += 3 # ak samohláska tak skip dve písmena
        else:
            výsledok.append(vtacik[i]) # pridanie samohlasok
            # ak je to spoluhláska skip jedna samohlas
            i += 2

    return ''.join(výsledok) # pospája výsledky do jedného slova


vtacik = input("Zadaj vetu v vtáčkovom jazyku: ")

# preklad
preložené = preklad(vtacik)

print("Preložená veta:", preložené)