# Phase-5-Capstone-Project
# HOTEL BOOKING AND CANCELLATION SYSTEM

![How-to-Cancel-Hotel-Reservation-on-Booking](https://github.com/MuchiriKinyua/Phase-5-Capstone-Project/assets/113877377/d3f25dff-c1d5-4a63-9cb7-aef9bb7d07ee)

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
**Checking for Missing Values**
We started by looking for missing values in our dataset. Here are the columns with missing values and how we handled them:

**Handling 'Country' Missing Values**
We found some missing values in the 'country' column (about 0.41% of the total data). Since this is a small percentage, we decided to drop those rows.
**Handling 'Agent' Missing Values**
The 'agent' column also had missing values. Since this column is crucial, we filled the missing values with '0', representing clients who didn't use an agent.
**Handling 'Company' Missing Values**
The 'company' column had a high percentage (94.43%) of missing values, so we decided to drop the entire column.
**Handling 'Children' Missing Values**
The 'children' column had a small number (4) of missing values. We filled these with the median value.
**Checking for Duplicates**
We checked for duplicate records in our dataset and found none.
**Checking for Placeholders**
We looked for and removed placeholders in our categorical columns to improve code readability.
**Removing Whitespace**
We ensured that there were no leading or trailing whitespaces in any of our columns.
**Handling Outliers**
We identified outliers in the 'lead_time' and 'adr' columns. However, we chose not to remove them as they could contain important information for predicting hotel cancellations.
Our data is now cleaned and ready for analysis.

## 5. EDA
### Univariate Analysis Results
#### 1. Repeated Guests
- **Observation:** The count of repeated guests is low, indicating a higher influx of new guests.
- **Insight:** Hotels should focus on retaining and attracting repeated guests, potentially through loyalty programs.

#### 2. Reservation Status
- **Observation:** Check-out guests have the highest count, while no-shows have the lowest.
- **Insight:** Guests who complete their stays contribute significantly to revenue, while no-shows should be addressed to minimize revenue loss.

#### 3. Hotel Preference
- **Observation:** City hotels are more preferred than resort hotels.
- **Insight:** Factors like location, pricing, or service quality may influence guests' hotel preferences.

#### 4. Cancellation Overview
- **Observation:** Most guests did not cancel, indicating positive revenue trends.
- **Insight:** Understanding customer preferences and satisfaction contributes to a positive business outlook.

#### 5. Distribution Channel
- **Observation:** Travel/Tour Agents (TATO) have the highest count, while Undefined has the lowest.
- **Insight:** Guests prefer using travel companies for bookings, emphasizing the significance of partnerships with travel agencies.

### Bivariate Analysis

#### 1. Market Segment vs. Cancellation
- **Observation:** Online bookings (TA) show higher cancellation counts compared to offline bookings.
- **Insight:** Remote cancellation options lead to higher online cancellations, highlighting the importance of streamlined online cancellation processes.

#### 2. Customer Type vs. Cancellation
- **Observation:** Transient customer types are more likely to cancel or not cancel.
- **Insight:** Focusing on service quality for transient guests may enhance overall satisfaction.

#### 3. Hotel Type vs. Cancellation
- **Observation:** City hotels experience more cancellations than resort hotels.
- **Insight:** City hotels should analyze factors contributing to cancellations and implement strategies for improvement.

### Multivariate Analysis 

#### 1. Market Segment, Previous Bookings, and Cancellations
- **Observation:** Loyalty patterns vary among market segments, offering insights into consistent customer behavior.
- **Insight:** Tailoring strategies for each market segment enhances loyalty and operational efficiency.

#### 2. Hotel Type, Weekend Nights, and Week Nights
- **Observation:** City hotels have concentrated weekend stays, while resort hotels show a more balanced distribution.
- **Insight:** Operational planning and targeted marketing can be optimized based on these patterns for enhanced guest satisfaction and efficiency.

## 6. Data Preprocessing
6.1 Correlation Analysis
We started by examining the correlation between numerical columns. A heatmap was created to visualize the correlation matrix. Notably, a correlation coefficient of 0.54 indicated a moderate positive correlation between 'arrival_date_year' and 'arrival_date_week_number.' To enhance model stability and interpretability, we retained only 'arrival_date_week_number.' Additionally, columns like 'name,' 'email,' 'phone-number,' and 'credit_card' were dropped due to privacy concerns and to reduce dimensionality and computational complexity.

6.2 Creating 'total_guest' Column
We introduced a new feature, 'total_guests,' which represents the sum of 'adults,' 'children,' and 'babies.' This consolidation simplifies the representation of the number of guests.

6.3 Binary Features for Special Requests
Considering that over 50% of the dataset had no special requests, we created a binary feature, 'has_special_requests,' to represent whether any special requests were made by guests. This not only reduces computational complexity but also retains essential information about guest preferences.

6.4 Lead Time Histogram
A histogram of 'lead_time' was generated to visualize the distribution. Wider bins were used to accommodate the positively skewed distribution. Subsequently, we categorized lead times into five groups for better analysis.

6.5 Binary Feature for Room Types
A binary feature, 'reserved_is_assigned,' was introduced to indicate whether the assigned room type matched the reserved room type.

6.6 Creating a Single DateTime Column
Columns related to arrival date were combined into a single datetime column to simplify date-related operations.

6.7 'cancelations_rate' Feature
We calculated the 'cancelations_rate' by considering the ratio of previous cancellations to total bookings. The original columns were then dropped.

6.8 Handling DateTime Columns
Columns like 'reservation_status_date,' 'arrival_date,' and 'reservation_status' were dropped as they were no longer needed.

6.9 One-Hot Encoding
Categorical columns were one-hot encoded to convert them into a format suitable for machine learning models.

6.10 Train-Test Split and Class Imbalance
The dataset was split into training and testing sets after scaling the features. To address class imbalance, the Synthetic Minority Over-sampling Technique (SMOTE) was employed on the training dataset, resulting in an equal distribution of canceled and non-canceled bookings.

- The dataset was extensively processed and transformed, resulting in a structured and balanced dataset ready for further analysis and model training. The preprocessing steps aimed to enhance the dataset's quality, reduce dimensionality, and address class imbalance, setting the stage for effective machine learning model development.

## 7. Data Modelling
**Model Training and Evaluation:**
Trained and evaluated multiple classification models, including Logistic Regression, Decision Trees, Random Forest, Gradient Boosting, Support Vector Machines (SVM), and Neural Networks.
Used common evaluation metrics such as accuracy, precision, recall, and F1 score.
**Hyperparameter Tuning:**
Applied hyperparameter tuning using techniques like GridSearchCV and RandomizedSearchCV to optimize model performance.

Model Results:
**Logistic Regression:**
Achieved an accuracy of approximately 82.03%.
Utilized a classification report to provide detailed insights into precision, recall, and F1 score for both classes (Class 0 and Class 1).
Employed ROC curves to visualize the model's performance.
**Decision Trees:**
Initially trained a Decision Tree model and evaluated its performance metrics.
Conducted hyperparameter tuning using GridSearchCV to optimize the Decision Tree model.
Achieved an accuracy of 92% on the training data and 84% on the test data.
**Random Forest:**
Created a Random Forest Classifier with 100 trees .
Generated a confusion matrix and visualized it as a heatmap.
Provided accuracy scores for both classes (Not Cancelled and Cancelled).
**Gradient Boosting:**
Implemented a Gradient Boosting Classifier using the Pipeline module.
Conducted cross-validation to evaluate the model's performance on training and test datasets.
Utilized RandomizedSearchCV for hyperparameter tuning and identified the best parameter combination.
Displayed training and testing metrics, including accuracy, F1 score, precision, and recall.
**SVM (Support Vector Machines):**
Trained an SVM model with a linear kernel and evaluated its performance.
Applied SMOTE for oversampling to address class imbalance.
Utilized cross-validation to assess the model's generalization performance.
**Neural Networks:**
Implemented a neural network with three layers (input, hidden, and output).
Compiled the model using binary crossentropy loss and Adam optimizer.
Trained the neural network for 20 epochs and displayed training loss.
Achieved an accuracy of 84% on the test data.
**Model Storage:**
Saved the trained Logistic Regression model to a file (logistic_regression_model.pkl).
Saved the trained Random Forest model to a file (random_forest_model.pkl).
Saved the trained Gradient Boosting model to a file (gradient_boost_model.pkl).
Saved the trained Neural Network model to a file (keras_model.h5).

## 8. Evaluation
**Chosen Metric: Accuracy**
We opted for accuracy as our primary evaluation metric due to its stability and simplicity. Accuracy represents the overall correctness of the model's predictions.

**Top 3 Performing Models**:
**Gradient Boosting Model:**
Achieved high accuracy on both training and testing data.
Robust performance in terms of precision, recall, and F1-score.
Demonstrated effectiveness in handling the classification task.

**Random Forest Model:**
Showcased strong accuracy with reliable performance on the test set.
Interpretable confusion matrix highlighted good classification results.
Provides a balance between simplicity and effectiveness.

**Neural Networks Model:**
Utilized a deep learning approach for complex patterns.
Demonstrated competitive accuracy, precision, recall, and F1-score.
Leverages the power of neural networks for intricate relationships.

**Model Selection Rationale:**
The decision to choose these three models is based on their consistent and high accuracy across various evaluation metrics. The Gradient Boosting model excels in capturing complex relationships, the Random Forest model provides robust results with simplicity, and the Neural Networks model leverages deep learning capabilities.

**Future Considerations:**
Further optimization and fine-tuning may be explored, and ensemble methods could be considered for combining the strengths of multiple models. Regular monitoring and updates to the models should be conducted to ensure performance remains effective over time.

Users can refer to this README for quick insights into the success of the models in addressing the classification task.
## 9. Conclusions
1. **Customer Retention:**
   - Guests who have visited the hotel are not returning.

2. **Cancellations in City Hotel:**
   - City hotels experience higher cancellation rates.

3. **Improving Guest Experience:**
   - Focus on understanding the reasons for guest checkouts and cancellations.

4. **Meal Preferences:**
   - Guests prefer Bed and Breakfast (BB) over Full Board (FB).

5. **Booking Channels:**
   - Guests prefer using Travel/Tour Agents (TATO) for bookings.

6. **Traffic Analysis:**
   - Both City and Resort hotels receive high traffic during weekends. Resort hotels have higher traffic during weekdays.

7. **Online Travel Agent vs. Offline TA:**
   - Online travel agents have a larger clientele but also experience higher cancellations.
   - 
## 10. Recommendations
## Recommendations

1. **Rewarding Repeat Guests:**
   - Implement a rewards program for repeat guests to foster loyalty.
   - Offer special packages, discounts, or exclusive perks to encourage repeat bookings.
2. **Staff Training:**
   - Invest in comprehensive training for staff to enhance guest experience.
   - Focus on customer service, conflict resolution, and personalized interactions.
3. **Diverse Advertising:**
   - Utilize a multi-channel advertising strategy, including social media, billboards, and television.
   - Increase visibility and attract a diverse audience through targeted marketing.
4. **Web Application for Direct Bookings:**
   - Develop a user-friendly web application for guests to book and inquire directly.
   - Streamline the booking process to enhance convenience for potential guests.
5. **Seasonal Discounts:**
   - Introduce discounts during specific times of the year to boost bookings.
   - Capitalize on seasonal trends and offer attractive promotions.
6. **Partnerships with AgentCompanies:**
   - Establish partnerships with companies to attract clients through their agents.
   - Leverage corporate relationships to drive business and increase occupancy.
7. **Enhancements to Facilities:**
   - Improve the hotel's aesthetic appeal by adding plants and art.
   - Increase floor space to alleviate congestion and create a more spacious environment.
     
Implementation of these strategies can contribute to the long-term success and growth of the hotel.
