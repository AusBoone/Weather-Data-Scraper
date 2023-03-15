# Weather Data Scraper

This is a Python script that scrapes daily average temperature data for a specified city and date range from weather.com. The script uses the following Python libraries:

requests - Used to send HTTP requests to the website and retrieve the HTML content.
beautifulsoup4 - Used to parse the HTML content and extract the temperature data.
pandas - Used to store the temperature data in a DataFrame and perform data analysis.
matplotlib - Used to create a line chart of the daily average temperatures.
datetime - Used to handle date objects and convert between date formats.

# Usage
To use the script, you need to specify the city name and the date range for which you want to scrape the temperature data. To do this, modify the following lines of code in the script:

city = 'New York, NY'
start_date = '2022-01-01'
end_date = '2022-01-31'

Replace 'New York, NY' with the name of the city you want to scrape data for, and '2022-01-01' and '2022-01-31' with the start and end dates of the date range you want to scrape data for.

Once you've modified these lines of code, you can run the script using the following command:

python weather_data_scraper.py

The script will scrape the temperature data, save it to a CSV file named weather_data.csv, and then analyze and plot the data. You can find the CSV file and the plot in the same directory where you saved the script.

# Imports
Here's an explanation of why each import is required:

requests - Used to send HTTP requests to the website and retrieve the HTML content.
beautifulsoup4 - Used to parse the HTML content and extract the temperature data.
pandas - Used to store the temperature data in a DataFrame and perform data analysis.
matplotlib - Used to create a line chart of the daily average temperatures.
datetime - Used to handle date objects and convert between date formats.
