import web 
import app 
import csv  
import json  

'''
    Controller Alumnos que es invocado cuando el usuario ingrese a la
    URL: http://localhost:8080/alumnos?action=get&token=1234
'''


class Alumnos:

    app_version = "0.03" 
    file = 'static/csv/alumnos.csv'  

    def __init__(self):  
        pass  

    def GET(self):
        try:
            data = web.input()  
            if data['token'] == "1234":  
                if data['action'] == 'get':  
                    result = self.actionGet(self.app_version, self.file)  
                    return json.dumps(result)  
                else:
                    result = {} 
                    result['app_version'] = self.app_version  
                    result['status'] = "Command not found"
                    return json.dumps(result)  
            else:
                result = {}  
                result['app_version'] = self.app_version 
                result['status'] = "Invalid Token"
                return json.dumps(result)  # Parsea el diccionario result a formato json
        except Exception as e:
            print("Error" + str(e.args()))
            result = {}  # crear diccionario vacio
            result['app_version'] = self.app_version  # version de la webapp
            result['status'] = "Values missing, sintaxis: alumnos?action=get&token=XXXX"
            return json.dumps(result)  # Parsea el diccionario result a formato json

    @staticmethod
    def actionGet(app_version, file):
        try:
            result = {}  
            result['app_version'] = app_version  
            result['status'] = "200 ok"  

            with open(file, 'r') as csvfile: 
                reader = csv.DictReader(csvfile)  
                alumnos = []  
                for row in reader:  
                    fila = {}  
                    fila['matricula'] = row['matricula']  
                    fila['nombre'] = row['nombre']  
                    fila['primer_apellido'] = row['primer_apellido']  
                    fila['segundo_apellido'] = row['segundo_apellido']  
                    fila['carrera'] = row['carrera']  
                    alumnos.append(fila)  
                result['alumnos'] = alumnos  
            return result  
        except Exception as e:
            result = {} 
            print("Error {}".format(e.args()))
            result['app_version'] = app_version  
            result['status'] = "Error "  
            return result  