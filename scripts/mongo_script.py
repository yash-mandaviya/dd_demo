from pymongo import MongoClient
import csv

# Connect to the MongoDB instance
connection_string = "mongodb://127.0.0.1:27017/?directConnection=true"
client = MongoClient(connection_string)

# Create or access the database named 'Data-Dynamos-DB'
db_name = 'Data-Dynamos-DB'
db = client[db_name]

# Create or access the collection for income levels by education
collection_name_1 = 'income_levels_by_education_collection'
income_levels_by_education_collection = db[collection_name_1]

# Create or access the collection for employment forecast
collection_name_2 = 'employment_forecast_collection'
employment_forecast_collection = db[collection_name_2]

# Create or access the collection for geographic education distribution
collection_name_3 = 'geographic_education_distribution_collection'
geographic_education_distribution_collection = db[collection_name_3]

# Import data from the 'dd_m1_income_levels_by_education.csv' file into the income_levels_by_education_collection
with open('content/dd_m1_income_levels_by_education.csv', 'r') as file:
    csv_data = csv.reader(file)
    next(csv_data)  # Skip the header row
    for row in csv_data:
        data = {
            'year': row[0],
            'region': row[1],
            'type of work': row[2],
            'level of education': row[4],
            'age group': row[5],
            'both sex combined' : row[6],
            'male' : row[7],
            'female' : row[8],
        }
        income_levels_by_education_collection.insert_one(data)

# Retrieve and display all data from the income_levels_by_education_collection
print("Data from income_levels_by_education collection:\n")
for data in income_levels_by_education_collection.find():
    print(data)

# Import data from the 'dd_m3_geographic_education_distribution.csv' file into the geographic_education_distribution_collection
with open('content/dd_m3_geographic_education_distribution.csv', 'r') as file:
    csv_data = csv.reader(file)
    next(csv_data)  # Skip the header row
    for row in csv_data:
        data = {
            'region': row[0],
            'education_level': row[1],
            'enrollment': row[2],
            'graduation': row[3]
        }
        geographic_education_distribution_collection.insert_one(data)

# Retrieve and display all data from the geographic_education_distribution_collection
print("Data from geographic_education_distribution collection:\n")
for data in geographic_education_distribution_collection.find():
    print(data)

# Close the MongoDB connection
client.close()