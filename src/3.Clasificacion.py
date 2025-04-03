import pandas
import os
import cv2
import tensorflow as tf
import numpy

ruta=r'/home/jovyan/Clasificacion_tableros/Data/Fotos'
fotos_pred=None
for i in range(5):
    pre_fotos=pandas.DataFrame(os.listdir(rf'{ruta}/Tipo {i+1}'),columns=['Foto'])
    pre_fotos['Tipo']=i+1
    pre_fotos['Ruta']=rf'{ruta}/Tipo {i+1}'
    fotos_pred=pandas.concat([fotos_pred,pre_fotos])
fotos_pred.reset_index(drop=True,inplace=True)
fotos_pred=pandas.get_dummies(fotos_pred,columns=['Tipo'],dtype=int)
print(fotos_pred)

size=500
images_pred=[]
image_size=(size,size)
for i in range(len(fotos_pred)):
    foto=fotos_pred['Foto'][i]
    ruta=fotos_pred['Ruta'][i]
    # print(rf'{ruta}\{foto}')
    foto=cv2.imread(rf'{ruta}/{foto}')
    foto=cv2.resize(foto,image_size)
    # cv2.imshow('foto',foto)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()
    foto=numpy.array(foto)/255
    images_pred.append(foto)

tipo=fotos_pred[['Tipo_1','Tipo_2','Tipo_3','Tipo_4','Tipo_5']]
X=numpy.array(images_pred)
Y=numpy.array(tipo)
print(f'Forma de X: {X.shape}')
print(f'Forma de Y: {Y.shape}')

model = tf.keras.models.load_model('model.h5')

Y_predic=pandas.DataFrame(model.predict(X),
                          columns=['Tipo_1_pred','Tipo_2_pred','Tipo_3_pred','Tipo_4_pred','Tipo_5_pred'])
for i in Y_predic.columns:
    Y_predic[i.replace('_pred','_prob')]=Y_predic[i].apply(lambda x:round(x,4))
    Y_predic[i]=Y_predic[i].apply(lambda x:round(x,0))
    # Y_predic.rename(columns={i:i.replace('_','__')},inplace=True)
print(Y_predic)

Y_predic.to_excel('Comparativo de clasificacion.xlsx',index=False)

