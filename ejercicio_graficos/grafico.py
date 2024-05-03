import pandas as pd
import matplotlib.pyplot as plt
import ejercicio_pandas

df_productos = pd.DataFrame(productos, columns=[{"nombre", "cantidad_disponible"}])

plt.plot(df["nombre"], df["cantidad_disponible"])
plt.title("Título con pandas")
plt.show()
