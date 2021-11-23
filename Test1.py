import exifread
import exifread as er
import os
import sys

dircont = input("Please Enter the path of your directory")
directory = os.listdir(dircont)
for file in directory:
    if file.endswith (('jpg','JPG','png','PNG','tiff','TIFF')):
        file_path = os.path.join(dircont, fil)
        print (file_path)
        f = open(file_path, 'rb')
        tags = exifread.process_file(f)
        
        
        for tag in tags.keys():
            if tag not in ('JPEGThumbnail', 'TIFFThumbnail', 'Filename', 'EXIF MakerNote'):
                print ("Key: %s, value %s" % (tag, tags[tag]))
                print("File %s log saved." % file)
print("All done!")
