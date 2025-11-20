# Análisis de Desperdicios y Ventas de un Restaurante
Este proyecto analiza el impacto económico de las fugas de stock en un restaurante. 
A partir de datos simulados con precios reales de **mayoristas argentinos**, estima pérdidas por categoría y predice ahorros posibles con la implementación de un sistema de gestión.

## Objetivo del proyecto
- Identificar las pérdidas (desde anuales hasta diarias) dadas a las fugas no identificadas
- Qué platos se están viendo mayormente afectados, para dar soluciones más específicas
- Demostrar los resultados luego de las optimizaciones
- Explicar la importancia de la implementación de estos sistemas y el abandono de las viejas y malas costumbres

## Estructura
```
analisis-de-desperdicios/
|-- data/                # datasets limpios y crudos
|-- notebooks/           # análisis principal
|-- scripts/             # lógica reutilizable y tareas
|-- dashboard.png        # captura del dashboard
|-- requirements.txt     # librerías usadas
|-- README.md            # este archivo
```

## Tecnologías utilizadas
- Python, utilizando Jupyter Notebooks
- Pandas, para la limpieza y procesado de datasets
- Matplotlib, para el graficado y análisis de datos
- Power BI, para el diseño del dashboard

## Proceso de análisis
### 1. Exploración inicial y Búsqueda de datasets
Para este proyecto se utilizó una combinación de **datasets simulados** y **fuentes reales** con el objetivo de representar el funcionamiento de un restaurante promedio.
 
#### 1. `Restaurant_Data.xlsx`
Dataset principal con el histórico de ventas y costos del restaurante ficticio.

**Hoja: Orders**
- `Date`: día de la transacción  
- `Time`: Horario de la transacción
- `Order Number`: Número de orden  
- `Item`: PK del item  
- `Count`: Cantidad vendida

**Hoja: Items**
- `Item`: PK del item   
- `Category`: Categoría del item (Desserts, Sides, Main Courses...)
- `Sub Category`: Sub-categoría del item (Pasta, Vegan...)
- `Item Name`: Nombre del item (Coffe, Beer, Burguers...) 
- `Price`: Costo del item (en dólares)
- `Cost`: Costo de producción

> **Nota:**: La columna de `costos` no fue utilizada durante el análisis, ya que este mismo está centrando en el mercado argentino.

### Otras fuentes consultadas
Además del dataset principal, se analizaron:
- **Informe de precios del INDEC (`informe_indec.pdf`)**  
- **Artículos y reportes sectoriales** relacionados a desperdicio en gastronomía  
- **Publicaciones de mayoristas** para estimar costos reales  

> Más detalles sobre cada dataset, supuestos y estructura en `data/README.md`

--- 

### 2. Data Wrangling
Luego de haber identificado en el **Exploratory Data Analysis** (EDA) las tareas encomendadas, se realizaron diversas tareas:
- Eliminación de valores nulos
- Traducción de DataFrames
- Formateo a `snake_case`
- Pasado a unidades en común (ej: precio en g -> precio en kg)
- Conversión de tipo de cambio
- Paso a mercado argentino
- Agregado de métricas y cálculos que dejan listos los datos para ser graficados

> **Aclaración sobre la traducción del dataset**
>
> La traducción del dataset fue ejecutada con la librería `deep_translator`, y si bien es la más estable, suelen demorar mucho sus procesos. Esto era grave, ya que relentizaba todo el notebook por una simple traducción de ~1500 celdas, por lo que decidí manejarla de manera externa con el script `traducir_df.py`, que traduce externamente y almacena en un CSV, aumentando así de manera drástica la velocidad del código. 

---

### 3. Paso al mercado argentino
En el paso a mercado argentino me enfrenté a un problema: el dataset del restaurante y el del INDEC **utilizan esquemas distintos**, lo que hacia imposible su comparación directa.\
Para resolverlo, se creó un diccionario de equivalencias (con IA), donde cada categoría/subcategoría del restaurante fue mapeada a una categoría homogénea equivalente del INDEC.

**Beneficios del enfoque**
- Reduce la probabilidad de errores por falta de coincidencias exactas.
- Permite usar precios reales sin necesidad de replicar recetas individuales.
- Mantiene consistencia entre datasets muy diferentes.
- Hace el proyecto más escalable y realista.

**Limitaciones conocidas**
- Se pierde algo de granularidad a nivel producto final.
- Algunas recetas podrían tener composiciones diferentes según el restaurante.
- Los costos estimados representan un promedio de mercado, no una receta específica.

Aun así, este método es adecuado para un análisis económico general, comparaciones temporales y estimación del impacto del desperdicio dentro de un restaurante promedio.

> Para más información acerca de la estrategia implementada y detalles técnicos asistir a `paso_mer_arg.ipynb`

---

### 4. Reporte en Power BI
Finalmente, desarrollé un reporte en Power BI, donde analizo, explico y muestro las diversas métricas y KPIs que me parecieron de valor para este
escenario hipotético.

**KPIs:**
- **Desperdicio general** -> % y $
- **Ganancia de categorías afectada** -> % (ej: pérdida de ganancia de un 7% en [categoría])
- Comparación temporal de ventas **con y sin optimización**

**Insights:**
- Productos con más pérdidas 