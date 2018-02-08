import pygame
import pygame.camera
import os
import os.path

def DeleteExistingPicture(text_file, folder):
    ##folder = '/home/pi/webcam'
    for the_file in os.listdir(folder):
        file_path = os.path.join(folder, the_file)
        try:
            if os.path.isfile(file_path):
                os.unlink(file_path)
                text_file.write("delete files :" +file_path +"\n")
        except Exception as e:
            text_file.write(str(e)+"\n")
return

def GetPhoto(text_file, folder, mydate):
        ##folder = '/home/pi/webcam'
    os.environ['PYGAME_CAMERA'] = 'opencv'
    pygame.init()
    pygame.camera.init()
    cam=pygame.camera.Camera("/dev/video0",(1280, 1050)) 
    try:
        cam.start()
        text_file.write("started cam"+"\n")
        image = cam.get_image()    
    except SystemError as e:
        text_file.write( "Exception: "+str(e) +"\n")
        if (str(e)=="ioctl(VIDIOC_S_FMT) failure: no supported formats"):
            try:
                text_file.write("try to reboot \n")
                text_file.Close()
                os.system('reboot')
            except:
                text_file=open("output.txt", "a")
                text_file.write("Failed to reboot \n")
        else:    
            time.sleep(20)
            text_file.write("Thread sleep 20 sec"+"\n")
            cam.start()
            text_file.write("REstarted cam"+"\n")
            image = cam.get_image()
    except:
        text_file.write( "UNHANDLED Exception during cam.start(): "+str(e) +"\n")
        
    try:
        cam.stop()
        text_file.write( "stopped cam1"+"\n")
    except SystemError as e:
        text_file.write( "Exception during cam.stop(): "+str(e) +"\n")
        time.sleep(20)
        cam.stop()
        text_file.write( "thread.sleep(20) and REstopped cam1"+"\n")
    except:
        text_file.write( "UNHANDLED Exception during cam.stop(): "+str(e) +"\n")

    mypath=folder+'/'+mydate+'.jpg'
    pygame.image.save(image,mypath)
    text_file.write( "saved file at:"+mypath +"\n")
return