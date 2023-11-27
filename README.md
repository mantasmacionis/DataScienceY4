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
  - [Tools/Techniques](#tools-and-techniques)
  - [Technologies](#technologies)
  - [Personal/College Projects](#personalcollege-projects)  
  - [Professional Projects](#professional-projects)
- [Opportunities & Challenges](#opportunities-and-challenges)

## Introduction
4th Year software development student working on developing skills related to AI, machine learning, and Data Science.

## Background
This portfolio will present technologies and tools which I am familiar with and what I am currently working on learning. To showcase areas which I am best suited for in a professional project development environment.

## Content

### Data Sets
- [Loan Default Dataset](https://www.kaggle.com/datasets/nikhil1e9/loan-default)
- [Example Data Set2](#)

### Tools/Techniques
- [Tool/Technique 1](#)
- [Tool/Technique 2](#)

### Technologies
- Programming: Python, Jupyter Notebooks
- Data Manipulation: Pandas, MatPlotlib, Seaborn
- Machine Learning: sklearn, SMOTE

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

Below is the df.isna() command being utilised to confirm that the database contains no Null or void values
<img src=https://github.com/mantasmacionis/DataScienceY4/blob/main/AdvancedPortfolioDraft/nullorvoidcheck.png alt="df.isna()" width="800" height="300"/>
Below is the df.dropduplicates() command being used to drop any duplicate rows(Dataset remains the same as there are no duplicates)
<img src=https://github.com/mantasmacionis/DataScienceY4/blob/main/AdvancedPortfolioDraft/dropduplicates.png alt="df.dropduplicates()" width="800" height="300"/>
After doing this basic preprocessing, the dataset needed to be balanced, the main factor in this dataset is whether or not a loan was defaulted on
(0 is non defaulted 1 is defaulted) The initial imbalance is represented in this bar chart diagram
<img src=https://github.com/mantasmacionis/DataScienceY4/blob/main/AdvancedPortfolioDraft/initialimbalance.png alt="initialimbalance" width="800" height="350"/>
SMOTE was chosen to create synthetic data which would have a default value of 1(defaulted on a loan), SMOTE works on numerical values only so a conversion was done to temporarily turn certain columns into number classificiation.

  Below is a sample image of the main columns which contain String data before conversion to numbers
<img src=https://github.com/mantasmacionis/DataScienceY4/blob/main/AdvancedPortfolioDraft/beforenumerical.png alt="beforenumerical" width="900" height="300"/>  
  Below is a sample image of the main columns which contain String data after conversion to numbers
<img src=https://github.com/mantasmacionis/DataScienceY4/blob/main/AdvancedPortfolioDraft/afternumerical.png alt="afternumerical" width="900" height="225"/>

  After SMOTE was applied to the dataset, columns were set back to their original wording.
  <img src=https://github.com/mantasmacionis/DataScienceY4/blob/main/AdvancedPortfolioDraft/SMOTEtail.png alt="SMOTEtail" width="900" height="225"/>




## Data Visualizations
  
This section includes visualisations created after the dataset has been balanced by using SMOTE.
Age Distribution of individuals included in the dataset
<img src=https://github.com/mantasmacionis/DataScienceY4/blob/main/AdvancedPortfolioDraft/agedistribution.png alt="agedistribution" width="900" height="350"/>

Income Box Plot for the dataset
<img src=https://github.com/mantasmacionis/DataScienceY4/blob/main/AdvancedPortfolioDraft/incomeboxplot.png alt="incomeboxplot" width="900" height="350"/>

Education Level Bar Chart
<img src=https://github.com/mantasmacionis/DataScienceY4/blob/main/AdvancedPortfolioDraft/educationlevelbarchart.png alt="educationlevelbarchart" width="900" height="350"/>

Average loan size taken by defaulters versus non defaulters
<img src=https://github.com/mantasmacionis/DataScienceY4/blob/main/AdvancedPortfolioDraft/loanamountstaken.png alt="loanamountstaken" width="900" height="350"/>

Education level of Non-Defaulters 
<img src=https://github.com/mantasmacionis/DataScienceY4/blob/main/AdvancedPortfolioDraft/nondefaulteducation.png alt="nondefaulteducation" width="900" height="350"/>

Education level of Defaulters 
<img src=https://github.com/mantasmacionis/DataScienceY4/blob/main/AdvancedPortfolioDraft/defaulteducation.png alt="defaulteducation" width="900" height="350"/>




## Exploratory Data Analysis

Using a machine learning model on the dataset - stats after application shown below 
<img src=https://github.com/mantasmacionis/DataScienceY4/blob/main/AdvancedPortfolioDraft/mlstatistics.png alt="mlstatistics" width="900" height="350"/>

ML generated stats put into a barchart, to predict the numerical columns which are the largest factors in default probability
<img src=https://github.com/mantasmacionis/DataScienceY4/blob/main/AdvancedPortfolioDraft/factorbarchart.png alt="factorbarchart" width="900" height="350"/>

Averages for the whole dataset - after SMOTE has been applied
<img src=https://github.com/mantasmacionis/DataScienceY4/blob/main/AdvancedPortfolioDraft/datasetaverages.png alt="datasetaverages" width="900" height="450"/>

- **Sources**
  - Kaggle Dataset used: https://www.kaggle.com/datasets/nikhil1e9/loan-default
  
  
  
- **Tools & Techniques**
  The main tools & Techniques utilised in this project include:
  
  [Jupyter notebooks](https://jupyter.org/) - used to create functionality
  
  <a href="https://jupyter.org/" target="_blank">Jupyter notebooks</a> - used to create functionality

  [Jupyter notebooks](https://jupyter.org/)(:onclick="window.open(this.href, '_blank'); return false;")
  
  Pandas Library - used for data pre processing and for chart creation
  
  sklearn - used for the Machine Learning algorithm applied to the dataset
  
  MatPlotLib - used for visualizations
  
  SMOTE - used for balancing of the dataset
  

### Professional Projects
- [Project1](#)

## Opportunities & Challenges
The opportunities and challenges which I have encountered during my time learning and using technologies I am now familiar with, how my experiences have affected my learning trajectory/growth, and understanding of different topics.
