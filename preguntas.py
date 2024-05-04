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
    """
    ¿Cuál es la cantidad de filas en la tabla `tbl0.tsv`?

    Rta/
    40

    """
    # retorno la cantidad de registro con la función len (me mide la cantidad de filas)
    # respuesta_op1= (len(tbl0))
    # return respuesta_op1
    
    # atributos: Columnas
    # Registros: filas
    # shape devuelve una tupla con el dimensionamiento de la tabla 0= fila, 1= columnas
    # en este caso me devuelve la cantidad de filas de la tupla
    
    respuesta_op2=tbl0.shape[0]
    return respuesta_op2  

def pregunta_02():
    """
    ¿Cuál es la cantidad de columnas en la tabla `tbl0.tsv`?

    Rta/
    4

    """
    # .columns devuelve una lista con los nombres de las columnas, cuando utilizo len
    # me permite sacar la longuitud de la lista, en este caso me mide la longitud de las columnas
    respuesta_op2= len(tbl0.columns)
    return respuesta_op2
    
    # otra forma de hacerlos es a través de la función shape, que me permite trael la cantidad de filas
    # respuesta_op1=tbl0.shape[1]
    # return respuesta_op1

def pregunta_03():
    """
    ¿Cuál es la cantidad de registros por cada letra de la columna _c1 del archivo
    `tbl0.tsv`?

    Rta/
    A     8
    B     7
    C     5
    D     6
    E    14
    Name: _c1, dtype: int64

    """
    # En este caso solo necesito la columna _c1 de la tabla, por lo que creo una variable
    # En este caso requiere un data serie, en donde selecciono la columna _c1, realizo un conteo de dicha variable y la organizo como un indice.  
    # en este caso creo un data serie (información de una sola columna)
    columna_letras = tbl0["_c1"]
    conteo_letras = columna_letras.value_counts().sort_index()
    
    return conteo_letras


def pregunta_04():
    """
    Calcule el promedio de _c2 por cada letra de la _c1 del archivo `tbl0.tsv`.

    Rta/
    A    4.625000
    B    5.142857
    C    5.400000
    D    3.833333
    E    4.785714
    Name: _c2, dtype: float64
    """
    # en este caso también creo un data serie, 
    # agrupando la información con base en la columna _c1 y
    # calculando la media de _c2
    # con el fin de ahorrar espacio de máquina puedo definir en el mismo retorno la respuesta 
    return tbl0.groupby("_c1")["_c2"].mean()


def pregunta_05():
    """
    Calcule el valor máximo de _c2 por cada letra en la columna _c1 del archivo
    `tbl0.tsv`.

    Rta/
    _c1
    A    9
    B    9
    C    9
    D    7
    E    9
    Name: _c2, dtype: int64
    """
    # el procedimiento es el mismo que el anterior, agrupo con base en _c1
    # pero esta vez calculo para el campo _c2 el valor máximo.
    # para ahorrar espacio de máquina dejo en el retorno el resultado
    
    return tbl0.groupby("_c1")["_c2"].max()


def pregunta_06():
    """
    Retorne una lista con los valores unicos de la columna _c4 de del archivo `tbl1.csv`
    en mayusculas y ordenados alfabéticamente.

    Rta/
    ['A', 'B', 'C', 'D', 'E', 'F', 'G']

    """
# forma 1: 
# a. Creo una nueva variable, seleccionando solo el campo _c4 de la tabla 0, 
# y uso la función apply para que los string pasen de minúscula a mayúscula.
# b. creo una 
#   
# tbl1['_c4'] = tbl1['_c4'].apply(str.upper)
# Respuesta_06 = list(tbl1.sort_values(by='_c4', ascending=True)['_c4'].unique())
# Respuesta_06

# Forma 2
# Var = list(sorted(set(tbl1['_c4'].str.upper())))
# Var

# Respuesta_06 = list(tbl1.sort_values(by='_c4', ascending=True)['_c4'].unique())
# Respuesta_06


# for i in Respuesta_06:
#     Respuesta_07.append(i)
#     # print(i)

    # respuesta_06=[]
    # tbl1["_c4"]=tbl1["_c4"].str.upper()
    # respuesta_06= list(tbl1.sort_values(by="_c4", ascending=True)["_c4"].unique())

    respuesta_parcial_may= tbl1['_c4'].apply(str.upper)
    
    Respuesta= list(respuesta_parcial_may.sort_values(ascending=True).unique())
    Respuesta
    
    return Respuesta


def pregunta_07():
    """
    Calcule la suma de la _c2 por cada letra de la _c1 del archivo `tbl0.tsv`.

    Rta/
    _c1
    A    37
    B    36
    C    27
    D    23
    E    67
    Name: _c2, dtype: int64
    """
    #
    # es el mismo ejercicio que el anterior, creo un data set agrupando por _c1
    # y calculando la suma de variable _c2.
    
    return tbl0.groupby("_c1")["_c2"].sum()


def pregunta_08():
    """
    Agregue una columna llamada `suma` con la suma de _c0 y _c2 al archivo `tbl0.tsv`.

    Rta/
        _c0 _c1  _c2         _c3  suma
    0     0   E    1  1999-02-28     1
    1     1   A    2  1999-10-28     3
    2     2   B    5  1998-05-02     7
    ...
    37   37   C    9  1997-07-22    46
    38   38   E    1  1999-09-28    39
    39   39   E    5  1998-01-26    44

    """
    
    # debido a que vamos a crear una nueva columna, se sugiere crear una copia de la tabla
    # se crea la copia de la tabla
    tbl0_c=tbl0.copy()
    
    # para ahorrar espacio de máquina, retorno con la creación de una nueva columna, con la función assign 
    # creo una función que sería la suma de las columnas _c0 y _c2
    return tbl0_c.assign(suma=tbl0_c["_c0"]+tbl0_c["_c2"])


def pregunta_09():
    """
    Agregue el año como una columna al archivo `tbl0.tsv`.

    Rta/
        _c0 _c1  _c2         _c3  year
    0     0   E    1  1999-02-28  1999
    1     1   A    2  1999-10-28  1999
    2     2   B    5  1998-05-02  1998
    ...
    37   37   C    9  1997-07-22  1997
    38   38   E    1  1999-09-28  1999
    39   39   E    5  1998-01-26  1998

    """
    # de igual manera creo una copia de la tabla original
    tbl0_c=tbl0.copy()
    
    # para ahorrar espacio máquina creo en el retorno el resultad
    # creo una nueva columna con la función assign llamada "year"
    # que sería igual a la columna _c3,
    # con la función str.split separo la variable string por -
    # de igual manera traigo el str ubicado en la posición 0, que es el año
    
    return tbl0_c.assign(year=tbl0_c["_c3"].str.split("-").str[0])


def pregunta_10():
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
    # realizo un agrupamiento con pase en la columna _c1 (valores únicos) y ordenados
    # de la columna _c2 utilizo la función apply para realizar una función específica. 
    #
    # df.groupby('_c1')['_c2']: Esta parte del código agrupa los valores de _c2 según los valores únicos de _c1.
    # .apply(lambda x: ':'.join(map(str, sorted(x)))): Se aplica una función lambda a cada grupo.
    # sorted(x): Ordena los valores del grupo en orden ascendente.
    # map(str, ...): Convierte cada valor del grupo en una cadena de texto.
    # ':'.join(...): Une los valores del grupo en una sola cadena separada por :.
    # .reset_index(): Restablece el índice del DataFrame resultante, garantizando que _c1 y la nueva columna tengan un índice limpio y continúen desde 0.
    
    resultado = tbl0.groupby('_c1')['_c2'].apply(lambda x: ':'.join(map(str, sorted(x)))).reset_index()
    
    resultado.set_index("_c1", inplace=True)
    
    return resultado


def pregunta_11():
    """
    Construya una tabla que contenga _c0 y una lista separada por ',' de los valores de
    la columna _c4 del archivo `tbl1.tsv`.

    Rta/
        _c0      _c4
    0     0    b,f,g
    1     1    a,c,f
    2     2  a,c,e,f
    3     3      a,b
    ...
    37   37  a,c,e,f
    38   38      d,e
    39   39    a,d,f
    """
    resultado = tbl1.groupby('_c0')['_c4'].apply(lambda x: ','.join(sorted([e.lower() for e in x]))).reset_index()
    return resultado


def pregunta_12():
    """
    Construya una tabla que contenga _c0 y una lista separada por ',' de los valores de
    la columna _c5a y _c5b (unidos por ':') de la tabla `tbl2.tsv`.

    Rta/
        _c0                                  _c5
    0     0        bbb:0,ddd:9,ggg:8,hhh:2,jjj:3
    1     1              aaa:3,ccc:2,ddd:0,hhh:9
    2     2              ccc:6,ddd:2,ggg:5,jjj:1
    ...
    37   37                    eee:0,fff:2,hhh:6
    38   38                    eee:0,fff:9,iii:2
    39   39                    ggg:3,hhh:8,jjj:5
    """
    # creo una variable que contenga una copia de la tabla 2, debido a que voy a modificar el orden
    respuesta_11=tbl2.copy()
    # creo una nueva variable, a partir de la copia de la tabla 2 para organizar con base en la columna _c5a
    respuesta_intermedia=respuesta_11.sort_values(["_c5a","_c5b","_c0"])
    # creo una nueva variable combinando la clumna _c5a y _c5b
    nueva_columna=respuesta_intermedia.assign(_c5=respuesta_intermedia["_c5a"]+":"+respuesta_intermedia["_c5b"].astype(str))
    # creo una nueva variable con la respuesta
    respuesta_final=nueva_columna.groupby("_c0")["_c5"].agg(",".join).reset_index()
    
    return respuesta_final


def pregunta_13():
    """
    Si la columna _c0 es la clave en los archivos `tbl0.tsv` y `tbl2.tsv`, compute la
    suma de tbl2._c5b por cada valor en tbl0._c1.

    Rta/
    _c1
    A    146
    B    134
    C     81
    D    112
    E    275
    Name: _c5b, dtype: int64
    """
    # crear una nueva tabla, a partir de la tabla 0 y tabla 2
    # columna _co es la clave, hay que computar  tbl2 por cada valor de tbl0
    Df_fusion= pd.merge(tbl2,tbl0,on="_c0")
    Respuesta_13= Df_fusion.groupby("_c1")["_c5b"].sum()
    return Respuesta_13
##
##