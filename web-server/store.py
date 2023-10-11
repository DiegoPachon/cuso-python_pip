import requests

def get_categories():
    r = requests.get("https://api.escuelajs.co/api/v1/categories")
    print("Categorias")
    print(r.status_code)
    #print(r.text)
    #tipo de dato
    print(type(r.text))
    categories = r.json() 
     # Obtener los primeros 10 registros
    first_10_categories = categories[:10]
    
    for category in first_10_categories:
        print (category["name"])
          