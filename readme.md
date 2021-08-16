# Eureka Labs Challange

## Task

### Stock Market API Service

Expose an API endpoint where I can POST my data and sign up for an API key that will be used later.

Expose an API endpoint where I can hit and get stock market information, as a security mechanism use the API key obtained previously in order to validate user and make sure that no authorized user will consume the service (use request header for that purpose). 

Here are some examples of stock symbols
- Facebook (FB)
- Apple (AAPL)
- Microsoft (MSFT)
- Google (GOOGL)
- Amazon (AMZN)

The system will make use of a web service called Alpha Vantage, this will provide stock market information.

Information that will be retrieved in the response of the service as json format will contain:
- Open price
- Higher price
- Lower price
- Variation between last 2 closing price values.

**Alpha Vantage API**
```
https://www.alphavantage.co/documentation/
API Key: X86NOH6II01P7R24
```

API call sample to get stock prices from Facebook:

`https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=FB&outputsize=compact&apikey=X86NOH6II01P7R24`

**Considerations:**
- API URL structure is up to you.
- Initial data for sign up: name, last name, email.
- Validation rules for signup data are up to you.
- Json structure is up to you.
- It will be a big plus if you deploy the services somewhere in the cloud (heroku, gcloud, aws, azure, etc). It's ok if you just do it locally.
- Use github (or other git repo).
- Programming language: Python.
- BONUS: If you can implement API throttling, that's a big one. Throttling rules are up to you (1 API call per second allowed or 10 API calls per minute, etc).
- Log every API call received, log format is up to you.
- Place a README.md file with instructions in the github repo so test can be performed and checked.

## Solution

API built with Django and DRF, exposed and deployed in this [Heroku Site](https://eurekalabs-challenge.herokuapp.com/).

### How to use it?

1. Please access this [Signup URL](https://eurekalabs-challenge.herokuapp.com/register/) to register as a valid user. 
1. Provide all the fields in the form to create a user. If the data are valid after confirming the form the following message will appear: 
> User Created Successfully. Login for get auth token and make requests
1. Enter the following [link](https://eurekalabs-challenge.herokuapp.com/api/token/) to authenticate and get the valid token (JWT) to use the application.
1. If the data is correct the application will return two tokens: an access token and a refresh token. 
  1. You will have to use the access token and include it in the request headers as a Bearer Token. As follows
  > 'Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9....'
  1. To learn more about JWT and its uses, please access the following [link](https://jwt.io/)
1. To use the api, you must access the following (https://eurekalabs-challenge.herokuapp.com/api/[SYMBOL]?[QUERY_STRINGS_PARAMS]). For instance, the following URL:
> https://eurekalabs-challenge.herokuapp.com/api/FB?function=TIME_SERIES_INTRADAY&interval=30min

Where Symbol is the one corresponding to the name of the equity of your choice.
For the use of other parameters please see Alpha Vantage [API Documentation](https://www.alphavantage.co/documentation/)


Thanks