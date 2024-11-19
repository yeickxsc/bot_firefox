import gspread
from oauth2client.service_account import ServiceAccountCredentials
import csv
class GoogleSheet:
    def __init__(self, key_file_path, spreadsheet_id, ):
        # Definir el alcance de la API de Google Sheets y Drive
        self.scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
        
        # Obtener las credenciales de la cuenta de servicio usando el archivo JSON de claves
        self.creds = ServiceAccountCredentials.from_json_keyfile_name(key_file_path, self.scope)
        
        # Autorizar el cliente de Google Sheets con las credenciales obtenidas
        self.client = gspread.authorize(self.creds)
        
        # ID de la hoja de cálculo de Google Sheets
        self.spreadsheet_id = spreadsheet_id
        
        

    def read_file_sheet(self):
        # Abrir la hoja de cálculo de Google Sheets usando su ID
        spreadsheet = self.client.open_by_key(self.spreadsheet_id)
        
        # Obtener todas las hojas de trabajo en la hoja de cálculo
        sheets = spreadsheet.worksheets()
        
        # Iterar sobre cada hoja de trabajo
        for sheet in sheets:
            print(sheet)
            if sheet.title !='R X sincronizar':
                # Seleccionar la hoja de trabajo actual por su título
                worksheet = spreadsheet.worksheet(sheet.title)
                
                # Leer todos los datos de la hoja de trabajo
                values = worksheet.get('A:AB')
        print(values)
        for i in values[1:]:
            print(i)

    def inserta_tickets(self,valores):
        # Abrir la hoja de cálculo de Google Sheets usando su ID
        spreadsheet = self.client.open_by_key(self.spreadsheet_id)
         # Seleccionar la hoja donde quieres insertar los datos (por ejemplo, la primera hoja)
        worksheet = spreadsheet.sheet1
        for i in valores:
            worksheet.append_row(i)  # Agregar una fila con los datos
            
                
l_valores = [['SPP_DLO_4', 'angel.arellanes@solistica.com', 'Mejora RA21'],
['SPP_DLO_5', 'laura.fuentes@solistica.com', 'Mejora RA22'],
['SPP_DLO_6', 'daniela.soto@solistica.com', 'Mejora RA23']]
# Uso de la clase
if __name__ == "__main__":
    key_file_path = 'D:/documentos/trabajo/python/both/bot_firefox/key-bot-soporte-portal.json'  # Ruta al archivo JSON
    spreadsheet_id = '1ab8KckU5aCW9s0ckExR5kko8wYZJDRhhBY12EpEadJc'      # ID de la hoja de cálculo

    # Crear una instancia de GoogleSheet
    google_sheet = GoogleSheet(key_file_path, spreadsheet_id)
    
    # Leer los datos de las hojas
    google_sheet.read_file_sheet()

    #google_sheet.inserta_tickets(l_valores)

