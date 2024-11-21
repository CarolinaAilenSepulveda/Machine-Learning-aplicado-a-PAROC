#Defino una función para realizar el interpolado de valores y para completar el dataset con los valores nuevos calculados

#FUNCIONES -------------------------------------------
def Obtener_indices(data, hormona):
  lista_aux = []
  for i in range(len(data)):
    if str(data.iloc[i][hormona]) == "nan":
       lista_aux.append({"x":data.iloc[i]['Indice'], "posicion": i })
  return lista_aux

def Interpolar(data,hormona,grado):
  lista_retorno = []
  lista = Obtener_indices(data,hormona)
  data_aux = data
  data = data.dropna(subset=[hormona])
  x = data['Indice']
  y = data[hormona]
  f_interpolada = InterpolatedUnivariateSpline(x,y,k=grado)

  for i in lista:
    lista_retorno.append({"posicion": i["x"], "valor_interpolado":float(f_interpolada(i["x"])) })
  return lista_retorno

#Interpolación ADIPSG IDA
lista_id19_adipsg = Interpolar(idA,"adipsg",180,540,1)

#Recorro la lista generada y completo los valores interpolados en la copia del dataframe
for i in lista_idA_adipsg:
  idA_interpolado.loc[idA_interpolado['Indice'] == i["posicion"], 'adipsg'] = i["valor_interpolado"]

#Grafico la hormona ADIPSG interpolada con el Cortisol sin interpolar para comparar las curvas
#Empiezo con el IDA
x_adipsg=idA_interpolado["Indice"]
y_adipsg=idA_interpolado["adipsg"]

idA_interpolado_cortsg=idA_interpolado.dropna(subset="cortsg")
y_cortisol=idA_interpolado_cortsg["cortsg"]
x_cortisol = idA_interpolado_cortsg["Indice"]

plot.plot(x_adipsg,y_adipsg, mew=1, label="ADIPONECTINA")
plot.plot(x_cortisol,y_cortisol, mew=1, label="CORTISOL")

plot.xlabel("Días a partir del parto (origen)")
plot.ylabel("Hormona ADIPSG/CORTSG")
plot.legend()
plot.title("ADIPSG/CORTSG para IDA")

#Función para interpolar todas las hormonas
#En el indice ya tengo anclado el cero en el día de parto, es decir si calculo la diferencia entre
#el día de parto y el primer dia de transición folicular, y ese valor se lo sumo a Indice tengo los valores de las hormonas
#anclados al primer día de transición folicular

nombres_hormonas = ["adipsg","pdsg","cpeptsg","elgsg","fshsg","hcgsg"]
lista_aux = []

def Interpolar_hormonas_parto(dataset,nuevo_dataset,id,texto):
  for i in nombres_hormonas:
    lista_aux = Interpolar(dataset,i,1)
    for j in lista_aux:
      nuevo_dataset.loc[nuevo_dataset['Indice'] == j["posicion"], i] = j["valor_interpolado"]
  dataset_final = nuevo_dataset.dropna(subset="cortsg")
  normalizar(nuevo_dataset)
  normalizar(dataset_final)
  fig, axs = plot.subplots(3, 3)
  fig.suptitle("Hormonas interpoladas con origen en " + texto + " "  + id)
  axs[0, 0].plot(nuevo_dataset["Indice"],nuevo_dataset["adipsg"],"tab:green")
  axs[0, 0].set_title("ADIPSG")
  axs[0, 1].plot(nuevo_dataset["Indice"],nuevo_dataset["cpeptsg"],'tab:red')
  axs[0, 1].set_title("CPEPTSG")
  axs[0, 2].plot(nuevo_dataset["Indice"],nuevo_dataset["elgsg"],'tab:orange')
  axs[0, 2].set_title("ELGSG")
  axs[1, 1].plot(nuevo_dataset["Indice"],nuevo_dataset["fshsg"],'tab:purple')
  axs[1, 1].set_title("FSHSG")
  axs[1, 2].plot(nuevo_dataset["Indice"],nuevo_dataset["hcgsg"],'tab:cyan')
  axs[1, 2].set_title("HCGSG")
  axs[2, 0].plot(nuevo_dataset["Indice"],nuevo_dataset["pdsg"],'tab:pink')
  axs[2, 0].set_title("PDSG")
  axs[1, 0].plot(dataset_final["Indice"],dataset_final["cortsg"],'tab:brown')
  axs[1, 0].set_title("CORTSG")
  fig.tight_layout()
  plot.savefig(str(id) + texto +".jpg",  bbox_inches='tight')

#Función para mover el origen del dataset
def Modificar_origen(dataset, parto,nuevo_origen):
  lista = []
  parto = datetime.strptime(parto, "%Y-%m-%d")
  primer_d_t = datetime.strptime(nuevo_origen, "%Y-%m-%d")
  intervalo = primer_d_t - parto
  traslacion = intervalo.days #Calculo la diferencia de dias entre el origen actual y el nuevo
  for i in range(len(dataset["Indice"])): #Recorro todos los valores del dataset
    lista.append(dataset.iloc[i]["Indice"] - traslacion)
  return lista

#Funcion para encontrar el tope de la hormona
def tope(hormona):
    varianza = np.var(hormona, ddof = 1)
    desviacion_estandar = np.sqrt(varianza)
    promedio = np.mean(hormona)
    tope_maximo = promedio + (1.5 * desviacion_estandar)
    return tope_maximo

lista_tope_vacia = []

#Funcion para normalizar el dataset con el tope de la hormona
def normalizar(dataset):
  columns_names_list = list(dataset.columns.values)
  for i in columns_names_list:
    if i != "Fecha de la muestra" and i != "Indice" and i !=  "pdsg":
      auxiliar = tope(dataset[i])
      dataset.loc[dataset[i] > auxiliar, i] = auxiliar
    if i == "pdsg":
        dataset.loc[dataset[i] > 5000, i] = 5000

nombres_hormonas = ["adipsg","pdsg","cpeptsg","elgsg","fshsg","hcgsg"]
lista_aux = []

def Graficar_sininterpolar(dataset,id,texto):
  fig, axs = plot.subplots(3, 3)
  fig.suptitle("Hormonas sin interpolar con origen en " + texto + " "  + id)
  axs[0, 0].plot(dataset["Indice"],dataset["adipsg"],"tab:green")
  axs[0, 0].set_title("ADIPSG")
  axs[0, 1].plot(dataset["Indice"],dataset["cpeptsg"],'tab:red')
  axs[0, 1].set_title("CPEPTSG")
  axs[0, 2].plot(dataset["Indice"],dataset["elgsg"],'tab:orange')
  axs[0, 2].set_title("ELGSG")
  axs[1, 1].plot(dataset["Indice"],dataset["fshsg"],'tab:purple')
  axs[1, 1].set_title("FSHSG")
  axs[1, 2].plot(dataset["Indice"],dataset["hcgsg"],'tab:cyan')
  axs[1, 2].set_title("HCGSG")
  axs[2, 0].plot(dataset["Indice"],dataset["pdsg"],'tab:pink')
  axs[2, 0].set_title("PDSG")
  axs[1, 0].plot(dataset["Indice"],dataset["cortsg"],'tab:brown')
  axs[1, 0].set_title("CORTSG")
  fig.tight_layout()
  plot.savefig(str(id) + " " + texto + " " + "SinInterpolar" +".jpg",  bbox_inches='tight')

# Función para verificar y reemplazar valores no numéricos a partir de la segunda columna
def modificar_vacios(df):
    for column in df.columns[2:]:  # Empezar desde la tercera columna
        for index, value in df[column].items():
            try:
                # Intentar convertir el valor a flotante o entero
                if isinstance(value, str) and value.strip() == '':
                    raise ValueError('Empty string')
                float_value = float(value)
                int_value = int(float_value)
            except ValueError:
                df.at[index, column] = float('nan')

modificar_vacios(idB)
idB.head(8)