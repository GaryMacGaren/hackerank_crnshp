## Environment:
- Python version: 3.7
- Django version: 3.0.6
- Django REST framework version: 3.11.0

## Read-Only Files:
- rest_api/tests.py
- manage.py

## Data:
Example of a weather data JSON object:
```
{
   "id": 1,
   "date": "1985-01-01",
   "lat": 36.1189,
   "lon": -86.6892,
   "city": "Nashville",
   "state": "Tennessee",
   "temperatures": [17.3, 16.8, 16.4, 16.0, 15.6, 15.3, 15.0, 14.9, 15.8, 18.0, 20.2, 22.3, 23.8, 24.9, 25.5, 25.7, 24.9, 23.0, 21.7, 20.8, 29.9, 29.2, 28.6, 28.1]
}
```

## Requirements:
The REST service must expose the /weather/ endpoint, which allows for managing the collection of weather records in the following way:


POST request to `/weather/`:

- creates a new weather data record
- expects a valid weather data object as its body payload, except that it does not have an id property; you can assume that the given object is always valid
- adds the given object to the collection and assigns a unique integer id to it
- the response code is 201 and the response body is the created record, including its unique id


GET request to `/weather/`:

- the response code is 200
- the response body is an array of matching records, ordered by their ids in increasing order
- accepts an optional query string parameter, date, in the format YYYY-MM-DD, for example /weather/?date=2019-06-11. When this parameter is present, only the records with the matching date are returned.
- accepts an optional query string parameter, city, and when this parameter is present, only the records with the matching city are returned. The value of this parameter is case insensitive, so "London" and "london" are equivalent. Moreover, it might contain several values, separated by commas (e.g. city=london,Moscow), meaning that records with the city matching any of these values must be returned.
- accepts an optional query string parameter, sort, that can take one of two values: either "date" or "-date". If the value is "date", then the ordering is by date in ascending order. If it is "-date", then the ordering is by date in descending order. If there are two records with the same date, the one with the smaller id must come first.


GET request to `/weather/<id>/`:

- returns a record with the given id
- if the matching record exists, the response code is 200 and the response body is the matching object
- if there is no record in the collection with the given id, the response code is 404<br><br>
## ******************* QUESTION_RESPONSE *****************

A monolithic application is not the best solution for the Cornershop application due to the fact that we do not know, among the many processes running simultaneously, who is in control.

Instead, splitting central bank data into microservices would be a better solution.<br><br>

<img src="WhatsAppImage.png" alt="cornershop high level structure"/><br><br>

Each microservice would have its own database, and it would be possible to better manage the application, in addition to allowing the scalability of new markets/branches and customers.

Stores and branches need to be separate microservices, since there is a price for the stores (official) and another one practiced in the branches. In addition to these, customers, products, shoppers and schedules need to be separated.

All of these could communicate directly, and would be a better solution than monolithic too, but a better architectural pattern would be event-based communication.

For example: A customer makes an appointment for a purchase from the supermarket. The microservice of that customer's branch needs to be informed of this purchase, in order to be able to separate the products involved. In addition, it is necessary to register this event in another service, so that later, close to that appointment, a shopper can be informed and be able to make the purchase for the customer.


To scale the application, a store and branch orchestrator is needed, always ready to add a new store/branch, update the product catalog (events) and update the application (customers) with the new purchase options.

In this way, several processors could run simultaneously (asynchronously), in addition to making the application more reliable and scalable.


