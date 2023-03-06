import unittest
import requests
import os

class TestServerConnection(unittest.TestCase):
    def test_server_connection(self):
        """Test if the server is up and running."""
        # En caso de estar corriendolo en local sustituir grobid por localhost
        grobid_url = "http://grobid:8070/api/isalive"
        try:
            r = requests.get(grobid_url)
        except:
            self.fail("GROBID server does not appear up and running, the connection to the server failed")

        status = r.status_code

        if status != 200:
            self.fail("GROBID server does not appear up and running " + str(status))
        else:
            print("GROBID server is up and running")

class TestExistDir(unittest.TestCase):
    def test_exist_dir(self):
        if os.path.exists('../resources'):
            print("The directory is created")
        else:
            self.fail("You have to create a directory named: AI-and-Open-Science/nanosecurity/resources")

class TestEmptyAndPDF(unittest.TestCase):
    def test_empty_and_pdf(self):
        if len(os.listdir('../resources') ) == 0:
            self.fail("Directory is empty. You have too add some PDFs to process")
        else:    
            carpeta = '../resources'
            archivos = os.listdir(carpeta)
            archivos_pdf = [archivo for archivo in archivos if archivo.endswith('.pdf')]
            archivos_no_pdf = []
            for archivo in archivos:
                if not os.path.exists("../resources/figures"):
                    if not archivo.endswith('.pdf') :
                        self.fail("Error processing the file: ", archivo)
                        archivos_no_pdf.append(archivo)
                else:
                    print(f'PDF file: {archivo} correct.')
            
if __name__ == '__main__':
    unittest.main()