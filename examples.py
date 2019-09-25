import pydicom as dicom
import pandas

# Data Location
data_dir = '/deepData/DataSetXfer/DataSets/tcia-ddsm-all/ClassicalPathFormat/CBIS-DDSM/'

# CSV files for data paths and descriptions
train_csv = '/deepData/DataSetXfer/DataSets/tcia-ddsm-all/ClassicalPathFormat/mass_case_description_train_set.csv'
test_csv = '/deepData/DataSetXfer/DataSets/tcia-ddsm-all/ClassicalPathFormat/mass_case_description_test_set.csv'


train_csv_data = pandas.read_csv(train_csv)

print(train_csv_data[['cropped_image_path', 'pathology']].to_dict())