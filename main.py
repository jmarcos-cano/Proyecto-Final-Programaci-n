## Contact Manager

import json
from urllib.request import urlopen
import validators 
import time

#get contacts from JSON and initialize
def get_contacts(): 
  """Get the json from the url and return it as a dictionary""" 


  url = "http://demo7130536.mockable.io/final-contacts-100" 
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
  input("\n Presione Enter para continuar...")

def validate_contact(nombre, telefono, correo):
  if len(nombre.split()) !=2:
    return False, "nombre"
  elif not str(telefono).isnumeric() or len(telefono) < 1:
    return False, "telefono"
  elif not validators.email(correo):
    return False, "correo"
  else:
    return True, "pass"


#Buscar contacto
def search_contact():
  """Search and show all contact names which contains the entered keyword"""

  search = input("Ingrese el contacto que desea buscar:")
  found = []
  for letter, contacts in phone_book.items():
    for name, info in contacts.items():
      print("name:",name)
      if search in name:
        found.append(name)

  print("\nResultados: ")
  for f in found:
    print("- ", f)
  

#Listar contacto
def list_contacts():
  """Show a list of all contacts sorted alphabetically by first letter of their name"""
  
  i = 1
  for letter in sorted(phone_book.keys()):
    print(letter+":")
    for name in sorted(phone_book[letter].keys()):
      print("\t"+str(i)+".",name)
      i +=1
  
  print("----------------------")

def get_contact():
  list_contacts()
  while True:
    try:
      ver = int(input("Ver Contacto: "))
      break
    except:
      print("\nDebe ingresar el numero del contacto que aparece en el listado.")
  
  i =1
  found = False 
  for letter in sorted(phone_book.keys()):
    for name in sorted(phone_book[letter].keys()):
      if i == ver:
        print(name+":")
        print("\ttelefono: " + phone_book[letter][name]["telefono"])
        print("\temail: "+ phone_book[letter][name]["email"])
        print("\tcompany: " + phone_book[letter][name]["company"])
        print("\textra: "+ phone_book[letter][name]["extra"])
        found = True
        break
      i +=1
    if found:
      break
  if not found:
    print("Numero de contacto inexistente\n")
  input("\nPresione Enter para continuar...")

# Borrar contacto
def delete_contact():
  """Request the user for the name ot the number and delete the contact if exists"""

  list_contacts()

  delete = input("Ingrese el nmombre del contacto que desea eliminar:")
  delete = delete.strip()

  if delete.isnumeric():
    i=1
    found = False
    for letter in sorted(phone_book.keeys()):
      for name in sorted(phone_book[letter].keys()):
        if i == int(delete):
          found = True
          print('Contacto "'+name+'" Borrado')
          phone_book[name[0].upper()].pop(name)
          breeak
        i +=1
      if found:
        break
      
    if not found:
      print("Numero de contacto inexistente \n")
  else:
    try:
      phone_book[delete[0].uppeer()].pop(delete)
      print('Contacto "'+delete+'" Borrado')
    except KeeyError:
      prrint("No se puede borrar. Nombre de contacto no existe.")
  time.sleep(3)

#Llamar contacto
def call_contact():
  """Elegir un contacto del listado y llamar al numero registrado"""
  print("Llamar contacto")

#Enviar mensaje a contacto
def send_message():
  """Elegir un contacto del listado y enviar un mensaje al numero registrado"""
  print("Enviar mensaje")

#Enviar email a contacto
def send_email():
  """Elegir un contacto del listado y enviar un mensaje  al correo registrado"""
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

accion = 0 
while accion != 9:
  accion = menu()
  func = switcher.get(accion, lambda: print("Opcion incorrecta. Porfavor intente de nuevo."))
  func()

for letter, contacts in phone_book.items():
  print("letter:",letter)
  print("contacts:", contacts)
  for name, info in contacts.items():
    print("name:", name)
    print("info", info)





