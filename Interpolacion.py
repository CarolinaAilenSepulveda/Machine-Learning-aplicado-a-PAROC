#Librerías
%matplotlib inline
import pandas as pd
pd.__version__
import altair as alt
import requests
import io
import matplotlib.pyplot as plot
import numpy as np
import seaborn as sns
from bokeh.io import output_notebook, show
from bokeh.plotting import figure
from bokeh.models.annotations import Label
from scipy.interpolate import InterpolatedUnivariateSpline

#Token generado en mi cuenta personal de Github para acceder al repositorio privado
username = ''
token = ''

github_session = requests.Session()
github_session.auth = (username, token)

#Defino una función para realizar el interpolado de valores y para completar el dataset con los valores nuevos calculados

#FUNCIONES -------------------------------------------
def Obtener_indices(data, hormona):
  lista_aux = []
  for i in range(len(data)):
    if str(data.iloc[i][hormona]) == "nan":
       lista_aux.append({"x":data.iloc[i]['Indice'], "posicion": i })
  return lista_aux

def Interpolar(data,hormona, limite_inf, limite_sup,grado):
  lista_retorno = []
  lista = Obtener_indices(data,hormona)
  data_aux = data
  data = data.dropna(subset=[hormona])
  x = data['Indice']
  y = data[hormona]
  f_interpolada = InterpolatedUnivariateSpline(x,y,k=grado)

  x1=np.linspace(limite_inf,limite_sup)
  y1 = f_interpolada(x1)

  #Grafico la curva real e interpolada de la Progesterona
  plot.plot(x1,y1, label = hormona +" interpolada")
  plot.plot(x,y,"x", mew=2, label=hormona + " real")
  plot.xlabel("Días a partir del parto (origen)")
  plot.ylabel(hormona)
  plot.legend()
  plot.title(hormona + " real vs interpolada")
  for i in lista:
    print(hormona + " interpolada x=" + str(i["x"]) + ": " + str(f_interpolada(i["x"])))
    lista_retorno.append({"posicion": i["x"], "valor_interpolado":float(f_interpolada(i["x"])) })
  return lista_retorno
#-----------------------------------------------------

#Interpolación Progesterona ID19
lista_id19 = Interpolar(idA,"pdsg",180,540,1)

#Realizo una copia del dataframe para que el original de GitHub siga sin cambios
id19_interpolado = idA.copy()

#Recorro la lista generada y completo los valores interpolados en la copia del dataframe
for i in lista_idA:
  id19_interpolado.loc[idA_interpolado['Indice'] == i["posicion"], 'pdsg'] = i["valor_interpolado"]

  lista_idA_fshsg = Interpolar(idA,"fshsg",180,540,1)

for i in lista_idA_fshsg:
  idA_interpolado.loc[idA_interpolado['Indice'] == i["posicion"], 'fshsg'] = i["valor_interpolado"]