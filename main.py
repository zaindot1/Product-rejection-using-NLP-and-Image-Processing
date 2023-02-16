from urllib.error import ContentTooShortError

import mysql.connector
import shutil
import urllib.request

hostname = 'localhost'
username = 'root'
password = ''
database = 'fsa_staging'
myConnection = mysql.connector.connect( host=hostname, user=username, passwd=password, db=database )
urls=[]
base_url='https://sgp1.digitaloceanspaces.com/f-images/image/f-images/'
def doQuery( conn,order ) :
    cur = conn.cursor()
    cur.execute("SELECT image FROM oc_product_image WHERE sort_order='%i'"%(order))
    for image in cur.fetchall():
        urls.append((base_url+image[0],order))

for category in (5,3):
    doQuery( myConnection,category)
    print(urls)
myConnection.close()

def download_image(url, file_path, file_name):
    full_path = file_path + str(file_name) + '.jpg'
    try:
        urllib.request.urlretrieve(url, full_path)

    except (ContentTooShortError) as e:
        return None

file_name=1
for url in urls:
    print(url[0])
    download_image(url[0], str(url[1])+'/', file_name)
    file_name+=1

