from django.db import models

class User:
    def __init__(self, id: int,  name: str, email: str, active: bool):    
        self.id = id
        self.name = name
        self.email = email
        self.active = active 

    def __str__(self):
        return f"id: {self.id}, name: {self.name}, email: {self.email}, active: {self.active}"