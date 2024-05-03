"""
Laboratorio - Manipulación de Datos usando Pandas
-----------------------------------------------------------------------------------------

Este archivo contiene las preguntas que se van a realizar en el laboratorio.

Utilice los archivos `tbl0.tsv`, `tbl1.tsv` y `tbl2.tsv`, para resolver las preguntas.

"""
import csv
import pandas as pd

tbl0 = pd.read_csv("tbl0.tsv", sep="\t")
tbl1 = pd.read_csv("tbl1.tsv", sep="\t")
tbl2 = pd.read_csv("tbl2.tsv", sep="\t")


def pregunta_01():

    tabla_01=len(tbl0)
    return tabla_01

def pregunta_02():
    
    tabla_02=len(tbl0.columns)
    return tabla_02

def pregunta_03():

    tabla_03=tbl0['_c1'].value_counts()
    tabla_03.rename('_c1', inplace=True)
    tabla_03=tabla_03.sort_index()
    return tabla_03

def pregunta_04():

    tabla_04=tbl0.groupby('_c1')['_c2'].mean()
    return tabla_04

def pregunta_05():

    tabla_05=tbl0.groupby('_c1')['_c2'].max()
    return tabla_05

def pregunta_06():

    tabla_06=tbl1['_c4'].unique()
    tabla_06=[element.upper() for element in tabla_06]
    tabla_06=sorted(tabla_06)
    return tabla_06


def pregunta_07():

    tabla_07=tbl0.groupby('_c1')['_c2'].sum()
    return tabla_07


def pregunta_08():

    tbl0['suma']=tbl0['_c0']+tbl0['_c2']
    return tbl0

def pregunta_09():

    tbl0['year']=tbl0['_c3'].str.split('-').str[0]
    return tbl0

def pregunta_10():

    tabla_10=tbl0.groupby('_c1')['_c2'].apply(lambda x: ':'.join(sorted(x.astype(str))))
    tabla_10.columns=['_c0', '_c1']
    tabla_10=pd.DataFrame(tabla_10)
    return tabla_10

def pregunta_11():

    tabla_11=tbl1.groupby('_c0')['_c4'].apply(lambda x: ','.join(sorted(x))).reset_index()
    tabla_11.columns=['_c0', '_c4']
    return tabla_11
    


def pregunta_12():

    tbl2['_c5']=tbl2['_c5a']+':'+tbl2['_c5b'].astype(str)
    tabla_12=tbl2.groupby('_c0')['_c5'].apply(lambda x: ','.join(sorted(x))).reset_index()
    return tabla_12




def pregunta_13():
   
    combined = pd.merge(tbl0, tbl2, on='_c0')
    tabla_13=combined.groupby('_c1')['_c5b'].sum()
    return tabla_13

pregunta_01()