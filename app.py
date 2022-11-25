import streamlit as st
import pandas as pd
import os 
import random


st.set_page_config(page_title="Chris Comunicador SC", page_icon="comunicador_sc.png", layout="wide", initial_sidebar_state="expanded")

with st.sidebar: 
    
    st.image("comunicador_sc.png")
    st.title("Chris Comunicador SC")
    # choice = st.radio("Navegación", ["Contesta","Ejecuta"])
    st.info("¡Comunicate usando metodologías científicas!")

st.title("Sigue estos pasos:")

df = pd.read_csv("comunicador_sc.csv")

decorar_frases = df.iloc[5].values.tolist()
decorar_frases = decorar_frases[5:]
decorar_frases = [x for x in decorar_frases if str(x) != 'nan']

comportamientos_habituales = df.iloc[6].values.tolist()
comportamientos_habituales = comportamientos_habituales[5:]
comportamientos_habituales = [x for x in comportamientos_habituales if str(x) != 'nan']

idis = df.iloc[7].values.tolist()
idis = idis[5:]
idis = [x for x in idis if str(x) != 'nan']

anti_aros_psicologicos = df.iloc[8].values.tolist()
anti_aros_psicologicos = anti_aros_psicologicos[5:]
anti_aros_psicologicos = [x for x in anti_aros_psicologicos if str(x) != 'nan']

respuestas_y_contractores = df.iloc[9].values.tolist()
respuestas_y_contractores = respuestas_y_contractores[5:]
respuestas_y_contractores = [x for x in respuestas_y_contractores if str(x) != 'nan']

magueadores_y_contramaqueadores = df.iloc[10].values.tolist()
magueadores_y_contramaqueadores = magueadores_y_contramaqueadores[5:]
magueadores_y_contramaqueadores = [x for x in magueadores_y_contramaqueadores if str(x) != 'nan']

autodescualificadores = df.iloc[11].values.tolist()
autodescualificadores = autodescualificadores[5:]
autodescualificadores = [x for x in autodescualificadores if str(x) != 'nan']

desarmadores = df.iloc[12].values.tolist()
desarmadores = desarmadores[5:]
desarmadores = [x for x in desarmadores if str(x) != 'nan']

rutinas_anti_cuelgue = df.iloc[13].values.tolist()
rutinas_anti_cuelgue = rutinas_anti_cuelgue[5:]
rutinas_anti_cuelgue = [x for x in rutinas_anti_cuelgue if str(x) != 'nan']

rutinas_gestuales = df.iloc[14].values.tolist()
rutinas_gestuales = rutinas_gestuales[5:]
rutinas_gestuales = [x for x in rutinas_gestuales if str(x) != 'nan']

abrir = df.iloc[15].values.tolist()
abrir = abrir[5:]
abrir = [x for x in abrir if str(x) != 'nan']

kino_accidental = df.iloc[16].values.tolist()
kino_accidental = kino_accidental[5:]
kino_accidental = [x for x in kino_accidental if str(x) != 'nan']

personalizar = df.iloc[17].values.tolist()
personalizar = personalizar[5:]
personalizar = [x for x in personalizar if str(x) != 'nan']

falcarse = df.iloc[18].values.tolist()
falcarse = falcarse[5:]
falcarse = [x for x in falcarse if str(x) != 'nan']

valor_1 = df.iloc[19].values.tolist()
valor_1 = valor_1[5:]
valor_1 = [x for x in valor_1 if str(x) != 'nan']

aislar = df.iloc[20].values.tolist()
aislar = aislar[5:]
aislar = [x for x in aislar if str(x) != 'nan']

sexualizar = df.iloc[21].values.tolist()
sexualizar = sexualizar[5:]
sexualizar = [x for x in sexualizar if str(x) != 'nan']

valor_2 = df.iloc[22].values.tolist()
valor_2 = valor_2[5:]
valor_2 = [x for x in valor_2 if str(x) != 'nan']

analizar_idis = df.iloc[23].values.tolist()
analizar_idis = analizar_idis[5:]
analizar_idis = [x for x in analizar_idis if str(x) != 'nan']

kino_intencional = df.iloc[24].values.tolist()
kino_intencional = kino_intencional[5:]
kino_intencional = [x for x in kino_intencional if str(x) != 'nan']

cualificar = df.iloc[25].values.tolist()
cualificar = cualificar[5:]
cualificar = [x for x in cualificar if str(x) != 'nan']

cierre_de_beso = df.iloc[26].values.tolist()
cierre_de_beso = cierre_de_beso[5:]
cierre_de_beso = [x for x in cierre_de_beso if str(x) != 'nan']

cierre_de_telefono = df.iloc[27].values.tolist()
cierre_de_telefono = cierre_de_telefono[5:]
cierre_de_telefono = [x for x in cierre_de_telefono if str(x) != 'nan']

romance = df.iloc[28].values.tolist()
romance = romance[5:]
romance = [x for x in romance if str(x) != 'nan']

reconsolidar = df.iloc[29].values.tolist()
reconsolidar = reconsolidar[5:]
reconsolidar = [x for x in reconsolidar if str(x) != 'nan']

invitacion_real = df.iloc[30].values.tolist()
invitacion_real = invitacion_real[5:]
invitacion_real = [x for x in invitacion_real if str(x) != 'nan']

plan_d2 = df.iloc[31].values.tolist()
plan_d2 = plan_d2[5:]
plan_d2 = [x for x in plan_d2 if str(x) != 'nan']

invitacion_final = df.iloc[32].values.tolist()
invitacion_final = invitacion_final[5:]
invitacion_final = [x for x in invitacion_final if str(x) != 'nan']

plan_final = df.iloc[33].values.tolist()
plan_final = plan_final[5:]
plan_final = [x for x in plan_final if str(x) != 'nan']

anti_rum = df.iloc[34].values.tolist()
anti_rum = anti_rum[5:]
anti_rum = [x for x in anti_rum if str(x) != 'nan']

if st.button('👹 Generar nuevas ideas para la comunicación 👹'):
    st.markdown("<hr/>", unsafe_allow_html=True)

    decorar_frases_sample = random.sample(decorar_frases, 1)
    comportamientos_habituales_sample = random.sample(comportamientos_habituales, 1)
    idis_sample = random.sample(idis, 1)
    anti_aros_psicologicos_sample = random.sample(anti_aros_psicologicos, 1)
    respuestas_y_contractores_sample = random.sample(respuestas_y_contractores, 1)
    magueadores_y_contramaqueadores_sample = random.sample(magueadores_y_contramaqueadores, 1)
    autodescualificadores_sample = random.sample(autodescualificadores, 1)
    desarmadores_sample = random.sample(desarmadores, 1)
    rutinas_anti_cuelgue_sample = random.sample(rutinas_anti_cuelgue, 1)
    rutinas_gestuales_sample = random.sample(rutinas_gestuales, 1)

    abrir_sample = random.sample(abrir, 1)
    kino_accidental_sample = random.sample(kino_accidental, 1)
    personalizar_sample = random.sample(personalizar, 1)
    falcarse_sample = random.sample(falcarse, 1)
    valor_1_sample = random.sample(valor_1, 1)
    aislar_sample = random.sample(aislar, 1)
    sexualizar_sample = random.sample(sexualizar, 1)
    valor_2_sample = random.sample(valor_2, 1)
    analizar_idis_sample = random.sample(analizar_idis, 1)
    kino_intencional_sample = random.sample(kino_intencional, 1)
    cualificar_sample = random.sample(cualificar, 1)
    cierre_de_beso_sample = random.sample(cierre_de_beso, 1)
    cierre_de_telefono_sample = random.sample(cierre_de_telefono, 1)
    romance_sample = random.sample(romance, 1)
    reconsolidar_sample = random.sample(reconsolidar, 1)
    invitacion_real_sample = random.sample(invitacion_real, 1)
    plan_d2_sample = random.sample(plan_d2, 1)
    invitacion_final_sample = random.sample(invitacion_final, 1)
    plan_final_sample = random.sample(plan_final, 1)
    anti_rum_sample = random.sample(anti_rum, 1)

    col1, col2 = st.columns(2)
    with col1:
        st.subheader('**Paso: Abrir Decorando frases**')
        st.write(abrir_sample)
        st.write(decorar_frases_sample)

        st.subheader('**Paso: Kino Accidental**')
        st.write(kino_accidental_sample)

        st.subheader('**Paso: Personalizar**')
        st.write(personalizar_sample)

        st.subheader('**Paso: Falcarse**')
        st.write(falcarse_sample)

        st.subheader('**Paso: Valor 1**')
        st.write(valor_1_sample)

        st.subheader('**Paso: Aislar**')
        st.write(aislar_sample)

        st.subheader('**Paso: Sexualizar**')
        st.write(sexualizar_sample)

        st.subheader('**Paso: Valor 2**')
        st.write(valor_2_sample)

        st.subheader('**Paso: Analizar IDIS**')
        st.write(analizar_idis_sample)

        st.subheader('**Paso: Kino Intencional**')
        st.write(kino_intencional_sample)

        st.subheader('**Paso: Cualificar**')
        st.write(cualificar_sample)

        st.subheader('**Paso: Cierre de Beso**')
        st.write(cierre_de_beso_sample)

        st.subheader('**Paso: Cierre de Teléfono**')
        st.write(cierre_de_telefono_sample)

        st.subheader('**Paso: Romance**')
        st.write(romance_sample)

        st.subheader('**Paso: Reconsolidar**')
        st.write(reconsolidar_sample)

        st.subheader('**Paso: Invitación Real**')
        st.write(invitacion_real_sample)

        st.subheader('**Paso: Plan D2**')
        st.write(plan_d2_sample)

        st.subheader('**Paso: Invitación Final**')
        st.write(invitacion_final_sample)

        st.subheader('**Paso: Plan Final**')
        st.write(plan_final_sample)

        st.subheader('**Paso: Anti Rum**')
        st.write(anti_rum_sample)


    with col2:
        st.subheader('Si es lampara o quiere que me coma su basura, la Juancha')
        st.write('Es dar frases incompletas para que la persona se enganche en algo y luego crearle historias con eso que hablo. hacerlo imaginar mucho. de la historia que está contando salen las cuerdas que usare para envidearlo. (Pero ud estaba ahi y que, y salio y se le acerco y luego..., usted estaba y sentia que, como queeeeeee).')

        st.subheader('Decorar frases')
        st.write(decorar_frases_sample)

        st.subheader('Comportamientos habituales')
        st.write(comportamientos_habituales_sample)

        st.subheader('IDIS')
        st.write(idis_sample)

        st.subheader('Anti aros psicologicos')
        st.write(anti_aros_psicologicos_sample)

        st.subheader('Respuestas y contractores')
        st.write(respuestas_y_contractores_sample)

        st.subheader('Magueadores y contramaqueadores')
        st.write(magueadores_y_contramaqueadores_sample)

        st.subheader('Autodescualificadores')
        st.write(autodescualificadores_sample)

        st.subheader('Desarmadores')
        st.write(desarmadores_sample)

        st.subheader('Rutinas anti cuelgue')
        st.write(rutinas_anti_cuelgue_sample)

        st.subheader('Rutinas gestuales')
        st.write(rutinas_gestuales_sample)


    
