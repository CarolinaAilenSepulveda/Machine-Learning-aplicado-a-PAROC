#SVC predictor: Support Vector Machines
url = ""
download = github_session.get(url).content

pacroc_dataframe = pd.read_csv(io.StringIO(download.decode('utf-8')))
pacroc_dataframe.columns = ['ID', 'Días entre parto y ciclo ovulatorio-transición folicular','Clase','Valor medio ADIPSG']

y = pacroc_dataframe['Clase'].values.reshape(-1,1)
x = pacroc_dataframe['Valor medio ADIPSG'].values.reshape(-1,1)
x_train,x_test,y_train,y_test=train_test_split (x,y,train_size=0.6,random_state=0)
features=['Clase']

modelo_1 = SVC(random_state=0).fit(x_train, y_train)


y_predicta=modelo_1.predict(x_test,)

print ('------------------------------------------------------------------------')
print ('CURVA ROC (receiver operating characteristic)')
print ('------------------------------------------------------------------------')

#Grafico curva ROC

RocCurveDisplay.from_estimator(modelo_1, x_test, y_test)

plt.show()

print('Reporte del clasificador')
print(classification_report(y_test, y_predicta))

#Función para entrenar el modelo y probar con los ID que tienen fecha de parto y transición folicular completa (25)
lista_dias = []
lista_id_mod = []

#Armo una lista nueva con las columnas a agregar en cada dataset, según su número de filas y el número de días entre parto
#y primer día de transición folicular
for i in lista_x:
  lista_dias.append(np.full(i["fila"], i["dias"]))

#Recorro los dataframe para preparlos
indice = 0
for i in lista_id:
  i["x"] = lista_dias[indice]
  i.fillna(i.idxmin()["cortsg"], inplace=True)
  lista_id_mod.append(i)
  indice = indice + 1

#Aca ya tengo la lista de ID con la nueva columna y sin NaN
#Preparo los datos
df = pd.concat(lista_id_mod, ignore_index=True)
x = df.drop(columns=["x","Fecha de la muestra","Indice"])
y = df["x"] #Variable a encontrar

X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=0)

# Modelos a utilizar
models = {
    "Linear Regression": LinearRegression(),
    "Decision Tree": DecisionTreeRegressor(random_state=0),
    "Support Vector Regressor": SVR(kernel='linear'),
    "ElasticNet" : ElasticNetCV(),
    "Lasso" : LassoCV(),
    "Random Forest R":RandomForestRegressor(random_state=0)
}

# Evaluación de los modelos
results = {}

for name, model in models.items():
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    mse = mean_squared_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)
    results[name] = {"MSE": mse, "R²": r2}

# Mostrar los resultados de cada modelo
for model_name, metrics in results.items():
    print(f"Modelo: {model_name}")
    print(f"  MSE: {metrics['MSE']}")
    print(f"  R²: {metrics['R²']}")
    print()

#Pruebo el modelo con una persona de las 25 de la cual se la cantidad de días real ID181
nueva_persona = lista_id_mod[A].drop(columns=["Fecha de la muestra","Indice","x"])

# Predicción para una nueva persona con el mejor modelo
prediccion = models["Linear Regression"].predict(nueva_persona)

print("El valor de dias entre parto y transición folicular fue estimado en:",prediccion[0])

hormonas = ["adipsg","pdsg","cpeptsg","elgsg","fshsg","hcgsg","cortsg"]

def Rellenar_hormonas(dataset):
  for i in hormonas:
    dataset.fillna(dataset.idxmin()[i], inplace=True)

Rellenar_hormonas(idB)
id5.head()

PartialDependenceDisplay.from_estimator(models["Linear Regression"], X_train,  ["adipsg","pdsg","cpeptsg","elgsg","fshsg","hcgsg","cortsg"])

plot.show()