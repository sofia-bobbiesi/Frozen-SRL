import pandas as pd
# Ejercicio 2.1
_PRODUCT_DF = pd.DataFrame({"product_name": ["Chocolate", "Granizado",
"Limon", "Dulce de Leche"], "quantity": [3,10,0,5]})
def is_product_available(product_name, quantity):
    pass


""" Ejercicio 2.2:
Si miramos el diagrama de flujo al momento de la decisión de stock, encontramos un
potencial loop infinito, ya que el usuario podría continuar ingresando productos inválidos
o sin stock. Reformule la función para solucionar este problema. """