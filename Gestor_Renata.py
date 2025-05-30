import streamlit as st 
import pandas as pd 
import plotly_express as px 
#import matplotlib.pyplot as plt

st.set_page_config(layout="wide")

#color = st.color_picker("Pick A Color", "#00f900")
#st.write("The current color is", color)

df = pd.read_csv("Gestor_Renata.csv", sep=",")


df=df.sort_values("Nome")

df["Colab"] = df["Nome"]
df["Compet"] = df["Competencia"]
df["Setor"] = df["Nível de Avaliação"]
df["Setorial"] = df["Nível de Avaliação"]
df["Comenta"] = df["Comentário"]
df["Avaliar"] = df["Avaliador"]


st.write("""
# Cerejeiras - Análise de Competências
""" )
aval = ["Autoavaliação","Gestor","Pares","Liderados"]

st.sidebar.write("""
## Renata Souza de Paula
""" )

Nome = st.sidebar.selectbox("Avaliados",df["Colab"].unique())

df_filtered = df[df["Colab"] == Nome]
#df_filtered

df_Média = df_filtered.groupby("Compet")[["Autoavaliação","Gestor","Pares","Liderados"]].mean().round(decimals=1).reset_index()
#df_Média

aval = ["Autoavaliação","Gestor","Pares","Liderados"]
#----------------------------------------------------------------------

#Avaliado = str(Nome)
st.write("""
## Competências
""" ), Nome

fig_comp = px.bar(df_Média, y=aval, x="Compet", barmode='group', color_discrete_map = {"Autoavaliação":"#281BD2", "Gestor":"#764D29","Pares":"#EDEC7C", "Liderados":"#F0A652"})
fig_comp.update_layout(xaxis_title="Competências", yaxis_title="Médias")

fig_comp

#df_filtered

#-------------------------------------------------------------------------------------------

st.write("""
## Análise das Perguntas
""" ), Nome

aval1 = ["Liderados","Pares", "Gestor", "Autoavaliação"]

#df["CompetUniqx"] = df_filtered["Competencia"]
#df["CompetUniqx"]
df_CompetUniq = df_filtered["Competencia"].dropna().reset_index(drop = True)

unica_Competencia = st.selectbox("Escolha a Competência",df_CompetUniq.unique(),index=1)

df_filtered2 = df_filtered[df["Compet"] == unica_Competencia]

fig_Perg = px.bar(df_filtered2, y="Pergunta", x=aval1, orientation="h", barmode='group', color_discrete_map = {"Autoavaliação":"#281BD2", "Gestor":"#764D29","Pares":"#EDEC7C", "Liderados":"#F0A652"})
fig_Perg.update_layout(xaxis_title="Médias", yaxis_title="Perguntas")
fig_Perg

coment = st.checkbox("Comentários")
df_filteredy = df[df["Comenta"] == "Sim"]
#df_filteredy

if coment:

    col1, col2 = st.columns([1, 3])

    with col1:
        df_filtered3 = df_filteredy[df["Nome"] == Nome]
       # df_filtered3
        Coment = st.selectbox("Comentário de :",df_filtered3["Avaliador"].unique())
    
    with col2:
        df_filteredz = df_filtered3[df["Avaliador"] == Coment]
        df_coment = df_filteredz.iloc[:,7]
        df_coment
        


#-----------------------------------------------------------------------------------------
st.write("""
## Desempenho Geral por Competência
""" )

Compet_Desemp = st.selectbox("Defina a Competência",df["Compet"].dropna().unique(),index=1)

aval1 = ["Autoavaliação","Gestor","Pares","Liderados"]

df_filtered5 = df[df["Compet"] == Compet_Desemp]

df_MédiaGeral = df_filtered5.groupby("Nome")[["Autoavaliação","Gestor","Pares","Liderados"]].mean().round(decimals=1).reset_index()
#df_MédiaGeral

fig_DesenvGeral = px.bar(df_MédiaGeral, y=aval1, x="Nome", barmode='group',color_discrete_map = {"Autoavaliação":"#281BD2", "Gestor":"#764D29","Pares":"#EDEC7C", "Liderados":"#F0A652"})
fig_DesenvGeral.update_layout(xaxis_title="Colaboradores do Setor", yaxis_title="Médias")
fig_DesenvGeral

#---------------------------------------------------------------------------------

st.write("""
## Desempenho Geral dos Avaliados
""" )

AvalEquipe = st.checkbox("Exibir avaliação da Equipe")

if AvalEquipe:
   

    #df_filtered3 = df[df["Competencia"] == Compet_Desemp]
    #df_filtered3

    #df_MédiaSetor = df_filtered5.groupby("Setor")[["Auto Avaliação","Avaliador"]].mean().reset_index()
    #df_MédiaSetor

    #fig_Setor = px.bar(df_MédiaSetor, y=aval, x="Setor", barmode='group', color_discrete_map = {"Auto Avaliação":"Brown", "Avaliador":"Yellow"})
    #fig_Setor.update_layout(xaxis_title="Setores", yaxis_title="Médias")
    #fig_Setor



    df_filtered7 = df
    #df_filtered3

    #df_MédiaSetor = df_filtered7.groupby("Nome")[["Autoavaliação","Gestor","Pares","Liderados"]].mean().round(decimals=1).reset_index()
    df_MédiaSetor = df_filtered7.groupby("Nome")[["Liderados","Pares","Gestor","Autoavaliação"]].mean().round(decimals=1).reset_index()
    #df_MédiaSetor

    #fig_Setor = px.bar(df_MédiaSetor, x=aval, y="Nome", orientation="h", barmode='group', color_discrete_map = {"Autoavaliação":"Blue", "Gestor":"#00F900","Pares":"#F9AF00", "Liderados":"#F900D2"})
    
    fig_Setor = px.bar(df_MédiaSetor, x=aval, y="Nome", orientation="h", barmode='group', color_discrete_map = {"Autoavaliação":"#281BD2", "Gestor":"#764D29","Pares":"#EDEC7C", "Liderados":"#F0A652"})
    fig_Setor.update_layout(xaxis_title="Média", yaxis_title="Colaborador")
    fig_Setor

#---------------------------------------------
    
