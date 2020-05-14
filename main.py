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

#Llamar contacto
def call_contact():
  print("Llamar contacto")

#Enviar mensaje a contacto
def send_message():
  print("Enviar mensaje")

#Enviar email a contacto
def send_email():
  print("Enviar email")

#Exportar contactos 
def export_contacts():
  print("Exportar")

#exit
def exit():
  print("Salir del programa")

#Menu
def menu():
  print("------ Agenda Telefonica --------")
  print("1. Ingresar contacto")
  print("2. Buscar contacto")
  print("3. Lista contactos")
  print("4. Borrar contacto")
  print("5. Llamar contacto")
  print("6. Enviar mensaje a contacto")
  print("7. Enviar email a contacto")
  print("8. Exportar contactos")
  print("9. Salir")

  try: 
    op = int(input("Escoja una opcion: "))
    return op
  except:
    print("Opcion incorrecta. Porfavor ingrese otra vez.")
    return None
  
contacts = get_contacts()

switcher = {
  1: add_contact,
  2: search_contact,
  3: list_contacts,
  4: delete_contact,
  5: call_contact,
  6: send_message,
  7: send_email,
  8: export_contacts,
  9: exit,
}

accion = 0 
while accion != 9:
  accion = menu()
  func = switcher.get(accion, lambda: print("Opcion incorrecta, intente de nuevo."))
  func()



