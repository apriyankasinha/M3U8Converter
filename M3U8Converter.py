import logging
import os
import pandas as pd
import shutil
import ConversionLogger

logger = ConversionLogger.create_logger()

try:
    csvfile = 'FileNameList.csv'
    files = pd.read_csv(csvfile)
    logger.info(csvfile + ' Read Successfully')
except Exception as e:
    logger.error(e)
    logger.info('Place the M3U8Converter exe and FileNameList.csv file in the same folder')
    exit()

for index, file in files.iterrows():
    try:
        extloc = file['CompleteFilePath'].rindex('.')
        slashloc = file['CompleteFilePath'].rindex('\\')
    except Exception as e:
        logger.error(str(e) + ': ' + file['CompleteFilePath']  + ': Check the file path is complete along with extension')
        continue   

    filedir = file['CompleteFilePath'][:slashloc]
    filename = file['CompleteFilePath'][slashloc+1:extloc]
    ext = file['CompleteFilePath'][extloc:]
    
    try:
        if ' ' in filename:
            updatedfilename = filename.replace(' ', '_')
            file['CompleteFilePath'] = filedir + '\\' + updatedfilename + ext
            
            os.chdir(filedir)
            os.rename(filename + ext, updatedfilename + ext)
            filename = updatedfilename
            logger.info(filename + ' renamed to remove spaces')
        
        os.chdir(filedir)
        os.mkdir(filename)
        logger.info(filename + ' folder created at ' + filedir)
        
        shutil.move(file['CompleteFilePath'], filedir +'\\' + filename + '\\' + filename + ext)
        logger.info(filename + ' moved to folder ' + filedir + '\\' + filename)
        
        os.chdir(filename)
        
        command = 'ffmpeg -i "{}" -acodec aac -preset ultrafast -c:v libx264 -f ssegment -hls_flags delete_segments -segment_list {}.m3u8 -segment_list_type hls -segment_list_size 0 {}_%6d.ts'.format(filename + ext, filename, filename)
        stream = os.popen(command)
        output = stream.read()
        logger.info('File Converted: ' + filename)
    except Exception as e:
        logger.error(e)

logger.info('All files in ' + csvfile + ' processed.')
print('Check ConversionLog for details.')
input('\nPress Enter key to Exit')