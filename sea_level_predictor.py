import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress
import numpy as np

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    x = df['Year']
    y = df['CSIRO Adjusted Sea Level']
    plt.scatter(x, y, alpha=0.9, cmap='Spectral')

    # Create first line of best fit
    lin_out = linregress(x,y)
    fig, ax = plt.subplots(figsize=(10,5))
    ax.scatter(x,y)
    x_fit= np.linspace(df['Year'].min(),2050)
    y_fit =  x_fit*lin_out[0] + lin_out[1]
    ax.plot(x_fit,y_fit)
    # Create second line of best fit
    x2= df['Year'][120: -1]
    y2= df['CSIRO Adjusted Sea Level'][120:-1]
    lin_out2 = linregress(x2,y2)
    x_fit2= np.linspace(2000,2050)
    y_fit2 =  x_fit*lin_out2[0] + lin_out2[1]
    ax.plot(x_fit2 ,y_fit2)


    # Add labels and title
    ax.set_title("Rise in Sea Level")
    ax.set_xlabel('Year')
    ax.set_ylabel('Sea Level (inches)')
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()