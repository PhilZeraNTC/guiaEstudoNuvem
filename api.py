from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Hello World"}

class Sorvete(BaseModel):
    id: int
    sabor: str

sorvetes = [
    Sorvete(id=1, sabor='Chocolate'),
    Sorvete(id=2, sabor='Morango')
]

@app.get("/sorvetes/", response_model=list[Sorvete])
def obter_sorvetes():
    return sorvetes

@app.post("/sorvetes/", response_model=Sorvete)
def adicionar_sorvete(sorvete: Sorvete):
    sorvetes.append(sorvete)
    return sorvete

@app.put("/sorvetes/{sorvete_id}/", response_model=Sorvete)
def atualizar_sorvete(sorvete_id: int, novo_sorvete: Sorvete):
    for sorvete in sorvetes:
        if sorvete.id == sorvete_id:
            sorvete.sabor = novo_sorvete.sabor
            return sorvete

@app.delete("/sorvetes/{sorvete_id}/")
def excluir_sorvete(sorvete_id: int):
    for i, sorvete in enumerate(sorvetes):
        if sorvete.id == sorvete_id:
            del sorvetes[i]
            return