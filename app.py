import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
from shiny.express import ui, input, render

# Add page options for the overall app.
ui.page_opts(title="pyshiny App with plot", fillable=True)

# create a sidebar with slider input
with ui.sidebar():
    # Add a slider for specifying the number of bins in the histogram.
    # The ui.input_slider function is called with 5 arguments:
    # 1. A string id ("selected_number_of_bins") that uniquely identifies this input.
    # 2. A string label (e.g., "Number of Bins") to be displayed alongside the slider.
    # 3. An integer representing the minimum number of bins
    # 4. An integer representing the maximum number of bins
    # 5. An integer representing the initial value of the slider
    ui.input_slider(
        "selected_number_of_bins",  # Unique ID for the input value
        "Number of Bins",  # Label displayed alongside the slider
        0,  # Minimum number of bins
        100,  # Maximum number of bins
        20,  # Initial value of the slider
    )

# Define the reactive output chart functions
@render.plot(alt="A histogram")
def histogram():
    np.random.seed(3)
    x = 100 + 15 * np.random.randn(437)
    # Create a histogram plot using the selected number of bins and green color
    plt.hist(x, input.selected_number_of_bins(), density=True, color='green')

@render.plot(alt="A scatterplot")
def scatterplot():
    np.random.seed(42)
    x = np.random.normal(size=100)
    y = np.random.normal(size=100)
    sns.scatterplot(x=x, y=y, color='blue')

