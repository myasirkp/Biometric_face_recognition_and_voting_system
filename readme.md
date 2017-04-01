Biometric (face) recognition and Voting system.

Capturing facial data and using as a means for authentication.
It is implemented using Raspberry Pi 3, Python 2.7 and opencv 3.0.0.
Image is captured using picamera, but also possible with any other camera also.

the code is split into main four steps

1. Capturing images for the training- along with it the voter data is collected.

the code for the continuous capture of the images is in capture.py

the data of the users is saved into a csv file. (Better to use a database- may be mysql, try it!)

the associated with it is in create_file.py

the code for updating the user data is in 

2. Training of images and save the result as a .xml file.
The xml file helps to load the data whenever needed eliminating the need to train in Raspberry Pi.

The algorithm used is LBPH that is available with opencv in the haar cascades along with the contrib packages.

The code is in train.py

3. The capturing of current image for detection.
Available in capture_detect.py

4. Recognizing the person and searching and updating the file.

The previously saved xml file is loaded and the most probable match is found.

The code is recognize.py - for recognizing.
search_id.py - for updating the file.

The actual project files I used is in the folder actual_project_files
The files are:
 cap.py - capturing images for training and file creation.
 new.py - training the images and saving it to xml file.
 capd.py - capturing the image for detection.
 newd.py - recognizing and updating the database.

The file I used to store info is table.csv

I have encapsulated all the codes into a gui platform created with Tkinter, code in gui.py
For any queries email to toyasirkp@gmail.com
