# general imports
import csv

# open csv file
interest_rate_data_usa_csv_file = open("csvFiles/interest_rate_data_usa.csv", "r")

# create reader object for the csv file
interest_rate_data_usa_csv_reader = csv.reader(interest_rate_data_usa_csv_file)

# convert csv to a list
data_list = list(interest_rate_data_usa_csv_reader)

# create dictionary for the sum of each monthly reported federal funds rate for any given year
interest_rate_dictionary_sum = {}
# create dictionary for number of months where the effective federal funds rate was reported in any given year
interest_rate_dictionary_count = {}
# create a dictionary for the average federal funds rate for any given year
interest_rate_dictionary_average = {}

# populate interest rate dictionary sum and count variants
for row in range(1, len(data_list)):
    effective_federal_funds_rate = 6
    year = 0

    if (data_list[row][effective_federal_funds_rate] != ''):
        if data_list[row][year] not in interest_rate_dictionary_sum: 
            interest_rate_dictionary_sum[data_list[row][year]] = float(data_list[row][effective_federal_funds_rate])
            interest_rate_dictionary_count[data_list[row][year]] = 1
        else:
            interest_rate_dictionary_sum[data_list[row][year]] += float(data_list[row][effective_federal_funds_rate])
            interest_rate_dictionary_count[data_list[row][year]] += 1

# populate interest rate dictionary average variant
for key in interest_rate_dictionary_count:
    interest_rate_dictionary_average[key] = interest_rate_dictionary_sum.get(key) / interest_rate_dictionary_count.get(key)

def get_cleaned_interest_rate_data():
    return interest_rate_dictionary_average