# Gerador de palavras do português

Programa escrito em Python para geração de uma lista de palavras (e suas respectivas variações) do português a partir de um dicionário de palavras (`pt_BR.dic`) e um dicionário de regras de variação (`pt_BR.aff`).

Os dicionários foram obtidos do seguinte repositório: [https://github.com/uefs/dic-ptbr-latex](https://github.com/uefs/dic-ptbr-latex).

Nesse repositorio seguem 2 scripts:
- `gerar dicionario.py`: Gera um arquivo `pt_BR.txt` com todas as palavras e suas respectivas variações. Ao todo são gerados 8318832 palavras (usando os dicionários presentes nesse repositório)
- `conversor sem acentos.py`: A partir do arquivo `pt_BR.txt` gerado pelo programa anterior, gera um novo arquivo, chamado de `pt_BR-sem-acentos.txt`, que contém todas as palavras do arquivo anterior normalizadas para ASCII (Ex.: "alçapão" -> "alcapao"). Palavras que possuam hífen (`-`) ou ponto (`.`) foram removidas.