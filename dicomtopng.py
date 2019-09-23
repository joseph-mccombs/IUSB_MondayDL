import dicom
import os

data_path = '../ddsm/ClassicalPathFormat/CBID-DDSM/'

for curdir, dirs, files in os.walk(data_path):
    for f in files:
        if not f.endswith('.dcm'):
            continue

        file_path = os.path.join(curdir,f)
        data = dicom.read_file(file_path)
        print(data)
        exit()