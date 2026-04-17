import matplotlib.pyplot as plt
import seaborn as sns
from cycler import cycler

# Base seaborn style
sns.set_theme(style="whitegrid")

# Custom color cycle to match your Plotly theme
plt.rcParams["axes.prop_cycle"] = cycler(color=[
    "#971C1C",  
    "#FB6363",  
    "#8B0000",  
    "#DC1212",  
    "#FA8072"   
])

# Figure and axes backgrounds
plt.rcParams["figure.facecolor"] = "#FFFFFF"
plt.rcParams["axes.facecolor"] = "#F8F8F8"
plt.rcParams["savefig.facecolor"] = "#FFFFFF"

# Font styling
plt.rcParams["font.family"] = "sans-serif"
plt.rcParams["font.size"] = 12
plt.rcParams["text.color"] = "#000000"
plt.rcParams["axes.labelcolor"] = "#000000"
plt.rcParams["axes.labelweight"] = "bold"
plt.rcParams["axes.labelsize"] = 12
plt.rcParams["xtick.color"] = "#000000"
plt.rcParams["ytick.color"] = "#000000"

# Title styling
plt.rcParams["axes.titlecolor"] = "#000000"
plt.rcParams["axes.titlesize"] = 18
plt.rcParams["axes.titleweight"] = "bold"
plt.rcParams["axes.titlepad"] = 12


# Axis lines and grid
plt.rcParams["axes.edgecolor"] = "#A4A3A3"
plt.rcParams["grid.color"] = "#FFFFFF"
plt.rcParams["grid.linestyle"] = "-"
plt.rcParams["grid.linewidth"] = 1.0

# Legend
plt.rcParams["legend.frameon"] = False
plt.rcParams["legend.facecolor"] = "none"
plt.rcParams["legend.edgecolor"] = "none"

# Optional: cleaner spines
plt.rcParams["axes.spines.top"] = False
plt.rcParams["axes.spines.right"] = False
