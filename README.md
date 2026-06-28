## AI-Driven Deepfake Image Detection Using Machine Learning
# Author: Harshal Vijay Hivarkar
# Affiliation: Suryodaya College of Engineering & Technology

Date: March 2026

# Abstract
The rapid spread of AI-generated synthetic media poses a critical threat to digital trust, journalism, and personal security. Conventional approaches to detecting manipulated images rely on manual forensic analysis and do not scale to the volume of content generated daily. This project presents a machine learning-based deepfake image detection system trained on a curated dataset of 8,000 labeled images (real and fake) with 24 visual and frequency-domain features. Multiple classification models were developed and compared, including Logistic Regression, Random Forest, and Convolutional Neural Network (CNN), using a preprocessing pipeline with image normalization, feature extraction, and StandardScaler to prevent data leakage. Model selection was based on 5-Fold Cross-Validation, ROC-AUC score, and test accuracy. The final deployed model achieves 91.4% accuracy and 94.6% AUC. The system is integrated into a Flask web application that allows users to upload image files and receive instant authenticity scores and manipulation risk predictions.

# Introduction
The proliferation of deepfake technology — powered by Generative Adversarial Networks (GANs) and diffusion models — has made it increasingly easy to create hyper-realistic synthetic images that are indistinguishable to the human eye. This poses serious risks in areas such as misinformation, identity fraud, and political manipulation. Early and accurate detection of deepfake images is therefore a pressing need in modern digital security and content moderation. However, identifying manipulated images is challenging because generation techniques evolve rapidly and synthetic artifacts are often subtle. Machine learning offers a data-driven alternative — by learning visual and frequency-domain patterns from labeled real and fake images, a trained model can assist analysts and platforms in flagging synthetic content automatically. This project applies that idea practically by building a complete detection pipeline using a curated image dataset. The goal is not only to build an accurate model but also to make it accessible. A Flask-based web application wraps the trained model, allowing non-technical users to upload image files through a simple interface and receive an instant authenticity score along with a manipulation risk level. This project covers the full workflow from exploratory data analysis and model comparison to hyperparameter tuning and deployment.

# Literature Review
Several studies have used face image datasets for binary deepfake classification. Common approaches include SVM-based forensics, frequency analysis, and CNN-based feature extraction. Most prior work focuses only on accuracy on benchmark datasets such as FaceForensics++. This project improves on that by using cross-validation, AUC scoring, and a proper preprocessing pipeline to avoid data leakage — common pitfalls in earlier implementations — while also incorporating both spatial and frequency-domain features for more robust detection.

# Methodology
The Deepfake Image Detection system follows a structured pipeline. First, the user uploads an image file (JPEG or PNG). The system then preprocesses the image — resizing to a standard resolution, normalizing pixel values, and extracting features across two domains: spatial (texture, noise patterns, facial landmark inconsistencies) and frequency (FFT-based spectral analysis to detect GAN fingerprints). Next, the trained classification model processes these combined features to assess whether the image is real or synthetically generated. At the same time, lightweight heuristic rules check for common manipulation artifacts such as unnatural blurring around facial edges, color histogram anomalies, and metadata inconsistencies. The outputs from the ML model and heuristic checks are combined into a final prediction score. The system then presents the user with an authenticity verdict, a confidence percentage, and a risk level (Low / Medium / High) in clear, non-technical language.

# Implementation
The project is built in Python using standard libraries including NumPy, OpenCV, scikit-learn, and TensorFlow/Keras for the CNN component. The user interface is a simple web page where users can drag and drop or upload an image file. The backend preprocesses the image, extracts spatial and frequency features, and passes them to the trained model. The CNN extracts deep visual features while heuristic rules add supplementary artifact warnings. The system merges these outputs and formats the result in plain English using short bullet points — for example, "Frequency domain analysis detected GAN-typical spectral artifacts" or "Facial boundary shows unnatural smoothing consistent with face-swap manipulation." The design prioritizes speed, simplicity, and interpretability for non-expert users.

# Results and Discussion
MetricScoreTest Accuracy91.4%ROC-AUC94.6%5-Fold CV Accuracy88.1% ± 2.9%Precision (macro)90%Recall (macro)92%
The CNN model performed best overall — it captured deep spatial features that shallow models missed. Random Forest showed competitive performance using handcrafted frequency features alone, demonstrating that frequency-domain analysis is a strong standalone signal. Logistic Regression provided a useful interpretable baseline but struggled with complex GAN artifacts. The combination of spatial and frequency features consistently outperformed either domain in isolation.

# Limitations

Dataset size (8,000 images) may not generalize across all GAN architectures and generation methods
Only one curated dataset is used; model may not perform equally on newer diffusion-based fakes
No video deepfake detection — limited to static images only
Model performance degrades on heavily compressed or low-resolution images
Web app has no authentication, data storage, or audit logging
Model is not validated against adversarially crafted images designed to evade detection


# Future Scope

Train on larger, more diverse datasets including diffusion model outputs (e.g., Stable Diffusion, DALL·E)
Extend detection to video frames and audio-visual deepfakes
Add SHAP or LIME for explainability (show which image regions influenced the prediction)
Integrate with social media content moderation pipelines via REST API
Build a mobile-friendly version for real-time camera-based detection
Add user authentication, prediction history, and batch processing for enterprise use
Explore adversarial training to improve robustness against evasion attacks


# Conclusion
This project demonstrates a complete end-to-end machine learning workflow — from data exploration and feature engineering to model training, evaluation, and web deployment — applied to the critical problem of deepfake image detection. The system achieves strong performance on the curated image dataset and provides a usable interface for real-time authenticity predictions. It serves as a solid foundation for a production-grade digital media verification tool applicable to journalism, social platforms, and law enforcement.

# References

[1] FaceForensics++ Dataset: Rössler et al., 2019 — https://github.com/ondyari/FaceForensics
[2] Scikit-learn Documentation: https://scikit-learn.org
[3] TensorFlow/Keras Documentation: https://www.tensorflow.org
[4] OpenCV Documentation: https://docs.opencv.org

