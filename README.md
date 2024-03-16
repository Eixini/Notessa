# Notessa

This application allows you to create notes of many types.

## Installing dependencies
To install dependencies you need to run the following command: <br/>
```
pip install -r requirements.txt
```
_The version of Python for which the project was developed: 3.12_<br/><br/>
The entry point to applications is the `app.py` file,
which is located in the `Notessa` directory.
```
You need to enter the command while above the directory!

Notessa
├── app.py
├── ...
└── ...
```
While in the directory above, you need to run the command: <br/>
for Windows<br/>
```
python -m Notessa.app
```
for Linux<br/>
```
python3 -m Notessa.app
```

## Known Issues
- There is no check for a connected microphone and webcam
- When recording a video note, if you pause it, the recording will behave incorrectly
- If you open and close VoiceNote and VideoNote several times in a row to create notes, 
the application will crash with the error `Process finished with exit code -1073741819 (0xC0000005)`
- If you select a microphone several times in a row,
the program crashes with the error `Process finished with exit code -1073741819 (0xC0000005)`