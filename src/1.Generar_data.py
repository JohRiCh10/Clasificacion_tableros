import pandas
import os

#Leer las fotos almacenadas en las carpetas
ruta=r'/home/jovyan/Clasificacion_tableros/Data/Fotos'
fotos=None
for i in range(5):
    pre_fotos=pandas.DataFrame(os.listdir(rf'{ruta}/Tipo {i+1}')[0:50],columns=['Foto'])
    pre_fotos['Tipo']=i+1
    pre_fotos['Ruta']=rf'{ruta}/Tipo {i+1}'
    fotos=pandas.concat([fotos,pre_fotos])
fotos.reset_index(drop=True,inplace=True)
fotos=pandas.get_dummies(fotos,columns=['Tipo'],dtype=int)
fotos.to_excel('data.xlsx',index=False)