from .regra import Regra
import re


class Sufixo(Regra):
    def _criar_padrao_regex(self, padrao:str) -> re.Pattern:
        return re.compile('.*'+padrao+"$")
    
    def obter_variacoes(self, palavra:str) -> list[str]:
        novas_palavras:list[str] = [palavra]

        for suf_rem, suf_add, padrao in self._sub_regras:
            if padrao.match(palavra) and (suf_rem == "0" or palavra.endswith(suf_rem)):
                #pss -> [p]alavra [s]em [s]ufixo
                if suf_rem == "0":
                    pss = palavra
                else:
                    pss = palavra[:-len(suf_rem)]
                
                novas_palavras.append("".join((pss, suf_add)))
        
        return novas_palavras