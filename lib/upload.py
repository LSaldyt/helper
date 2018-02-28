from .google import get_service
from apiclient.http import MediaFileUpload
import os.path

def upload(filepath, mimetype='image/jpeg'):
    service = get_service('drive')
    file_metadata = {'name': os.path.basename(filepath)}
    media = MediaFileUpload(filepath,
                        mimetype=mimetype)
    #results = service.files().list(
    #    pageSize=10,fields="nextPageToken, files(id, name)").execute()
    #items = results.get('files', [])
    #if not items:
    #    print('No files found.')
    #else:
    #    print('Files:')
    #    for item in items:
    #        print('{0} ({1})'.format(item['name'], item['id']))

    file = service.files().create(body=file_metadata,
        				media_body=media,
        				fields='id').execute()
    print('File ID: %s' % file.get('id'))
