# Data  
Este directorio contiene los datasets utilizados en el proyecto, así como la documentación y fuentes que justifican los supuestos realizados.

---

### Directorios
- **raw/**: Posee los datos crudos, sin ningún tipo de proceso.
- **staging/**: Almacena los datos de manera previa en formato CSV luego de pasar por el EDA
- **clean/**: Contiene los datos procesados, listos para análisis.
 

## Datasets empleados

### **1. Índice de Precios al Consumidor (IPC - INDEC)**
Usado para:
- obtener valores de referencia sobre precios de alimentos en Argentina  
- estimar tendencias inflacionarias relevantes al análisis de costos  

Fuente: https://www.indec.gob.ar/indec/web/Nivel4-Tema-3-5-31

---

### **2. Restaurant Cost and Sales Dataset (Kaggle)**  
Dataset base utilizado para simular ventas y costos en un restaurante promedio.  
Contiene dos hojas (`Orders` e `Items`) con precios originalmente expresados en **USD**, lo cual se ajustó usando tipo de cambio actualizado.

Fuente: https://www.kaggle.com/datasets/virtualschool/restaurant-cost-and-sales-dataset

---

### **3. DolarAPI**
Usado para:
- convertir precios de USD a ARS  
- simular escenarios realistas en base al tipo de cambio vigente  

API: https://dolarapi.com/v1/dolares/blue

---

## Investigación complementaria

- Declaraciones del CEO de PedidosYa sobre la gestión de stock en dark stores (Fuente: Forbes)
- Estudio sobre desperdicio de alimentos en hoteles y restaurantes de Santa Fe (Fuente: Repositorio UNLP)
- Informe del PNUMA (2021) sobre desperdicio global de alimentos  
- Reportes sectoriales sobre merma promedio en restaurantes (Fuente: FUDO)  

---

## Conclusiones metodológicas
La literatura revisada muestra niveles de merma de entre **4% y 17%** dependiendo del país y el tipo de operación gastronómica.  
Para este proyecto se adopta un valor de referencia del:

# **10% de desperdicio promedio**
Este número se utiliza para estimar pérdidas económicas en el restaurante ficticio, y constituye un parámetro clave en el modelo analítico.
