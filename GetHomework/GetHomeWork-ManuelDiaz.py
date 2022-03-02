#Importaciones
from operator import truediv
from pickle import FALSE, TRUE
import webbrowser
import requests
import json
import os
#Importación de la función creada en el archivo SubirArchivosGitHub
from SubirArchivosGitHub import *

#Esta función devuelve la tarea de la semana al recibir el numero de seman como parámetro
def GetHomeWork(SemanaN,FilePath):
    
    for i in range(1,SemanaN+1):
        Enlace="https://fpmir.azurewebsites.net/{}/AZFMIR?AZFNUM={}".format("api",str(i))
        webbrowser.open(Enlace, new=2)
        response=requests.get(Enlace).text
        if response=="El Key introducido es invalido o aun no esta disponible":
            print("Para la semana ", i," no hay contenido")
            if i != 1:
                print("Se descargaron archivos hasta la semana ",i-1)
            else:
                print("No se descargo ningun archivo")
            break
        else: 
            #Comprobar y manejar la apertura del archivo de recepción
            try:
                archivo=open(FilePath + "\Semana"+str(i)+".json","w")
            except:
                print("No se pudo crear o abrir el archivo ",FilePath,"\Semana",i)
                exit()
            #Comprobar y manejar tanto la conversión del json a string como la apertura del archivo de recepción
            try:
                response_info=json.loads(response)    
                json.dump(response_info,archivo,indent=6)
            except:
                print("El script JSON no fue insertado en el archivo exitosamente por favor revise el script")
                archivo.close()
                exit()
            else: 
                print("Archivo creado y script JSON insertado exitosamente")
                archivo.close()
    if i==SemanaN:
        print("Se lograron descargar todas las semanas exitosamente")        

#Variables de entrada    
InputSemana=int(input("Ingrese semana:"))
InputFile=input("Ingrese la ruta donde requiere guardar los archivos:")
#MensajeCommit=("Ingrese mensaje de commit:")
#TokenGitHub=input("Ingrese Token:")
#NombreRepo=input("Ingrese nombre de Repo:")

#Comprobación de ruta para guardar el archivo
if (os.path.isdir(InputFile) == 0): 
    print("La ruta para guardar el archivo no existe por favor intente de nuevo colocando una ruta existente")
    exit()
#Llamada a la función GetHomeWork creada arriba
GetHomeWork(InputSemana,InputFile)

#Llama a la función creada en el archivo SubirArchivosGitHub.py
#SubirGitHub(MensajeCommit,TokenGitHub,InputFile,NombreRepo)
