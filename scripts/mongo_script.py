from pymongo import MongoClient
import csv

# Connect to MongoDB
connection_string = "mongodb://127.0.0.1:27017/?directConnection=true"
client = MongoClient(connection_string)

# Create the database
db_name = 'Data-Dynamos-DB'
db = client[db_name]

# Create the income_levels_by_education collection
collection_name_1 = 'income_levels_by_education_collection'
income_levels_by_education_collection = db[collection_name_1]

# Create the employmentForecast collection
collection_name_2 = 'employment_forecast_collection'
employment_forecast_collection = db[collection_name_2]

# Create the geographic_education_distribution collection
collection_name_3 = 'geographic_education_distribution_collection'
geographic_education_distribution_collection = db[collection_name_3]

# Open the CSV file for income_levels_by_education_collection
with open('content/dd_m1_income_levels_by_education.csv', 'r') as file:
    # Read the CSV data
    csv_data = csv.reader(file)

    # Skip the header row
    next(csv_data)

    # Iterate over each row in the CSV data
    for row in csv_data:
        # Create a dictionary to store the data
        data = {
            'education_level': row[0],
            'wage_rate': row[1]
        }
        
        # Insert the data into the income_levels_by_education collection
        result = income_levels_by_education_collection.insert_one(data)

# Get all data from the income_levels_by_education collection
income_levels_by_education_collection_data = income_levels_by_education_collection.find()

print("Data from income_levels_by_education collection:\n")

# Iterate over each document in the income_levels_by_education collection
for data in income_levels_by_education_collection_data:
    # Print the data
    print(data)

# Open the CSV filec for geographic_education_distribution_collection
with open('content/dd_m3_geographic_education_distribution.csv', 'r') as file:
    # Read the CSV data
    csv_data = csv.reader(file)
    
    # Skip the header row
    next(csv_data)
    
    # Iterate over each row in the CSV data
    for row in csv_data:
        # Create a dictionary to store the data
        data = {
            'region': row[0],
            'education_level': row[1],
            'enrollment': row[2],
            'graduation': row[3]
        }
        
        # Insert the data into the geographic_education_distribution collection
        result = geographic_education_distribution_collection.insert_one(data)

# Get all data from the education collection
geographic_education_distribution_collection_data = geographic_education_distribution_collection.find()

print("Data from geographic_education_distribution collection:\n")

# Iterate over each document in the geographic_education_distribution collection
for data in geographic_education_distribution_collection_data:
    # Print the data
    print(data)

# Close the MongoDB connection
client.close()