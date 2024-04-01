import requests

SERVICE_HOST = 'localhost'
SERVICE_HOST_PORT='4999'
SERVICE_STUDENT_PATH = '/api/restaurants'

def get_endpoint():
    return 'http://'+ SERVICE_HOST+':'+SERVICE_HOST_PORT

def get_restaurants():
    response = requests.get(get_endpoint()+SERVICE_STUDENT_PATH)
    if response.json:
        print(response.json())

def create_restaurant(data):
    response = requests.post(get_endpoint()+SERVICE_STUDENT_PATH, json=data)
    if response.status_code == 200:
        print("Restaurante criado com sucesso!")
    else:
        print("Falha ao criar restaurante. Código de status:", response.status_code)

def get_restaurant(restaurant_id):
    response = requests.get(get_endpoint()+SERVICE_STUDENT_PATH+'/'+str(restaurant_id))
    if response.json:
        print(response.json())

def find_restaurant(cityName):
    response = requests.get(get_endpoint()+SERVICE_STUDENT_PATH+'?cityName='+str(cityName))
    if response.json:
        print(response.json())

def delete_restaurant(restaurant_id):
    response = requests.delete(get_endpoint() +SERVICE_STUDENT_PATH+'/'+ str(restaurant_id))
    if response.status_code == 200:
        print("Restaurant deleted successfully.")
    else:
        print("Failed to delete restaurant.")

def update_restaurant(restaurant_id, data):
    response = requests.put(get_endpoint()+SERVICE_STUDENT_PATH+'/'+str(restaurant_id), json=data)
    if response.status_code == 200:
        print("Restaurant updated!")
        # print(response.json())  # Se desejar, imprima a resposta do servidor
    else:
        print("Error:", response.status_code)
        # print(response.text)  # Imprime a mensagem de erro retornada pelo servidor, se houver

def print_menu():
    print("\nOPTIONS:")
    print("> Type 'L' to list restaurants")
    print("> Type 'C' to create a restaurant")
    print("> Type 'R' to read a restaurant")
    print("> Type 'E' to edit a restaurant")
    print("> Type 'D' to delete a restaurant")
    print("> Type 'F' to find a restaurant by city")
    print("> Type 'Q' to quit\n")

def input_restaurant_data():
    name = input("Name: ")
    postalCode = input("Postal Code: ")
    streetAddress = input("Street Address: ")
    addressLocality = input("Locality: ")
    addressRegion = input("Region: ")
    addressCountry = input("Country: ")
    url = input("URL: ")
    menu = input("Menu: ")
    telephone = input("Telephone: ")
    priceRange = input("Price Range: ")
    return {
        "name": name,
        "address": {
            "postalCode": postalCode,
            "streetAddress": streetAddress,
            "addressLocality": addressLocality,
            "addressRegion": addressRegion,
            "addressCountry": addressCountry
        },
        "url": url,
        "menu": menu,
        "telephone": telephone,
        "priceRange": priceRange
    }

exit_flag = False
while not exit_flag:
    print_menu()
    command = input("Command: ")
    if command.upper() == 'L':
       get_restaurants()
    elif command.upper() == 'C':
        data = input_restaurant_data()
        create_restaurant(data)
    elif command.upper() == 'R':
        id = input("Type id number: ")
        try:
            get_restaurant(id)
        except ValueError:
            print("Invalid command. Please try again.")
    elif command.upper() == 'E':
        id = input("Type id number: ")
        try:
            get_restaurant(id)
            data = input_restaurant_data()
            update_restaurant(id, data)
        except ValueError:
            print("Invalid command. Please try again.")
    elif command.upper() == 'D':
        id = input("Type id number: ")
        try:
            delete_restaurant(id)
        except ValueError:
            print("Invalid command. Please try again.")
    elif command.upper() == 'F':
        cityName = input("City name: ")
        find_restaurant(cityName)
    elif command.upper() == 'Q':
        exit_flag = True