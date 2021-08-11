# Yasmin Gil
# yasmingi@usc.edu
# COVID-19 Cases analysis

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def DailyReportAnalysis():
    # import data from github and read into data frame
    daily_reports_url='https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_daily_reports_us/07-16-2021.csv'
    confirmed_global_url = 'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv'
    recovered_global_url = 'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_recovered_global.csv'
    dailyreports_us = pd.read_csv(daily_reports_url)
    confirmed_global = pd.read_csv(confirmed_global_url)
    recovered_global = pd.read_csv(recovered_global_url)

    # Which State has highest number of confirmed cases?
    # use daily reports US and store in confirmed_states in descending order
    confirmed_states_desc = dailyreports_us[['Province_State', 'Confirmed']].sort_values(by='Confirmed', ascending=False)
    # select first row of data frame
    print('1. The state with the highest confirmed cases is',
          confirmed_states_desc.iloc[0,0], 'with',
          confirmed_states_desc.iloc[0,1], 'confirmed cases')

    # What is the difference in highest testing rate
    # and lowest testing rate & drop nulls
    testing_rates_desc = dailyreports_us[['Province_State', 'Testing_Rate']].sort_values(by='Testing_Rate', ascending=False).dropna()
    # Calculate difference between highest and lowest test rate
    diff = testing_rates_desc.iloc[0,1] - testing_rates_desc.iloc[-1,1]
    print('2. The difference in Testing Rate between the state that tests the most:',
          testing_rates_desc.iloc[0,0], 'and the state that tests the least:',
          testing_rates_desc.iloc[-1,0], 'is', diff)

    # Plot num daily new cases in the world for top 5 countries
    # with highest confirmed cases from july 1 2020 - july 1 2021
    # 1. Get top 5 countries
    confirmed_global = confirmed_global.sort_values(by='7/1/21', ascending=False)
    recovered_global = recovered_global.sort_values(by='7/1/21', ascending=False)
    #print(confirmed_global.head())
    confirmed_global_top5 = confirmed_global.iloc[0:5, :]
    recovered_global_top5 = recovered_global.iloc[0:5, :]
    # print(confirmed_global_top5)
    # print(recovered_global_top5)

    # pd.set_option('display.max_columns', None)

    # get the right dates
    confirmed_global_top5_dates = confirmed_global_top5.loc[:,'6/30/20':'7/1/21']
    recovered_global_top5_dates = recovered_global_top5.loc[:,'6/30/20':'7/1/21']

    # because it is running total, we need to subtract from the day before
    for x in range(len(confirmed_global_top5_dates.columns)-1):
        confirmed_global_top5_dates.iloc[:, 366-x] = confirmed_global_top5_dates.iloc[:,366-x] - confirmed_global_top5_dates.iloc[:,366-x-1]
        recovered_global_top5_dates.iloc[:,366-x] = recovered_global_top5_dates.iloc[:,366-x] - recovered_global_top5_dates.iloc[:,366-x-1]

    # plot on two subplots, first the confirmed
    fig, ax = plt.subplots(1,2)
    ax[0].plot(confirmed_global_top5_dates.iloc[0, 1:], label='US')
    ax[0].plot(confirmed_global_top5_dates.iloc[1, 1:], label='India')
    ax[0].plot(confirmed_global_top5_dates.iloc[2, 1:], label='Brazil')
    ax[0].plot(confirmed_global_top5_dates.iloc[3, 1:], label='France')
    ax[0].plot(confirmed_global_top5_dates.iloc[4, 1:], label='Russia')
    # set labels and title
    ax[0].set(xlabel='Date', ylabel='Confirmed per day', title='Confirmed Cases per day')
    ax[0].legend()

    # plot the recovered
    ax[1].plot(recovered_global_top5_dates.iloc[0, 1:], label='India')
    ax[1].plot(recovered_global_top5_dates.iloc[1, 1:], label='Brazil')
    ax[1].plot(recovered_global_top5_dates.iloc[2, 1:], label='Turkey')
    ax[1].plot(recovered_global_top5_dates.iloc[3, 1:], label='Russia')
    ax[1].plot(recovered_global_top5_dates.iloc[4, 1:], label='Argentina')

    ax[1].set(xlabel='Date', ylabel='Recovered per day', title='Recovered Cases per day')
    plt.show()





def main():
    print('Hello World')
    DailyReportAnalysis()

if __name__ == '__main__':
    main()

