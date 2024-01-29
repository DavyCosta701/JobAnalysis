from dataclasses import dataclass, field, asdict
import pandas as pd

@dataclass
class Vaga:
    nome: str = None
    descricao: str = None
    

@dataclass
class ListaVagas:
    lista_vagas: list[Vaga] = field(default_factory=list)
    
    def get_dataframe(self):
        return pd.json_normalize((asdict(vaga) for vaga in self.lista_vagas), sep="_")
    
    def save_to_csv(self, filename):
        self.get_dataframe().to_csv(f"{filename}.csv")
        

