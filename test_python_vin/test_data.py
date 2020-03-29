'''
Created on 28 mar 2020

@author: maxx
'''

test_1_data = {
  "records": [
    {
      "vin": "VSSZZZ6JZ9R056308",
      "date": "2017-01-02",
      "data_provider_id": 10,
      "odometer_reading": 10010,
      "service_details": [
        "Oil changed",
        "Tires rotated"
      ]
    },
    {
      "vin": "VSSZZZ6JZ9R056308",
      "date": "2017-06-20",
      "data_provider_id": 10,
      "odometer_reading": 12100,
      "service_details": [
        "Tires replaced"
      ]
    },
    {
      "vin": "VSSZZZ6JZ9R056308",
      "date": "2018-02-12",
      "data_provider_id": 10,
      "odometer_reading": 15100,
      "service_details": [
        "Windshield replaced"
      ]
    },
    {
      "vin": "VSSZZZ6JZ9R056308",
      "date": "2018-04-01",
      "data_provider_id": 10,
      "odometer_reading": 5600,
      "service_details": [
        "Air dam replaced",
        "Oil main"
      ]
    },
    {
      "vin": "VSSZZZ6JZ9R056308",
      "date": "2018-06-23",
      "data_provider_id": 10,
      "odometer_reading": 6400,
      "service_details": [
        "Rear axle oil exchanged",
        "Engine oil pump repaired/replaced"
      ]
    }
  ]
}

test_1_result = {
  "records": [
    {
      "vin": "VSSZZZ6JZ9R056308",
      "date": "2017-01-02",
      "data_provider_id": 10,
      "odometer_reading": 10010,
      "service_details": [
        "Oil changed",
        "Tires rotated"
      ]
    },
    {
      "vin": "VSSZZZ6JZ9R056308",
      "date": "2017-06-20",
      "data_provider_id": 10,
      "odometer_reading": 12100,
      "service_details": [
        "Tires replaced"
      ]
    },
    {
      "vin": "VSSZZZ6JZ9R056308",
      "date": "2018-02-12",
      "data_provider_id": 10,
      "odometer_reading": 15100,
      "service_details": [
        "Windshield replaced"
      ]
    },
    {
      "vin": "VSSZZZ6JZ9R056308",
      "date": "2018-06-23",
      "data_provider_id": 10,
      "odometer_reading": 6400,
      "service_details": [
        "Rear axle oil exchanged",
        "Engine oil pump repaired/replaced"
      ]
    },
    {
      "vin": "VSSZZZ6JZ9R056308",
      "date": "2018-04-01",
      "odometer_rollback" : True,
      "data_provider_id": 10,
      "odometer_reading": 5600,
      "service_details": [
        "Air dam replaced",
        "Oil main"
      ]
    }
  ]
}

test_2 = {
  "records": [
    {
      "vin": "VSSZZZ6JZ9R056309",
      "date": "2017-01-02",
      "data_provider_id": 10,
      "odometer_reading": 10010,
      "service_details": [
        "Oil changed",
        "Tires rotated"
      ]
    }
  ]
}

test_3 = {
  "records": [
  ]
}

test_error1 = {
  "records": [
    {
      "vin": "VSSZZZ6JZ9R056312",
      "date": "2017-01-02",
      "data_provider_id": 10,
      "odometer_reading": 10010,
      "service_details": [
        "Oil changed",
        "Tires rotated"
      ]
    }
  ]
}

test_error2 = {
  "records": [
    {
      "vin": "VSSZZZ6JZ9R056313",
      "date": "2017-01-02",
      "data_provider_id": 10,
      "odometer_reading": 10010,
      "service_details": [
        "Oil changed",
        "Tires rotated"
      ]
    },
    {
      "vin": "VSSZZZ6JZ9R056313",
      "date": "2017-06-20",
      "data_provider_id": 10,
#      "odometer_reading": 12100,
      "service_details": [
        "Tires replaced"
      ]
    }
  ]
}