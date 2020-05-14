## Contact Manager

import json
from urllib.request import urlopen

def get_contacts(): 
  url = "http://demo7130536.mockable.io/contacts"
  response = urlopen(url)
  data = json.loads(response.read())
  return(data)

#Añadir contacto
def add_contact():
  print("Añadir contacto")

#Buscar contacto
def search_contact():
  print("Listar contactos")
  print(contacts)

# Borrar contacto
def delete_contact():
  print("Borrar contacto")

#Listar contacto
def list_contacts():
  print("Listar contactos")
  print(contacts)






