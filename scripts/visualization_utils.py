import matplotlib.pyplot as plt
import plotly.express as px

def plot_time_series(data, x_col, y_col, title, plot_type='line'):
    if plot_type == 'line':
        plt.figure(figsize=(10, 6))
        plt.plot(data[x_col], data[y_col], marker='o')
        plt.title(title)
        plt.xlabel(x_col)
        plt.ylabel(y_col)
        plt.grid(True)
        plt.show()
    elif plot_type == 'interactive':
        fig = px.line(data, x=x_col, y=y_col, title=title)
        fig.show()
