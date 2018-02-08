from azure.storage.blob import BlockBlobService
from azure.storage.blob import ContentSettings
import os



def VerifyAndGetBlobs(text_file, mydate):
    myBlockBlobService = BlockBlobService(account_name=os.environ.get('AZURE_BLOBSTORAGE_NAME'), account_key=os.environ.get('AZURE_STORAGE_KEY'))
    text_file.write("Got BlockBlobService at time:" +mydate +"\n");

    mylist=myBlockBlobService.list_blobs('blobcontainer')
    text_file.write( "found blobs:"+"\n")
    for blob in mylist.items: text_file.write( blob.name +"\n")

    newlist= []
    for blob in mylist.items:
        if 'webcam' in blob.name:
            newlist.append(blob)

    while len(newlist)>10:
        text_file.write("deleting blob "+ newlist[0].name +"\n")
        myBlockBlobService.delete_blob('blobcontainer', newlist[0].name)
        newlist.remove(newlist[0])
return myBlockBlobService

def CreateNewBlob(text_file, myBlockBlobService, mydate):
    myBlockBlobService.create_blob_from_path('blobcontainer', 'webcam_'+mydate, '/home/pi/webcam/'+mydate+'.jpg', content_settings = ContentSettings(content_type='image/jpg'))
    text_file.write( "created blob named webcam"+mydate +"\n")
return