from string import join

fileHandle = open( 'errorOfClassification.bat', 'w' )

for xi in range(1,18):
    for yi in range(1,4):
        x = str(xi)
        y = str(yi)
        correctFile = join([join(['survey00',x],''),y,'labeled','fragged','xml'],'.')
        checkFile = join(['classifiedSurvey',join(['00',x],''),y,'xml'],'.')
        cmdLine = join(['SketchCorrectness',correctFile, checkFile],' ')
        fileHandle.write(cmdLine)
        fileHandle.write('\n')
fileHandle.close()
        
