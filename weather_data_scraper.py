import requests
from bs4 import BeautifulSoup
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime, timedelta


def scrape_weather_data(city, start_date, end_date):
    """
    Scrape weather data from weather.com for the specified city and date range.

    Args:
        city (str): Name of the city to retrieve weather data for.
        start_date (str): Start date of the date range to retrieve weather data for, in the format 'YYYY-MM-DD'.
        end_date (str): End date of the date range to retrieve weather data for, in the format 'YYYY-MM-DD'.

    Returns:
        A pandas DataFrame containing the weather data for the specified date range.
    """
    # Convert date strings to datetime objects
    start_date = datetime.strptime(start_date, '%Y-%m-%d')
    end_date = datetime.strptime(end_date, '%Y-%m-%d')

    # Create empty lists to store data
    dates = []
    temperatures = []

    # Loop through each day in the date range and scrape the weather data
    current_date = start_date
    while current_date <= end_date:
        # Construct the URL for the current date and city
        url = f'https://weather.com/weather/history/d/{current_date.strftime("%Y%m%d")}/hourly/l/{city}'
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')

        # Extract the temperature data from the page
        temperature_elements = soup.find_all('span', {'class': 'temp'})
        hourly_temperatures = [int(e.text.strip('°')) for e in temperature_elements]

        # Calculate the daily average temperature and add it to the list
        daily_average_temperature = sum(hourly_temperatures) / len(hourly_temperatures)
        dates.append(current_date.strftime('%Y-%m-%d'))
        temperatures.append(daily_average_temperature)

        # Move on to the next day
        current_date += timedelta(days=1)

    # Create a pandas DataFrame from the data
    weather_data = pd.DataFrame({'Date': dates, 'Temperature (°F)': temperatures})

    return weather_data


def save_weather_data(weather_data, filename):
    """
    Save the weather data to a CSV file.

    Args:
        weather_data (pandas DataFrame): The weather data to save.
        filename (str): The name of the file to save the data to.
    """
    weather_data.to_csv(filename, index=False)


def load_weather_data(filename):
    """
    Load weather data from a CSV file.

    Args:
        filename (str): The name of the file to load the data from.

    Returns:
        A pandas DataFrame containing the weather data.
    """
    weather_data = pd.read_csv(filename)
    return weather_data


def analyze_weather_data(weather_data):
    """
    Analyze the weather data and print out some statistics.

    Args:
        weather_data (pandas DataFrame): The weather data to analyze.
    """
    mean_temperature = weather_data['Temperature (°F)'].mean()
    median_temperature = weather_data['Temperature (°F)'].median()
    max_temperature = weather_data['Temperature (°F)'].max()
    min_temperature = weather_data['Temperature (°F)'].min()

    print(f'Mean temperature: {mean_temperature:.2f}°F')
    print(f'Median temperature: {median_temperature:.2f}°F')
    print(f'Maximum temperature: {max_temperature:.2f}°F')
    print(f'Minimum temperature: {min_temperature:.2f}°F')


def plot_weather_data(weather_data):
    """
    Create a line chart of the daily average temperatures.

    Args:
        weather_data (pandas DataFrame): The weather data to plot.
    """
    # Convert the dates to datetime objects and set them as the index of the DataFrame
    weather_data['Date'] = pd.to_datetime(weather_data['Date'])
    weather_data.set_index('Date', inplace=True)

    # Create the line chart
    plt.plot(weather_data.index, weather_data['Temperature (°F)'])

    # Add labels and title
    plt.xlabel('Date')
    plt.ylabel('Temperature (°F)')
    plt.title('Daily Average Temperatures')

    # Show the plot
    plt.show()


if __name__ == '__main__':
    
    # Set the parameters for the weather data to scrape
    city = 'New York, NY'
    start_date = '2022-01-01'
    end_date = '2022-01-31'

    # Scrape the weather data and save it to a file
    weather_data = scrape_weather_data(city, start_date, end_date)
    save_weather_data(weather_data, 'weather_data.csv')

    # Load the weather data from the file, analyze it, and plot it
    loaded_weather_data = load_weather_data('weather_data.csv')
    analyze_weather_data(loaded_weather_data)
    plot_weather_data(loaded_weather_data)
