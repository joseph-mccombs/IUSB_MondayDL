import pydicom as dicom
import pandas
import os
from PIL import Image

# Data Location
data_dir = '/deepData/DataSetXfer/DataSets/tcia-ddsm-all/ClassicalPathFormat/CBIS-DDSM/'

# CSV files for data paths and descriptions
train_csv = '/deepData/DataSetXfer/DataSets/tcia-ddsm-all/ClassicalPathFormat/mass_case_description_train_set.csv'
test_csv = '/deepData/DataSetXfer/DataSets/tcia-ddsm-all/ClassicalPathFormat/mass_case_description_test_set.csv'

# set an output location
outpath = '../data/train/'

# Load csv data with pandas
train_csv_data = pandas.read_csv(train_csv)


data = train_csv_data[['cropped_image_path', 'pathology']]
print(data)

# Getting a single data entry
# Check out pandas docs on to_dict function - https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.to_dict.html
image_path = data['cropped_image_path'].to_list()[0]
fp = os.path.join(data_dir, image_path)

dcm = dicom.read_file(fp)
pixel_data = dcm.pixel_array
im = Image.fromarray(pixel_data)
im.save('tmp.png')


# counter = 0
# for file, pathology in zip(data['cropped_image_path'], data['pathology']):
#     fp = os.path.join(data_dir, file)
#     pixel_data = dicom.read_file(fp).pixel_array
#     pixel_data = Image.fromarray(pixel_data)
#     ben_mag = ''
#     if 'benign' in pathology.lower():
#         ben_mag = 'benign'
#     elif 'malignant' in pathology.lower():
#         ben_mag = 'malignant'
#     else:
#         print(pathology)
#     out = outpath + ben_mag + '/{}.png'.format(counter)
#     pixel_data.save(out)
#     counter += 1