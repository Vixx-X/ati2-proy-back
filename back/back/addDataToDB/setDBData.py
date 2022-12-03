import json
import os
import django
from django.db import connection
import geonamescache
from countryinfo import CountryInfo
from geosky import geo_plug
from back.apps.address.models import City, Continent, Country, State
from phonenumbers.phonenumberutil import country_code_for_region

gc = geonamescache.GeonamesCache()
continents = gc.get_continents()
countries = gc.get_countries()

# print countries dictionary
for continent in continents:
    try:
        Continent(name=continents[continent]["asciiName"]).save()
    except:
        pass

CONTINENTS_CODE = {
    "AF": "Africa",
    "AN": "Antarctica",
    "AS": "Asia",
    "EU": "Europe",
    "NA": "North America",
    "OC": "Oceania",
    "SA": "South America",
}

for country in countries:
    continent = Continent.objects.filter(name=CONTINENTS_CODE[countries[country]['continentcode']]).first()
    countryDB = Country(
        iso_3166_1_a2=countries[country]['iso'].upper(),
        iso_3166_1_a3=countries[country]['iso3'],
        iso_3166_1_numeric=countries[country]['isonumeric'],
        printable_name=countries[country]['name'],
        name=countries[country]['name'],
        phone_code=country_code_for_region(countries[country]['iso'].upper())
        continent=continent,
    ).save()

    try:
        countryDB = Country.objects.filter(name=countries[country]['name']).first()
        countryInfo = CountryInfo(countries[country]['name'])
        states = countryInfo.provinces()
        for state in states:
            try:
                State(
                    name=state,
                    country=countryDB,
                ).save()
            except django.db.utils.IntegrityError:
                state2 = State.objects.filter(name=state).first()
                state2.country=countryDB
                state2.save()
        cities = geo_plug.all_State_CityNames(states[0])
        cities = json.loads(cities)
        for cityDict in cities:
            for stateName in cityDict:
                stateDB = State.objects.filter(name=stateName).first()
                for city in cityDict[stateName]:
                    City(
                        name=city,
                        state=stateDB,
                    ).save()
    except (KeyError, django.db.utils.IntegrityError) as error:
        print(countries[country]['name'])
        print('fail')
        print(error)
        continue

try:
    miranda = State.objects.filter(name='Miranda').first()
    City(
        name='Caracas',
        state=miranda,
    ).save()
except (KeyError, django.db.utils.IntegrityError) as error:
    pass

social_media = ['Twitter', 'Facebook', 'Instagram']

def load_vehicle_data_from_sql(): 
    file_path = os.path.join(os.path.dirname(__file__), '../sql/vehicles.data.sql')
    sql_statement = open(file_path).read()
    with connection.cursor() as c:
        c.execute(sql_statement)

try:
    load_vehicle_data_from_sql()
except Exception as error:
    print(error)
    pass

