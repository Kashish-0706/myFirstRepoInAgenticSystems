import pandas as pd 
import plotly.express as px

# load data
data = pd.read_csv("https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv")
df = pd.DataFrame(data)

# overview dataset
print(df.head())
# checking null values and datatypes
print(df.info())
# check statistical summary
print(df.describe())

# checking distribution of petal length by species
fig1 = px.histogram(df, x="petal_length", color="species", nbins=30, title="frequency of petal length")
fig1.show()
# Insights: this histogram shows that setosa has shorter petal lengths compared to versicolor and virginica, which can help in distinguishing between the species.  


# checking distribution of sepal width by species to identify outliers
fig2 = px.box(df, x="species", y="sepal_width", color="species", title="sepal width box plot")
fig2.show()
# Insights: The Box plot reveals that setosa has a wider range of sepal widths than the other species. There is a visible outlier in the setosa sepal width which is lower than the average for this species.This information can be useful for understanding the variability within each species and identifying any unusual measurements.   

# checking relationship between petal length and petal width by species
fig3 = px.scatter(df, x="petal_length", y="petal_width", color="species", size="sepal_length", title="petal_length vs petal_width")
fig3.show()
# Insights: The Scatter plot shows a strong positive correlation between petal length and petal width, especially for versicolor and virginica. Setosa, has shorter petals and is clustered in the lower left corner of the plot. This indicates that petal length and width can be good indicators for distinguishing between the species.      

# checking correlation between numerical features
corr = df[["sepal_length", "sepal_width", "petal_length", "petal_width"]].corr()
fig4 = px.imshow(corr, text_auto=True, title="Correlation Heatmap")
fig4.show()
# Insights: The Heatmap reveals a strong positive correlation between petal length and petal width, while sepal width has a negative correlation with sepal length. This suggests that petal measurements are closely related, while sepal measurements may vary independently. Understanding these correlations can help in feature selection for predictive modeling. 
                   

