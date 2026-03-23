from locust import HttpUser, task, between
import random

class AutorUser(HttpUser):

    wait_time = between(1, 2)

    @task
    def criar_e_buscar_autor(self):

        # cria autor
        response = self.client.post("/autores", json={
            "nome": "Autor Teste"
        })

        # depois lista autores
        self.client.get("/autores")
