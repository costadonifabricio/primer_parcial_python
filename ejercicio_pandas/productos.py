import pandas as pd

def tienda_ropas_accesorios():
    productos = [
    {"nombre": "Camiseta", "precio": 20, "cantidad_disponible":100},
    {"nombre": "Pantalón", "precio": 30, "cantidad_disponible": 80},
    {"nombre": "Zapatos", "precio": 50, "cantidad_disponible": 50},
    {"nombre": "Reloj", "precio": 100, "cantidad_disponible": 30},
    {"nombre": "Gorra", "precio": 15, "cantidad_disponible": 120},
    {"nombre": "Bufanda", "precio": 25, "cantidad_disponible": 60},
    {"nombre": "Sudadera", "precio": 40, "cantidad_disponible": 70},
    {"nombre": "Bolsa", "precio": 35, "cantidad_disponible": 90},
    {"nombre": "Chaqueta", "precio": 80, "cantidad_disponible": 40},
    {"nombre": "Gafas de sol", "precio": 45, "cantidad_disponible":25},
    {"nombre": "Calcetines", "precio": 10, "cantidad_disponible":150},
    {"nombre": "Sombrero", "precio": 20, "cantidad_disponible": 55},
    {"nombre": "Pulsera", "precio": 5, "cantidad_disponible": 200},
    {"nombre": "Pendientes", "precio": 15, "cantidad_disponible":180},
    {"nombre": "Cinturón", "precio": 20, "cantidad_disponible":100},
    {"nombre": "Vestido", "precio": 60, "cantidad_disponible": 35},
    {"nombre": "Corbata", "precio": 25, "cantidad_disponible": 75},
    {"nombre": "Bolso", "precio": 70, "cantidad_disponible": 45},
    {"nombre": "Paraguas", "precio": 30, "cantidad_disponible": 65},
    {"nombre": "Collar", "precio": 40, "cantidad_disponible": 85},
    ]

    # Se crea un DataFrame llamado df_productos con dos columnas
    df_productos = pd.DataFrame(productos, columns=["nombre", "cantidad_disponible"])

    # Se agrego una nueva columna llamada precio ya que en el DataFrame solo pedia Columnas de nombre y cantidad_disponible
    df_productos["precio"] = [20, 30, 50, 100, 15, 25, 40, 35, 80, 45, 10, 20, 5, 15, 20, 60, 25, 70, 30, 40]

    # Valor total del inventario (precio * cantidad_disponible) para cada producto
    df_productos["valor_total_inventario"] = df_productos["precio"]*df_productos["cantidad_disponible"]
    # El valor total del inventario sumando el valor total de cada producto.
    df_productos["valor_total_suma_productos"] = df_productos["precio"].cumsum() * df_productos["cantidad_disponible"]

    # Simulacion de ventas de todos los productos, si quiere realizar mas ventas reemplaz el nnumero 1 por otro valor
    df_productos["Productos_Vendidos"] = df_productos["cantidad_disponible"] - df_productos["cantidad_disponible"] + 1 
    # Aqui se resta la cantidad de unidad vendidas al total disponible de cada producto 
    df_productos["cantidad_disponible"] = df_productos["cantidad_disponible"] - df_productos["Productos_Vendidos"]
    return df_productos
# Se imprime los resultados
print(tienda_ropas_accesorios())