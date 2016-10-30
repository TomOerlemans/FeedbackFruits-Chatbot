# FeedbackFruits-Chatbot

FeedbackFruits-Chatbot is a chatbot build using the ChatterBot Python library. The ChatterBot library comes with several useful adapters, these are used for: input/output, data storage and as logic adapters for matching input and output. 


For this project the terminal adapter is used for input and output, and the Json file storage adapter is used for data storage. These adapters were picked as they need the least amount of additional software and are best suited for quick development.  The Closest Match Adapter is used to match input and output. This adapter was chosen because it showed the best tradeoff between computation time and accuracy during testing.


The closest match adapter uses the fuzzywuzzy library to compute the Levenshtein distance. This algorithm computes the distance between two strings, as the minimum number of character edits needed to change one string into another. 


FeetbackFruits-Chatbot has the following features:

•	It can return the time for any: postal code, city, region and country

•	It can recognize a wide variety of input sentences as time requests

•	It is robust to misspelling of location names

•	It recognizes certain countries which have multiple time zones, and adjusts its output accordingly




The image below illustrates the event flow of the program:



![alt tag](https://github.com/TomOerlemans/FeedbackFruits-Chatbot/blob/master/flowchart.png)

