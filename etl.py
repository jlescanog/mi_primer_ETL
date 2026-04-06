import pandas as pd 
import glob
import os

# Verificar que existen los archivos CSV descargados
archivos = glob.glob('data/ecommerce_*.csv')
if not archivos:
    print("❌ No se encontraron los archivos. Asegurate de descargarlos en la carpeta data/")
    print("   Deberías tener: ecommerce_orders.csv, ecommerce_customers.csv, etc.")
else:
    print(f"📂 Archivos encontrados: {len(archivos)}")
    for f in sorted(archivos):
        print(f"  - {os.path.basename(f)}")

# Cargando los csv principales:

df_orders = pd.read_csv('data/ecommerce_orders.csv')
df_order_items = pd.read_csv('data/ecommerce_order_items.csv')
df_customers = pd.read_csv('data/ecommerce_customers.csv')
df_products = pd.read_csv('data/ecommerce_products.csv')

# Explorando csv

print(f"\n📊 Resumen:")
print(f"Orders: {len(df_orders)} filas, {len(df_orders.columns)} columnas")
print(f"Order Items: {len(df_order_items)} filas")
print(f"Customers: {len(df_customers)} filas")
print(f"Products: {len(df_products)} filas")

print("\n🔍 Primeras filas de orders:")
print(df_orders.head())
print("\n📋 Info de orders:")
print(df_orders.info())

# Identificando valores nulos

print("\n❌ Valores nulos:")
print(df_orders.isnull().sum())
print(df_order_items.isnull().sum())
print(df_customers.isnull().sum())
print(df_products.isnull().sum())

# Valores nulos solo en:
# df_orders
# promotion_id        3784
# notes               4188

#Ejemplos: eliminando filas con nulos df.dropna
df_orders_elimnando = df_orders.dropna(subset=['promotion_id', 'notes'])

#Ejemplo: rellenando valores nulos con un valor específico df.fillna
df_orders_rellenando = df_orders.fillna({'promotion_id': 0, 'notes': 'Sin información'})

print(f"Filas antes: {len(df_orders)}")
print(f"Filas después (eliminando nulos): {len(df_orders_elimnando)}")
print(f"Filas después (rellenando nulos): {len(df_orders_rellenando)}")

# Salida:
# Filas antes: 5000
# Filas después (eliminando nulos): 199
# Filas después (rellenando nulos): 5000

#Rellenamos con 0 para no dismiuir el tamaño del dataset!!

df_orders = df_orders_rellenando.copy()
print(df_orders.isnull().sum())



