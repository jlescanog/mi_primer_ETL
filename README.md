# Mi Primer ETL - E-commerce Data Pipeline

## Objetivos

Este proyecto implementa un pipeline ETL (Extract, Transform, Load) completo para procesar datos de un sistema de e-commerce. El objetivo es demostrar cómo extraer datos de archivos CSV, limpiarlos y transformarlos, y finalmente cargarlos en formatos listos para análisis, como CSV y Parquet.

### Funcionalidades:
- **Extracción**: Carga datos de múltiples tablas CSV (orders, order_items, customers, products, categories).
- **Transformación**: Limpia datos eliminando nulos y duplicados, corrige tipos de datos y agrega campos calculados como mes de orden y indicador de alto valor.
- **Carga**: Guarda los datos limpios en CSV y Parquet, además de métricas agregadas (ventas por cliente y por mes).

## Requisitos

- Python 3.8 o superior
- Entorno virtual recomendado

## Instalación y Configuración

1. **Clona o descarga el proyecto** en tu máquina local.

2. **Crea un entorno virtual** (opcional pero recomendado):
   ```
   python -m venv venv
   ```

3. **Activa el entorno virtual**:
   - En Windows: `.\venv\Scripts\Activate.ps1`
   - En macOS/Linux: `source venv/bin/activate`

4. **Instala las dependencias**:
   ```
   pip install -r requirements.txt
   ```

5. **Asegúrate de que los archivos de datos estén en la carpeta `data/`**:
   - ecommerce_orders.csv
   - ecommerce_order_items.csv
   - ecommerce_customers.csv
   - ecommerce_products.csv
   - ecommerce_categories.csv

## Ejecución

Ejecuta el script principal:
```
python etl.py
```

El script mostrará el progreso de cada etapa (Extract, Transform, Load) y guardará los resultados en la carpeta `output/`.

## Estructura del Proyecto

```
mi_primer_ETL/
├── data/
│   ├── ecommerce_brands.csv
│   ├── ecommerce_categories.csv
│   ├── ecommerce_customers.csv
│   ├── ecommerce_inventory.csv
│   ├── ecommerce_order_items.csv
│   ├── ecommerce_orders.csv
│   ├── ecommerce_products.csv
│   ├── ecommerce_promotions.csv
│   ├── ecommerce_reviews.csv
│   ├── ecommerce_suppliers.csv
│   └── ecommerce_warehouses.csv
├── output/
│   ├── orders_clean.csv
│   ├── orders_clean.parquet
│   ├── ventas_por_cliente.csv
│   └── ventas_por_mes.csv
├── etl.py
├── requirements.txt
└── README.md
```

## Notas

- Los archivos en `data/` deben estar presentes para que el script funcione.
- La carpeta `output/` se crea automáticamente si no existe.
- El script usa pandas para el procesamiento de datos y pyarrow para guardar en formato Parquet.

¡Disfruta explorando tu primer pipeline ETL!