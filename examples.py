import pydicom as dicom
import pandas

# Data Location
data_dir = '/deepData/DataSetXfer/DataSets/tcia-ddsm-all/ClassicalPathFormat/CBIS-DDSM/'

# CSV files for data paths and descriptions
train_csv = '/deepData/DataSetXfer/DataSets/tcia-ddsm-all/ClassicalPathFormat/mass_case_description_train_set.csv'
test_csv = '/deepData/DataSetXfer/DataSets/tcia-ddsm-all/ClassicalPathFormat/mass_case_description_test_set.csv'


train_csv_data = pandas.read_csv(train_csv)
# Check out pandas docs on to_dict function - https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.to_dict.html
data = train_csv_data[['cropped_image_path', 'pathology']].to_dict(orient='list')

for file, pathology in zip(data['cropped_image_path'], data['pathology']):
    print(file, pathology)