import requests as requests
from colorama import Fore
import json

def options():
    print("Menu")
    print("1) View all countries")
    print("2) Search by Country")
    print("3) Search by Currency")
    print("4) Search by Capital")

    choice = input("Chooose an option (1-4): ")
    return choice

def viewAllCountries():
    for country in countries:
        print(country["name"])

def searchByCountry():
    countryName = input("Enter a country to search for: ")

    for country in countries:
        if countryName.lower() in country["name"].lower():
            print("Name:", country["name"])
            print("Capital:", country["capital"])
            print("Population:", country["population"])
            print("Currency:", country["currency"])
            print("Phone:", country["phone"])

def searchByCurrency():
    currencyInput = input("Enter a currency to search for: ")

    for country in countries:
        if currencyInput.lower() in country["currency"].lower():
            print("Name:", country["name"])

def searchByCapital():
    capitalInput = input("Enter a capital to search for: ")

    for country in countries:
        if capitalInput.lower() in country["capital"].lower():
            print("Name:", country["name"])

print("Loading SimpleAPI...")
response = requests.get("https://api.sampleapis.com/countries/countries")

if response.status_code == 200:
    countries = response.json()
    print("SimpleAPI has successfully loaded!")
    choice = options()

    if choice == "1":
        viewAllCountries()
    elif choice == "2":
        searchByCountry()
    elif choice == "3":
        searchByCurrency()
    elif choice == "4":
        searchByCapital()
    else:
        print(Fore.RED, "The API could not be called from https://api.sampleapis.com/countries/countries")
