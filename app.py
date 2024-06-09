import streamlit as st
import pandas as pd
import plotly.express as px

def main():
    st.title("World Population Map")

    # File upload
    uploaded_file = st.file_uploader("Upload CSV", type=['csv'])

    if uploaded_file is not None:
        # Load data
        worldpop = pd.read_csv(uploaded_file)
        
        # Sidebar for year selection
        # year = st.sidebar.slider("Select Year", min_value=worldpop['Year'].min(), max_value=worldpop['Year'].max())
        
        # Filter data for selected year
        #filtered_data = worldpop[worldpop['Year'] == year]

        # Get unique years
        unique_years = worldpop["Year"].unique()

        # Sidebar for year selection
        start_year = st.sidebar.number_input("Start Year", min_value=int(unique_years.min()), max_value=int(unique_years.max()), value=int(unique_years.min()))
        end_year = st.sidebar.number_input("End Year", min_value=int(unique_years.min()), max_value=int(unique_years.max()), value=int(unique_years.max()))

        # Filter data for selected year range
        filtered_data = worldpop[(worldpop['Year'] >= start_year) & (worldpop['Year'] <= end_year)]


        # Create choropleth map
        fig = px.choropleth(filtered_data,
                            locations="Country",
                            locationmode="country names",
                            color="Population",
                            hover_name="Country",
                            hover_data=["Country", "Year", "Population"],
                            color_continuous_scale=px.colors.sequential.Plasma,
                            range_color=[filtered_data["Population"].min(), filtered_data["Population"].max()],
                            animation_frame="Year",
                            title="World Population",
                            labels={'Population': 'Population'})
                            #,template='plotly_dark'

        # Update layout
        fig.update_geos(projection_type='equirectangular',
                        showcountries=True,
                        showcoastlines=False,
                        showland=True,
                        landcolor="black",
                        showframe=False,
                        showocean=False,
                        showlakes=False,
                        showrivers=False)

        # Show the map
        st.plotly_chart(fig)

if __name__ == "__main__":
    main()
