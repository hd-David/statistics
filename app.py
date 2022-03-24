from flask import Flask, jsonify
import csv, pprint

pp = pprint.PrettyPrinter(indent=4)

big_data = []
with open("SmallData.csv", "r") as file:
    file_reader = csv.DictReader(file)
    for data in file_reader:
        big_data.append(data)

app = Flask(__name__)

"""
    Inputs: year.
    Outputs: list of dictionaries.
    What the function is doing: filtering the country with highest statistcs or
    maximum value based on the which year they enter.
    build a new list after filtering and then find the maximum value from the filtered list.
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
    Find the countries with the population above what the user provides based on the year provided.
    Inputs: year, population
    Output : list of dictionaries
    What the function is doing: filtering all the countries with populations above the user want to check.
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
    Checking the country with big land
    Inputs : year
    Output: list of dictionaries
    What the function is doing: filtering the the country with big surface area
"""
@app.route("/country/<year>")
def couuntry_with_big_land(year):
    big_area = []
    for big_land in big_data:
        if big_land["SeriesCode"] == "AG.SRF.TOTL.K2":
            big_area.append(big_land)
    max_value2 =max(big_area, key=lambda x:x[year])
    return jsonify(max_value2)


""" 
     Inputs : first year and last year
     Outputs : list of dictionary
     What the function is doing: calculating the population growth between  two years entered by the user.
 """
@app.route("/growth/<country>/<year1>/<year2>")
def population_growth(year1,year2):
    total_growth = []
    for growth in big_data:
        if growth["SeriesCode"] == "SP.POP.TOTL":
            total_growth.append(growth) 
            #pp.pprint(total_growth)
    for pop in total_growth:
        pp.pprint(pop)
        pop_growth = ((int(pop[year1])- int(pop[year2])) / int(pop[year2])) *100
        float(pop_growth)
    return jsonify(pop_growth)


"""
    Inputs: country name, year, seriescode
    Outputs: list of dictionaries in json format
    what the function is doing: it is filtering by country name and Series code provided by the user
"""
@app.route("/filter-by-country/<CountryCode>/<SeriesCode>")
def filter_by_country(CountryCode,SeriesCode):
    country_data = []
    for data in big_data:
        if data["CountryCode"] == CountryCode:
            if data["SeriesCode"] == SeriesCode:
                country_data.append(data)                  
    return jsonify(country_data)