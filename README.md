# Deep Learning class 9/23,9/25


#### Before getting started

1. Get your environment set up
     * Set up your anaconda environment on the linux systems
        * Go to https://www.anaconda.com/distribution/#download-section
        * Download the linux installer (can use wget)
        * Run the bash install script in your home directory
        
    * Install needed pythong packaged using conda install (if package is not found on conda use pip install)
        * Some packaged you may want to install are ...
        * keras
        * tensorflow-gpu
        * pandas
        * pydicom (this one, for example, is installed via pip and not conda)
        
2. Run Cats & Dogs example
    * Get code from Dr. Wolfer + Jeyan (https://github.com/jeyoor/iusb-dl/) and understand the sequential and functional APIs of keras
    * Run code on the linux machines and make sure the models are working
    * Mess with some hyperparameters and see how they affect the training accuracy of your model
        * some examples of this would be setting difference sizes of the convolutional, pooling, or dense layers
        * mess with learning rate
    * In the file conv2.py, what do the **ImageDataGenerator()** (line 17) and **flow_from_directory()** (line 26) function do?
    * **HINT:** https://keras.io/preprocessing/image/#flow_from_directory - look at what the classes argument does
    * Look at how the cats and dogs data is stored and the directory structure, ******THIS IS VERY IMPORTANT******
    


3. Prepare DICOM breast cancer lesion data set
    * Read about the data set here https://wiki.cancerimagingarchive.net/display/Public/CBIS-DDSM
    * This data set is already downloaded on the linux machines so you DO NOT need to download it yourself
    
    
#### What to do
    Data Location
    /deepData/DataSetXfer/DataSets/tcia-ddsm-all/ClassicalPathFormat/CBIS-DDSM/
    
    CSV files for data paths and descriptions
    /deepData/DataSetXfer/DataSets/tcia-ddsm-all/ClassicalPathFormat/mass_case_description_train_set.csv
    /deepData/DataSetXfer/DataSets/tcia-ddsm-all/ClassicalPathFormat/mass_case_description_test_set.csv
    
##### Use the CSV files and pydicom to create a workable data set

In the real world data is hardly ever in a nice usable state - even data sets created by universities made to be used by
 researchers (this one is from Stanford). In machine learning/data science a large amount of time spent is on "data wrangling" or "data munging". 
 
 So you, as a junior data scientist, have been tasked with cleaning up this data set!

1. Use a CSV reader such as pandas (but any CSV/text reader will do) to read in the data
2. Using the "cropped_image_path" and "pathology" columns create a directory structure in your home directory for training a model to predict whether a lesion is malignant or benign
3. Read in the DICOM file using pydicom read_file() function and pixel_array attribute
4. Save the image as a png with the appropriate name and in the appropriate location based on whether it is in Training/Testing set and Malignant/Benign
5. Run the conv2.py or conv2-func.py models on your new dataset
6. adjust the model architecture and parameters and record setup and results for comparison