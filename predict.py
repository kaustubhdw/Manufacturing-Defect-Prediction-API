import requests

url = 'http://127.0.0.1:5000/predict'
input_data = {
    "ProductionVolume": 500,
    "ProductionCost": 12000,
    "SupplierQuality": 8,
    "DeliveryDelay": 2,
    "DefectRate": 0.03,
    "QualityScore": 95,
    "MaintenanceHours": 10,
    "DowntimePercentage": 1.5,
    "InventoryTurnover": 6,
    "StockoutRate": 0.02,
    "WorkerProductivity": 92,
    "SafetyIncidents": 1,
    "EnergyConsumption": 2000,
    "EnergyEfficiency": 85,
    "AdditiveProcessTime": 12,
    "AdditiveMaterialCost": 250
}

response = requests.post(url, json=input_data)

print(response.json())
