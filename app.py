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
    Finding the most populated country
    The inputs: year.
    The output: list of dictionaries.
    What the function is doing: filtering the country with highest population or
    maximum value based on the which year they enter.
    build a new list after filtering and then find the maximum value from the filtered list.
"""
@app.route("/highest/<year>")
def most_populated_country(year):
    filtered_list = []
    for populated in big_data:
        if populated["SeriesCode"] == "SP.POP.TOTL":
            filtered_list.append(populated)
    max_value = max(filtered_list, key=lambda x:x[year])
    return jsonify(max_value)   
   

"""
    Find the countries with the population above ten million based on the year provided.
    Inputs: year, population
    Output : list of dictionaries
    What the function is doing: filtering all the countries with populations above ten
    million.
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
    Inputs : series code 
    Output: list of dictionaries
    What the function is doing: filtering the land with big surface area
"""
@app.route("/country/<year>")
def couuntry_with_big_land(year):
    big_area = []
    for big_land in big_data:
        if big_land["SeriesCode"] == "AG.SRF.TOTL.K2":
            big_area.append(big_land)
    max_value2 =max(big_area, key=lambda x:x[year])
    return jsonify(max_value2)


""" Finding the population growth from 2015 to 2021
     Inputs : first year and last year, country
     Outputs : list of dictionary
     What the function is doing: calculating the population growth between the year
2015 upto 2021.
 """
@app.route("/growth/<country>/<year1>/<year2>")
def population_growth(country,year1,year2):
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
    Inputs : years( two or more years)
    Output : list of dictionary
    What the function is doing: the function is comparing the GDP growth maybe for
    the past two years and return the country with the lowest GDP growth rate.
"""
@app.route("/GDP-growth/<SeriesCode>/<year>")
def GDP_growth(SeriesCode):
    SeriesCode_data = []
    for data in big_data:
        if data["SeriesCode"] == SeriesCode:
            SeriesCode_data.append(data)
    return jsonify(SeriesCode_data)


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