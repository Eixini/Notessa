# Notessa

This application allows you to create notes of many types.

# Table of contents
- [Building the project](#building-the-project)
- [Creating a translation](#creating-a-translation)
- [Known Issues](#known-issues)

## Installing dependencies
To install dependencies you need to run the following command: <br/>
```shell
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
While in the directory above, you need to run the command: <br/><br/>
for Windows<br/>
```shell
python -m Notessa.app
```
for Linux<br/>
```bash
python3 -m Notessa.app
```

## Building the project
While in the directory with the app.py file, enter the command: <br/>
```shell
pyinstaller --name="Notessa" -w app.py
```
The application will be built, and a Notessa.spec file will be created in the same directory. 
Subsequently, you can build/rebuild the project using this manifest: <br/>
```shell
pyinstaller Notessa.spec
```
## Creating a translation
While in the project directory, i.e. in "Notessa", to create a file for translation,
you must enter the following command: <br/>
```shell
pyside6-lupdate ./ -ts ru.ts
```
This file can then be opened in `Qt Linguist` and the required parts can be translated.
After the translation is completed, you need to convert the file from `.ts` to `.qm` format.
This is done as follows: <br/>
```shell
pyside6-lrelease ru.ts -qm ru.qm
```
After successful conversion,
the files must be placed in the project directory in the `./resource/translations/` directory
Next, if a resource file with translations exists,
you need to enter a line with a new translation file: <br/>
```xml
<RCC>
  <qresource>
    <file>translations/en.qm</file>
    <file>translations/ru.qm</file>
  </qresource>
</RCC>
```
Finally, you need to convert the resource file to a `Python` file as follows:
```shell
pyside6-rcc translations.qrc -o translations_rc.py
```

## Known Issues
- Sometimes, while in `CreateVideoNoteWidget` and after closing it, the application crashes.
The reason is not clear.
- Cannot find the correct canvas size in `CreatePaintNoteWidget`.
There have been attempts to measure the height of widgets to calculate the correct size,
but the attempts were unsuccessful.
- Currently, it is not possible to resize the entire application window.
This is because there is an issue with `PaintNote` canvas being sized correctly.
In addition, at the moment it is not clear how to correctly resize the `PaintNote` canvas 
(not scaling, but the size, as in the `Paint` graphic editor in `Windows`).
- The application window can be moved in `Windows`,
but it does not work in `Linux` (tested only in `Ubuntu 22.04`). The reason is not clear.
- In the `new version` of the application (applies to `Linux`, tested on `Ubuntu 22.04`),
it is not possible to get a preview from the webcam or record video,
although sound is recorded. In `Windows 10`, recording and display occurs correctly.
- There is no message about the need to manually restart the application after changing the language.