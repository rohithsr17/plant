
# Consolidated Plant Disease Detection System Using CNN

This project is a comprehensive system for detecting plant diseases from leaf images using Convolutional Neural Networks (CNN). The system identifies plant diseases, provides the disease name, and suggests appropriate fertilizers to help farmers and agriculturists maintain healthy crops.

## Table of Contents
- [Introduction](#introduction)
- [Existing System](#existing-system)
- [Proposed System](#proposed-system)
- [Modules](#modules)
- [Methodology](#methodology)
- [Architecture](#architecture)
- [Dataset](#dataset)
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Future Enhancements](#future-enhancements)
- [References](#references)

## Introduction
The system recognizes images of crop leaves, identifies diseases caused by bacteria and fungi, and suggests suitable fertilizers. By uploading an image of an affected plant, users can receive valuable insights about the disease and its cause, enabling informed decisions.

## Existing System
Traditional methods for plant disease detection involve distance metric learning and clustering, which group similar pixels together. However, these methods struggle with unsupervised or weakly supervised data due to a lack of unified theories and efficient algorithms.

## Proposed System
The proposed system leverages CNN for accurate and automated plant disease detection. Key components include:
- **Matrix Factorization** for preprocessing plant disease data.
- **Image Segmentation** to isolate specific parts of the plant.
- **Feature Extraction** to identify disease patterns.
- **Classification** using CNN.
- **Disease Identification** and **Fertilizer Suggestion** based on classification results.

## Modules
The system comprises three main modules:
1. **User Module**: Allows users to upload diseased plant images and view detailed reports.
2. **Admin Module**: Enables the admin to process uploaded images and compare them with trained models for disease prediction.
3. **Client Module**: Recommends fertilizers to users based on the detected disease.

## Methodology
The project uses the following image processing and machine learning steps:
1. **Preprocessing**: Cleaning and normalizing images.
2. **Image Segmentation**: Identifying and isolating infected areas.
3. **Feature Extraction**: Extracting disease-relevant features from segmented areas.
4. **Classification**: Using CNN for disease classification.

## Architecture
The system consists of:
- A user interface for image upload and disease information retrieval.
- A database to store image data, user information, and model predictions.
- CNN-based backend processing to detect diseases and suggest fertilizers.

## Dataset
- **Source**: Code-sharing platform on GitHub.
- **Training Data**: 1838 images, including 865 fruit images and 1006 vegetable images.
- **Testing Data**: 30 images.

### Dataset Breakdown by Crop
- Apple: 208 images
- Blueberry: 40 images
- Cherry: 48 images
- Corn: 224 images
- Grape: 248 images
- Orange: 40 images
- Peach: 88 images
- Pepper: 86 images
- Potato: 120 images
- Raspberry: 32 images
- Soybean: 80 images
- Strawberry: 80 images
- Tomato: 520 images

## Features
- **Disease Detection**: Upload leaf images to identify diseases using CNN.
- **Fertilizer Recommendation**: Based on disease analysis, recommend appropriate fertilizers.
- **Admin Dashboard**: Manage image processing, model training, and disease prediction.
- **User-Friendly Interface**: Simple navigation for uploading images and viewing results.

## Technologies Used
- **Convolutional Neural Network (CNN)**: For image classification.
- **Python**: Core programming language.
- **Database**: Stores image data and user details.
- **Web Framework**: Provides a user interface for easy access and interaction.

## Future Enhancements
- **Integration with Environmental Sensors**: Combine image data with sensor data to predict disease outbreaks.
- **Mobile Application**: For real-time disease detection on-the-go.
- **Drone Integration**: Use drones to capture and analyze field images.
- **Weather Forecasting**: Include weather data to offer preventive recommendations.

## References
- [Identification of Plant Diseases Using CNN](https://www.researchgate.net/publication/339121688_Identification_of_plant_diseases_using_convolutional_neural_networks)
- [Agriculture Plant Disease Studies](https://www.mdpi.com/2077-0472/12/8/1192)
- [Other Relevant Studies and Articles](https://www.sciencedirect.com/science/article/pii/S2589721721000180)

## Conclusion
This plant disease detection system, powered by CNN, represents a valuable tool for early and accurate diagnosis of crop diseases. With continued improvements in machine learning and sensor integration, the system has the potential to support more robust agricultural practices, enabling farmers to make informed, timely decisions to protect their crops.

---

This README file provides a comprehensive overview of the project and can be further customized to include specific usage instructions if needed. Let me know if you want to add any additional details!
CONTACT: rohithsr1710@gmail.com
