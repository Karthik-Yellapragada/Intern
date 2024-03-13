from pymongo import MongoClient

# Connect to MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client["India_Population"]
collection = db["data"]

# Sample weather data (replace this with actual weather data)
population_data = [
{"State": "MAHARASHTRA", "Population": 37722136, "Male":19961736 , "Female": 17760400},
{"State": "UTTAR PRADESH", "Population": 25302925 , "Male": 13433369, "Female":11869556 },
{"State": "ANDHRA PRADESH", "Population": 18171615, "Male": 9192368, "Female":8979247 },
{"State": "MAHARASHTRA", "Population": 37722136, "Male":19961736 , "Female": 17760400},
{"State": "WEST BENGAL", "Population": 18063509, "Male":9357777 , "Female": 8705732},
{"State": "GUJARAT", "Population": 17835049, "Male":9541688 , "Female": 8293361},
{"State": "KARNATAKA", "Population": 15799896, "Male":8112840 , "Female": 7687056},
{"State": "TAMIL NADU", "Population": 13879395, "Male":6957261 , "Female": 6922134},
{"State": "DELHI", "Population": 13481997, "Male":7201322 , "Female": 6280675},
{"State": "MADHYA PRADESH", "Population": 11023091, "Male":5761143 , "Female": 5261948},
{"State": "RAJASTHAN", "Population": 10443016, "Male":5484470 , "Female": 4958546},
]

# Insert weather data into MongoDB
collection.insert_many(population_data)

print("Weather data inserted successfully.")
