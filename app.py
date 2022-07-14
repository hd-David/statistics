tfrom flask import Flask, jsonify
import csv, pprint, ast

pp = pprint.PrettyPrinter(indent=4)

big_data = []
with open("BigData1.csv", "r") as file:
    file_reader = csv.DictReader(file)
    for data in file_reader:
        big_data.append(data)

app = Flask(__name__)

"""
Filtering the country with highest statistics or maximum value based on year and SeriesCode.
Inputs:
    year (int): any year can be used in this function.
    SeriesCode (str): any series code can be used to find the highest statistics the user is looking for.
Outputs:
    List of dictionaries in json format containing filtered data.
"""
@app.route("/highest/<SeriesCode>/<year>")
def highest_country(SeriesCode,year):
    filtered_list = []
    for populated in big_data:
        if populated["SeriesCode"] == SeriesCode:
            filtered_list.append(populated)
    max_value = max(filtered_list, key=lambda x:x[year])
    return jsonify(max_value)   
   

"""
filtering all the countries with populations above the user's input.
Inputs: 
    year (int) whichever year the users choose to use.
    population (int) it is the number entered by the user.
Output : 
    list of dictionaries in json format containing filtered data.
"""
@app.route("/populations/<years>/<population>")
def population_above(years, population):
    countries_above_ten = []
    filtered_list = []
    for popular in big_data:
        if popular["SeriesCode"] == "SP.POP.TOTL":
            filtered_list.append(popular)
    for populate in filtered_list:
        if populate[years] > population:
            countries_above_ten.append(populate)
    return jsonify(countries_above_ten)      

""" 
Calculating the statistics growth between  two years entered by the user.
Inputs : 
    two different years ( str) the previous and current year
Outputs : 
    statistics growth (float)
"""
@app.route("/statistics-growth/<SeriesCode>/<year1>/<year2>")
def statistics_growth(SeriesCode,year1,year2):
    total_growth = []
    for growth in big_data:
        if growth["SeriesCode"] == SeriesCode:
            total_growth.append(growth) 
    for pop in total_growth:
        try:
            pop_growth = ((ast.literal_eval(pop[year1])- ast.literal_eval(pop[year2])) / ast.literal_eval(pop[year2])) *100
        except: # using error handling due to the fact that some statistics do not have values
            print(pop)
    return jsonify(pop_growth)


"""
Filtering by country name and Series code provided by the user
Inputs: 
    countryCode (type of str) Country code is the abbreviation of the countries name
    seriescode(type of str)   Series code is the code to identify the different number of statistics.
Outputs: 
    list of dictionaries in json format containing filtered data.
"""
@app.route("/filter-by-country/<CountryCode>/<SeriesCode>")
def filter_by_country(CountryCode,SeriesCode):
    country_data = []
    for data in big_data:
        if data["CountryCode"] == CountryCode:
            if data["SeriesCode"] == SeriesCode:
                country_data.append(data)                  
    return jsonify(country_data)
