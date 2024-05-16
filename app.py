import pandas as pd
import numpy as np
import plotly.express as px

df = pd.read_csv('censoevolutivomovimentorendimento2016-2021.csv', nrows=5356,sep=';',encoding='latin1')

#df.info() #Fornece um resumo conciso do DataFrame, incluindo informações sobre o índice, o tipo de dado de cada coluna
#print(df.head(200))# Explora os primerios registros do DataFrame 
#print(df.tail())# Explora os ultimos registros do DataFrame 
# Realizar a análise estatística descritiva

 
#descricao_estatistica = df.describe(include=[np.number])
#print(descricao_estatistica)

dispersao_ano = px.scatter(df, x='ZONA',y='ANO',title='Ano por Zona')
dispersao_ano.show()

#TOTAL DE APROVADOS NO ENSINO FUNDAMENTAL
dispersao_totalEF_aprov = px.scatter(df, x='ZONA', y='TOTALEF_APROV',color='ANO',title =' Total de aprovados do ensino fundamental  (cor: Ano)')
dispersao_totalEF_aprov.show()

#TOTAL DE REPROVADOS NO ENSINO FUNDAMENTAL
dispersao_totalEF_reprov = px.scatter(df, x='ZONA', y='TOTALEF_REPROV',color='ANO',title =' Total de Reprovados do ensino fundamental  (cor: Ano)')
dispersao_totalEF_reprov.show()

#TOTAL DE CONCLUINTES NO ENSINO FUNDAMENTAL
dispersao_concluintesEF =  px.scatter(df, x='ZONA', y='CONCLUINTES_EF',color='ANO',title =' Concluintes do Ensino Fundamental por Zona (cor: Ano)')
dispersao_concluintesEF.show()

#TOTAL DE ABANDONO ENSINO FUNDAMENTAL
dispersao_abandonoEF = px.scatter(df, x='ZONA', y='TOTALEF_ABAND',color='ANO' ,title=' Total de Alunos em abandono por Zona (cor: Ano)')
dispersao_abandonoEF.show()

#----------------------------------------------------------------------------------------

#TOTAL DE APROVADOS NO ENSINO MEDIO

dispersao_totalEM_aprov = px.scatter(df, x='ZONA', y='TOTAL_EM_APROV',color='ANO',title =' Total de aprovados do ensino Medio  (cor: Ano)')
dispersao_totalEM_aprov.show()

#TOTAL DE REPROVADOS NO ENSINO MEDIO
dispersao_totalEM_reprov = px.scatter(df, x='ZONA', y='TOTAL_EM_REPROV',color='ANO',title =' Total de Reprovados do ensino Medio  (cor: Ano)')
dispersao_totalEM_reprov.show()

#TOTAL DE CONCLUINTES NO ENSINO MEDIO
dispersao_concluintesEM =  px.scatter(df, x='ZONA', y='CONCLUINTES_EM',color='ANO',title =' Concluintes do Ensino Medio (cor: Ano)')
dispersao_concluintesEM.show()

#TOTAL DE ABANDONO ENSINO MEDIO
dispersao_abandonoEM = px.scatter(df, x='ZONA', y='TOTAL_EM_ABAND',color='ANO' ,title=' Total de Alunos em abandono por Zona no ensino Medio (cor: Ano)')
dispersao_abandonoEM.show()

#-------------------------------------------------------------------------------------------------------

#TOTAL DE ALUNOS APROVADOS NAS ESCOLAS PARTICULARES
dispesao_aprovescPAR=px.scatter(df, x='ZONA', y='EJAIITOTAL',color='ANO' ,title=' Total de Alunos aprovados por Zona em escolas Particulares (cor: Ano)')
dispesao_aprovescPAR.show()
#EPAPROV

#TOTAL DE ALUNOS REPROVADOS NAS ESCOLAS PARTICULARES
dispesao_reprovescPAR=px.scatter(df, x='ZONA', y='EJAITOTAL',color='ANO' ,title=' Total de Alunos reprovados por Zona em escolas Particulares (cor: Ano)')
dispesao_reprovescPAR.show()
#EPREPROV

#TOTAL DE ALUNOS QUE ABANDONARAM AS ESCOLAS PARTICULARES
dispesao_abandonoescPAR=px.scatter(df, x='ZONA', y='EPABAND',color='ANO' ,title=' Total de Alunos em abandono por Zona em escolas Particulares (cor: Ano)')
dispesao_abandonoescPAR.show()


#----------------------------------------------------------------------------------------------------------------------

dispesao_EJATOTAL=px.scatter(df, x='ZONA', y='EJATOTAL',color='ANO' , aspect=1, ci=None,title=' Total de Alunos no EJA(EDUCAÇÃO DE JOVENS E ADULTOS) por Zona em escolas (cor: Ano)')
dispesao_EJATOTAL.show()

histograma = px.histogram(df, x='EJAITOTAL',y='EJAIITOTAL',color='ANO')
histograma.show()