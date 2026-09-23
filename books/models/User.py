from django.db import models

class User(models.Model):
    def _init_(self, name, email, password, active):
        self.name = name
        self.email = email
        self.password = password
        self.active = active 