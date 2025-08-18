
```markdown
# 🎯 QoE, Visual Attention & Spatial Audio in 360° Videos

This study explores how spatial sound affects participants' visual attention and Quality of Experience (QoE) in immersive 360° environments.

Participants were exposed to identical video content under four audio conditions:

- ❌ No sound  
- 🎧 Stereo  
- 🌀 First-order Ambisonics  
- 🌀 Third-order Ambisonics  

They wore a head-mounted display (HMD) with integrated eye tracking and were seated on a rotating chair (3DoF). Physiological data was also collected via the Empatica E4 — a medical-grade wearable for real-time data capture.

---

## 🔗 Companion Visualization Tool

To visualize spatial audio and visual attention data in-browser, use the following companion project:

🎧 [JSAmbisonics – Web Player with Gaze & Audio Overlays](https://github.com/hirwaam/JSAmbisonics)  
A browser-based 360° video player with:
- Spatial audio playback (Stereo, FOA, HOA)
- Real-time gaze, pupil, and head pose overlays
- Sound energy and fixation heatmaps

Built using Three.js, Omnitone, and extended for interactive QoE analysis.

---

## 📦 Dataset Overview

The dataset includes eight folders:

- `foin`, `fout` – First-order sound (indoor/outdoor)
- `hoin`, `hout` – Third-order sound (indoor/outdoor)
- `stin`, `stout` – Stereo sound (indoor/outdoor)
- `nsin`, `nsout` – No sound (indoor/outdoor)

Each folder contains three subfolders:

- `_gazedata` – Eye gaze + pupil diameter (`.csv`)
- `_posedata` – Head pitch/yaw data (`.csv`)
- `_HR` – Heart rate data (`.csv`)

---

## 🔍 File Naming Convention

Example:  
`gazedata-20211215-153657_16735.csv`

- `gazedata`: Data type (gaze)
- `20211215-153657`: Date + time
- `16735`: Stimulus sequence (videos 1, 6, 3, 7, 5)

---

## ⏱ Sampling Rates

- Gaze/Pose: 120 samples per second  
  (~36,000 samples per 5-minute video)  
- Heart Rate: 1 sample per second  
  (~300 samples per session)

---

## 👁️ Gaze Data

- 146 total files across 8 conditions  
- 18 or 19 files per subfolder  
- Captures gaze vectors and pupil diameter from both eyes

---

## 🧭 Pose Data

- Captures pitch and yaw from head movement  
- 146 files across 8 conditions  
- Same sampling and structure as gaze data

---

## ❤️ Heart Rate Data

- 73 total files  
- Includes:
  - Baseline heart rate
  - During indoor video playback
  - During outdoor video playback  
- Organized by sound condition

---

## 📝 Subjective Questionnaire

A 20-item questionnaire was developed to measure:

- Presence  
- Immersion  
- Spatial sound perception  

Based on a 5-point Likert scale (ACR – Absolute Category Rating).  
Informed by prior validated QoE questionnaires.

---

## 👨‍💻 Author

Amit Hirway  
PhD Candidate, Technological University of the Shannon  
Supervisors: Dr. Niall Murray, Dr. Yuansong Qiao  
📩 [a.hirway@research.ait.ie](mailto:a.hirway@research.ait.ie)

---

## 📜 License

This dataset and documentation are intended for academic and research use.  
Please cite the source if used in any publication or derivative work.

---

```


