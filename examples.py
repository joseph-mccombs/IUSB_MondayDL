import pydicom as dicom
import pandas
import os
import scipy.misc

# Data Location
data_dir = '/deepData/DataSetXfer/DataSets/tcia-ddsm-all/ClassicalPathFormat/CBIS-DDSM/'

# CSV files for data paths and descriptions
train_csv = '/deepData/DataSetXfer/DataSets/tcia-ddsm-all/ClassicalPathFormat/mass_case_description_train_set.csv'
test_csv = '/deepData/DataSetXfer/DataSets/tcia-ddsm-all/ClassicalPathFormat/mass_case_description_test_set.csv'

# output location
outpath = '~/data/train/'

train_csv_data = pandas.read_csv(train_csv)
# Check out pandas docs on to_dict function - https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.to_dict.html
data = train_csv_data[['cropped_image_path', 'pathology']].to_dict(orient='list')
counter = 0

for file, pathology in zip(data['cropped_image_path'], data['pathology']):
    fp = os.path.join(data_dir, file)
    pixel_data = dicom.read_file(fp).pixel_array

    outpath += pathology.lower() + '/{}.png'.format(counter)

    scipy.misc.imsave(outpath, pixel_data)