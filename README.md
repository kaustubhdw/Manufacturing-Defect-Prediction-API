# Manufacturing-Defect-Prediction-API

## Overview
This Flask-based API allows users to upload a manufacturing dataset, train a logistic regression model to predict defect statuses, and make predictions for new manufacturing data inputs. It handles data scaling, model persistence, and provides endpoints for uploading data, training, and predictions.

---

## Features
1. **Upload Dataset**  
   Upload a CSV dataset for training and prediction.

2. **Train Model**  
   Train a logistic regression model on the uploaded data with `DefectStatus` as the target.

3. **Predict Defects**  
   Predict manufacturing defect statuses using input feature values and receive results with confidence scores.

---

## Endpoints

### 1. `/upload`
**Method**: POST  
**Description**: Upload a dataset for training.  
**Request Body**:  
- File (`multipart/form-data`): The CSV file containing the manufacturing dataset.

**Example Response**:  
```json
{
    "message": "File uploaded successfully.",
    "columns": ["Column1", "Column2", "Column3", ...]
}
```

### 2. `/train`
**Method**: POST  
**Description**: Train a logistic regression model using the uploaded dataset.  
**Example Response**:  
```json
{
    "message": "Model trained successfully.",
    "accuracy": 0.85,
    "f1_score": 0.88
}
```

### 3. `/predict`
**Method**: POST  
**Description**: Make predictions based on feature input.  
**Request Body**: JSON object containing feature names and their corresponding values.

**Example Input**:  
```json
{
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
```

**Example Response**:  
```json
{
    "Downtime": "Yes",
    "Confidence": 0.92
}
```

---

## Required Libraries
- Flask  
- pandas  
- numpy  
- scikit-learn  
- joblib  

Install dependencies using:  
```bash
pip install flask pandas numpy scikit-learn joblib
```

---

## Files

### 1. **`app.py`**
Main application file containing API logic.

### 2. **`upload_file.py`**
Script for uploading datasets using the `/upload` endpoint.

### 3. **`train_model.py`**
Script for invoking the `/train` endpoint to train the model.

### 4. **`predict.py`**
Script to send feature values to the `/predict` endpoint for predictions.

### 5. **Dataset**
The dataset must include the following columns:
- `ProductionVolume`  
- `ProductionCost`  
- `SupplierQuality`  
- `DeliveryDelay`  
- `DefectRate`  
- `QualityScore`  
- `MaintenanceHours`  
- `DowntimePercentage`  
- `InventoryTurnover`  
- `StockoutRate`  
- `WorkerProductivity`  
- `SafetyIncidents`  
- `EnergyConsumption`  
- `EnergyEfficiency`  
- `AdditiveProcessTime`  
- `AdditiveMaterialCost`  
- **Target Column**: `DefectStatus`

---

## Usage

### 1. Start the Flask API
Run `app.py`:  
```bash
python app.py
```

### 2. Upload Dataset
Run `upload_file.py`:  
```bash
python upload_file.py
```

### 3. Train the Model
Run `train_model.py`:  
```bash
python train_model.py
```

### 4. Predict Defects
Run `predict.py`:  
```bash
python predict.py
```

---

## Example Dataset

| ProductionVolume | ProductionCost | SupplierQuality | DeliveryDelay | ... | DefectStatus |
|-------------------|----------------|------------------|----------------|-----|--------------|
| 500              | 12000          | 8               | 2              | ... | 1            |
| 750              | 15000          | 7               | 3              | ... | 0            |

Save your dataset as `manufacturing_defect_dataset.csv`.

---

## Author
Kaustubh Dwivedi

---

## License
MIT License
