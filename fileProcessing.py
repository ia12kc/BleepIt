'''
Created on Mar 11, 2017

@author: abe
'''
#to test module simply processFile(filename)
def processFile(filename):
    #filename output 
    file=filename.lower()
    acceptableFile=False
    listOfFormats=[]
    listOfPossibleFormats=['.m4a','.mp4','.3gp','.m4b','.m4p','.m4r','.m4v','.caf',\
                           '.mp3','.ogg','.opus','.webm','.mka','.flac',\
                           '.ape','.tta','.mpc','.mp+','.mpp','.ra','.ram',\
                           '.spx','.oga','.wma']
    listOfFormats.append('.wav')
    
    for i in range(listOfFormats.count()):
            if file.endwith(listOfFormats[i]):
                acceptableFile=True
    
    def addFormat(f):
        
        for i in range(listOfFormats.count()):
            if f==listOfFormats[i]:
                print "error"
                #return Error message
                #Format already in list
                
        for i in range(listOfPossibleFormats.count()):
            if f==listOfPossibleFormats[i]:
                listOfFormats.append(f)
            
    return acceptableFile
        
