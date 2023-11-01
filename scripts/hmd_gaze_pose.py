def execute(my_eyetracker):
	hmd_gaze_data(my_eyetracker)
	
import sys
import time
import os
import json
import datetime
import socket, time
import numpy as np
from socket import *
import tobii_research as tr

# Make it work for Python 2+3 and with Unicode
import io
try:
    to_unicode = unicode
except NameError:
    to_unicode = str
	
os.system("cls") 


#Find connected eyetracker
found_eyetrackers = tr.find_all_eyetrackers()    
my_eyetracker = found_eyetrackers[0]

# Enter experiment phase
userInputPhase = raw_input("Experiment Phase: [test/real]")

# Enter subject number
userInputSubjectNum = raw_input("Subject No.:[1-60]")

# Enter group
userInputVideoGroup = raw_input("Group:[ns/st/fo/ho]")

# Indoor/Outdoor Viewing
userInputVideoCat = raw_input("Viewing Category:[in/out]")

if userInputVideoCat == "in":
	# Enter sequence for indoor media
	userInputVideoSeq = raw_input("Enter Sequence for Indoor Media:[13567,31567,71365,16735,76513]")
else:
	# Enter sequence for outdoor media
	userInputVideoSeq = raw_input("Enter Sequence for Outdoor Media:[12456,65412,16245,25164,16542]")
	
time.sleep(5)

path1 = userInputPhase
print(path1)
if not os.path.exists(path1):
    os.makedirs(path1)

path2 = userInputVideoGroup
print(path2)
if not os.path.exists(os.path.join(userInputPhase, userInputVideoGroup)):
	os.makedirs(os.path.join(path1, path2))

path3 = userInputSubjectNum
print(path3)
if not os.path.exists(os.path.join(userInputPhase, userInputVideoGroup, userInputSubjectNum)):
	os.makedirs(os.path.join(path1, path2, path3))
	
path4 = userInputVideoSeq
print(path4)
if not os.path.exists(os.path.join(userInputPhase, userInputVideoGroup, userInputSubjectNum, userInputVideoSeq)):
	os.makedirs(os.path.join(path1, path2, path3, path4))
	
# get the current script path
here = os.path.dirname(os.path.realpath(__file__))

# create the subdir
subdir = os.path.join(path1, path2, path3, path4)

# Get filename for writing gaze information
filename_gaze = "gazedata-" + datetime.datetime.now().strftime("%Y%m%d-%H%M%S") + ".csv"

# get the complete path to write the gaze information
filepath_gaze = os.path.join(here, subdir, filename_gaze)

# Get filename for writing pose information
filename_pose = "posedata-" + datetime.datetime.now().strftime("%Y%m%d-%H%M%S") + ".csv"

# get the complete path to write the pose information
filepath_pose = os.path.join(here, subdir, filename_pose)

# Get filename for writing pose information as json
filename_pose_json = "posedata-json-" + datetime.datetime.now().strftime("%Y%m%d-%H%M%S") + ".json"

# get the complete path to write the pose information as json
filepath_pose_json = os.path.join(here, subdir, filename_pose_json)

client_socket = socket(AF_INET, SOCK_DGRAM)
client_socket.bind(('',7755))

global_hmd_gaze_data = None

def hmd_gaze_data_callback(hmd_gaze_data):
	global global_hmd_gaze_data
	global_hmd_gaze_data = hmd_gaze_data
   	
	seconds_since_epoch = time.time()
	
	with open(filepath_gaze, "a") as fhandle_gaze:
		#write gaze details to file
		fhandle_gaze.write(str(seconds_since_epoch) + "," + str(global_hmd_gaze_data) + "\n")
	
		
	with open(filepath_pose, "a") as fhandle_pose:
		data = client_socket.recv(512)
		#write pose details to file
		fhandle_pose.write(str(seconds_since_epoch) + "," + data.decode() + "\n")
	
	
	with open(filepath_pose_json, "a") as fhandle_pose_json:
		#write pose details to file in json format
		fhandle_pose_json.write(data + ",")
		
def countdown():	
	stopwatch=300

	while stopwatch >0:
		time.sleep(1)
		print stopwatch,
		stopwatch -=1	
		
def openapp():
	
	base_dir = r'C:\experiment_files'
	base_filename = userInputVideoGroup + "_" + userInputVideoCat + "_" + userInputVideoSeq
	filename_suffix = 'mov'
	
	fullpath_app = os.path.join(base_dir, userInputVideoGroup, userInputVideoCat,  '.'.join((base_filename, filename_suffix)))
	
	os.startfile(fullpath_app)
	
def hmd_gaze_data(my_eyetracker):
	global global_hmd_gaze_data
	
	openapp()

	print("Subscribing to gaze data for eye tracker with serial number {0}.".format(my_eyetracker.serial_number))
	
	time.sleep(2)
	
	my_eyetracker.subscribe_to(tr.EYETRACKER_HMD_GAZE_DATA, hmd_gaze_data_callback, as_dictionary=True)
	
	# Wait while some HMD gaze data is collected.
	time.sleep(300)
	
	my_eyetracker.unsubscribe_from(tr.EYETRACKER_HMD_GAZE_DATA, hmd_gaze_data_callback)
	print("\n\nUnsubscribed from HMD gaze data.Thanks for viewing!!! Your data has been successfully stored and prpcessed..")
	
	os.system("taskkill /im GoProVRPlayer_x64.exe /f")
	print("\n\nClosed GoPro Application..")
	
execute(my_eyetracker)

