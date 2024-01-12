from io import TextIOWrapper
from regras import *


regras: dict[str, Regra] = {}
tipos: dict[str, type[Regra]] = {"PFX": Prefixo, "SFX": Sufixo}
palavras: list[str] = []


def obter_regras(arquivo: TextIOWrapper):
    ln: str = arquivo.readline()

    while ln:
        ln = ln.strip()

        if not (ln and (ln.startswith("PFX") or ln.startswith("SFX"))):
            ln = arquivo.readline()
            continue

        tipo, identif, modo, qtde = ln.split()
        r = tipos[tipo](identif)

        for _ in range(int(qtde)):
            sr = arquivo.readline().strip().split()
            r.adicionar_regra(sr[2], sr[3], sr[4])

        regras[identif] = r
        ln = arquivo.readline()


def gerar_palavras(arquivo: TextIOWrapper):
    arquivo.readline()

    for ln in iter(arquivo.readline, ""):
        ln = ln.strip()
        try:
            palavra, rgs = ln.split("/")
            for rg in rgs:
                if rg != "Ý":
                    palavras.extend(regras[rg].obter_variacoes(palavra))

        except ValueError:
            palavras.append(ln)


if __name__ == "__main__":
    with open("pt_BR.aff", encoding="iso8859-1") as arquivo:
        print("Lendo arquivo de regras")
        obter_regras(arquivo)

    with open("pt_BR.dic", encoding="iso8859-1") as arquivo:
        print("Gerando palavras a partir das regras")
        gerar_palavras(arquivo)

    print("Ordenando as palavras geradas")
    palavras.sort(key=str.lower)

    with open("pt_BR.txt", "w", encoding="utf-8") as arquivo:
        print("Escrevendo arquivo")
        for palavra in palavras:
            arquivo.write("".join((palavra, "\n")))

        print(f'Arquivo "{arquivo.name}" criado com {len(palavras)} palavras')
