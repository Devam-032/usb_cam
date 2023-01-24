#!/usr/bin/env python3
# from __future__ import print_function
# import cv2
# import os
# import numpy as np
# import array as arr

# videomainfolder = 'videos'
# myFolders = os.listdir(videomainfolder)
# print(myFolders)
# num = 1

# if not os.path.exists('Images'):
#     os.makedirs('Images')

# if not os.path.exists('videos'):
#     os.makedirs('Images')

# for folder in myFolders:
#     os.makedirs(str(num)
#     Imagemainfolder = 'Images'
#     videopath = mainfolder +'/'+folder #path = video/1

#     print(videopath)
#     myList = os.listdir(videopath)
#     print(f"total no of video detected {len(myList)}")
#     for vidN in myList:
#         #videopath = videopath+'/'+vidN
#         vidcap = cv2.VideoCapture(videopath)
#         def getFrame(sec):
#             vidcap.set(cv2.CAP_PROP_POS_MSEC,sec*1000)
#             hasFrames,image = vidcap.read()
#             if hasFrames:
#                 imagepath = Imagemainfolder+"/"+str(num)
#                 cv2.imwrite(os.path.join(imagepath ,"image"+str(count)+".jpg"), image)    # save frame as JPG file
#             return hasFrames
#         sec = 0
#         frameRate = 1 #//it will capture image in each 0.5 second
#         count=1
#         success = getFrame(sec)
        
#         while success:
#             count = count + 1
#             sec = sec + frameRate
#             sec = round(sec, 2)
#             success = getFrame(sec) 
                  
#     num=num+1

# mainfolder = 'Images'
# myFolders = os.listdir(mainfolder)
# print(myFolders)

# for folder in myFolders:
#     path = mainfolder +'/'+folder
#     print(path)
#     images=[]
#     myList = os.listdir(path)
#     print(f"total no of image detected {len(myList)}")
#     for imgN in myList:
#         dim=(1024,768)
#         imagepath = path+'/'+imgN
#         print(imagepath)
#         image = cv2.imread(imagepath,cv2.IMREAD_COLOR)
#         image = cv2.resize(image,dim,interpolation=cv2.INTER_AREA)
#         images.append(image)


#     stitcher = cv2.Stitcher.create()
#     ret,pano = stitcher.stitch(images)
#     print(pano.shape[0])
#     print(pano.shape[1])
#     #height = img.shape[0]
#     #width = img.shape[1]
#     pano = cv2.resize(pano,(2100,700),interpolation=cv2.INTER_AREA)
#     pano = pano[100:pano.shape[0]-100,300:pano.shape[1]-300]
    

#     for alpha in np.arange(0.5,1,0.1)[::-1]:
#         overlay = pano.copy()
#         output1 = pano.copy()

#         cv2.rectangle(overlay,(433,464),(937,526),(191,165,143),-1)
#         #cv2.putText(overlay,"hello".format(alpha),(10,30),cv2.FONT_HERSHEY_SIMPLEX,1.0,(58,79,122),3)

#         cv2.addWeighted(overlay,alpha,output1,1-alpha,0,output1)
#         #print("alpha={},beta={}".format(alpha,1-alpha))

#     for alpha in np.arange(0.8,1,0.1)[::-1]:
#         overlay = output1.copy()
#         outputFinal = output1.copy()

#         cv2.putText(overlay,"Hello".format(alpha),(10,30),cv2.FONT_HERSHEY_SIMPLEX,1.0,(71,38,10),3)

#         cv2.addWeighted(overlay,alpha,outputFinal,1-alpha,0,outputFinal)
#         #print("alpha={},beta={}".format(alpha,1-alpha))


#         if ret==cv2.STITCHER_OK:
#             print("panorama generated")
#             cv2.imshow(folder,outputFinal)
#             cv2.waitKey(10)
#         else:
#             print("Error during Stitching")

# cv2.waitKey(0)

from __future__ import print_function
import cv2
import os
import numpy as np
import array as arr

mainfolder = 'videos'
myFolders = os.listdir(mainfolder)
print(myFolders)
num = 1

for folder in myFolders:
    Imagemainfolder = 'Images'
    videopath = mainfolder +'/'+folder #path = video/1

    print(videopath)
    myList = os.listdir(videopath)
    print(f"total no of video detected {len(myList)}")
    for vidN in myList:
        videopath = videopath+'/'+vidN
        vidcap = cv2.VideoCapture(videopath)
        def getFrame(sec):
            vidcap.set(cv2.CAP_PROP_POS_MSEC,sec*1000)
            hasFrames,image = vidcap.read()
            if hasFrames:
                imagepath = Imagemainfolder+"/"+str(num)
                cv2.imwrite(os.path.join(imagepath ,"image"+str(count)+".jpg"), image)    # save frame as JPG file
            return hasFrames
        sec = 0
        frameRate = 1 #//it will capture image in each 0.5 second
        count=1
        success = getFrame(sec)
        
        while success:
            count = count + 1
            sec = sec + frameRate
            sec = round(sec, 2)
            success = getFrame(sec) 
                  
    num=num+1

mainfolder = 'Images'
myFolders = os.listdir(mainfolder)
print(myFolders)

for folder in myFolders:
    path = mainfolder +'/'+folder
    print(path)
    images=[]
    myList = os.listdir(path)
    print(f"total no of image detected {len(myList)}")
    for imgN in myList:
        dim=(1024,768)
        imagepath = path+'/'+imgN
        print(imagepath)
        image = cv2.imread(imagepath,cv2.IMREAD_COLOR)
        image = cv2.resize(image,dim,interpolation=cv2.INTER_AREA)
        images.append(image)


    stitcher = cv2.Stitcher.create()
    ret,pano = stitcher.stitch(images)
    print(pano.shape[0])
    print(pano.shape[1])
    #height = img.shape[0]
    #width = img.shape[1]
    pano = cv2.resize(pano,(2100,700),interpolation=cv2.INTER_AREA)
    pano = pano[100:pano.shape[0]-100,300:pano.shape[1]-300]
    

    for alpha in np.arange(0.5,1,0.1)[::-1]:
        overlay = pano.copy()
        output1 = pano.copy()

        cv2.rectangle(overlay,(433,464),(937,526),(191,165,143),-1)
        #cv2.putText(overlay,"hello".format(alpha),(10,30),cv2.FONT_HERSHEY_SIMPLEX,1.0,(58,79,122),3)

        cv2.addWeighted(overlay,alpha,output1,1-alpha,0,output1)
        #print("alpha={},beta={}".format(alpha,1-alpha))

    for alpha in np.arange(0.8,1,0.1)[::-1]:
        overlay = output1.copy()
        outputFinal = output1.copy()

        cv2.putText(overlay,"Hello".format(alpha),(10,30),cv2.FONT_HERSHEY_SIMPLEX,1.0,(71,38,10),3)

        cv2.addWeighted(overlay,alpha,outputFinal,1-alpha,0,outputFinal)
        #print("alpha={},beta={}".format(alpha,1-alpha))


        if ret==cv2.STITCHER_OK:
            print("panorama generated")
            cv2.imshow(folder,outputFinal)
            cv2.waitKey(10)
        else:
            print("Error during Stitching")

cv2.waitKey(0)



        

        
