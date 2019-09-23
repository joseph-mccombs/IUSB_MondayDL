import pydicom as dicom
import os
from PIL import Image

data_path = '../ddsm/ClassicalPathFormat/CBIS-DDSM/'

for curdir, dirs, files in os.walk(data_path):
    for f in files:
        if not f.endswith('.dcm'):
            continue

        file_path = os.path.join(curdir,f)
        data = dicom.read_file(file_path)
        print(file_path)
        print(data)
        img = Image.fromarray(data.pixel_array)
        img.save('tmp.png')

        exit()