import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.seasonal import seasonal_decompose

# Function to decompose time series
def decompose_time_series(data, date_column, value_column, period):
    data[date_column] = pd.to_datetime(data[date_column])
    data.set_index(date_column, inplace=True)
    
    try:
        decomposition = seasonal_decompose(data[value_column], model='additive', period=period)
        trend = decomposition.trend
        seasonal = decomposition.seasonal
        residual = decomposition.resid
    except ValueError as e:
        print(f"Error: {e}")
        return None, None, None
    
    return trend, seasonal, residual

# Function to plot time series
def plot_time_series(data, x_col, y_col, title):
    plt.figure(figsize=(10, 6))
    plt.plot(data[x_col], data[y_col], marker='o')
    plt.title(title)
    plt.xlabel(x_col)
    plt.ylabel(y_col)
    plt.grid(True)
    plt.show()

# Load data
def load_data(file_path):
    return pd.read_csv(file_path)

# Main function
def main():
    # Load data
    sprint_velocity = load_data('data/sprint_velocity.csv')
    backlog_size = load_data('data/backlog_size.csv')
    team_productivity = load_data('data/team_productivity.csv')

    # Print first few rows of each dataset to verify
    print("Sprint Velocity Data:")
    print(sprint_velocity.head())

    print("\nBacklog Size Data:")
    print(backlog_size.head())

    print("\nTeam Productivity Data:")
    print(team_productivity.head())

    # Perform time series decomposition for each dataset
    trend_velocity, seasonal_velocity, residual_velocity = decompose_time_series(sprint_velocity, 'Date', 'Velocity', period=12)
    trend_backlog, seasonal_backlog, residual_backlog = decompose_time_series(backlog_size, 'Date', 'BacklogSize', period=12)
    trend_productivity, seasonal_productivity, residual_productivity = decompose_time_series(team_productivity, 'Date', 'Productivity', period=12)

    if trend_velocity is not None:
        # Plot decomposed components for each dataset
        trend_velocity.plot(title='Sprint Velocity Trend')
        plt.show()

        seasonal_velocity.plot(title='Sprint Velocity Seasonality')
        plt.show()

        residual_velocity.plot(title='Sprint Velocity Residuals')
        plt.show()

        # Plot original time series for each dataset
        plot_time_series(sprint_velocity, 'Date', 'Velocity', 'Sprint Velocity Over Time')
        plot_time_series(backlog_size, 'Date', 'BacklogSize', 'Backlog Size Over Time')
        plot_time_series(team_productivity, 'Date', 'Productivity', 'Team Productivity Over Time')

if __name__ == "__main__":
    main()
import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.seasonal import seasonal_decompose

# Function to decompose time series
def decompose_time_series(data, date_column, value_column, period):
    data[date_column] = pd.to_datetime(data[date_column])
    data.set_index(date_column, inplace=True)
    
    try:
        decomposition = seasonal_decompose(data[value_column], model='additive', period=period)
        trend = decomposition.trend
        seasonal = decomposition.seasonal
        residual = decomposition.resid
    except ValueError as e:
        print(f"Error: {e}")
        return None, None, None
    
    return trend, seasonal, residual

# Function to plot time series
def plot_time_series(data, x_col, y_col, title):
    plt.figure(figsize=(10, 6))
    plt.plot(data[x_col], data[y_col], marker='o')
    plt.title(title)
    plt.xlabel(x_col)
    plt.ylabel(y_col)
    plt.grid(True)
    plt.show()

# Load data
def load_data(file_path):
    return pd.read_csv(file_path)

# Main function
def main():
    # Load data
    sprint_velocity = load_data('data\\sprint_velocity.csv')
    backlog_size = load_data('data\\backlog_size.csv')
    team_productivity = load_data('data\\team_productivity.csv')

    # Print first few rows of each dataset to verify
    print("Sprint Velocity Data:")
    print(sprint_velocity.head())

    print("\nBacklog Size Data:")
    print(backlog_size.head())

    print("\nTeam Productivity Data:")
    print(team_productivity.head())

    # Perform time series decomposition for each dataset
    trend_velocity, seasonal_velocity, residual_velocity = decompose_time_series(sprint_velocity, 'Date', 'Velocity', period=12)
    trend_backlog, seasonal_backlog, residual_backlog = decompose_time_series(backlog_size, 'Date', 'BacklogSize', period=12)
    trend_productivity, seasonal_productivity, residual_productivity = decompose_time_series(team_productivity, 'Date', 'Productivity', period=12)

    if trend_velocity is not None:
        # Plot decomposed components for each dataset
        trend_velocity.plot(title='Sprint Velocity Trend')
        plt.show()

        seasonal_velocity.plot(title='Sprint Velocity Seasonality')
        plt.show()

        residual_velocity.plot(title='Sprint Velocity Residuals')
        plt.show()

        # Plot original time series for each dataset
        plot_time_series(sprint_velocity, 'Date', 'Velocity', 'Sprint Velocity Over Time')
        plot_time_series(backlog_size, 'Date', 'BacklogSize', 'Backlog Size Over Time')
        plot_time_series(team_productivity, 'Date', 'Productivity', 'Team Productivity Over Time')

if __name__ == "__main__":
    main()
