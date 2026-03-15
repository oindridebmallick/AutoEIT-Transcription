# AutoEIT Transcription Prototype

A prototype system for **automatic transcription of second-language learner speech** from **Elicited Imitation Tasks (EIT)** using modern speech recognition and audio preprocessing techniques.

This project demonstrates an **end-to-end pipeline** that processes raw learner audio, converts it to text, and evaluates transcription accuracy against reference sentences.

---

## Project Motivation

The **Elicited Imitation Task (EIT)** is widely used in linguistic research to measure **global language proficiency**. However, analyzing EIT data requires **manual transcription of learner audio recordings**, which is:

* time-consuming
* expensive
* difficult to scale for large datasets

Most commercial speech-to-text systems perform poorly with **non-native speech**, especially when speakers have:

* diverse language backgrounds
* strong accents
* disfluencies
* partial sentence repetitions

This project explores a **machine learning pipeline** to automatically transcribe learner speech and reduce the need for manual transcription.

---

## System Pipeline

The prototype implements the following workflow:

```
Audio Input
   ↓
Noise Reduction & Preprocessing
   ↓
Speech-to-Text Transcription (Whisper)
   ↓
Transcript Cleaning
   ↓
Evaluation using Word Error Rate
```

This pipeline produces a final transcription and compares it with a reference sentence to measure transcription quality.

---

## Features

* Audio preprocessing and noise reduction
* Speech transcription using OpenAI Whisper
* Cleaning of filler words in transcripts
* Evaluation using Word Error Rate (WER)
* Modular pipeline structure for future improvements

---

## Project Structure

```
AutoEIT-Transcription
│
├── audio/
│   └── sample.wav
│
├── scripts/
│   ├── preprocess.py
│   ├── transcribe.py
│   ├── clean_text.py
│   ├── evaluate.py
│
├── results/
│   └── example_output.txt
│
├── main.py
├── requirements.txt
├── README.md
└── demo_output.png
```

---

## Technologies Used

* Python
* PyTorch
* OpenAI Whisper
* Librosa
* Noisereduce
* JiWER

These tools enable efficient audio preprocessing and transcription evaluation.

---

## Installation

Clone the repository:

```
git clone https://github.com/yourusername/AutoEIT-Transcription.git
cd AutoEIT-Transcription
```

Install dependencies:

```
pip install -r requirements.txt
```

---

## Running the Pipeline

Execute the main pipeline:

```
python main.py
```

The system will:

1. preprocess the input audio
2. transcribe the speech
3. clean the transcription
4. compute transcription accuracy

---

## Example Output

```
Input Audio: sample.wav

Predicted Transcription:
el niño está jugando en el parque

Word Error Rate: 0.07
Accuracy: 93%
```

A sample output file is included in the `results` directory.

---

## Future Improvements

This prototype can be extended with:

* fine-tuning Whisper on non-native learner speech
* speaker segmentation for longer recordings
* automatic EIT scoring based on target sentences
* multilingual learner speech adaptation
* dataset support for large-scale linguistic analysis

---

## Research Context

This project is inspired by the **AutoEIT system**, which aims to automate transcription and scoring of Elicited Imitation Task responses for language learning research.

---

## Author

Oindri Debmallick
Computer Science Engineering (Data Science)
SRM Institute of Science and Technology

---

## License

This project is released for educational and research purposes.
