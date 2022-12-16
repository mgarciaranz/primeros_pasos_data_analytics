#----------------------------------------------LIBRERIAS----------------------------------------------------------------------
import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns  
import plotly.express as px
import streamlit.components.v1 as components
import pickle as pkle
import os.path

#----------------------------------------------CONFIGURACIÓN DE PÁGINA ----------------------------------------------------------------------

st.set_page_config(page_title="Internet Revolution", layout="wide") # después establecer el título de página, su layout e icono 


#---------------------------------------------- COSAS QUE PODEMOS USAR EN TODA NUESTRA APP----------------------------------------------------------------------
df_region=pd.read_csv('internet_region_TS.csv')
df_countries=pd.read_csv('final_countries_TS.csv')
fixed_20=pd.read_csv('fixed_broadband_20.csv')
st.set_option('deprecation.showPyplotGlobalUse', False)


#---------------------------------------------- EMPIEZA LA APP ----------------------------------------------------------------------
st.sidebar.subheader('Proyecto realizado por Marta García Ranz')
st.sidebar.subheader('''
    OBJETIVO:
    Conoce todo lo que debes saber sobre las cifras y tendencias de la **revolución de Internet** desde sus inicios hasta hoy.
    ''')
st.sidebar.subheader('**TABLA DE CONTENIDOS:**')
st.sidebar.write('¡Disfruta la lectura de las siguientes páginas!')
# creamos un botón en el side bar con el que nos movemos a la siguiente página
next = st.sidebar.button('Siguiente página')
#creamos la lista de opciones
#tiene que estar en el mismo orden que la que pasaremos al 'radio button'
new_choice = ["Introducción a la historia de Internet","Tratado de datos","Datos de la evolución (1990 - actualidad)", "Análisis Regional con Power BI","Brecha Digital", "Modelo Predictivo","Conclusión"] 

if os.path.isfile('next.p'): # next cliked el indice de la pagina que va a intenatar mostrar
    next_clicked = pkle.load(open('next.p', 'rb'))

    if next_clicked == len(new_choice):
        next_clicked = 0 # cuando next clicked es igual a la longitud de mi lista, vuelve a la pagina 0 de incio
else:
    next_clicked = 0 # cuando nextp no existe, significa que acabamos de abrirlo y portanto empieza en cero.

# comprobamos si el ususario ha hecho click en
# next button y aumentamos el indice (next_clicked)
if next:
    #incrementamos el valor para pasar a la siguiente pàgina
    next_clicked = next_clicked +1

    # comprobamos si estamos al final de la lusta de paginas
    if next_clicked == len(new_choice):
        next_clicked = 0 # volvemos a la pagina de inicio

# creamos el 'radio button' 
choice = st.sidebar.radio('Páginas:',("Introducción a la historia de Internet","Tratado de datos","Datos de la evolución (1990 - actualidad)","Análisis Regional con Power BI", "Brecha Digital","Modelo Predictivo","Conclusión"), index=next_clicked)

# pickle the index associated with the value, to keep track if the radio button has been used
pkle.dump(new_choice.index(choice), open('next.p', 'wb'))

# finally get to whats on each page
st.sidebar.subheader('**FUENTES:**')
st.sidebar.markdown('https://www.itu.int/en/ITU-D/Statistics/Pages/stat/default.aspx')
st.sidebar.markdown('https://marketing4ecommerce.net/historia-de-internet/')
st.sidebar.markdown('https://ayudaleyprotecciondatos.es/2021/06/22/brecha-digital/')
st.sidebar.markdown('https://financesonline.com/number-of-internet-users/')
#------------------------------------------------------intro---------------------------------------------------------------------------------------#
if choice == 'Introducción a la historia de Internet':
    st.title('LA GRAN REVOLUCIÓN DE INTERNET: CIFRAS Y TENDENCIAS')
    st.write('Internet ha supuesto una gran revolución, su nombre, una abreviatura de los términos **Network** (red, en inglés) e **Interconnect** (de interconexión), indican precisamente el motivo para el cual fue creado: **acelerar las comunicaciones**.')
    st.subheader('Introducción a la historia de Internet: primeros acontecimientos y escenario actual.')    
    col1, col2 = st.columns((2,3), gap='large')
    with col1: 
        st.subheader('')
        st.image('istockphoto-1224972179-612x612.jpg')
        st.subheader('')
        st.image('email.webp')
    with col2:
        st.subheader('''
            Inicio
            Internet nace en **Estados Unidos**, durante los años de la Guerra Fría, como un proyecto militar para asegurar las comunicaciones entre diferentes puntos del territorio en caso de sufrir un ataque de la entonces URSS. En este contexto, en 1957, se organiza en Estados Unidos la Advanced Research Projects Agency conocida como ARPA. Sus investigaciones sobre redes descentralizadas y sistemas de comunicación inmunes a ataques externos, sentaron los fundamentos de lo que décadas más tarde sería conocido como Internet.
            ''')

        st.subheader('''
            Hitos en la historia de internet:
                  ''')
        st.write('1962: Primer proyecto ARPAnet.')
        st.write('1969: Envío del primer mensaje entre dos computadoras.')
        st.write('1971: Roy Tomlinson inventa el correo y la arroba, se envía el primer email.')
        st.write('1974: Vin Cerf y Kahn proponen un protocolo llamado TCP/IP ')
        st.write('1990: Primera página web WWW, world wide web.') 
        
        st.subheader('''
            Actualidad
            Año tras año se incrementa de forma exponencial el número de usuarios de internet en el mundo, una cifra que se ha visto impulsada en parte por la gran penetración que han tenido los dispositivos móviles.
            No hay duda de que **internet ha cambiado la forma en que el mundo aprende, se comunica, hace negocios, etc.**
            Las nuevas tecnologías de la información y las comunicaciones (TIC) ofrecen **grandes oportunidades de mejora**, sin embargo, son todavía muchos los desafíos a los que se enfrenta como la **desigualdad en el acceso digital**, o **prácticas abusivas** (spam,  piratería,  usurpación de identidad, etc.).
            El objetivo de este proyecto es analizar **la evolución de internet** y **las desigualdades en cuanto a acceso** digital que persisten hoy en día.
            ''')
#-----------------------------------------------------dataset---------------------------------------------------------------------------------------#    
elif choice=="Tratado de datos":
    st.title('LA GRAN REVOLUCIÓN DE INTERNET: CIFRAS Y TENDENCIAS')
####### dataset original de kaggle
    st.subheader('Dataset para analizar el numero de ususarios (% de la población) desde 1990-actualidad')
    st.write('Nuestro punto de partida son dos datasets obtenidos de Kaggle, uno con el numero de usuarios como porcentaje de la población y otro en cifras absolutas. Si bien son una buena base con la que empezar a trabajar, faltan datos para el período 2016-2021. Asimismo, los países no están clasificados por regiones o grupos. A continuación, veremos cómo se añaden **nuevas filas** y **columnas** para completar la información.')
    df_share_internetusers= pd.read_csv('share-of-individuals-using-the-internet.csv')
    df_penetration=pd.read_csv('broadband-penetration-by-country.csv')
    df_num_internetusers = pd.read_csv('number-of-internet-users-by-country.csv')
    st.write('**Usuarios de internet (% de la población)**')
    st.dataframe(df_share_internetusers)
    st.markdown('Fuente:https://www.kaggle.com/datasets/pavan9065/internet-usage')
    st.write('**Usuarios de internet (cifras absolutas)**')
    st.dataframe(df_num_internetusers)
    st.markdown('Fuente:https://www.kaggle.com/datasets/pavan9065/internet-usage')

###### nuevas filas
    st.subheader('Nuevas filas: ampliación del dataset para los años del 2016 al 2021')
    df_ampliacion_user_percentage=pd.read_excel('ampliacion.xlsx', header=3)
    subdata_ampliacion_user_percentage = df_ampliacion_user_percentage[['Country Name', 'Country Code','2016','2017','2018','2019','2020','2021']]
    
    st.write('**Ampliación "usuarios de internet(% de la población)" para los años 2016-2021**')
    st.dataframe(subdata_ampliacion_user_percentage)
    st.markdown('Fuente:https://data.worldbank.org/indicator/IT.NET.USER.ZS')
    st.write('No se ha encontrado directamente la información del número de usuarios de internet por país, por lo que los datos faltantes se han calculado a partir del porcentaje de usuarios y el total de la población. A continuación se muestra el dataframe con los datos de **población**.')
    df_poblacion=pd.read_excel('poblacion.xlsx')
    st.write('**Población**')
    st.dataframe(df_poblacion)
    st.markdown('Fuente:https://data.worldbank.org/indicator/IT.NET.USER.ZS')
###### nuevas columnas
    st.subheader('Nuevas columnas: Sub región, Región, y Grupo de Ingresos')
    df_geo=pd.read_csv('geography.csv')
    st.write('Nos parece interesante agrupar los países en regiones y subregiones. Para ello se utiliza una clasificación realizada por el Departamento de Asuntos Económicos y Sociales de las Naciones Unidas. En el siguiente mapa se pude observar la misma')
    st.write('**Mapa de las Sub Regiones del mundo (clasificación de las Naciones Unidad)**')
    chart16 = px.choropleth(df_geo, locations='Country Name', locationmode='country names',color='Sub-region Name', color_continuous_scale= 'Tealgrn')
    st.plotly_chart(chart16 , use_container_width=True)
    st.markdown('Fuente:https://unstats.un.org/unsd/methodology/m49/overview')
    st.write('Además, con la finalidad de hacer un estudio sobre la brecha digital global que existe hoy en día, necesitamos conocer para cada país, el grupo de ingreso al que pertenece. En este caso empleamos la clasificación de países por grupo de ingresos que realiza el Banco Mundial.')
    chart17= px.choropleth(df_geo, locations='Country Name', locationmode='country names',color='Grupo de Ingresos del Banco Mundial ')
    st.write('**Mapa de los países por grupos de ingreso (clasificación del Banco Mundial)**')
    st.plotly_chart(chart17 , use_container_width=True)
    st.markdown('Fuente:https://ilostat.ilo.org/es/resources/concepts-and-definitions/classification-country-groupings/')
    st.write('**Dataset Resultante**')###vamos a mosotrar un sub dataframe para espanna
    sub_df_countries=(df_countries[['Country Name','ISO3 Code','Region Name','Sub-region Name','Year','Grupo de Ingresos','Internet users (%)','Number of internet users']])
    spain=sub_df_countries[sub_df_countries['Country Name']=='Spain']
    st.dataframe(spain.set_index('Country Name'))### para que no se muestre el num del índice del dataframe general
##### dataset brecha digital
    st.subheader('Dataset Brecha Digital')
    st.write('En la sección número 5 del proyecto hablamos de las diferencias de acceso digital entre los distintos países del mundo en función del poder adquisitivo de sus ciudadanos. En este análisis, para evaluar de manera correcta las diferencias entre los países de distinto nivel de ingreso, es necesario tener en cuenta tanto la calidad como el método de acceso a internet, es por ello que utilizaremos la variable “Suscripciones de banda ancha”.')
    st.write('**Suscripciones de banda ancha fija en el 2020 (por cada 100 personas)**')
    st.dataframe(fixed_20)
###### definicion de variables
    st.subheader('Definición de las variables del proyecto')
    st.write('**Internet Users/Usuarios de Internet**: Personas que han utilizado Internet en los últimos 3 meses. Han podido conectarse a través de un ordenador, teléfono móvil, TV digital, etc.')
    st.write('**Fixed broadband subscriptions(per 100 people)/Suscripciones a banda ancha fija (por cada 100 personas)**: Las suscripciones a banda ancha fija incluye las siguientes tecnologías: DSL, Satélite, Cable, Wireless, y Fibra, entre otros. Este total se mide independientemente del método de pago.')
    st.pyplot()
#------------------------------------------------------evolucion---------------------------------------------------------------------------------------#
elif choice == 'Datos de la evolución (1990 - actualidad)':
    st.title('LA GRAN REVOLUCIÓN DE INTERNET: CIFRAS Y TENDENCIAS')
    st.subheader('''
        Internet tiene más de 50 años: datos de su evolución.
        A continuación, se muestra la evolución del número de usuarios de internet como porcentaje de la población. 
        En 1990, año en el que comienza la **gráfica**, solo la mitad del uno por ciento de la población mundial estaba en línea.
        En la década de los noventa, al menos en algunas partes del mundo, esto comienza a cambiar.
    ''')
    st.write('''
        En el año 2000, año en el que estalla la burbuja de las empresas “puntocom”, el 43 % de los estadounidenses tenía acceso a internet. En la Euro área, lo hacía el 22%. Pero en la mayor parte del mundo, internet no había llegado aún, en ese momento menos del 7% del mundo estaba en línea
        ''')
    st.write('''
        Quince años después, en 2016, en Estados Unidos, el 84% de las personas tenía acceso a internet. Durante estos años, países de muchas partes del mundo se pusieron al día, veamos el siguiente **mapa**, y sobrepasaron esta cifra. Islandia, Bermudas y Bahrain encabeza la clasificación con el 98% de la población en línea en 2016 ( veamos **ranking**).
        En el otro extremo del espectro, todavía hay países donde casi nada ha cambiado desde 1990, veamos **tabla**.  
        ''')
    st.write('''
        No obstante, la tendencia general a nivel mundial, tal y como muestra el gráfico, es clara: el número de usuarios de internet crece cada año.
        ''')
    tabs = st.tabs(["Gráficos", "Mapa", "Ranking", "Tabla"])
    tab_plots= tabs[0]
    zona_label = df_region['Entity'].unique().tolist()
    with tab_plots:
        Region='World'
        ZONA=df_region[df_region['Entity']==Region]
        chart2=px.line(ZONA, x='Year', y='Internet users (%)', title=f'{Region} : Evolución del numero de ususuarios de internet(% de la población)',color_discrete_sequence=px.colors.sequential.RdBu)
        st.plotly_chart(chart2, use_container_width=True)
        ############## select box country
        paises=list(df_countries['Country Name'].unique())
        option1= st.selectbox ('Seleccione un país:',sorted(paises),index=186)
        PH=df_countries[df_countries['Country Name']==option1]
        chart15=px.line(PH, x='Year', y='Internet users (%)', title=f'{option1} : Evolución del numero de ususuarios de internet(% de la población)',color_discrete_sequence=px.colors.sequential.RdBu)
        st.plotly_chart(chart15 , use_container_width=True)
        st.pyplot()

    tab_plots= tabs[1]
    with tab_plots:
        ########### Slider annos
        option2 =  st.slider('Seleccione un año:', min_value=1990,max_value=2021,value=2016,step=2)
        year_dat=df_countries[df_countries['Year']==option2]
        st.write(f'**Año {option2} -Mapa interactivo de la varible Usuarios de internet (% de la población).**')
        chart12=px.choropleth(year_dat, locations='Country Name', locationmode='country names',color='Internet users (%)',width=1300,height=600, color_continuous_scale= 'Tealgrn')
        st.plotly_chart(chart12 , use_container_width=True)
        st.pyplot()

    tab_plots= tabs[2]
    with tab_plots:
        ########### Slider annos
        option3 =  st.slider('Seleccione un año:', min_value=1991,max_value=2020,value=2015,step=1)
        year_dat=df_countries[df_countries['Year']==option3]
        top_yr=year_dat.sort_values(by='Internet users (%)',ascending=False).head(15)
        st.write(f'**Año {option3} Ranking Superior (15)**')
        chart8=px.bar(top_yr,x='Country Name', y='Internet users (%)',color='Region Name',color_discrete_sequence=px.colors.sequential.Tealgrn_r)
        st.plotly_chart(chart8 , use_container_width=True)
        tail_yr=year_dat.sort_values(by='Internet users (%)',ascending=False).tail(15)
        st.write(f'**Año {option3} Ranking Inferior (15)**')
        chart9=px.bar(tail_yr,x='Country Name', y='Internet users (%)',color='Region Name',color_discrete_sequence=px.colors.sequential.Sunset_r)
        st.plotly_chart(chart9 , use_container_width=True)
        st.pyplot()

    tab_plots= tabs[3]
    with tab_plots:
        ########### Slider annos
        annos=list(df_countries['Year'].unique())
        option4 =  st.selectbox('Seleccione un año:', sorted(annos),index=30)
        year_dat=df_countries[df_countries['Year']==option4]
        menos_20=year_dat[year_dat['Internet users (%)']<20]
        st.write(f'**Año {option4}- Tabla de los países con menos de un 20% de usuarios de internet (% de la población).**')
        st.table(menos_20[['Country Name','Region Name','Sub-region Name','Internet users (%)']].set_index('Country Name'))
        #st.table(df.assign(hack='').set_index('hack'))
#-----------------------------------powerbi---------------------------------------------------------------------------------------#
elif choice == 'Análisis Regional con Power BI':
    st.title('LA GRAN REVOLUCIÓN DE INTERNET: CIFRAS Y TENDENCIAS')
    st.subheader('''
        Análisis Regional con Power BI
        Esta en una herramienta donde se puede visualizar en detalle y profundidad los datos para cada una de las regiones.
        El panel consta de 4 gráficas: evolución del número de usuarios en cifras absolutas, distribución por grupos de ingreso, y ranking superior e inferior de los países con mayor penetración medida como usuarios en porcentaje de la población.
        ''')
    st.markdown('<iframe title="AA_PowerBI_Regiones" width="1140" height="541.25" src="https://app.powerbi.com/reportEmbed?reportId=01fff4cc-ed35-420c-aabc-3aae11b6d0e4&autoAuth=true&ctid=8aebddb6-3418-43a1-a255-b964186ecc64" frameborder="0" allowFullScreen="true"></iframe>',unsafe_allow_html=True)
    st.subheader('''
        ¿Existen países que no estén conectados a internet?
        Internet ha supuesto una gran revolución, influyendo en un elevado número de aspectos de nuestra vida cotidiana. Y aunque muchos de nosotros no podemos imaginar nuestras vidas sin los servicios que brinda, hoy en día todavía hay países que no tienen acceso a internet. A continuación. se enumeran aquellos que bloquean ciertos contenidos o tienen acceso muy limitado.
        ''')
    st.write('**China** : Tiene el mayor numero de usuarios de internet en el mundo, pero con una censura extrema,  el gobierno ha implementando más de 60 regulaciones.')
    st.write('**Cuba**: Internet se introdujo a finales de la década de 1990. No obstante, su implantación se estancó por varias razones, entre ellas la falta de financiación y las restricciones del gobierno.')
    st.write('**Irán**: El gobierno restringe la velocidad de internet con el objetivo de frustrar a los usuarios y limitar sus comunicaciones. ')
    st.write('**Corea del Norte**: El acceso a internet está disponible, pero estrictamente limitado. ')
    st.write('**Arabia Saudita**: Algunos sitios web están bloqueados. Como ejemplo, desde el 2006 se bloqueó el acceso a Wikipedia y Google Translate ya que se utilizaban para eludir los filtros que había colocado el gobierno')
    st.write('**Siria**:  Se han prohibido varios sitios web por razones políticas y se han arrestado a las personas que accedían a ellos.')
    st.write('**Uzbekistán**: La población tuvo acceso a internet por primera vez a finales de 1995. No obstante, su crecimiento ha sido lento, hoy día aproximadamente solo 9 millones de personas están conectadas a internet, siendo el total de la población 32 millones.')
    st.write('**Vietnam**: El acceso a internet está bloqueado por el gobierno, especialmente a los sitios que lo critican. También se bloquea la información sobre oposición política en el extranjero, temas religiosos o derechos humanos.')
    st.write('**Myanmar**: El acceso a redes sociales como Facebook, Twitter e Instagram se bloqueó temporalmente en un esfuerzo por silenciar la disidencia.')
    st.markdown('https://financesonline.com/number-of-internet-users/')
#------------------------------------------------------brecha digital---------------------------------------------------------------------------------------#
elif choice == "Brecha Digital":
    st.title('LA GRAN REVOLUCIÓN DE INTERNET: CIFRAS Y TENDENCIAS')
    st.subheader('''
        Análisis de la Brecha Digital
        Llegados a este punto sabemos que internet nos ofrecen muchas oportunidades que pueden mejorar nuestra vida, sin embargo, no todo el mundo puede acceder a las mismas. 
        La diferencia de accesibilidad y uso de tecnologías digitales para determinadas personas o grupos se conoce como **brecha digital** y la lucha para combatirla se ha convertido en parte de la agenda de muchos gobiernos e instituciones de todo el mundo.
        Hay varias **causas de origen** de la brecha digital, puede ser una cuestión de condiciones socioeconómicas, situación geográfica, género, edad, cuestiones culturales, etc.
        ''')
    st.subheader('Tipos de brecha digital')
    st.write('1. Brecha digital global (primer nivel), que se refiere a las diferencias entre los distintos países del mundo.')
    st.write('2. Brecha social digital (segundo nivel), relacionada con las desigualdades existentes dentro de un determinado país.')
    st.write('3. Brecha digital democrática (tercer nivel), que se refiere al nivel de participación de los individuos en las actividades políticas y sociales, basado en el uso de las nuevas tecnologías.')
        
    st.subheader('''
        Brecha digital global en 2020
        Analizamos las diferencias de acceso digital entre los distintos países del mundo en función del poder adquisitivo de sus ciudadanos. Para evaluar de manera correcta las diferencias entre los países de distinto nivel de ingreso, es necesario tener en cuenta tanto la calidad como el método de acceso a internet, es por ello que utilizaremos la variable “Suscripciones de banda ancha (por cada 100 personas)”.    
        ''')
    st.write('**Mapa de conexiones de banda ancha fija en 2020 (por cada 100 personas)**')
    chart13=fig = px.choropleth(fixed_20, locations='Country Name', locationmode='country names', color='2020', color_continuous_scale= 'Magenta',width=1100,height=600)
    chart13.update_layout(coloraxis = dict(colorbar = dict(len = 0.70, orientation = 'h',y = -0.16,x =0.925,xanchor = 'right')))
    st.plotly_chart(chart13 , use_container_width=True)
    st.write('**¿Existe una diferencia estadísticamente significativa entre los países con distinto nivel de ingreso?**')
    st.write('Hemos realizado el **Test Saphiro Wilk** y concluido que la hipótesis nula de que la distribución de la variable "Suscripciones de banda ancha fija" era normal se puede rechazar. Por lo tanto, las comparaciones que hagamos para saber si existen diferencias significativas respecto a la variable "Suscripciones" se harán con el **test Mann Whitney**.')
    col1, col2 = st.columns(2)
    with col1:
        st.write('**CONCLUSION DEL CONTRASTE DE HIPOTESIS A/B TESTING**')
        st.write('**Existe una diferencia estadísticamente significativa entre:**')
        st.write('- Entre países con **ingresos altos** y **ingresos bajos**.')
        st.write('- Entre países con **ingresos mediano alto** y **ingresos bajos**.')
    #with col2:
        
    st.pyplot()
#----------------------------------------------Modelo Predictivo----------------------------------------------------
elif choice=="Modelo Predictivo":
    st.title('LA GRAN REVOLUCIÓN DE INTERNET: CIFRAS Y TENDENCIAS')
    st.subheader('Modelo predictivo: ARIMA (2,3,1)')
    st.write('Por último, implementamos un modelo predictivo utilizando ARIMA. **ARIMA** es un modelo estadístico que utiliza variaciones y regresiones de datos estadísticos con el fin de encontrar patrones para una predicción hacia el futuro. ')
    st.write('Uno de los problemas con el dataset como ya se ha comentado era la falta de datos para el periodo 2016-2021. En la página del World Bank hemos podido completar la información para varios de los países, no obstante, no hemos podido hacerlo para todos.')
    st.write('En esta sección, utilizamos la serie temporal **número de usuarios** desde 1990 hasta 2015 y utilizando el siguiente modelo ARIMA (p=2, d=3,q=1), predecimos los valores para los siguientes 10 periodos, es decir del 2016 al 2025. ')
    st.write('**Número de personas conectadas a internet en el mundo: Serie original vs Predicciones**')
    st.image('modelo_predictivo.png')
    st.write('Para validar el modelo, dividimos los datos en train y test, y calculamos el **RMSE(raíz del error cuadrático  medio)**. El RMSE de las diferencias entre los valores reales y predichos es 29119.656. Teniendo en cuenta las cifras que se intentan predecir son miles de millones, éste es un error pequeño.')
    st.write('Además, el nuevo informe **‘Digital 2022 April Global Statshot’** , sobre número de usuarios de internet, revela que la cifra mundial para el 2021 sobrepasa los 5 mil millones, comprobamos que el resultado de nuestro modelo también es así.')
    st.write('Gracias al modelo, podemos dibujar la evolución del número de usuarios mundiales desde 2016 hasta 2021, completando nuestro estudio, y predecir los siguientes años. Comprobamos que la tendencia general es que cada año se incrementa de exponencialmente el número de usuarios. Como bien señalan diversas fuentes, esto se debe a la penetración de los dispositivos móviles, podemos consultar más información en el siguiente enlace:')
    st.markdown('https://marketing4ecommerce.net/historia-de-internet/')
#---------------------------------------------------conclusion---------------------------------------------------------------------------------------#   
elif choice == 'Conclusión':
    st.title('LA GRAN REVOLUCIÓN DE INTERNET: CIFRAS Y TENDENCIAS')
    st.subheader('Número de personas conectadas a internet en el mundo:')
    st.image('modelo_predictivo.png')
    st.write('La velocidad a la que aumenta el número de personas conectadas a internet en el mundo es increíblemente rápida')
    st.write('En 1990, solo la mitad del uno por ciento de la población mundial tenía acceso, Estados Unidos era el país con el mayor porcentaje de usuarios de internet, un 0.78%, seguido de Noruega con 0.70%, y Suiza con 0.59%. ')
    st.write('En el año 2000, año en el que estalla la burbuja de las empresas “puntocom”, en Estados Unidos, el 44% de las personas ya tenía acceso a internet. En la Euro área, lo hacía el 22%. Pero en la mayor parte del mundo, Internet no había llegado aún, en ese momento menos del 7% del mundo estaba en línea.')
    st.write('Quince años después, en 2016, el 44% de la población mundial está conectada. En el ranking de países con mayor penetración nos encontramos con Islandia, Luxemburgo, Liechtenstein, Bermuda y Bahrain que superan en porcentaje de usuarios a Estados Unidos. ')
    st.write('En último ranking de 2020, en el top 5 tenemos cuatro países asiáticos y uno europeo: los Emiratos Arabes Unidos, Bahrain, Qatar, Kuwait e Islandia, con porcentajes iguales o cercanos al 100%. El valor que predice nuestro modelo para 2020 es un total de aproximadamente 5 mil millones de usuarios en el mundo.')
    st.write('La tendencia general global, tal y como muestra nuestro análisis predictivo, es clara: el número de usuarios de internet crece cada año. En Europa, solo Albania, Ucrania y San Marino tienen un porcentaje por debajo del 95%. Sin embargo, no podemos olvidarnos de que todavía hay países donde prácticamente la situación no ha cambiado desde 1990. ')
    st.write('Las nuevas tecnologías de la información y las comunicaciones (TIC) ofrecen grandes oportunidades para el desarrollo de las naciones, sin embargo, hemos comprobado que existen diferencias de acceso digital estadísticamente significativas entre los países con ingresos altos o mediano altos y los países de ingresos bajos. Es por ello que todavía queda trabajo por hacer y la lucha para combatir la brecha digital debe ser parte de la agenda de gobiernos e instituciones de todo el mundo.')