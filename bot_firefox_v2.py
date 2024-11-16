from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.firefox.options import Options
import time
from conexion_google_sheet import GoogleSheet

key_file_path = 'C:/Users/Condor/AppData/Local/Programs/Python/Python313/VENV/prueba/codigos/key-bot-soporte-portal.json'
spreadsheet_id = '1ab8KckU5aCW9s0ckExR5kko8wYZJDRhhBY12EpEadJc'

api = GoogleSheet(key_file_path,spreadsheet_id)

driver = None
profile_path = 'C:/Users/Condor/AppData/Roaming/Mozilla/Firefox/Profiles/wccts2il.perfil_bot'
#business_units = ['SPP_DLO','SPP_PLO','SPP_RTL', 'SPP_MKT']
business_units = ['DLO','PLO','RTL', 'MKT']
mail_subject = ''
mail_sender = ''

#Función para obtener el último registro de la lista que se obtenga
def get_last_row_id(data):
    last_row_id = int(data[-1][0].split('_')[-1])
    return last_row_id

try:

    options = Options()
    options.binary_location = 'C:/Program Files/Mozilla Firefox/firefox.exe'

    # Configura el perfil en Options mediante argumentos específicos
    options.add_argument(f"-profile {profile_path}")

    service = FirefoxService(executable_path='C:/Users/Condor/AppData/Local/Programs/Python/Python313/VENV/prueba/drivers/geckodriver.exe')
    driver = webdriver.Firefox(service=service, options=options)
   
    driver.get('https://mail.zoho.com/zm/#mail/folder/inbox')
    time.sleep(10)

    elements = driver.find_elements(By.CLASS_NAME,'zmList')
    
    rows_to_insert = []

    for bu in business_units:
        for element in elements:
            data = element.get_attribute("aria-label").upper()
            if f'SPP_{bu}' in data:

                #Traer información para la bu en turno
                rows_in_sheet = api.read_file_sheet(bu)

                #Obtener el último registro
                last_row_id = get_last_row_id(rows_in_sheet)
                
                meta_data = [d.strip() for d in data.split(',')]
                mail_sender = meta_data[0].split('FROM')[-1].strip()
                mail_subject = meta_data[2].split('SUBJECT')[-1].strip()

                #Verificar que no exista un registro con asunto igual:
                exists_subject = any(mail_subject in sublist for sublist in rows_in_sheet)

                if not exists_subject:
                    last_row_id = last_row_id+1
                    next_row_id = bu+'_'+str(last_row_id)
                    pre_row = [next_row_id, mail_sender, mail_subject]
                    rows_to_insert.append(pre_row)

        api.inserta_tickets(rows_to_insert, bu)

except Exception as e:
    print(f'Ocurrió un error: {e}')
finally:
    if driver:
        driver.quit()
