import gspread
from oauth2client.service_account import ServiceAccountCredentials

class gss:
    def __init__(self, credentials, sheet_id):
        self.credentials = credentials
        self.sheet_id = sheet_id
        self.client = self.client

        
        # creating client
        def client(self):
            scope = ['', '']
            credentials = ServiceAccountCredentials.from_json_keyfile_name(self.credentials, scope)
            return gspread.authorize(credentials)