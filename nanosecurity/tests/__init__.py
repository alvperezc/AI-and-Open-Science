import requests
import os

def _test_server_connection():
        """Test if the server is up and running."""
        grobid_url = "http://localhost:8070/api/isalive"
        try:
            r = requests.get(grobid_url)
        except:
            print("GROBID server does not appear up and running, the connection to the server failed")
            raise ServerUnavailableException

        status = r.status_code

        if status != 200:
            print("GROBID server does not appear up and running " + str(status))
        else:
            print("GROBID server is up and running")

def _test_exist_dir():
    if os.path.exists('../resources'):
        print("The directory is created")
    else:
        print("You have to create a directory named: AI-and-Open-Science/nanosecurity/resources")

def _test_empty_and_pdf():
    if len(os.listdir('../resources') ) == 0:
        print("Directory is empty. You have too add some PDFs to process")
    else:    
        carpeta = '../resources'
        archivos = os.listdir(carpeta)
        archivos_pdf = [archivo for archivo in archivos if archivo.endswith('.pdf')]
        archivos_no_pdf = []
        for archivo in archivos:
            if not archivo.endswith('.pdf'):
                archivos_no_pdf.append(archivo)

        if len(archivos_pdf) == len(archivos):
            print('Todos los archivos son PDF.')
        else:
            print('Hay archivos que no son PDF:', archivos_no_pdf)

###########################################################################################################################3
_test_server_connection()
_test_exist_dir()
_test_empty()