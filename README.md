[![Maintenance](https://img.shields.io/badge/Maintained%3F-yes-green.svg)](https://GitHub.com/Naereen/StrapDown.js/graphs/commit-activity) [![contributions welcome](https://img.shields.io/badge/contributions-welcome-brightgreen.svg?style=flat)](https://github.com/dwyl/esta/issues)

# [#] IOT Device Tracker
> The website provides visualization of different server data with date wise filter.


## User Guide
> 1. Open the IOT Device Tracker website
> 2. Enter the desired range of start and end date and press submit.
> 3. The results are displayed straight from the database and are stored in cache server.
>![App Screenshot](https://github.com/pulkitmunjral/SmarterCodes/blob/with_swagger/screen_shots/1.PNG)
>
>
> 4. If you submit range which is already present in cache the output is displayed straight from cache server.
>![App Screenshot](https://github.com/pulkitmunjral/SmarterCodes/blob/with_swagger/screen_shots/2.PNG)
>
>
> 5. You can directly pass the desired range into the URL also.
> Example: https://smartercodes.herokuapp.com/details/start_date=2020-01-01/end_date=2021-01-01
>
>
> 6. If no data is found between your given range, then custom error is thrown.
>![App Screenshot](https://github.com/pulkitmunjral/SmarterCodes/blob/with_swagger/screen_shots/3.PNG)
>
>
> 7. Swagger documentation is available at [URL](https://smartercodes.herokuapp.com/swagger)
>![App Screenshot](https://github.com/pulkitmunjral/SmarterCodes/blob/with_swagger/screen_shots/5.PNG)
>
>
> 8. Custom error page is displayed to user for any website failures.
>![App Screenshot](https://github.com/pulkitmunjral/SmarterCodes/blob/with_swagger/screen_shots/4.PNG)
>
>
> 9. A copy of Log is sent to the admin for each error.
>![App Screenshot](https://github.com/pulkitmunjral/SmarterCodes/blob/with_swagger/screen_shots/6.PNG)


## Features
* Accept date range to provide desired details
* Custom error messages are displayed to user.
* Error logs are sent to admin on each failure.
* Used Redis server to provide instant response, reducing time response.
* Used Swagger UI for api documentation
* Used Cron job locally to trigger api which loads data in database every hour.

## How to Contribute
We are open for suggestion and contributions, pull requests are welcome.

For major changes, please open an issue first to discuss what you would like to change.

If you'd like to contribute, please follow [CONTRIBUTING.md](https://github.com/pulkitmunjral/SmarterCodes/blob/with_swagger/CONTRIBUTING.md)


## Author 
Pulkit Munjral  – pulkit.munjral@gmail.com
 
 You can find me here at:
[Github](https://github.com/pulkitmunjral/)
[LinkedIn](https://www.linkedin.com/in/pulkitmunjral/)

## Credits
Credits goes to SmarterCodes who gave me opportunity to showcase my skills and I would like to thank Mr. Jatin Sharma and Mr. Satwinder for their support.
