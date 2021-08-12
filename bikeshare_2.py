import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    cities = ['chicago','new york city', 'washington']
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city = input(print("choose a city (chicago, new york city, washington)"))
    while city not in cities:
        city = input(print('please,choose from the specific cities')).lower()
    # get user input for month (all, january, february, ... , june)
    
    months = ["january", "february", "march", "april", "may", "june"]

    month = input(print("do you want a specific month(from january to june) ? or all")).lower()

    while month not in months and month != "all":
        month = input(print("please enter a valid value")).lower()
    # get user input for day of week (all, monday, tuesday, ... sunday)

    days = ['saturday','sunday','monday','tuesday','wednesday','thursday','friday']
    day = input(print("choose the day or choose all")).lower()
    while day not in days and day != "all":
        day = input(print("please enter a valid day or write all"))

    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    cities = {'chicago':'chicago.csv', 'new york city':'new_york_city.csv', 'washington':'washington.csv'}

    df = pd.read_csv(cities[city])
    #convert start time column to date time
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    df['month'] = df['Start Time'].dt.month

    df['day_of_week'] = df['Start Time'].dt.day_name()

    if month != "all":
        months = ["january", "february", "march", "april", "may", "june"]
        month = months.index(month) + 1

        df = df[df['month'] == month]
        
        
    if day != "all":
        
        df = df[df['day_of_week'] == day.title()]


    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    common_month = df['month'].mode()[0]


    # display the most common day of week
    common_day = df['day_of_week'].mode()[0]

    # display the most common start hour
    common_hour = df['Start Time'].dt.hour.mode()[0]
    
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    common_start_station = df['Start Station'].value_counts()[0]
    print("most commonly used start station is: ", common_start_station)
    # display most commonly used end station
    common_end_station = df['End Station'].value_counts()[0]
    print("most commonly used end station is: ", common_end_station)
    # display most frequent combination of start station and end station trip
    most_combination_end_and_start = df.groupby(['Start Station','End Station']).size().idxmax()
    print(most_combination_end_and_start)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
   


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    total_travel_time =  df['Trip Duration'].sum() / 60 / 60
    print('total hours of traveling time is: ',round(total_travel_time,2))
    # display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print('the mean of traveling time is: ',mean_travel_time)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    user_types = df['User Type'].value_counts()
    print('the count of user types :', user_types)
    # Display counts of gender
    gender = df['Gender'].value_counts()
    print('the count of genders is: ',gender)
    # Display earliest, most recent, and most common year of birth
    earliest = df['Birth Year'].min()
    most_recent = df['Birth Year'].max()
    most_common = df['Birth Year'].mode()
    print("the earliest year of birth is : ", earliest,"\n")
    print("the most recent year of birth is : ",most_recent,'\n')
    print("the most common year of birth is : ",most_common,'\n')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
