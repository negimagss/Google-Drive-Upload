from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
import os
#Login to Google Drive and create drive object
g_login = GoogleAuth()
g_login.LocalWebserverAuth()
drive = GoogleDrive(g_login)


#test_file = drive.CreateFile({'title': 'AllCompanyNames.xlsx'})

test_file = drive.CreateFile({'parents': [{'id': '1lHrzs0Ch0fylYuUOgryznYWkx_v2mT3R'}]})
test_file.SetContentFile('AllCompanyNames.xlsx')
test_file.Upload({'convert': True})