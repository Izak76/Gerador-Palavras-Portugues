import unicodedata as ud


def normalizar(txt:str) -> str:   #https://github.com/pythonprobr/palavras/blob/master/converter.py
    norm_txt = ud.normalize('NFKD', txt)
    shaved = ''.join(c for c in norm_txt if not ud.combining(c))
    return ud.normalize('NFC', shaved)


def possui_caracteres_validos(txt:str) -> bool:
    for c in map(ord, txt):
        if not ((64 < c < 91) or (96 < c <123)):
            return False
    
    return True


palavras = set()

with open("pt_BR.txt", encoding="utf-8") as arquivo:
    print("Normalizando palavras")
    for ln in iter(arquivo.readline, ""):
        ln = ln.strip()
        ln_norm = normalizar(ln)

        if possui_caracteres_validos(ln_norm):
            palavras.add(ln_norm)


print("Ordenando as palavras geradas")
palavras = sorted(palavras, key=str.lower)

with open("pt_BR-sem-acentos.txt", 'w', encoding="utf-8") as arquivo:
    print("Escrevendo arquivo")
    for palavra in palavras:
        arquivo.write("".join((palavra, "\n")))
    
    print(f'Arquivo "{arquivo.name}" criado com {len(palavras)} palavras')