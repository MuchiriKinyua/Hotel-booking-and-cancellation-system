# Phase-5-Capstone-Project
## Overview
This project aims to analyze hotel booking data to understand and predict factors influencing cancellations. With a focus on City and Resort Hotels, the goal is to identify patterns and provide recommendations to mitigate cancellation risks. The predictive model developed will enhance revenue stability by recognizing seasonal trends, analyzing waiting times, and enabling personalized loyalty programs. Ultimately, the project seeks to optimize booking processes and contribute to increased profitability in the hotel industry.

## Table of Contents
1. Business Understanding
   1.1 Business Description
    1.2 Problem Statement
     1.3 Research Questions
2. Importing Libraries And Warnings
3. Data Understanding
4. Data Preparation
5. EDA
6. Data Preprocessing
7. Data Modelling
8. Evaluation
9. Recommendations
10. Conclusions
11. Challenges
 
## 1. Business Understanding
### 1.1 Business Description
Hotel bookings data encapsulates the intricate process through which guests reserve dates, specify stay durations, and express room preferences. Whether booked physically at hotel premises, through agents, or online platforms, this data reflects recent trends impacting City and Resort Hotels, particularly high cancellation rates leading to diminished revenue. This project seeks to meticulously analyze the dataset, pinpoint factors contributing to cancellations, and furnish actionable recommendations. By doing so, the objective is to empower hotel owners with insights to proactively manage risks, optimize profitability, and enhance the overall guest experience.
### 1.2 Problem Statement
The global hotel industry, pivotal in the tourism sector, faces challenges in an evolving landscape. Online reservations have surged due to convenience, options, and flexibility. Our aim is to build a predictive model for precise hotel booking and cancellation forecasts. By analyzing factors like reservation history, cancellations, market segments, and special requests, the model aims to identify seasonal trends and enhance revenue stability. Additionally, we'll explore personalized loyalty programs, leveraging insights to boost repeat bookings and strategically address industry challenges.
### 1.3 Research Questions
- What factors influence hotel reservation cancellations?
- Where do the majority of bookings occur, online or offline?
- How can we support hotels in making pricing and promotional decisions?
- Why do most reservations made by agents occur offline?
- Which distribution channels and market segments exhibit the highest booking success rate?
- How can booking strategies be refined to minimize cancellations and maximize revenue?
- What personalized services can be introduced to enhance guest experience?
- What strategies can be implemented to enhance collaboration with high-performing partners?
- What are the key preferences and behaviors of repeat guests?
- 
## 2. Importing Libraries And Necessary dependencies 
import pickle
import warnings
import numpy as np
import pandas as pd
import seaborn as sns
from sklearn import metrics
from sklearn.svm import SVC
from datetime import datetime
import matplotlib.pyplot as plt
warnings.filterwarnings("ignore")
from sklearn.decomposition import PCA
from sklearn.pipeline import Pipeline
from mpl_toolkits.mplot3d import Axes3D
from imblearn.over_sampling import SMOTE
from sklearn.dummy import DummyClassifier
from sklearn.metrics import roc_curve, auc
from keras import models, layers, optimizers
from matplotlib.animation import FuncAnimation
from sklearn.tree import DecisionTreeClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn.model_selection import train_test_split, GridSearchCV, cross_val_score, RandomizedSearchCV, cross_validate
from sklearn.metrics import classification_report, confusion_matrix, ConfusionMatrixDisplay, precision_score, recall_score, \
accuracy_score, f1_score, roc_curve, auc


## 3. Data Understanding
**Size of the Dataset:**
- The dataset comprises 119,390 rows and 36 columns.
**Columns:**
- Some important columns include:
    - `hotel`: Type of hotel (e.g., Resort Hotel, City Hotel).
    - `is_canceled`: Whether the booking was canceled (1) or not (0).
    - `lead_time`: Number of days between booking and arrival.
    - `arrival_date_month`: Month of arrival.
    - `stays_in_weekend_nights` and `stays_in_week_nights`: Number of weekend and week nights the guest stays.
    - `adults`, `children`, `babies`: Count of adults, children, and babies.
    - `previous_cancellations` and `previous_bookings_not_canceled`: Count of prior cancellations and non-canceled bookings.
    - `deposit_type`: Type of deposit made for the reservation.
    - `adr`: Average Daily Rate.
**Data Types:**
- The dataset contains a mix of data types, including integers, floats, and objects.
**Missing Data:**
- Some columns, such as `country`, `agent`, and `company`, have missing values.
**Customer Types:**
- Customers are categorized as `Transient`, `Contract`, `Transient-Party`, and `Group`.
### Summary
This dataset helps us understand trends in hotel bookings, cancellations, and customer behaviors. We'll explore these patterns further in our analysis.

## 4. Data Preparation

## 5. EDA

## 6. Data Preprocessin

## 7. Data Modelling

## 8. Evaluation

## 9. Recommendations

## 10. Conclusions

## 11. Challenges

Before you begin, ensure you have met the following requirements:

- Python 3.x installed
- (Any other dependencies or prerequisites)

## Installation
