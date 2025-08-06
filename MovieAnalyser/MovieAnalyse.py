import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv(r'C:\Users\tanvi\OneDrive\Desktop\Python\MovieAnalyser\Movie.csv')

genre_counts = df['genres'].value_counts().head(10)
print(df.head())
print(df.columns)
# Plotting the pie chart
plt.figure(figsize=(8, 8)) 
plt.pie(genre_counts, labels=genre_counts.index, autopct='%1.1f%%', startangle=140)
plt.title('Movie Genre Distribution')
plt.axis('equal')  # Equal aspect ratio to make it a circle
plt.show()
year_counts = df['year'].value_counts().head(10)
plt.bar(year_counts.index, year_counts.values  )
plt.xlabel('Year')
plt.ylabel('Number of Movies')  
plt.title('Number of Movies per Year')
plt.show()
plt.scatter(df['name'].head(5),df['rating'].head(5))
plt.xlabel('Movie Name')        
plt.ylabel('Rating')
plt.title('Movie Ratings')
plt.show()