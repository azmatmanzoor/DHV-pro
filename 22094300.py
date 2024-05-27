import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import pandas as pd

# Load data from Excel file
file_path = 'cinema.xlsx'
df = pd.read_excel(file_path)

# Extract data
years = df['Year'].tolist()
admissions = df['Admissions (million)'].tolist()

# gradient color list
colors = plt.cm.viridis(np.linspace(0, 1, len(years)))

#bar chart
fig, ax = plt.subplots(figsize=(12, 7))
bars = ax.bar(years, admissions, color=colors, edgecolor='black', linewidth=1)

# title and labels
ax.set_title('Annual UK Cinema Admissions (2012-2021)', fontsize=16, fontweight='bold', color="red")
ax.set_xlabel('Year', fontsize=14, color="red")
ax.set_ylabel('Admissions (million)', fontsize=16, color="red")
ax.set_xticks(years)
ax.set_xticklabels(years, rotation=45)

# gridlines
ax.grid(True, linestyle='--', alpha=0.6)

# Annotate bars
for bar in bars:
    yval = bar.get_height()
    ax.text(bar.get_x() + bar.get_width() / 2, yval + 5, f'{yval}', ha='center', va='bottom', fontsize=10, fontweight='bold', color='dimgrey')

# Remove the top and right spines
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

# Highlight the drastic change in 2020 and 2021
for i, bar in enumerate(bars):
    if years[i] in [2020, 2021]:
        bar.set_edgecolor('red')
        bar.set_linewidth(3)

#  background color
fig.patch.set_facecolor('#f5f5f5')
ax.set_facecolor('#f5f5f5')

# Display the bar chart
plt.tight_layout()




# pie chart


# Extract data
territories = df['Territory'].tolist()
admissions_2021 = df['Admissions 2021 (million)'].tolist()

# Custom colors for the pie chart
colors = [
    '#ff9999', '#66b3ff', '#99ff99', '#ffcc99', '#c2c2f0', '#ffb3e6',
    '#c4e17f', '#76d7c4', '#f7b7a3', '#d9e3f0', '#ffb6c1', '#d1c4e9',
    '#b3e5fc'
]

# Ensure the color list is as long as the territories list
if len(colors) < len(territories):
    colors = colors * (len(territories) // len(colors)) + colors[:len(territories) % len(colors)]

# Explode effect to highlight a specific section (for demonstration, explode 'India')
explode = [0.1 if territory == 'India' else 0 for territory in territories]

# Create pie chart
fig, ax = plt.subplots(figsize=(8, 7))

wedges, texts, autotexts = ax.pie(
    admissions_2021,
    explode=explode,
    labels=territories,
    colors=colors,
    autopct='%1.1f%%',
    startangle=140,
    pctdistance=0.85,
    shadow=True,  # Add shadow for a 3D effect
    wedgeprops={'edgecolor': 'black', 'linewidth': 1.5}
)

# Draw a circle at the center of pie to make it look like a donut
centre_circle = plt.Circle((0, 0), 0.60, fc='white')
fig.gca().add_artist(centre_circle)

# Customizing text
for text in texts:
    text.set_fontsize(12)
    text.set_fontweight('bold')

for autotext in autotexts:
    autotext.set_fontsize(10)
    autotext.set_fontweight('bold')
    autotext.set_color('dimgrey')

# title
ax.set_title('\n\nLargest Cinema Markets by Admissions in 2021', fontsize=16, fontweight='bold', color="red")

# Equal aspect ratio ensures that pie is drawn as a circle.
ax.axis('equal')

# legend outside the pie chart
ax.legend(wedges, territories, title="Territories", loc="center left", bbox_to_anchor=(1, 0, 0.5, 1))

plt.tight_layout()




# line plot


box_office_gross = df['Box office gross (£ million)'].tolist()
change_on_previous_year = df['Change on previous year %'].tolist()
change_since_2012 = df['Change since 2012 %'].tolist()

# Create the plot
fig, ax1 = plt.subplots(figsize=(14, 8))

# Plot the box office gross
color = 'tab:blue'
ax1.set_xlabel('Year', color="red", fontsize=16, fontweight='bold')
ax1.set_ylabel('Box Office Gross (£ million)', color="red", fontsize=16)
ax1.plot(years, box_office_gross, color=color, marker='o', linestyle='-', linewidth=2, markersize=6)
ax1.tick_params(axis='y', labelcolor=color)

# secondary y-axis to plot the percentage changes
ax2 = ax1.twinx()
color = 'tab:red'
ax2.set_ylabel('Change %', color="red", fontsize=16, fontweight='bold')
ax2.plot(years, change_on_previous_year, color=color, marker='x', linestyle='--', linewidth=2, markersize=6, label='Change on Previous Year')
ax2.plot(years, change_since_2012, color='tab:green', marker='^', linestyle='-.', linewidth=2, markersize=6, label='Change since 2012')
ax2.tick_params(axis='y', labelcolor=color)

# title and grid
plt.title('UK Box Office Trends (2012-2021)', fontsize=16, fontweight='bold', color='red')
ax1.grid(True)

# legends
fig.tight_layout()
ax2.legend(loc='upper left', bbox_to_anchor=(0.15, 0.85))




#scatter plot 

# Extract data
years = df['Year'].tolist()
gross_top_20 = df['Gross box office of top 20'].tolist()
gross_21_50 = df['Gross box office of 21-50'].tolist()
gross_51_100 = df['Gross box office of 51-100'].tolist()
gross_rest = df['Gross box office of rest'].tolist()

sns.set(style="whitegrid")

# figure and axis
fig, ax = plt.subplots(figsize=(14, 8))

# Plot data with different markers and colors
sns.scatterplot(x=years, y=gross_top_20, s=100, color='b', marker='o', label='Top 20 Films', ax=ax)
sns.scatterplot(x=years, y=gross_21_50, s=100, color='g', marker='s', label='21-50 Films', ax=ax)
sns.scatterplot(x=years, y=gross_51_100, s=100, color='r', marker='^', label='51-100 Films', ax=ax)
sns.scatterplot(x=years, y=gross_rest, s=100, color='purple', marker='D', label='Rest of Films', ax=ax)

# annotations
for i, year in enumerate(years):
    ax.text(year, gross_top_20[i], f'{gross_top_20[i]:.1f}', color='b', ha='right', va='bottom',fontweight='bold')
    ax.text(year, gross_21_50[i], f'{gross_21_50[i]:.1f}', color='g', ha='right', va='bottom',fontweight='bold')
    ax.text(year, gross_51_100[i], f'{gross_51_100[i]:.1f}', color='r', ha='right', va='bottom',fontweight='bold')
    ax.text(year, gross_rest[i], f'{gross_rest[i]:.1f}', color='purple', ha='right', va='bottom',fontweight='bold')

# Customization
ax.set_title('Gross Box Office of Different Film Groups (2012-2021)', fontsize=16, fontweight='bold', color="red")
ax.set_xlabel('Year', fontsize=14, color="red")
ax.set_ylabel('Gross Box Office (£ million)', fontsize=14, color="red")
ax.legend()
ax.grid(True)
plt.savefig("22094300.png", dpi=300)





