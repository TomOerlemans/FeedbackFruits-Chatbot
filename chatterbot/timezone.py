import sys
from geopy import geocoders
import re
from fuzzywuzzy import fuzz
import re
import csv
import datetime


class TimeZone:

    def returnLocationRelatedWords( self, query ):
        """
        This function takes the user's input string and removes common words to try and filter out
        most words which are not related to the location.
        :param location: Unfiltered user's time query
        :return: filteredString: The user's query with most of the words unrelated to the location stripped off
        """
        query = re.sub("[^a-z0-9]+", " ", query, flags=re.IGNORECASE)  # Removes all special characters
        unrelatedWords = ['what', 'is', 'a', 'at', 'the', 'in', 'time', 'it', 'could', 'please',
                          'would', 'in', 'oke', 'okay' , 'ok', 'then', 'can', 'you', 'me', 'local', 'current',
                          'right', 'now', 'tell', 'give', 'hi', 'hello', 'tell', 'at' ,'zone', 'and',
                          'country', 'place', 'postal', 'code', 'also', 'be', 'moment', 'alright', 'good', 
                          'all', 'right', 'great', 'thanks', 'thank', 'you', 'currently']
        querywords = query.split()
        locationRelatedWords = [word for word in querywords if word.lower() not in unrelatedWords]
        locationRelatedWords = ' '.join(locationRelatedWords)
        return locationRelatedWords

    def returnCountryTimeZones( self, location ):
        """
        Checks whether the user's time query is related to a country which is known to have multiple timezones, and then returns a modified
        answer which includes all those timezones.
        :param location: Filterd user's query
        :return: countryTimezones: An empty string, or a string with multiple timezones related to the user's time query
        """
        confidence = 90
        countryResponseString = ""
        selectedCountry = ""
        with open('CountryTimeZone.csv', 'rb') as csvfile:
            countryDB = csv.reader(csvfile, delimiter=',')
            for country in countryDB:
                ratio = fuzz.ratio(location.lower(), country[0].lower())
                if ratio > confidence:
                    selectedCountry = country[0] + " has multiple time zones:"
                    currentTime = (datetime.datetime.utcnow() - datetime.timedelta(hours=int(country[1]))).strftime("%H:%M:%S")
                    countryResponseString = countryResponseString + "\n" + currentTime + " - " + country[2]
        return selectedCountry + countryResponseString

    def returnTime( self, location ):
        """
        This method returns the current time in response to an unformatted time query. It uses the geopy library to get the correct timezone,
        then using the datetimezone library it acquires the current time within that timezone.
        :param location: Unfiltered user's time query
        :return: Correctly formatted time response
        """
        locationFiltered = self.returnLocationRelatedWords(location)
        multipleTimeZones = self.returnCountryTimeZones(locationFiltered)

        if (len(multipleTimeZones) < 1):
            g = geocoders.GoogleV3()
            try:
                place, (lat, lng) = g.geocode(locationFiltered)
                timezone = g.timezone((lat, lng))
                outputLocation = re.sub("[^a-z0-9]+", " ", place.replace("Local", ""), flags=re.IGNORECASE)
                return "Local time in " + outputLocation + " is " + datetime.datetime.now(timezone).strftime("%H:%M:%S")
            except:
                return "Sorry I couldn't find the current time in " + locationFiltered + ". Are you sure that you spelled that correctly?"
        else:
            return multipleTimeZones