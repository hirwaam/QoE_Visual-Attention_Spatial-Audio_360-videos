The aim of this study is to explore the effects of spatial sound on participants' visual attention and Quality of Experience(QoE) in an immersive environment. For that purpose, different people were exposed to the same immersive videos, with different soundtrack conditions: no sound, stereo, first-order and third-order Ambisonics. During the experiment, participants wore an HMD with an integrated eye-tracker and were asked to perform a free-viewing experiment whilst seated in a rotating chair with 3DoF. To collect physiological data from participants, we used the Empatica E4 wristband, a medical grade wearable device that offers real-time data acquisition and software for in-depth analysis and visualization.

**Dataset Description**

This dataset contains eight folders: foin, fout, hoin, hout, nsin, nsout, stin, and stout. These correspond to the four sound conditions in indoor and outdoor environments. Here, foin and fout indicate the data acquired by making the participant watching videos with first-order sound in indoor and outdoor environments respectively. Similarly, the case for the other 3 sound conditions. Additionally, each folder contains three subfolders, such as: 1) Gaze data (_gazedata); 2) Heart rate data (_HR); 3) Pose data (_posedata) with the respective .csv files. The data regarding gaze and pupil diameter for both the left and right eyes can be found in the _gazedata folder. The data pertaining to the yaw and pitch can be found in the _posedata folder. Whereas, the heart rate data is available in the _HRdata folder. The heart rate data has been extracted after processing the HR.csv files available in the e4 folders. 

The folders include multiple files in .csv format, which comprise the data captured during the time the participant watched the videos. For example, consider a file “gazedata-20211215-153657_16735.csv” in foin/_gazedata subfolder. Here, the first term “gazedata” indicates the type of data contained in the file, “20211215_153657” indicates that the gaze and pupil diameter information was acquired from the participant on 15th December 2021 at the time 15:36:57. Further, the last term “16735” specifies that the participant was made to watch videos in the sequence 1,6,3,7, and 5. Files that have pose-related information have the prefix ‘pose’ and those that store heart-rate data have the prefix ‘HR’. The gaze and pose data were captured at a sampling rate of 120 samples/second, and hence for a total playback time of 300 seconds, approximately 36000 samples can be found in each file. The heart rate data was captured at a sampling rate of 1 sample/second, and hence for a total playback time of 300 seconds, 300 samples can be found in each file. 

**Gaze Data**

A total of 146 files are present in the dataset which contains information regarding the gaze data under eight different sub-folders. The total files present in each folder are: 18 files each in foin and fout, 18 files each in hoin, and hout, 19 files each in stin and stout, and 18 files each in nsin and nsout. Thus, the information regarding the gaze data is recorded for a total of 43,800 seconds of video playback time including both indoor and outdoor environments, and every file in the _gazedata folder comprises approximately 36000 samples.

**PoseData**

The pose data gives information regarding the pose of the participants while watching videos. Pitch indicates the movement of the head along the horizontal axis, while the movement in the vertical axis is given by yaw. Head movements can be used to identify the area where the visual attention of the user is concentrated, as the position of the head changes with the variation in the displayed visuals (and perhaps the sound and its nature viz. non-spatial/spatial). The pose data recorded are stored in the folder named _posedata, which has eight sub-folders. In this dataset, a total of 146 files are present with information containing the pose data, with 18 files contained in foin, 18 files in fout, 18 files each in hoin, and hout, 19 files in both stin and stout, and 18 files in nsin, and nsout, correspondingly, similar to the gaze data. Similar to the _gazedata, the files in the _posedata folder also contain around 36000 samples, recorded from when the participants were made to watch the sequence of 5 videos in indoor or outdoor conditions. 

**Heart Rate Data**

In total, 73 files with heart rate related data are contained in the dataset. Each file has information regarding heart rate of the participant in the baseline condition, heart rate when the participant watched videos in the Indoor category and heart rate when the participant watched videos in the Outdoor category along with the corresponding timestamp for a particular sound condition. The fo, ho, and ns folders comprise 18 files each, whereas the st folder includes a total of 19 files with heart rate data.

**Subjective Questionnaire**

A questionnaire consisting of twenty questions was developed to evaluate the participants' perception of presence, immersion, and spatiality of sound after watching the stimuli. Inputs from existing well-known questionnnaires were considered in the development of this questionnaire.  The absolute category rating (ACR) system, was used to rate each question. The rating system used a five-point Likert scale, where the participants indicated whether they agreed or disagreed with each statement.
