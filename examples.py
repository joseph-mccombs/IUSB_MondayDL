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

# There are many ways to work with CSV data, pandas has a ton of useful built in functions
data = train_csv_data[['cropped_image_path', 'pathology']]
print(data)

# Getting a single data entry
# Check out pandas docs on to_dict function - https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.to_dict.html
image_path = data['cropped_image_path'].to_list()[0]
fp = os.path.join(data_dir, image_path)

# Read in the file using pydicom
dcm = dicom.read_file(fp)

# get the pixel_array data from the dicom file
pixel_data = dcm.pixel_array

# convert pixel_array data to image data
im = Image.fromarray(pixel_data)

# save image as png
im.save('tmp.png')
