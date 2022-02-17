# M3U8Converter
This is an application that can be used to convert video files to m3u8 streaming format.

The path of each of the files tha needs to be converted is added to the csv file provided and the aplication is run. Conversion log is created which gives the details of the files conversion status.

To run the application, 2 files are required:
1. M3U8Converter.exe
2. FileNameList.csv

Both these files should be placed in the same folder in the system.

STEPS TO CONVERT VIDEOS to M3U8 FORMAT:

1. Place the files M3U8Converter.exe, FileNameList.csv in one folder.

2. Edit the FileNameList.csv file to contain the complete path of the file along with extension of th videos. Sample files names are added for reference. Save the changes. NOTE: Do not edit or remove first row data 'CompleteFilePath' which is header field used in the application.

3. Once the filenames are added to the csv, run the application file M3U8Converter.exe. This will open a console window to display the status of conversion process. Also a ConversionLog.log file is created in the same folder where app file and csv are available.

4. Once the process is complete, log file can be checked for the files that are converted or errors that need to be solved for conversion.
