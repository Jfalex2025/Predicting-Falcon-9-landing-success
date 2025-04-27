Project Name: SpaceX Falcon 9 First Stage Landing Prediction

Project Overview
In this capstone project, the goal was to predict whether the Falcon 9 first stage would successfully land using advanced machine learning models. SpaceX revolutionizes the space industry by reducing launch costs to $62 million compared to competitors charging upwards of $165 million. This significant cost advantage is due to SpaceX’s ability to reuse the Falcon 9’s first stage. By predicting the likelihood of a successful landing, we can better assess launch costs, gain operational insights, and support competitive pricing for potential market contenders.

Learning Objectives

By completing this project, you have developed expertise in:
•	Data Manipulation: Writing Python code to transform and handle complex data using Pandas.
•	Data Conversion: Transforming JSON structures into Pandas DataFrames.
•	Data Collection: Using RESTful APIs and web scraping techniques to gather comprehensive data.
•	Exploratory Data Analysis (EDA): Gleaning insights through scatter plots, bar charts, and SQL queries.
•	Data Visualization: Building interactive dashboards and maps with tools like Plotly Dash and Folium.
•	Machine Learning: Training classification models such as Logistic Regression, SVM, and Decision Trees to predict landing success.

Project Structure
1. Data Collection and Preparation
•	Objective: Collect data via SpaceX’s RESTful API and Wikipedia web scraping.
•	Techniques: 
o	Used requests for API calls and BeautifulSoup for extracting HTML tables.
o	Performed data cleaning and formatting with Pandas to prepare for analysis.

2. Exploratory Data Analysis (EDA)
•	Objective: Identify trends and relationships in the dataset.
•	Techniques: 
o	Created visualizations like scatter plots and bar charts.
o	Conducted SQL queries to filter, sort, and group data for valuable insights.

3. Data Visualization
•	Objective: Deliver insights interactively using dashboards and maps.
•	Activities: 
o	Built dashboards using Plotly Dash to allow users to explore launch data dynamically.
o	Visualized launch site distributions and proximity using Folium maps.

4. Machine Learning Model Development
•	Objective: Train and evaluate predictive models to classify landing success.
•	Techniques: 
o	Applied Logistic Regression, SVM, Decision Trees, and hyperparameter optimization.
o	Split data into training and testing subsets for evaluation.

Dataset Details
The dataset includes key metrics for Falcon 9 launches:
•	Flight Number
•	Launch Site
•	Class (Success/Failure)
•	Payload Mass (kg)
•	Booster Version and Category

Data Sources:
•	SpaceX’s API provided historical launch data.
•	Web scraping ensured additional details from Wikipedia.

Files and Directories
•	Data Collection: 
o	01_spacex-data-collection-api.ipynb: SpaceX API data retrieval.
o	02_spacex-web-scraping.ipynb: Parsing Wikipedia tables for additional data.
•	Data Wrangling: 
o	03_spacex_data_wrangling.ipynb: Cleaning and preparing datasets.
•	EDA and SQL: 
o	04_spacex-eda-sql-sqllite.ipynb: SQL queries for detailed insights.
o	05_spacex-eda-dataviz-v2.ipynb: Visualizing data relationships with Pandas and Matplotlib.
•	Geographical Analysis: 
o	06_launch-site-location.ipynb: Mapping launch site proximities with Folium.
•	Interactive Dashboards: 
o	07_spacex-dashboard.ipynb: Building dashboards for real-time insights.
•	Machine Learning Models: 
o	08_spacex-machine-learning-prediction.ipynb: Training and evaluating predictive models.

Key Results
1.	EDA Insights: 
o	Found a strong correlation between payload mass and landing success.
o	Specific launch sites demonstrated significantly higher success rates.
2.	Predictive Analysis: 
o	Models achieved an average accuracy of 0.83, showing consistent performance.
o	Hyperparameter tuning improved recall but revealed no single dominant model.
3.	Interactive Visualization: 
o	Dashboards and maps allowed users to explore data dynamically.

Conclusion
This project highlights the transformative potential of data science in aerospace. By combining data collection, interactive analytics, and machine learning, we developed a robust pipeline to predict Falcon 9 first-stage landings. These predictions can enhance SpaceX’s operational strategies, improve pricing models, and reinforce its competitive edge in the commercial space industry.

Appendix
1.	Presentation: A PDF summarizing project objectives, methodologies, and findings is available. 
1.	Presentation: A PDF summarizing project objectives, methodologies, and findings is available. 
o	Filename: SpaceX_Falcon_9_Landing_Prediction_Presentation.pdf
2.	GitHub Repository: 
o	Jfalex2025/Predicting-Falcon-9-landing-success

