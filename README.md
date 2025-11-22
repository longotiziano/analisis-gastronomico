# Análisis Gastronómico – Documentación General

Este repositorio contiene la **base del proyecto** de análisis gastronómico. Aquí se encuentran únicamente los elementos **compartidos** entre las dos investigaciones principales, cada una desarrollada en su propia branch.

El branch `main` no incluye análisis finales, sino:
- Datos crudos y limpios
- Scripts base
- Diccionarios y equivalencias
- Notebooks de preparación
- Infraestructura común

Las investigaciones completas se encuentran en branches separados.

---

## Arquitectura del Proyecto

El proyecto se compone de **dos análisis independientes**, que parten del mismo dataset base pero con objetivos completamente distintos:

---

### **Branch 1: `desperdicios-optimizacion`**

**Objetivo:**  
Analizar el rendimiento del restaurante, detectar fugas de stock, calcular desperdicios y estimar el ahorro potencial mediante una correcta gestión.

Incluye:
- Identificación de pérdidas 
- Impacto económico en categorías
- Proyección de ahorro tras la optimización
- KPIs y métricas de negocio
- Dashboard final

Este análisis está centrado exclusivamente en el **funcionamiento operativo del restaurante**.

---

### **Branch 2: `comparacion-eeuu-argentina`** (en proceso)

**Objetivo:**  
Comparar el costo de elaboración de distintos platos entre **Argentina** y **Estados Unidos**.

Incluye:
- Precios mayoristas argentinos vs. precios mayoristas estadounidenses
- Costo por receta en ambos mercados
- Diferencias económicas y proporciones
- Visualizaciones comparativas

Este análisis no utiliza métricas del restaurante ni KPIs operativos.  
Es un estudio económico **externo e independiente**.

---

## Contenido de `main`
```
analisis-gastronomico/
|-- data/ # datos crudos, limpios y staging
|-- scripts/ # scripts reutilizables
|-- notebooks/ # notebooks de preprocesamiento y wrangling
|-- equivalencias/ # diccionarios y mapeos usados para unificar categorías
|-- requirements.txt # dependencias del proyecto
|-- README.md # este archivo
```

---

## Tecnologías utilizadas

- **Python** (Jupyter Notebooks)  
- **Pandas** -> limpieza, feature engineering y transformación  
- **Matplotlib** -> visualizaciones base  
- **Power BI** -> dashboard de análisis  
- **Git + Git branches** -> arquitectura del proyecto  

---

## Proceso General

### 1. Exploración inicial y búsqueda de datasets
El proyecto utiliza una combinación de **datasets simulados** y **precios reales** obtenidos de mayoristas y reportes del INDEC.

#### `Restaurant_Data.xlsx`
Dataset base con ventas y recetas del restaurante ficticio.

### Otras fuentes consultadas
- Informe de precios del **INDEC**  
- Reportes del sector gastronómico  
- Fuentes complementarias para precios internacionales 
- APIs para consultado de cotizaciones 

Para más información revisar: `data/README.md`

---

### 2. Data Wrangling 

Tareas realizadas en esta etapa:
- Eliminación de nulos  
- Estandarización a `snake_case`  
- Unificación de unidades (g -> kg)  
- Conversión de moneda cuando corresponde  
- Limpieza general del dataset para que ambas branches lo utilicen igual  

> La traducción de columnas se mantuvo aislada para optimizar performance. Detalles en `scripts/README.md`.

---

### 3. Equivalencias y paso a mercado argentino

El dataset del restaurante posee categorías propias, mientras que el INDEC maneja un esquema completamente distinto.  
Para permitir análisis conjuntos, se generaron:

- Diccionarios de mapeo entre categorías  
- Equivalencias entre subcategorías  
- Unificación de criterios de clasificación  

Para más información revisar: `equivalencias/README.md`

---

## Instrucciones de uso

### 1. Instalar dependencias

```bash
pip install -r requirements.txt
```

### 2. Abrir los notebooks base

Los notebooks dentro de `/notebooks` generan los datasets limpios que luego consumen las branches.

### 3. Cambiar de branchs según análisis
```bash
git checkout desperdicios-optimizacion
# o
git checkout comparacion-eeuu-argentina
```

Cada branch contiene su propio README explicando el análisis completo.

## Nota final

Este repositorio está diseñado para escalar a múltiples análisis gastronómicos que compartan una misma base de datos y proceso de preparación.
Cada nueva investigación deberá implementarse como una branch independiente.

