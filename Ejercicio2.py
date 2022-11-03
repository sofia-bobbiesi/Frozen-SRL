import pandas as pd
from datetime import datetime, timedelta
from time import sleep

# Ejercicio 2.1
_PRODUCT_DF = pd.DataFrame({
    "product_name": ["Chocolate", "Granizado", "Limon", "Dulce de Leche"],
    "quantity": [3,10,0,5]
    })

def is_product_available(product_name, quantity):
    try:
        product = _PRODUCT_DF[_PRODUCT_DF["product_name"] == product_name]
        return product["quantity"].values[0] >= quantity
    except KeyError:
        return False

#  Ejercicio 2.2:
_RETRIES_ = {}

def is_product_available_2(product_name, quantity):
    
    if product_name + "_" + str(quantity) in _RETRIES_:
        product_time = _RETRIES_[product_name + "_" + str(quantity)]
        if product_time + timedelta(minutes=5) > datetime.now():
            print("No se puede realizar la consulta, intente más tarde")
            return

    try:
        product = _PRODUCT_DF[_PRODUCT_DF["product_name"] == product_name]
        stock = product["quantity"].values[0] >= quantity
        return stock
    except:
        stock = False
        return False
    finally:
        if not stock:
            _RETRIES_[product_name + "_" + str(quantity)] = datetime.now()
