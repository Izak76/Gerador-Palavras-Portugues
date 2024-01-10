from .regra import Regra
import re


class Prefixo(Regra):
    def _criar_padrao_regex(self, padrao:str) -> re.Pattern:
        return re.compile('^'+padrao+".*")
    
    def obter_variacoes(self, palavra:str) -> list[str]:
        novas_palavras:list[str] = [palavra]

        for pref_rem, pref_add, padrao in self._sub_regras:
            if padrao.match(palavra) and (pref_rem == "0" or palavra.startswith(pref_rem)):
                #psp -> [p]alavra [s]em [p]refixo
                if pref_rem == "0":
                    psp = palavra
                else:
                    psp = palavra[len(pref_rem):]
                
                novas_palavras.append("".join((pref_add, psp)))
        
        return novas_palavras