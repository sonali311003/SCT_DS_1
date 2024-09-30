import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
file_path = r"C:\Users\sonali gupta31102003\Downloads\API_SP.POP.TOTL_DS2_en_csv_v2_3401680\API_SP.POP.TOTL_DS2_en_csv_v2_3401680.csv"
data = pd.read_csv(file_path, skiprows=4)
# Display the first few rows and columns for inspection
print(data.head())
print(data.columns)

#Histogram for Population Distribution in 2023
population_2023 = data['2023'].dropna()

# Plotting the histogram
plt.figure(figsize=(10, 6))
plt.hist(population_2023, bins=20, color='brown', edgecolor='black')
plt.title('Population Distribution Across Countries in 2023')
plt.xlabel('Population')
plt.ylabel('Number of Countries')
plt.tight_layout()
plt.show()

#Average Population by Year
years = [str(year) for year in range(1999, 2023)]

#mean population by year
if all(year in data.columns for year in years):
    mean_population_by_year = data[years].mean()

    # Plotting the bar chart
    plt.figure(figsize=(12, 6))
    sns.barplot(x=mean_population_by_year.index, y=mean_population_by_year.values, palette="husl")
    plt.title('Average Population by Year (1999-2023)')
    plt.xlabel('Year')
    plt.ylabel('Average Population')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

#Population Distribution by Age (or any other variable)
age_data = {'Age Group': ['0-20', '21-64', '65+'],
            'Population (Million)': [512, 807, 98]}

age_df = pd.DataFrame(age_data)

plt.figure(figsize=(10, 6))
sns.barplot(x='Age Group', y='Population (Million)', data=age_df, palette="muted")
plt.title("Population Distribution by Age in 2022")
plt.xlabel('Age Group')
plt.ylabel('Population (Million)')
plt.tight_layout()
plt.show()


