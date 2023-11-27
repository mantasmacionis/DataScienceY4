# Mantas Macionis - Data Science Portfolio

## Personal Info
- Software Development BSc
- Email: [C00242178@setu.ie](mailto:C00242178@setu.ie)
- GitHub: [github.com/mantasmacionis](https://github.com/mantasmacionis)

## Table of Contents
- [Introduction](#introduction)
- [Background](#background)
- [Content](#content)
  - [Data Sets](#data-sets)
  - [Technologies](#technologies)
  - [Personal/College Projects](#personalcollege-projects)  
  - [Professional Projects](#professional-projects)
- [Opportunities & Challenges](#opportunities-and-challenges)

## Introduction
The primary objective of this portfolio is to offer a comprehensive showcase of my proficiency in the field of Data Science & Machine Learning. Through a selection of projects, my aim is to demonstrate my experience with tools and technologies used in this field. Each project has been a valuable learning opportunity and has given me insight into the scenarios in which Data Science & Machine learning can be applicable. 

## Background
I am a 4th Year software development student, looking to grow my skills related to the fields of Data Science & Machine learning. This portfolio will feature demonstrations of my projects which show first hand experience in key topics such as Data pre processing , Data Visualisations, Feature engineering and Exploratory data analysis. Below this section are the datasets, technologies and projects I have worked on.     

## Content

### Data Sets
- [Loan Default Dataset](https://www.kaggle.com/datasets/nikhil1e9/loan-default)

### Technologies
- Programming: [Python](https://www.python.org/), [Jupyter Notebooks](https://jupyter.org/)
- Data Manipulation: [Pandas](https://pandas.pydata.org/), [MatPlotlib](https://matplotlib.org/), [Seaborn](https://seaborn.pydata.org/)
- Machine Learning: [sklearn](https://scikit-learn.org/stable/), [SMOTE](https://imbalanced-learn.org/stable/over_sampling.html)

### Personal/College Projects
#### Project 1 - Loan Default dataset
- **Data Sources** - [KaggleDataset](https://www.kaggle.com/datasets/nikhil1e9/loan-default) , this is a high quality dataset from kaggle, featuring approx 250k rows. It contains info about customers and whether they defaulted on their loans or not. This data has a 10.0 usability score on Kaggle. Meaning it is well presented and will likely need minimal Preprocessing
  
**Dataset Details:**
1. Age: Age of the Individual
2. Income: The individuals yearly income($)
3. LoanAmount: The size of the loan the individual has gotten($)
4. CreditScore: credit score of the individual
5. MonthsEmployed: The number of months the individual has been consistently employed
6. NumCreditLines: The amount of credit lines an individual has available
7. InterestRate: The interest rate given to the individual on their loan(%)
8. LoanTerm: Length of the loan(months)
9. DTIRatio: Debt to income ratio of this individual
10. Education: The highest level of education this individual has achieved(PhD,Master's,Bacherlor's,High School)
11. EmploymentType: The employment category which best suits this individual(Full-Time,Part-Time,Self-Employed,Unemployed)
12. MaritalStatus: Marital status of the individual(Single,Married,Divorced)
13. HasMortgage: Whether the individual has a mortgage (yes/no)
14. HasDependants: Whether the individual has dependants or not(yes/no)
15. LoanPurpose: Reason the loan is being taken(Home,Auto,Business,Education or other)
16. HasCoSigner: Whether the individual has a cosigner(yes/no)
17. Default: Whether the individual has defaulted on their loan(0-no/1-yes)
  
## Data Preprocessing 
- The following section covers pre processing the data to prepare it for future sections, which will include data visualisations and exploratory data analysis.
- Upon initial inspection this dataset appeared to be high quality with no obvious issues such as missing data or odd variables. 
- To confirm whether the data needed pre processing the panda's library was utilised.
- The data was checked for key aspects such as Null or void values and duplicate values. 

Below are the first five rows of the dataset, giving a quick preview and showing their initial state before any changes are made.
<img src=https://github.com/mantasmacionis/DataScienceY4/blob/main/AdvancedPortfolioDraft/initialhead.png alt="df.headinitial" width="900" height="225"/>

Below are the last five rows of the dataset, showing the total size of the dataset and final figures.
<img src=https://github.com/mantasmacionis/DataScienceY4/blob/main/AdvancedPortfolioDraft/initialtail.png alt="df.tailinitial" width="900" height="225"/>

Below is the df.isna() command being utilised to confirm that the database contains no Null or void values
<img src=https://github.com/mantasmacionis/DataScienceY4/blob/main/AdvancedPortfolioDraft/nullorvoidcheck.png alt="df.isna()" width="800" height="300"/>

Below is the df.dropduplicates() command being used to drop any duplicate rows(Dataset remains the same as there are no duplicates)
<img src=https://github.com/mantasmacionis/DataScienceY4/blob/main/AdvancedPortfolioDraft/dropduplicates.png alt="df.dropduplicates()" width="800" height="300"/>


### Feature Engineering
- The following section will cover the process of transforming the data, By balancing the dataset.
- This will allow for more representative data visualisations.
- Data balancing is also crucial for the last topic covered in this project - exploratory data analysis, using a machine learning algorithm.

After the dataset was checked for Null/void values and duplicate values. The dataset needed to be balanced. 
The initial imbalance is represented in the diagram below.
0 represents a non default, 1 represents a default.
<img src=https://github.com/mantasmacionis/DataScienceY4/blob/main/AdvancedPortfolioDraft/initialimbalance.png alt="initialimbalance" width="800" height="350"/>

- SMOTE was chosen to create synthetic data which would have a default value of 1(defaulted on a loan), SMOTE works on numerical values only so a conversion was done to temporarily turn certain columns into number classificiation.

  Below is a sample image of the main columns which contain String data before conversion to numbers
<img src=https://github.com/mantasmacionis/DataScienceY4/blob/main/AdvancedPortfolioDraft/beforenumerical.png alt="beforenumerical" width="900" height="300"/> 

  Below is a sample image of the main columns which contain String data after conversion to numbers
<img src=https://github.com/mantasmacionis/DataScienceY4/blob/main/AdvancedPortfolioDraft/afternumerical.png alt="afternumerical" width="900" height="225"/>

  After SMOTE was applied to the dataset, columns were set back to their original wording.
  <img src=https://github.com/mantasmacionis/DataScienceY4/blob/main/AdvancedPortfolioDraft/SMOTEtail.png alt="SMOTEtail" width="900" height="225"/>




## Data Visualizations
  
- The following section covers data visualisations, visualisations created are done after the dataset has been balanced
- Different visualisation styles such as box plots and bar charts are utilised.
  
Age Distribution of individuals included in the dataset
<img src=https://github.com/mantasmacionis/DataScienceY4/blob/main/AdvancedPortfolioDraft/agedistribution.png alt="agedistribution" width="900" height="350"/>

Income Box Plot for the dataset
<img src=https://github.com/mantasmacionis/DataScienceY4/blob/main/AdvancedPortfolioDraft/incomeboxplot.png alt="incomeboxplot" width="900" height="350"/>

Education Level Bar Chart
<img src=https://github.com/mantasmacionis/DataScienceY4/blob/main/AdvancedPortfolioDraft/educationlevelbarchart.png alt="educationlevelbarchart" width="900" height="350"/>

Heatmap of Age vs Default
<img src=https://github.com/mantasmacionis/DataScienceY4/blob/main/AdvancedPortfolioDraft/heatmapdefaultage.png alt="heatmapdefaultage" width="900" height="400"/>

Average loan size taken by defaulters versus non defaulters
<img src=https://github.com/mantasmacionis/DataScienceY4/blob/main/AdvancedPortfolioDraft/loanamountstaken.png alt="loanamountstaken" width="900" height="350"/>

Education level of Non-Defaulters 
<img src=https://github.com/mantasmacionis/DataScienceY4/blob/main/AdvancedPortfolioDraft/nondefaulteducation.png alt="nondefaulteducation" width="900" height="350"/>

Education level of Defaulters 
<img src=https://github.com/mantasmacionis/DataScienceY4/blob/main/AdvancedPortfolioDraft/defaulteducation.png alt="defaulteducation" width="900" height="350"/>




## Exploratory Data Analysis
- The following section will cover Machine learning and statistics for the final balanced dataset.
- The sklearn library was utilised for the representations below and the model chosen was the Random Forest Classifier

After applying the RandomForestClassifier model to the dataset, the following stats were generated. 
<img src=https://github.com/mantasmacionis/DataScienceY4/blob/main/AdvancedPortfolioDraft/mlstatistics.png alt="mlstatistics" width="900" height="350"/>

Below is an example of the representations which can be created after the model has been used. The diagram is a barchart which visualises a prediction on the numerical columns which are the largest factors in default probability
<img src=https://github.com/mantasmacionis/DataScienceY4/blob/main/AdvancedPortfolioDraft/factorbarchart.png alt="factorbarchart" width="900" height="350"/>

Averages for the whole dataset - after SMOTE has been applied
<img src=https://github.com/mantasmacionis/DataScienceY4/blob/main/AdvancedPortfolioDraft/datasetaverages.png alt="datasetaverages" width="900" height="450"/>

- **Sources**
  - Kaggle Dataset used: https://www.kaggle.com/datasets/nikhil1e9/loan-default
  
  
  
- **Tools & Techniques**
  The main tools & Techniques utilised in this project include:
  
  [Jupyter notebooks](https://jupyter.org/) - used to create functionality
  
  [Pandas Library](https://pandas.pydata.org/) - used for data pre processing and for chart creation
  
  [sklearn](https://scikit-learn.org/stable/) - used for the Machine Learning algorithm applied to the dataset
  
  [MatPlotLib](https://matplotlib.org/) - used for visualizations
  
  [SMOTE](https://imbalanced-learn.org/stable/over_sampling.html) - used for balancing of the dataset

### Project 2 - Random Forests
- **Data Sources** - [JupyterNotebook](https://github.com/jakevdp/PythonDataScienceHandbook/blob/master/notebooks/05.08-Random-Forests.ipynb) , This project is based on the linked Jupyter notebook.

**Notebook Details:**
- This notebook features a walkthrough on Decision Trees and random forests.
- Decision tree topics include: The creation of a Decision tree, Overfitting visualisations.
- Random Forest tree topics include: Bagging classifiers, Random Forest Regression, Classifying digits with random forest and the confusion matrix.

#### Preparation 
- to get this project running, the initial import statement must be changed to specify which version of the seaborn whitegrid will be used.

Below is the import edit I made.
<img src=https://github.com/mantasmacionis/DataScienceY4/blob/main/AdvancedPortfolioDraft/torun.png alt="torun" width="900" height="225"/>

A helper file named helper05_08 must be downloaded for later code to display.
<img src=https://github.com/mantasmacionis/DataScienceY4/blob/main/AdvancedPortfolioDraft/helper.png alt="helper" width="900" height="175"/>


### Professional Projects
- [Project1](#)

## Opportunities & Challenges
The opportunities and challenges which I have encountered during my time learning and using technologies I am now familiar with, how my experiences have affected my learning trajectory/growth, and understanding of different topics.
