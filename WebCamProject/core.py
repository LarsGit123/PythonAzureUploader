# -*- coding: utf-8 -*-
from WebCamProject import BlobStorageInteraction
from WebCamProject import GetPictureUsingPyGame


if os.path.isfile("output.txt"):    
    statinfo= os.stat('output.txt')
    print ("logfile size (bytes): "+str(statinfo.st_size))
    if statinfo.st_size <=1048576:                  
        text_file=open("output.txt", "a")
    else:
        text_file=open("output.txt", "w")
else:
    text_file=open("output.txt", "w")
print( "open output.txt file")


mydate=datetime.now().strftime('%Y-%m-%d %H:%M:%S')
text_file.write(mydate)

blobservice= BlobStorageInteraction.VerifyAndGetBlobs(text_file, mydate)
GetPictureUsingPyGame.DeleteExistingPicture(text_file, '/home/pi/webcam')
GetPictureUsingPyGame.GetPhoto(text_file, '/home/pi/webcam', mydate)
BlobStorageInteraction.CreateNewBlob(text_file, blobservice, mydate)

print( "file close, successfully created and uploaded webcam"+mydate + "\n \n")
text_file.close()