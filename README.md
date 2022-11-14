# Data breach checker

1. Firstly you have to create an account to intelx to access the API:

https://intelx.io/signup

2. After successful registration, you will have an access to the API, which you can check out in the developer section

https://intelx.io/account?tab=developer

3. In the config.py you have to update the followings:
    * API key
    * Domain name you want to check out
    * Number of days in the period you would like to check

4. Run the main.py 

5. After successful run you should see a data_breach_results.txt 

## data_breach_results.txt 

#### The output document looks like the following

The investigated domain is `domain name`

Number of leaked data in the last period: `number of leaked data in last period`

Total number of leaked data: `total number of leaked data`

Data to start investigation: `json file containing various data of the databreaches`
