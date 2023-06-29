import pandas as pd
import json

# Load JSON data
with open('tcaReportAPIResponse.json', 'r') as f:
    json_data = json.load(f)

# Load Excel data
excel_data = pd.read_excel('strategies.xlsx')

# Convert JSON data and Excel data into sets of strings
json_values = {str(value) for json_obj in json_data for value in json_obj.values()}
excel_values = {str(value) for _, row in excel_data.iterrows() for value in row.values}

# Count the number of common values
common_values_count = len(json_values & excel_values)

# Calculate the total number of unique values in both files
total_values = len(json_values | excel_values)

# Calculate percentage of common values in both files
percentage_common = (common_values_count / total_values) * 100 if total_values != 0 else 0

print(f'\tÉ necessário considerar uma margem \n\tde erro em torno de 10% de acordo com o caracteres \n\tutilizados para formatar o arquivo json (que não estão presentes no excel).\n\n')

print(f'\tPercentual de valores únicos comuns entre o arquivo JSON \n\tcontendo a response da ATG API referente ao TCA Report e o \n\tarquivo excel obtido através da página ATG Admin {percentage_common:.2f}%')
