import requests 
import pandas as pd
import unidecode
from typing import Any, Tuple

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


def transformar_unidades(df: pd.DataFrame) -> Tuple[bool, pd.DataFrame | None]:
    """
    Función creada para, luego de recibir un DataFrame, crear uno nuevo con precios y unidades de medida modificados en base a un kilo.
    """
    lista_de_dicts = []
    avisos = []
    for fila in df.itertuples():
        col_udm = fila.unidad_de_medida

        if isinstance(col_udm, str):
            # Evitar filas que no requieren de actualización
            if col_udm != 'kg':
                col_udm = col_udm.replace('cc', 'g')
                col_udm = col_udm.replace('litros', 'kg')

                # En el caso de que sea "litro" singular
                if col_udm == 'litro':
                    col_udm = col_udm.replace('litro', 'kg')
                    cantidad = 1

                division = col_udm.split("_")

                # No aplico la función a elementos que no sean ni gramos ni kilos, evitando malas operaciones en (por ejemplo) unidades
                if division[-1] not in ['kg', 'g']:
                    avisos.append({'Valor no actualizado': fila.variedad})
                    dict_variedad = {'variedad': fila.variedad, 'unidad_de_medida': col_udm, 'precio': fila.precio }
                    lista_de_dicts.append(dict_variedad)
                    continue

                # Uso cantidad de operadores lógicos luego del razonamiento de como afrontar el orden en este bloque de código y teniendo
                # en cuenta diversos aspectos del DataFrame que limitan el uso de aplicaciones más simples con, por ejemplo, index().
                if len(division) > 2:
                    cantidad = float(division[1])
                elif len(division) == 2:
                    cantidad = float(division[0])
                else:
                    avisos.append({'Longitud de lista': fila.variedad})
                    continue
                
                if division[-1] == 'g':
                    # Reemplazo la variable "cantidad" en el caso de que se trate de gramos
                    cantidad = cantidad/1000 

                precio_kg = fila.precio / cantidad

                dict_variedad = {'variedad': fila.variedad, 'unidad_de_medida': 'kg', 'precio': precio_kg }
                lista_de_dicts.append(dict_variedad)

            else:
                dict_variedad = {'variedad': fila.variedad, 'unidad_de_medida': col_udm, 'precio': fila.precio }
                lista_de_dicts.append(dict_variedad)

    if avisos:
        print(avisos)
        return False, None
        
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