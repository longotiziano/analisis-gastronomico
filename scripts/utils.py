import requests 
import pandas as pd
import unidecode
from typing import Any, Tuple
import warnings

requests_headers = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/120.0 Safari/537.36"
    )
}

def realizar_request(url: str) -> Tuple[bool, Any | None]:
    """
    Función auxiliar para realizar requests HTTP y manejar errores de forma centralizada.
    Retorna:
    - (True, data) si la request fue exitosa
    - (False, None) si ocurrió algún error
    """ 
    try:
        # Realizar la request con un timeout
        response = requests.get(url, headers=requests_headers, timeout=(5, 10))
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f"Error al realizar la request a {url}: {e}")
        return False, None

    try:
        # Parsear la respuesta JSON
        data = response.json()
    except ValueError:
        print(f"Error al parsear la respuesta JSON de {url}")
        return False, None
    return True, data


def transformar_unidades(df: pd.DataFrame) -> pd.DataFrame:
    """
    Normaliza precios a precio por kilogramo.
    Acepta unidades como 'kg', 'g', 'litro', 'litros', '200_g', '500_g', 'lata_200_g' etc.
    Devuelve:
        - df_out (DataFrame): DataFrame transformado.
    """

    lista_de_dicts = []
    avisos = []

    for fila in df.itertuples():
        variedad = fila.variedad
        precio = fila.precio
        udm = fila.unidad_de_medida

        # Normalizo strings base
        if isinstance(udm, str):
            udm = udm.replace("cc", "g")
            udm = udm.replace("litros", "kg")
            udm = udm.replace("litro", "kg")

        # Caso base: si ya está en kg
        if udm == "kg":
            lista_de_dicts.append({
                "variedad": variedad,
                "unidad_de_medida": "kg",
                "precio": precio
            })
            continue

        # Intento parsear casos tipo "200_g" o "0.5_kg"
        partes = udm.split("_")

        if len(partes) == 2:
            cantidad_str, unidad = partes
        elif len(partes) == 3: # En caso de, por ejemplo: lata_200_g
            _, cantidad_str, unidad = partes
        else:
            avisos.append((variedad, udm, "Formato desconocido"))
        try:
            cantidad = float(cantidad_str)
        except:
            avisos.append((variedad, udm, "No pude leer la cantidad"))
            continue

        if unidad == "g":
            cantidad = cantidad / 1000  # paso a kg
        elif unidad != "kg":
            avisos.append((variedad, udm, "Unidad desconocida"))
            continue

        precio_kg = round((precio / cantidad), 2)

        lista_de_dicts.append({
            "variedad": variedad,
            "unidad_de_medida": "kg",
            "precio": precio_kg
        })



    # Avisos sin cortar ejecución
    if avisos:
        warnings.warn(f"Valores no reconocidos en transformar_unidades: {avisos}")

    return pd.DataFrame(lista_de_dicts)


def pasar_snake_case(celda: str) -> str:
    """
    Transformación a snake_case y eliminación de tildes.
    """
    if isinstance(celda, str):
        if "," not in celda and "." not in celda:
            celda = unidecode.unidecode(celda)
        else:
            celda = celda.replace(".", "").replace(",", ".")   
    
    return celda.lower().replace(" ", "_")


def aplicar_funcion_df(df: pd.DataFrame, cols: list, func):
    """
    Aplica una función a columnas específicas de un DataFrame.
    """
    for col in cols:
        df[col] = df[col].map(func)
        

def detectar_outliers_iqr(df: pd.DataFrame, col: str) -> pd.DataFrame:
    """
    Detecta outliers en una columna usando el método IQR (Tukey).
    Devuelve un DataFrame que contiene solo las filas con valores atípicos.
    """
    # Devuelve el valor debajo del cual cae un porcentaje específico de los datos.
    Q1 = df[col].quantile(0.25) # percentil 0.25
    Q3 = df[col].quantile(0.75) # percentil 0.75
    
    # Interquartile Range (rango donde se encuentran el 50% de los datos centrales)
    IQR = Q3 - Q1
    
    # Por regla de Tukey
    lim_inf = Q1 - 1.5 * IQR
    lim_sup = Q3 + 1.5 * IQR
    
    # Formo el DataFrame que contiene a los outliers
    outliers = df[(df[col] < lim_inf) | (df[col] > lim_sup)]
    return outliers


def traductor_cols(texto: str) -> str:
    """
    Dada una de las columnas de los DataFrames empleados, se retorna su traducción al español,
    con pasado a snake_case y sin tildes.
    - DataFrame Items: Item,Category,Sub Category,Item Name,Price,Cost
    - DataFrame Orders: Date,Time,Order Number,Item,Count
    """
    traducciones_fijas = {
    "Item": "item",
    "Category": "categoria",
    "Sub Category": "subcategoria",
    "Item Name": "nombre_producto",
    "Price": "precio",
    "Cost": "costo_produccion",
    "Date": "fecha_orden",
    "Time": "hora",
    "Order Number": "numero_de_orden",
    "Count": "cantidad"
    }   
    if texto not in traducciones_fijas:
        raise KeyError(f"No existe traducción para la columna: {texto}")
    
    traduccion = traducciones_fijas[texto]
    return traduccion