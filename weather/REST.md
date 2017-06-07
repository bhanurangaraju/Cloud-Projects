**Homework #2: Create a Weather ReSTful WebService**

**The objective of this project is to implement RESTful WebServices using Flask framework.**

**API Documentation:**
 
1.Description: List of all dates for which weather information is available as a JSON array. 

Link: [click to display all dates](http://35.167.0.44:5000/weather/historical/)

URI: http://35.167.0.44:5000/weather/historical/

Method: GET

Input Parameters: None

Sample Response:  JSON
[
{"DATE": "20130101"},
{"DATE": "20130102"},
..............]
---------------------------------------------------------------------------------------------------------------------

2.Description: Weather information for a particular date. If no information is available - 404 error

Link:[click for weather info on 2015-12-02](http://35.167.0.44:5000/weather/historical/20151202)

URI: http://35.167.0.44:5000/weather/historical/<date>

Method: GET

date format : YYYYMMDD

Response: Status code 200 OK for available date, Status code 404 Not Found for an invalid date

Example:
http://35.167.0.44:5000/weather/historical/20151202

Sample Response: JSON
{
  "DATE": "20151202",
  "TMAX": "49",
  "TMIN": "34"
}

----------------------------------------------------------------------------------------------------------------------
3.Description: Add weather information for a particular day

URI: http://35.167.0.44:5000/weather/historical/

Method: POST

Input: (application/json)

Sample Input 
{
  "DATE": "20170227",
  "TMAX": "73.5",
  "TMIN": "57"
}

Response: Status code 201 if added successfully/ 409 if creating a duplicate/ 406 if invalid date format

---------------------------------------------------------------------------------------------------------------
4.Description: Delete weather info a particular day

URI: http://35.167.0.44:5000/weather/historical/<date>

Method: DELETE

Input Parameters: Date <YYYYMMDD> 
Datatype: string

Response: 200 Record Delete / 404 Not Found if trying to delete an unexisting record

Example:
http://35.167.0.44:5000/weather/historical/20151202

Sample Response: JSON

Record deleted successfully
{
  "DATE": "20151202",
  "TMAX": "49",
  "TMIN": "34"
}

-------------------------------------------------------------------------------------------------------------------
5.Description: Weather forecast for next 7 days - the date could be an existing date or future date

Link: [click to forecast weather information on 2015-12-06](http://35.167.0.44:5000/weather/forecast/20151206)

URI:http://35.167.0.44:5000/weather/forecast/<date>

Input: date<YYYYMMDD>
Datatype : String

Response: Returns the next 7 days Maximum Temperature 

Example:
http://35.167.0.44:5000/weather/forecast/20151206

Response: JSON
[
  {
    "DATE": "20151206", 
    "TMAX": 43.63, 
    "TMIN": 28.15
  }, 
  {
    "DATE": "20151207", 
    "TMAX": 53.2, 
    "TMIN": 26.55
  }, 
  {
    "DATE": "20151208", 
    "TMAX": 49.49, 
    "TMIN": 39.06
  }, 
  {
    "DATE": "20151209", 
    "TMAX": 55.25, 
    "TMIN": 37.32
  }, 
  {
    "DATE": "20151210", 
    "TMAX": 53.76, 
    "TMIN": 38.55
  }, 
  {
    "DATE": "20151211", 
    "TMAX": 54.83, 
    "TMIN": 38.42
  }, 
  {
    "DATE": "20151212", 
    "TMAX": 62.07, 
    "TMIN": 50.97
  }
]
