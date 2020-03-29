Create a simple REST service capable of retrieving data for one Vehicle Identification Number (VIN), analyzing these different data points, and then providing an output view of the result in JSON format.

We will provide a REST server response that you will need to consume. These responses will contain records for a specific VIN, with additional metadata within those records.

You will need to identify records that have an "Odometer Rollback." Since an Odometer should always increase in value over time, an "Odometer Rollback" is defined as an event in which the Odometer no longer grows in an ascending manner. Please add a new output property to indicate the record on which the Odometer rollback occurred. This new property should only be on the record where the rollback event was recorded, all records following a rollback should remain untouched.

We still wish to see all of the original records and data in the output, plus the new field.

The solution should be provided in Java or Python. You are encouraged to use any third-party libraries you wish. However, you should deliver the end result in a way that allows us to inspect the code and run the application.

While you should not spend a lot of time working on this assignment, please write your software in such a manner so that it demonstrates your professional coding style. That includes writing tests, having good code organization, etc. Our goal is to get a feeling for how you work as a software developer.

You should submit your solution by sending us a copy of the code, as well as instructions on how to run the application. You can send it to us through Github or email if that is easier. As far as running the solution, a README file or Docker image will be acceptable - so long as it is easy for us to run the application on our end.

Once you have submitted your solution we will schedule a review session; please be prepared to present a running application on your own device. We will also ask you to make additional modifications based on new or changing requirements.

# JSON Schema for Input

	{
	   "$schema":"http://json-schema.org/draft-07/schema#",
	   "title":"CARFAX Challenge model",
	   "type":"object",
	   "required":[
	      "records"
	   ],
	   "properties":{
	      "records":{
	         "type":"array",
	         "items":{
	            "type":"object",
	            "required":[
	               "vin",
	               "date",
	               "data_provider_id",
	               "odometer_reading",
	               "service_details"
	            ],
	            "properties":{
	               "vin":{
	                  "date":"string",
	                  "description":"Vehicle identification number."
	               },
	               "date":{
	                  "date":"string",
	                  "description":"Date following format 'YYYY-MM-DD'."
	               },
	               "data_provider_id":{
	                  "type":"integer",
	                  "description":"Data provider id"
	               },
	               "odometer_reading":{
	                  "type":"integer",
	                  "description":"Odometer reading in KM"
	               },
	               "service_details":{
	                  "type":"array",
	                  "description":"List of service details e.g Oil changed, Tires rotated, etc",
	                  "items":{
	                     "type":"string"
	                  }
	               }
	            }
	         }
	      }
	   }
	}

#JSON Example records

Example VIN responses will be hosted at this URL format at runtime: ...

We should be able to put a VIN into your rest service and retrieve the correct response from the backend.

For example, for now, you can test using this URL: ...

	{
	   "records":[
	      {
	         "vin":"VSSZZZ6JZ9R056308",
	         "date":"2017-01-02",
	         "data_provider_id":10,
	         "odometer_reading":10010,
	         "service_details":[
	            "Oil changed",
	            "Tires rotated"
	         ]
	      },
	      {
	         "vin":"VSSZZZ6JZ9R056308",
	         "date":"2017-06-20",
	         "data_provider_id":10,
	         "odometer_reading":12100,
	         "service_details":[
	            "Tires replaced"
	         ]
	      },
	      {
	         "vin":"VSSZZZ6JZ9R056308",
	         "date":"2018-02-12",
	         "data_provider_id":10,
	         "odometer_reading":15100,
	         "service_details":[
	            "Windshield replaced"
	         ]
	      },
	      {
	         "vin":"VSSZZZ6JZ9R056308",
	         "date":"2018-04-01",
	         "data_provider_id":10,
	         "odometer_reading":5600,
	         "service_details":[
	            "Air dam replaced",
	            "Oil service"
	         ]
	      },
	      {
	         "vin":"VSSZZZ6JZ9R056308",
	         "date":"2018-06-23",
	         "data_provider_id":10,
	         "odometer_reading":6400,
	         "service_details":[
	            "Rear axle oil exchanged",
	            "Engine oil pump repaired/replaced"
	         ]
	      }
	   ]
	}