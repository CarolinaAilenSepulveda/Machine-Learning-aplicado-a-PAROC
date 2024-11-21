output_notebook()
pn.pane.Markdown('## PAROC')
dashboard_title = pn.panel('Pantalla interactiva - Proyecto PAROC')

#Primer gráfico hormonas de un solo ID
p = figure(title="Hormonas IDA vs Días a partir del parto", height=300, width=500)
p.xgrid.grid_line_color=None
p.ygrid.grid_line_alpha=0.5
p.xaxis.axis_label = 'Días a partir del parto'
p.yaxis.axis_label = 'Hormonas IDA'

p.line(x_adipsg, y_adipsg ,legend_label = 'ADIPSG',line_color="orange")
p.line(x_adipsg, y_cpeptsg ,legend_label = 'CPEPTSG',line_color="blue")
p.line(x_adipsg, y_elgsg ,legend_label = 'ELGSG',line_color="green")
p.line(x_adipsg, y_fshsg ,legend_label = 'FSHSG',line_color="yellow")
p.line(x_adipsg,y_hcgsg ,legend_label = 'HCGSG',line_color="pink")
p.line(x_adipsg, y_pdsg ,legend_label = 'PROGESTERONA',line_color="red")
p.line(x_cortisol, y_cortisol ,legend_label = 'CORTSG',line_color="grey")

p.legend.location = "top_left"
p.legend.title_text_font_style = "bold"
p.legend.title_text_font_size = "20px"
p.legend.label_text_font_size = "10px"
p.legend.click_policy="hide"

#Siguiente gráfico de hormona Progesterona por ID

p1 = figure(title="Hormona Progesterona por ID vs Días a partir del parto", height=300, width=500)
p1.xgrid.grid_line_color=None
p1.ygrid.grid_line_alpha=0.5
p1.xaxis.axis_label = 'Días a partir del parto'
p1.yaxis.axis_label = 'Hormona ADIPSG'

p1.line(idA_interpolado["Indice"], idA_interpolado["pdsg"] ,legend_label = 'ID19',line_color="orange")
p1.line(idB_interpolado["Indice"], idB_interpolado["pdsg"] ,legend_label = 'ID23',line_color="red")
p1.line(idC_interpolado["Indice"], idC_interpolado["pdsg"] ,legend_label = 'ID27',line_color="blue")
p1.line(idD_interpolado["Indice"], idD_interpolado["pdsg"] ,legend_label = 'ID28',line_color="green")
p1.line(idE_interpolado["Indice"],idE_interpolado["pdsg"] ,legend_label = 'ID36',line_color="yellow")
p1.line(idF_interpolado["Indice"],idF_interpolado["pdsg"] ,legend_label = 'ID37',line_color="purple")
p1.line(idG_interpolado["Indice"], idG_interpolado["pdsg"] ,legend_label = 'ID58',line_color="pink")

p1.legend.location = "top_left"
p1.legend.title_text_font_style = "bold"
p1.legend.title_text_font_size = "20px"
p1.legend.label_text_font_size = "10px"
p1.legend.click_policy="hide"

#Gráfico acumulativo hormonas por ID

suma_adipsgA = 0
suma_adipsgB = 0
suma_cpepC = 0
suma_cpepD = 0
suma_elgsgE =0
suma_elgsgF =0

#Si sirve el gráfico propongo hacer una función que realice las sumas en automático

for i in idA_interpolado["adipsg"]:
  suma_adipsgA = suma_adipsgA + i
for i in idA_interpolado["cpeptsg"]:
  suma_cpepA = suma_cpepA + i
for i in idB_interpolado["adipsg"]:
  suma_adipsgB = suma_adipsgB + i
for i in idB_interpolado["cpeptsg"]:
  suma_cpepB = suma_cpepB + i
for i in idA_interpolado["elgsg"]:
  suma_elgsgA = suma_elgsgA + i
for i in idB_interpolado["elgsg"]:
  suma_elgsgB = suma_elgsgB + i

ids = ["A", "B"]
hormonas = ["adipsg","cpeptsg","elgsg"]
data = {"ids": ids,
        "adipsg": [int(suma_adipsgA), int(suma_adipsgB)],
        "cpeptsg": [int(suma_cpepA), int(suma_cpepB)],
        "elgsg": [int(suma_elgsgA), int(suma_elgsgB)]
}

p2 = figure(x_range=ids, height=300, width=500, title="Hormonas acumuladas por ID",
            tools="hover", tooltips="$name @ids: @$name",toolbar_location= None)

p2.vbar_stack(hormonas,x = "ids", width=0.3,color= ["#225ea8",'#41b6c4', '#a1dab4'], source=data,
             legend_label=hormonas)

p2.y_range.start = 0
p2.x_range.range_padding = 0.2
p2.xgrid.grid_line_color = None
p2.axis.minor_tick_line_color = None
p2.outline_line_color = None
p2.legend.location = "bottom_left"
p2.legend.orientation = "vertical"

#Gráfico acumulativo por día para un solo ID (todas las mediciones de hormonas)
lista_fechas = []
for i in idA_interpolado["Indice"]:
    lista_fechas.append(str(i))

fechas = lista_fechas
hormonas_2 = ["adipsg","cpeptsg","elgsg"]
data_2 = {"fechas": fechas,
        "adipsg": idA_interpolado["adipsg"],
        "cpeptsg": idA_interpolado["cpeptsg"],
        "elgsg": idA_interpolado["elgsg"]
}

p3 = figure(x_range=fechas, height=500, width=1000, title="Hormonas acumuladas por día para IDA",
            tooltips="$name @fechas: @$name")

p3.vbar_stack(hormonas,x = "fechas", width=0.3,color= ["#225ea8",'#41b6c4', '#a1dab4'], source=data_2,
             legend_label=hormonas_2)

p3.y_range.start = 0
p3.x_range.range_padding = 0.2
p3.legend.location = "bottom_left"
p3.legend.orientation = "vertical"

#Armo las columnas del dashboard
header = pn.Column(dashboard_title)
column = pn.Column(
    pn.Row(
        p,
        p1),
    pn.Row(
        p2
    ),
    pn.Row(
        p3
    )
)
mini_dashboard = pn.Column(header, column)
mini_dashboard

#Guardo el dashboard como html para acceder aparte
#mini_dashboard.save('test.html')

#-----------------------------------------
#Segunda versión

output_notebook()
pn.pane.Markdown('## PAROC')
dashboard_title = pn.panel('Pantalla interactiva de hormonas - Proyecto PAROC')

#Primer gráfico hormonas de un solo ID
def Graficar_bok(x,adip,cpep,elg,fsh,hcg,pds,cort,titulo,label,origen):
  p = figure(title=titulo, height=300, width=500)
  p.xgrid.grid_line_color=None
  p.ygrid.grid_line_alpha=0.5
  p.xaxis.axis_label = origen
  p.yaxis.axis_label = label

  p.line(x, y_adipsg ,legend_label = 'ADIPSG',line_color="orange")
  p.line(x, y_cpeptsg ,legend_label = 'CPEPTSG',line_color="blue")
  p.line(x, y_elgsg ,legend_label = 'ELGSG',line_color="green")
  p.line(x, y_fshsg ,legend_label = 'FSHSG',line_color="yellow")
  p.line(x,y_hcgsg ,legend_label = 'HCGSG',line_color="pink")
  p.line(x, y_pdsg ,legend_label = 'PROGESTERONA',line_color="red")
  p.line(x, y_cortisol ,legend_label = 'CORTSG',line_color="grey")

  p.legend.location = "top_left"
  p.legend.title_text_font_style = "bold"
  p.legend.title_text_font_size = "20px"
  p.legend.label_text_font_size = "10px"
  p.legend.click_policy="hide"
  return p
#p = Graficar_bok(x_adipsg,"Hormonas IDA vs Días a partir del parto",'Hormonas IDA','Días a partir del parto')

#Armo las columnas del dashboard
#header = pn.Column(dashboard_title)
#column = pn.Column(
#    pn.Row(
#        p)
    #pn.Row(
    #    p2
    #),
    #pn.Row(
    #    p3
#    )

#mini_dashboard = pn.Column(header, column)
#mini_dashboard

#Guardo el dashboard como html para acceder aparte
#mini_dashboard.save('test.html')