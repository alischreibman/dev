import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Title and intro
st.title("The Caitlin Clark Effect")
st.markdown("Ali Schreibman and Jiwei Li")


st.markdown("""
### Research Question: How has Caitlin Clark's popularity influenced WNBA viewership and overall interest in women's basketball?
""")
st.markdown("""
### 🏀 Who is Caitlin Clark?
Caitlin Clark is an American professional basketball player, and she is one of the greatest collegiate athletes in history who created a phenomenon now known as the “Caitlin Clark effect” due to her dynamic playmaking, deep shooting range, and record-breaking performances that drew unprecedented attention to women's basketball. She was born on January 22, 2002. Clark joined NCAA Division I in 2020 at the University of Iowa and later became the all-time leading scorer and a two-time National Player of the Year. Caitlin Clark's impact on NCAA women's basketball was remarkable, marked by unprecedented levels of viewership and fan engagement. The championship game between Iowa and LSU drew 9.9 million viewers, which was the most-watched women's college basketball game on record. Furthermore, in 2024, because of her presence, several games featuring Iowa drew millions of viewers, as they had become a must-watch attraction. After graduation, Clark joined the WNBA in 2024, which also triggered a historic surge in viewership and fan engagement. The average viewership of regular-season WNBA games on ESPN jumped from 440,000 in 2023 to 1,400,000 in 2024, marking a staggering 218% year-over-year increase. This leap far surpassed the steady but modest growth seen in previous years, where viewership ranged from 171,000 to 440,000 between 2017 and 2023.
""")



# Embed a YouTube video
st.markdown("""
    ### Here is a brief explanation of her impact and some highlights from her rookie year with the Fever!
   
""")
st.markdown("""
    <iframe width="800" height="450" src="https://www.youtube.com/embed/D2gcyLrDLi0" frameborder="0" allowfullscreen></iframe>
""", unsafe_allow_html=True)

st.markdown("""
    <iframe width="800" height="450" src="https://www.youtube.com/embed/ifBI8gk0nmA" frameborder="0" allowfullscreen></iframe>
""", unsafe_allow_html=True)





#--- Data Explanation ---
st.markdown("""
### The Data
Our data was found from a number  of articles scraped from the New York Times as well as related articles. Most of our data is sourced from sports broadcasters such as ESPN and NBC. We also used Statista to fill in some gaps (also sourced from broadcasters).
""")





# --- Viewership Data ---
data = {
    "Year": [2018, 2019, 2020, 2021, 2022, 2023, 2024],
    "WNBA": [0.23,0.25,0.21,0.31,0.37,0.44,1.4],  #  data (in millions)
    "NBA": [1.5,1.4,1.2,1.2,1.4,1.5,1.5],  #  data (in millions)
    "NCAA_W": [2.0,2.1,0,2.0,2.7,5.2,9.3]  # NCAA Women's March Madness viewership
}

df = pd.DataFrame(data)

# --- NBA vs WNBA with Year Range Slider ---
st.markdown("### 📈 NBA vs WNBA Viewership")

# Slider to select year range
min_year, max_year = st.select_slider(
    "Select a year range to view WNBA and NBA data:",
    options=df["Year"].tolist(),
    value=(2018, 2024)
)

# Filter data based on selected range
filtered_df = df[(df["Year"] >= min_year) & (df["Year"] <= max_year)]

# Plot the filtered data
fig1, ax1 = plt.subplots(figsize=(10, 5))
ax1.plot(filtered_df["Year"], filtered_df["WNBA"], marker='o', label="WNBA")
ax1.plot(filtered_df["Year"], filtered_df["NBA"], marker='o', label="NBA")
ax1.set_title(f"WNBA and NBA Average Viewership ({min_year}–{max_year})")
ax1.set_xlabel("Year")
ax1.set_ylabel("Average Viewership (Millions)")
ax1.grid(True)
ax1.legend()
st.pyplot(fig1)
st.markdown("Note: Caitlin Clark was drafted first overall in the 2024 WNBA draft and started playing for the Indiana Fever the following season.")

# --- Chart 2: NCAA Women's March Madness ---
st.markdown("### 📊 NCAA Women's March Madness Viewership")
fig2, ax2 = plt.subplots(figsize=(10, 5))
ax2.plot(df["Year"], df["NCAA_W"], color='purple', marker='o', label="NCAA Women's March Madness")
ax2.set_title("NCAA Women's March Madness Viewership (2018–2024)")
ax2.set_xlabel("Year")
ax2.set_ylabel("Championship Game Viewership (Millions)")
ax2.grid(True)
ax2.legend()
st.pyplot(fig2)
st.markdown("Note: Caitlin Clark joined the NCAA as an Iowa Hawkeye in 2020. There was no March Madness that year due to COVID.")

#Attendance chart

import pandas as pd
import matplotlib.pyplot as plt

# Example Data: Replace this with actual WNBA attendance data.
data2 = {
    'Year': [2018, 2019, 2020, 2021, 2022, 2023, 2024],
    'Attendance': [6311, 5887, 0, 0, 1776, 4067, 17036]
}

# Create a DataFrame
df = pd.DataFrame(data2)

# Streamlit App Title
st.title("Indiana Fever Avg Per Game Attendance Over Time")

# Display the dataset (optional)
st.subheader("Fever Attendance Data")
st.write(df)

# Create a line chart using Matplotlib
fig, ax = plt.subplots()
ax.plot(df['Year'], df['Attendance'], marker='o', color='b', label='Attendance')

# Add labels and title
ax.set_xlabel("Year")
ax.set_ylabel("Attendance")
ax.set_title("WNBA Attendance Over Time")
ax.legend()

# Show the plot in the Streamlit app
st.pyplot(fig)

st.markdown("Note: the Fever did not host fans in 2020 or 2021 due to COVID")

#most viewed games
st.markdown("## 📺 Top 5 Most-Viewed WNBA Games – 2024")

# Corrected list of games with proper keys
top_games = [
    {"title": "5. Indiana Fever at New York Liberty – May 18, 2024", "viewership": "1.71 million viewers on ABC"},
    {"title": "4. Indiana Fever at Connecticut Sun – May 14, 2024", "viewership": "2.12 million viewers on ESPN2"},
    {"title": "3. Seattle Storm at Indiana Fever – August 18, 2024", "viewership": "2.23 million viewers on ABC"},
    {"title": "2. Chicago Sky at Indiana Fever – June 16, 2024", "viewership": "2.25 million viewers on CBS"},
    {"title": "1. Indiana Fever at Chicago Sky – June 23, 2024", "viewership": "2.3 million viewers on ESPN"},
]

# Create a separate expander for each game
for game in top_games:
    with st.expander(f"📺 {game['title']}"):
        st.write(f"**Viewership:** {game['viewership']}")
        

st.markdown("""
Notice how **all five most watched games** from 2024 were played in by Caitlin Clark's team, the Indiana Fever!
""")

st.markdown("""
### More Statistics
- Clark's Indiana Fever jersey is the top selling jersey ever for a draft pick (per Fanatics)
- The 2024 WNBA Draft drew in four times as many viewers as the previous year (2.45 million vs. 572,000, per ESPN)
- Clark's draft also demolished the former draft viewership record (601,000 in 2004, per ESPN)
- Ticket sales soared after Clark was drafted, with one team even upgrading to a bigger arena for their game against the Fever (per the Las Vegas Aces)
""")

st.markdown("""
### Future Work
- More specific merchandise/sales data for both the NBA and WNBA - how many women are buying merch compared to men?
- What other players seem to draw more viewers?
- Data from youth basketball programs - how many girls started playing basketball since 2021?
""")

st.markdown("""
###Conclusion
As you can see, Caitlin Clark has had an incredible impact on the WNBA and interest in women’s basketball. A true superstar, she has brought millions of new fans and viewers to the sport. There is no question that there is indeed a “Caitlin Clark Effect” on women’s basketball.
""")



st.markdown("""
### Sources:
https://www.voronoiapp.com/sports/WNBA-Viewership-Is-Breaking-Records-in-2024--1748
https://sportsmedianews.com/espns-nba-viewership-up-double-digits-from-2020-21-regular-season-average/
https://www.sportsbusinessjournal.com/Articles/2024/04/24/nba-regular-season-viewership/
https://www.sportsmediawatch.com/womens-final-four-ratings-history-espn/
https://espnpressroom.com/us/press-releases/2024/10/the-2024-wnba-season-delivers-record-viewership-across-espn-platforms/
https://www.wnba.com/news/wnba-delivers-record-setting-2024-season 
https://www.nbcnews.com/news/sports/caitlin-clarks-indiana-fever-jersey-becomes-top-selling-jersey-draft-p-rcna148226 
""")