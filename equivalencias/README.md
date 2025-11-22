# Documentación de equivalencias
### _Estrategia para unificar categorías entre el restaurante y el INDEC_

Este documento explica el proceso utilizado para mapear las categorías del restaurante con las materias primas del informe del INDEC, con el fin de estimar costos reales del mercado argentino y realizar un análisis económico consistente.

--- 

###  Problema a resolver
Ambos utilizan estructuras completamente diferentes, lo que hacía imposible calcular costos reales sin un sistema de correspondencia entre ambos esquemas. 

**Por ejemplo**: mientras que en el dataset del restaurante había categorías culinarias, en el INDEC se encontraban materias primas individuales

---

### Objetivo del sistema de equivalencias
- Permitir estimar costos reales de producción usando precios del INDEC.
- Conectar platos con materias primas, aun cuando no existan coincidencias exactas.
- Mantener consistencia, escalabilidad y flexibilidad dentro del pipeline de análisis.

---

### Metodología y supuestos
- Se asumió una estructura promedio de recetas tal que la suma de sus valores es igual a 5.
- Reviso sub-categorías de platos (las categorías sin indiferentes porque refiere a la carta, no al plato en sí)
- Los pesos no representan cantidades exactas
- Se privilegió la consistencia

**Ejemplo**:
```python
{
    'hamburguesas': {
        'carnes': 3,
        'panificados': 2, # Cada diccionario suma 5 puntos
        'verduras': 1
    },
    'ensaladas': {
        'verduras': 4
        'aceites': 1
    }
    # etc...
}
```
---

### Beneficios del enfoque
- Reduce la probabilidad de errores por falta de coincidencias exactas.
- Permite usar precios reales sin necesidad de replicar recetas individuales.
- Mantiene consistencia entre datasets muy diferentes.
- Hace el proyecto más escalable y realista.

---

### Limitaciones conocidas
- Se pierde algo de granularidad a nivel producto final.
- Algunas recetas podrían tener composiciones diferentes según el restaurante.
- Los costos estimados representan un promedio de mercado, no una receta específica.

Aun así, este método es adecuado para un análisis económico general, comparaciones temporales y estimación del impacto del desperdicio dentro de un restaurante promedio.

---

### Archivos
Los archivos contenidos en el directorio cumplen diversas responsabilidades:
- `categorias_indec.py`: Contiene el diccionario que le asigna al dataset del INDEC sus categorías
- `equivalencias_pesos.py`: Diccionario que asigna las subcategorías del dataset de `Items` una cantidad numérica de las categorías del INDEC

