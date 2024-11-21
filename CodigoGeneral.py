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
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.datasets import load_digits
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import RocCurveDisplay, classification_report,mean_squared_error, r2_score
from sklearn.tree import DecisionTreeRegressor
from sklearn.svm import SVR,SVC
from sklearn.linear_model import ElasticNetCV,LassoCV,LinearRegression
from sklearn.inspection import partial_dependence,PartialDependenceDisplay
from scipy.interpolate import InterpolatedUnivariateSpline
import pathlib
import panel as pn
import xarray as xr
import holoviews as hv
from bokeh.resources import INLINE,CDN
pn.extension('tabulator', template='material', sizing_mode='stretch_width')
from bokeh.palettes import HighContrast3,Spectral
import colorcet as cc
from datetime import datetime

#Token generado en mi cuenta personal de Github para acceder al repositorio privado
username = ''
token = ''

github_session = requests.Session()
github_session.auth = (username, token)

url = ""
download = github_session.get(url).content

pacroc_dataframe = pd.read_csv(io.StringIO(download.decode('utf-8')))
pacroc_dataframe.columns = ['ID','Fecha de parto','Fecha primer día de transición folicular con ciclo ovulatorio','Cantidad de días entre el parto y la ovulación','Origen']

pacroc_dataframe.columns
pacroc_dataframe.head()
alt.Chart(pacroc_dataframe).mark_point().encode(y='Cantidad de días entre el parto y la ovulación',x='ID',tooltip=['ID','Fecha de parto','Fecha primer día de transición folicular con ciclo ovulatorio','Cantidad de días entre el parto y la ovulación']).interactive()

url = ""
download = github_session.get(url).content

pacroc_dataframe = pd.read_csv(io.StringIO(download.decode('utf-8')))
pacroc_dataframe.columns = ['ID','Fecha de parto','Fecha primer día de transición folicular con ciclo ovulatorio','Cantidad de días entre el parto y la ovulación','Origen']

pacroc_dataframe.columns
pacroc_dataframe.head()

intervalos = [0,500]

pacroc_dataframe.plot.hist(bins=20, color='#F2AB6D', rwidth=0.5) # generamos el histograma a partir de los datos
plot.xticks(intervalos)
plot.ylabel('Frecuencia')
plot.xlabel('Días entre parto y ovulación')
plot.title('Histograma')

plot.show()

url = ""
download = github_session.get(url).content

pacroc_dataframe = pd.read_csv(io.StringIO(download.decode('utf-8')))
pacroc_dataframe.columns = ['ID','Fecha de parto','Fecha primer día de transición folicular con ciclo ovulatorio','Cantidad de días entre el parto y la ovulación','Origen']

plt.figure()    #Figura
plt.bar(pacroc_dataframe['ID'], pacroc_dataframe['Cantidad de días entre el parto y la ovulación'])          #El gráfico
plt.title('Gráfico de barras')      #El título
ax = plt.subplot()                   #Axis
ax.set_xlabel('ID')  #Nombre del eje x
ax.set_ylabel('Días entre parto y ovulación')  #Nombre del eje y

url = ""
download = github_session.get(url).content

pacroc_dataframe = pd.read_csv(io.StringIO(download.decode('utf-8')))

pacroc_dataframe.columns = ['muestra','ID','Fecha de parto','Fecha primer día de transición folicular con ciclo ovulatorio','Cantidad de días entre el parto y la ovulación','Origen','adipsg','cortsg','cpeptsg','e1gsg','fshsg','hcgsg','pdgsg']

pacroc_dataframe.columns
pacroc_dataframe.head()

alt.Chart(pacroc_dataframe).mark_point().encode(y= 'adipsg',x='muestra')


url = ""
download = github_session.get(url).content

pacroc_dataframe = pd.read_csv(io.StringIO(download.decode('utf-8')))

pacroc_dataframe.columns = ['muestra','ID','Fecha de parto','Fecha primer día de transición folicular con ciclo ovulatorio','Cantidad de días entre el parto y la ovulación','Origen','adipsg','cortsg','cpeptsg','e1gsg','fshsg','hcgsg','pdgsg']

pacroc_dataframe.columns
pacroc_dataframe.head()

alt.Chart(pacroc_dataframe).mark_point().encode(y= 'cortsg',x='muestra')

url = ""
download = github_session.get(url).content

pacroc_dataframe = pd.read_csv(io.StringIO(download.decode('utf-8')))

pacroc_dataframe.columns = ['muestra','ID','Fecha de parto','Fecha primer día de transición folicular con ciclo ovulatorio','Cantidad de días entre el parto y la ovulación','Origen','adipsg','cortsg','cpeptsg','e1gsg','fshsg','hcgsg','pdgsg']

pacroc_dataframe.columns
pacroc_dataframe.head()

alt.Chart(pacroc_dataframe).mark_point().encode(y= 'cpeptsg',x='muestra')

url = ""
download = github_session.get(url).content

pacroc_dataframe = pd.read_csv(io.StringIO(download.decode('utf-8')))

pacroc_dataframe.columns = ['muestra','ID','Fecha de parto','Fecha primer día de transición folicular con ciclo ovulatorio','Cantidad de días entre el parto y la ovulación','Origen','adipsg','cortsg','cpeptsg','e1gsg','fshsg','hcgsg','pdgsg']

pacroc_dataframe.columns
pacroc_dataframe.head()

alt.Chart(pacroc_dataframe).mark_point().encode(y= 'e1gsg',x='muestra')

url = ""
download = github_session.get(url).content

pacroc_dataframe = pd.read_csv(io.StringIO(download.decode('utf-8')))

pacroc_dataframe.columns = ['muestra','ID','Fecha de parto','Fecha primer día de transición folicular con ciclo ovulatorio','Cantidad de días entre el parto y la ovulación','Origen','adipsg','cortsg','cpeptsg','e1gsg','fshsg','hcgsg','pdgsg']

pacroc_dataframe.columns
pacroc_dataframe.head()

alt.Chart(pacroc_dataframe).mark_point().encode(y= 'pdgsg',x='muestra')

url = ""
download = github_session.get(url).content

pacroc_dataframe = pd.read_csv(io.StringIO(download.decode('utf-8')))

pacroc_dataframe.columns = ['muestra','ID','Fecha de parto','Fecha primer día de transición folicular con ciclo ovulatorio','Cantidad de días entre el parto y la ovulación','Origen','adipsg','cortsg','cpeptsg','e1gsg','fshsg','hcgsg','pdgsg']

pacroc_dataframe.columns
pacroc_dataframe.head()

alt.Chart(pacroc_dataframe).mark_point().encode(y= 'fshsg',x='muestra')

url = ""
download = github_session.get(url).content

pacroc_dataframe = pd.read_csv(io.StringIO(download.decode('utf-8')))

pacroc_dataframe.columns = ['muestra','ID','Fecha de parto','Fecha primer día de transición folicular con ciclo ovulatorio','Cantidad de días entre el parto y la ovulación','Origen','adipsg','cortsg','cpeptsg','e1gsg','fshsg','hcgsg','pdgsg']

pacroc_dataframe.columns
pacroc_dataframe.head()

alt.Chart(pacroc_dataframe).mark_point().encode(y= 'hcgsg',x='muestra')

# Gráfico de la hormona ADIPSG del ID 1 al 10
# Si grafico todos los ID las curvas quedan muy superpuestas

p = figure(title="Hormona ADIPSG por ID", height=700, width=1200)
p.xgrid.grid_line_color=None
p.ygrid.grid_line_alpha=0.5
p.xaxis.axis_label = 'Número de muestra'
p.yaxis.axis_label = 'ADIPSG'

p.line(pacroc_dataframe.index, pacroc_dataframe['A'],legend_label = 'ID=A',line_color='blue')
p.line(pacroc_dataframe.index, pacroc_dataframe['B'],line_color="orange",legend_label= 'ID=B')
p.line(pacroc_dataframe.index, pacroc_dataframe['C'],line_color="red",legend_label= 'ID=C')
p.line(pacroc_dataframe.index, pacroc_dataframe['D'],line_color="green",legend_label= 'ID=D')
p.line(pacroc_dataframe.index, pacroc_dataframe['E'],line_color="grey",legend_label= 'ID=E')
p.line(pacroc_dataframe.index, pacroc_dataframe['F'],line_color="pink",legend_label= 'ID=F')
p.line(pacroc_dataframe.index, pacroc_dataframe['G'],line_color="yellow",legend_label= 'ID=G')
p.line(pacroc_dataframe.index, pacroc_dataframe['H'],line_color="black",legend_label= 'ID=H')
p.line(pacroc_dataframe.index, pacroc_dataframe['I'],line_color="purple",legend_label= 'ID=I')


show(p)

#Dataframes auxiliares sin los valores nulos de la tabla, es decir los días que no hubieron mediciones
df1 = pacroc_dataframe[(pacroc_dataframe['A'] != 0)]
df2 = pacroc_dataframe[(pacroc_dataframe['B'] != 0)]

p = figure(title="Puntos importantes Hormona ADIPSG por ID - Rojo ID A - Verde ID B", height=350, width=900)
p.xgrid.grid_line_color=None
p.ygrid.grid_line_alpha=0.5
p.xaxis.axis_label = 'Número de muestra'
p.yaxis.axis_label = 'ADIPSG'

pacroc_dataframe = pacroc_dataframe.fillna(0)

p.square(pacroc_dataframe.index, pacroc_dataframe['A'], legend_label="ID=A, 80 días", size=3, line_color="orange", fill_color = None)
p.line(pacroc_dataframe.index, pacroc_dataframe['A'], legend_label="ID=A, 80 días", line_color="orange")

p.circle(pacroc_dataframe.index, pacroc_dataframe['S'], legend_label="ID=S, 1423 días", size=7, fill_color=None)
p.line(pacroc_dataframe.index, pacroc_dataframe['S'], legend_label="ID=S, 1423 días")

p.square(x = 16, y= pacroc_dataframe['A'].max(), color="red", size=5)
label = Label(x=16.5, y=36, x_offset=6, text="Máximo 36,16", text_baseline="middle", text_font_size ='13px', text_color = 'red')
p.add_layout(label)

p.circle(x = 18, y= pacroc_dataframe['S'].max(), color="green", size=5)
label = Label(x=21, y=10, x_offset=26, text="Máximo 9,94", text_baseline="middle", text_font_size ='13px', text_color = 'green')
p.add_layout(label)

p.square(x = 17, y= df1['A'].min(), color="red", size=5)
label = Label(x=41, y=5, x_offset=6, text="Mínimo 1,29", text_baseline="middle", text_font_size ='13px', text_color = 'red')
p.add_layout(label)

p.circle(x = 44, y= df2['S'].min(), color="green", size=5)
label = Label(x=45, y=2, x_offset=6, text="Mínimo 0,52", text_baseline="middle", text_font_size ='13px', text_color = 'green')
p.add_layout(label)

show(p)

output_notebook()

url = ""
download = github_session.get(url).content

pacroc_dataframe = pd.read_csv(io.StringIO(download.decode('utf-8')))
pacroc_dataframe.columns = ['ID', 'Días entre parto y ciclo ovulatorio-transición folicular','Clase','Valor medio ADIPSG']
url2 = ''
download2 = github_session.get(url2).content

pacroc_dataframe2 = pd.read_csv(io.StringIO(download2.decode('utf-8')))
pacroc_dataframe2.columns = ['ID', 'Días entre parto y ciclo ovulatorio-transición folicular','Clase','Valor medio ADIPSG']

p = figure(title="ADIPSG separada por clases: rojo clase 0 y verde clase 1", height=350, width=900)
p.xgrid.grid_line_color=None
p.ygrid.grid_line_alpha=0.5
p.xaxis.axis_label = 'Individuos de la clase'
p.yaxis.axis_label = 'ADIPSG por clase'

p.circle([0,1,2,3,4,5,6,7,8,9,10,11,12], pacroc_dataframe['Valor medio ADIPSG'], legend_label="Clase 0", size=3, line_color="red", fill_color ='red')
p.line([0,1,2,3,4,5,6,7,8,9,10,11,12], pacroc_dataframe['Valor medio ADIPSG'], legend_label="Clase 0", line_color = 'red')
p.circle([13,14,15,16,17,18,19,20,21,22,23,24,25,26], pacroc_dataframe2['Valor medio ADIPSG'], legend_label="Clase 1", size=3, line_color="blue", fill_color ='blue')
p.line([13,14,15,16,17,18,19,20,21,22,23,24,25,26], pacroc_dataframe2['Valor medio ADIPSG'], legend_label="Clase 1", line_color = 'blue')

show(p)

