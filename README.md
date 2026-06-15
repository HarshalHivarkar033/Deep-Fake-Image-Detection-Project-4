# README.md – Deep Fake Detection System (TrueLens)

# TrueLens – AI-Powered Deep Fake Detection System

## Overview

TrueLens is an AI-powered image authenticity detection system designed to identify potentially fake or AI-generated images. With the rapid growth of deepfakes and generative AI tools, verifying digital content has become increasingly important. This project analyzes uploaded images using multiple computer vision techniques and generates an authenticity score indicating whether the image is likely real or artificially generated.

---

## Problem Statement

Deepfake images and AI-generated content can be used to spread misinformation, manipulate public opinion, and create security risks. Manual verification is often difficult and time-consuming. TrueLens provides an automated solution for detecting suspicious images.

---

## Objectives

* Detect AI-generated or manipulated images.
* Analyze image authenticity using multiple detection techniques.
* Generate an authenticity score ranging from 0 to 100.
* Provide detailed analysis reports for users.

---

## Features

* Image Upload Support
* Frequency Domain Analysis
* Biological Consistency Analysis
* Architectural Consistency Analysis
* Authenticity Scoring System
* FastAPI-Based REST API
* JSON Response Output

---

## Technology Stack

### Programming Language

* Python

### Framework

* FastAPI

### Libraries

* OpenCV
* NumPy
* Uvicorn

### Concepts Used

* Computer Vision
* Image Processing
* Frequency Analysis
* Pattern Recognition
* Deep Fake Detection

---

## System Architecture

1. User uploads an image.
2. Image is validated and processed.
3. Frequency Analysis examines hidden image patterns.
4. Biological Analysis checks human-like structures.
5. Architectural Analysis evaluates structural consistency.
6. Individual scores are calculated.
7. Weighted scoring generates the final authenticity score.
8. Results are returned through the API.

---

## Working Methodology

### 1. Frequency Analysis

AI-generated images often contain unnatural frequency patterns that differ from real photographs. This module detects such irregularities.

### 2. Biological Analysis

Evaluates biological realism, including facial and anatomical consistency that may appear distorted in AI-generated images.

### 3. Architectural Analysis

Analyzes image structures, edges, and object consistency to identify abnormalities commonly found in synthetic images.

### 4. Authenticity Score Calculation

Overall Score =

( Frequency Score × 0.4 )

*

( Biological Score × 0.3 )

*

( Architectural Score × 0.3 )

The final score ranges from:

* 0 → Highly likely fake
* 100 → Highly likely real

---

## API Endpoint

### Analyze Image

POST /api/analyze

### Input

Upload an image file.

### Output Example

```json
{
  "authenticity_score": 82.5,
  "breakdown": {
    "frequency_analysis": {
      "score": 85.2
    },
    "biological_analysis": {
      "score": 80.1
    },
    "architectural_analysis": {
      "score": 82.0
    }
  }
}
```

---

## Installation

### Clone Repository

```bash
git clone https://github.com/yourusername/truelens.git
cd truelens
```

### Install Dependencies

```bash
pip install fastapi uvicorn opencv-python numpy python-multipart
```

### Run Application

```bash
python main.py
```

Or

```bash
uvicorn main:app --reload
```

---

## Applications

* Social Media Content Verification
* News and Journalism
* Cybersecurity
* Digital Forensics
* Fake Media Detection
* Online Content Moderation

---

## Future Enhancements

* Deep Learning-based Detection Models
* Video Deepfake Detection
* Real-time Camera Analysis
* Browser Extension Integration
* Mobile Application Support
* Explainable AI Reports

---

## Results

The system successfully evaluates image authenticity using multiple analysis techniques and provides a confidence-based authenticity score, helping users identify potentially fake or AI-generated images.

---

## Conclusion

TrueLens is a practical AI-based solution for detecting deepfake and AI-generated images. By combining frequency, biological, and architectural analyses, it provides a comprehensive approach to image authenticity verification and contributes to combating digital misinformation.

---

### Author

**Harshal Vijay Hivarkar**

Machine Learning & AI Internship Project

**Tech Stack:** Python | FastAPI | OpenCV | Computer Vision | Artificial Intelligence | Deep Fake Detection
