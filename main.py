## Contact Manager

import json
from urllib.request import urlopen
import validators 
import time

#get contacts from JSON and initialize
def get_contacts(): 
  """Get the json from the url and return it as a dictionary""" 

  #Change url valuee with the final url
  url = "http://demo7130536.mockable.io/contacts" 
  response = urlopen(url)
  data = json.loads(response.read())
  return(data)

phone_book = get_contacts()

#Añadir contacto
def add_contact():
  """Request the user to input all contact needed values and add it tio the contacts dictionary"""

  nombre = input("Ingrese el nombre del contacto: ")
  telefono = input("Ingrese el telefono del contacto:")
  correo = input("Ingrese el correo del contacto")
  empresa = input("(Opcional) Ingrese la empresa del contacto")
  extra = input("(Opcional) Ingrese infirmacion adicional del contacto")

  isOK, stage = validate_contact(nombre, telefono, correo)
  while isOK == False:
    if stage == "nombre":
      print("\n Nombre invalido. El nombre del contacto debe tener 2 palabras")
      nombre  = input("Ingrese el nombre del contacto: ")
    elif stage == "telefono":
      print("\n Telefono invalido. El numero de telefono debe incluir solo numeros")
      telefono= input("Ingrese el telefono del contacto:")
    elif stage == "correo":
      print("\n Correo invalido. El correo debe tener la forma -> ejemplo@example.org")
      correo = input("Ingrese el correo del contacto:")
    isOK, stage = validate_contact(nombre, telefono, correo)
  nombre =  nombre.strip()
  correo = correo.strip()
  contact = {
    "telefono": telefono,
    "correo": correo,
    "empresa": empresa,
    "extra": extra
  }

  try:
    old = phone_book[nombre[0].upper()]

    old[nombre] = contact
  except KeyError:
    phone_book[nombre[0].upper()] = {nombre: contact}
  print("\n Usuario agregado con exito!")
  time.sleep(2)

def validate_contact(nombre, telefono, correo):
  if len(nombre.split()) !=2:
    return False, "nombre"
  elif not str(telefono).isnumeric() or len(telefono) < 1:
    return False, "telefono"
  elif not validators.email(correo):
    return False, "correo"
  else:
    return True, "pass"

add_contact()

#Buscar contacto
def search_contact():
  """Search and show all contact names which contains the entered keyword"""

  print("Buscar contacto")
  print(contacts)

#Listar contacto
def list_contacts():
  """Show a list of all contacts sorted alphabetically by first letter of their name"""

  print("Listar contactos")
  print(contacts)

# Borrar contacto
def delete_contact():
  """Request the user for the name ot the number and delete the contact if exists"""
  print("Borrar contacto")

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
def exit_program():
  print("Va a salir de su agenda telefonica...")
  exit()

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
    print("Opcion incorrecta. Porfavor intete otra vez.")
    return None
  
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

"""
accion = 0 
while accion != 9:
  accion = menu()
  func = switcher.get(accion, lambda: print("Opcion incorrecta. Porfavor intente de nuevo."))
  func()

"""

for letter, contacts in phone_book.items():
  print("letter:",letter)
  print("contacts:", contacts)
  for name, info in contacts.items():
    print("name:", name)
    print("info", info)



