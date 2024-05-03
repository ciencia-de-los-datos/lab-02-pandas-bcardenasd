"""
Laboratorio - Manipulación de Datos usando Pandas
-----------------------------------------------------------------------------------------

Este archivo contiene las preguntas que se van a realizar en el laboratorio.

Utilice los archivos `tbl0.tsv`, `tbl1.tsv` y `tbl2.tsv`, para resolver las preguntas.

"""
import pandas as pd

tbl0 = pd.read_csv("tbl0.tsv", sep="\t")
tbl1 = pd.read_csv("tbl1.tsv", sep="\t")
tbl2 = pd.read_csv("tbl2.tsv", sep="\t")


def pregunta_01():

    filas = len(tbl0)
    return filas


def pregunta_02():

    cols = len(tbl0.columns)
    return cols


def pregunta_03():

    frecuencia_c1 = tbl0.value_counts("_c1")
    frecuencia_c1 = frecuencia_c1.sort_index()

    return frecuencia_c1

def pregunta_04():

    promedio_c2 = tbl0.groupby("_c1")["_c2"].mean()

    return promedio_c2

def pregunta_05():

    max_c2 = tbl0.groupby("_c1")["_c2"].max()

    return max_c2


def pregunta_06():

    letras = tbl1["_c4"].str.upper().unique()
    letras = sorted(letras)

    return letras


def pregunta_07():

    suma_c2 = tbl0.groupby("_c1")["_c2"].sum()

    return suma_c2


def pregunta_08():

    tbl0["suma"] = tbl0["_c0"] + tbl0["_c2"]

    return tbl0


def pregunta_09():

    tbl0["year"] = tbl0["_c3"].str.split("-").str[0]

    return tbl0


def pregunta_10(): #terminarlo
    """
    Construya una tabla que contenga _c1 y una lista separada por ':' de los valores de
    la columna _c2 para el archivo `tbl0.tsv`.

    Rta/
                                   _c1
      _c0
    0   A              1:1:2:3:6:7:8:9
    1   B                1:3:4:5:6:8:9
    2   C                    0:5:6:7:9
    3   D                  1:2:3:5:5:7
    4   E  1:1:2:3:3:4:5:5:5:6:7:8:8:9
    """


    letra_numeros = tbl0.groupby("_c1")["_c2"].apply(lambda x: ':'.join(sorted(x.astype(str))))
    
    return pd.DataFrame(letra_numeros)




def pregunta_11():

    letras_c4 = tbl1.groupby("_c0")["_c4"].apply(lambda x: ",".join(sorted(x))).reset_index()

    return letras_c4


def pregunta_12():

    lista_parcial = tbl2["_c5a"] + ":" + tbl2["_c5b"].astype("str")

    df = pd.DataFrame(tbl2["_c0"])
    df["_c5"] = lista_parcial
    df = df.groupby("_c0")["_c5"].apply(lambda x: ",".join(sorted(x))).reset_index()
    
    return df


def pregunta_13():

    numeros_repetidos = tbl2.groupby("_c0")["_c5b"].sum()

    df = pd.DataFrame(numeros_repetidos)

    df["letras"] = tbl0["_c1"]

    agrupacion = df.groupby("letras")["_c5b"].sum()

    return agrupacion