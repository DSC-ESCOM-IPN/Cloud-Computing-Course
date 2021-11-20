import os
from time import sleep
from google.cloud import storage
from google.oauth2 import service_account

DOWNLOAD_FOLDER = './docs/'
if not os.path.exists(DOWNLOAD_FOLDER):
    os.mkdir(DOWNLOAD_FOLDER)

CREDENTIALS = service_account.Credentials.from_service_account_file(
    './credentials.json')

CLIENT = storage.Client(
    credentials=CREDENTIALS, project=os.environ.get('GCP_PROJECT'))

BUCKET_NAME = os.environ.get('GCP_BUCKET_NAME')
BUCKET = CLIENT.get_bucket(BUCKET_NAME)


def clear():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')


def list_blobls():
    print('Objects in bucket:')
    for index, blob in enumerate(list(BUCKET.list_blobs())):
        print(f'{index} - {blob.name}')


def upload_blob():
    path = input('Enter blob path: ')
    filename = path.split('/')[-1]
    blob = BUCKET.blob(filename)
    blob.upload_from_filename(path)
    print(f'Uploaded to {blob.public_url}')


def download_blob():
    source_blob_name = input('Enter source blob name: ')
    destination_file_name = DOWNLOAD_FOLDER + source_blob_name
    blob = BUCKET.blob(source_blob_name)
    blob.download_to_filename(destination_file_name)
    print(
        f'Downloaded storage object {source_blob_name} to local file {destination_file_name}')


def delete_blob():
    blob_name = input('Enter blob name: ')
    blob = BUCKET.blob(blob_name)
    if not storage.Blob(blob_name, BUCKET).exists(CLIENT):
        print(f'{blob_name} is not in {BUCKET_NAME}')
        return
    blob.delete()
    print(f'Blob {blob_name} deleted.')


if __name__ == '__main__':
    try:
        while True:
            input('Press any key to continue...')
            clear()
            print('1 - List blobs')
            print('2 - Upload blob')
            print('3 - Download blob')
            print('4 - Delete blob')
            print('0 - Exit')
            opt = int(input('Enter an option: '))
            print('\n')
            if opt == 0:
                break
            if opt == 1:
                list_blobls()
            elif opt == 2:
                upload_blob()
            elif opt == 3:
                download_blob()
            elif opt == 4:
                delete_blob()
    except Exception as e:
        print(e)
        print('\nBye')
        sleep(1)
        clear()
