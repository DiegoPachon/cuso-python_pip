import requests

def get_products():
    r = requests.get("https://api.escuelajs.co/api/v1/products")
    print("Productos")
    print(r.status_code)
    #print(r.text)
    #tipo de dato
    print(type(r.text))
    products = r.json() 
    
     # Obtener los primeros 10 registros
    first_10_products = products[:10]
    
    # Imprimir los primeros 10 registros
    for product in first_10_products:
        print (product["title"])

    #for product in first_10_products:
     #   print (product["title"])
          