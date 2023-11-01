import sys
import time
import os
import tobii_research as tr

os.system("cls") 

found_eyetrackers = tr.find_all_eyetrackers()    
my_eyetracker = found_eyetrackers[0]

### Eye Tracker Details
print("\n\n\n##### My eye tracker details#####")

print("Address: " + my_eyetracker.address)
print("Model: " + my_eyetracker.model)
print("Name (It's OK if this is empty): " + my_eyetracker.device_name)
print("Serial number: " + my_eyetracker.serial_number)

### Eye Tracker License

license_file_path = "./se_license_pro_VR_models"
 
print("\n\n\nApplying license from {0}.".format(license_file_path))
with open(license_file_path, "rb") as f:
	license = f.read()

failed_licenses_applied_as_list_of_keys = my_eyetracker.apply_licenses([tr.LicenseKey(license)])
failed_licenses_applied_as_list_of_bytes = my_eyetracker.apply_licenses([license])
failed_licenses_applied_as_key = my_eyetracker.apply_licenses(tr.LicenseKey(license))
failed_licenses_applied_as_bytes = my_eyetracker.apply_licenses(license)

if len(failed_licenses_applied_as_list_of_keys) == 0:
	print("Successfully applied license from list of keys.")
else:
	print("Failed to apply license from list of keys. Validation result: {0}.".
		format(failed_licenses_applied_as_list_of_keys[0].validation_result))

if len(failed_licenses_applied_as_list_of_bytes) == 0:
	print("Successfully applied license from list of bytes.")
else:
	print("Failed to apply license from list of bytes. Validation result: {0}.".
		format(failed_licenses_applied_as_list_of_bytes[0].validation_result))

if len(failed_licenses_applied_as_key) == 0:
	print("Successfully applied license from single key.")
else:
	print("Failed to apply license from single key. Validation result: {0}.".
		format(failed_licenses_applied_as_key[0].validation_result))

if len(failed_licenses_applied_as_bytes) == 0:
	print("Successfully applied license from bytes object.")
else:
	print("Failed to apply license from bytes object. Validation result: {0}.".
		format(failed_licenses_applied_as_bytes[0].validation_result))


### Eye Tracker Capabilities
print("\n\n\n##### My eye tracker capabilities #####")

if tr.CAPABILITY_CAN_SET_DISPLAY_AREA in my_eyetracker.device_capabilities:
	print("The display area can be set on the eye tracker.")
else:
	print("The display area can not be set on the eye tracker.")
  
if tr.CAPABILITY_HAS_EYE_IMAGES in my_eyetracker.device_capabilities:
	print("The eye tracker can deliver an eye image stream.")
else:
	print("The eye tracker can not deliver an eye image stream.")

if tr.CAPABILITY_HAS_HMD_GAZE_DATA in my_eyetracker.device_capabilities:
	print("The eye tracker can deliver a HMD gaze data stream.")
else:
	print("The eye tracker can not deliver a HMD gaze data stream.")
 
if tr.CAPABILITY_CAN_DO_HMD_BASED_CALIBRATION in my_eyetracker.device_capabilities:
	print("The eye tracker can do a HMD screen based calibration.")
else:
	print("The eye tracker can not do a HMD screen based calibration.")
  
if tr.CAPABILITY_HAS_HMD_LENS_CONFIG in my_eyetracker.device_capabilities:
	print("The eye tracker can get/set the HMD lens configuration.")
else:
	print("The eye tracker can not get/set the HMD lens configuration.")


### Eye Tracker Tracking Mode Details
initial_eye_tracking_mode = my_eyetracker.get_eye_tracking_mode()
print("\n\n\n##### My eye tracker's tracking mode details #####")

print("The eye tracker's initial eye tracking mode is {0}.".format(initial_eye_tracking_mode))

try:
	for eye_tracking_mode in my_eyetracker.get_all_eye_tracking_modes():
		my_eyetracker.set_eye_tracking_mode(eye_tracking_mode)
		print("Eye tracking mode set to {0}.".format(eye_tracking_mode))
finally:
	my_eyetracker.set_eye_tracking_mode(initial_eye_tracking_mode)
	print("Eye tracking mode reset to {0}.".format(initial_eye_tracking_mode))
	

### Eye Tracker HMD Current Lens Configuration
old_lens_configuration = my_eyetracker.get_hmd_lens_configuration()
print("\n\n\n##### My eye tracker's lens current configuration #####") 

print("Got Current HMD lens configuration from tracker with serial number {0}:".format(my_eyetracker.serial_number))
print("Left: {0}".format(old_lens_configuration.left))
print("Right: {0}".format(old_lens_configuration.right))
	
### Eye Tracker HMD New Lens Configuration
from tobii_research import HMDLensConfiguration

new_lens_configuration = HMDLensConfiguration(left=(0.0, 0.0, 0.0), right=(0.0, 0.0, 0.0))
my_eyetracker.set_hmd_lens_configuration(new_lens_configuration)

print("\n\n\n##### My eye tracker's new lens configuration #####") 

print("Set New HMD lens configuration for tracker with serial number {0}:".format(my_eyetracker.serial_number))
print("Left: {0}".format(new_lens_configuration.left))
print("Right: {0}".format(new_lens_configuration.right))

### Eye Tracker Gaze Output Frequency
print("\n\n\n##### My eye tracker's gaze output frequency #####") 

initial_gaze_output_frequency = my_eyetracker.get_gaze_output_frequency()
print("The eye tracker's initial gaze output frequency is {0} Hz.".format(initial_gaze_output_frequency))

for gaze_output_frequency in my_eyetracker.get_all_gaze_output_frequencies():
	my_eyetracker.set_gaze_output_frequency(gaze_output_frequency)
	print("Gaze output frequency set to {0} Hz.".format(gaze_output_frequency))