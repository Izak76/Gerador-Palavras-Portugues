import abc, re


class Regra(abc.ABC):
    def __init__(self, identificador:str):
        self._identificador = identificador
        self._sub_regras:list[tuple[str, str, re.Pattern]] = []
    
    def __repr__(self) -> str:
        return f"{type(self).__name__}(Identificador={self._identificador})"
    
    @abc.abstractmethod
    def _criar_padrao_regex(self, padrao:str) -> re.Pattern:
        pass

    def adicionar_regra(self, remover:str, adicionar:str, ocorrencia:str) -> None:
        self._sub_regras.append((remover, adicionar.split("/")[0], self._criar_padrao_regex(ocorrencia)))
    
    @abc.abstractmethod
    def obter_variacoes(self, palavra:str) -> list[str]:
        pass