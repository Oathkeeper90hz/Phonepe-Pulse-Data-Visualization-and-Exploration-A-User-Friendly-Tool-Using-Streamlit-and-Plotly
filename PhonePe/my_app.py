import streamlit as st
import mysql.connector
import pandas as pd
import plotly.express as px

# Define your database connection parameters
db_config = {
    "host": "localhost",
    "user": "root",
    "password": "######",#your sql password
    "database": "######",#your database
}

# Establish a database connection
connection = mysql.connector.connect(**db_config)

# Create a cursor
mycursor = connection.cursor()

# Function to close the database connection
def close_db_connection():
    mycursor.close()
    connection.close()

# Define CSS for purple color and big font size
purple_style = (
    "color: purple; "
    "font-size: 36px; "
    "font-weight: bold;"
)

# Set page title
st.set_page_config(page_title="PhonePe Info")

# Create a Streamlit sidebar with menu options
menu_choice = st.sidebar.radio("Menu", ["Home", "About", "Analyze Data", "Visualize Data", "Contact"])

# Define the content for the About page
if menu_choice == "Home":
    # Add a custom figure/icon (e.g., using an emoji) before "Home"
    st.markdown(
        """
        <div style="display: flex; align-items: center; gap: 10px;">
            🏠 Home
        </div>
        """,
        unsafe_allow_html=True
    )

    # The rest of your "Home" content goes here

    # Title with purple color and bigger font
    st.markdown("<h1 style='{} font-size: 48px;'>Welcome to PhonePe Home</h1>".format(purple_style),
                unsafe_allow_html=True)

    # Subtitle with purple color and big font
    st.markdown("<h2 style='{}'>PhonePe is a mobile payment platform</h2>".format(purple_style), unsafe_allow_html=True)

    # Create two columns for layout
    left_column, right_column = st.columns(2)

    # PhonePe logo in the left column
    left_column.image("phonepe_logo.png", width=300)

    # Description in violet color in the right column
    with right_column:
        st.markdown(
            """
            <div style="text-align: left; color: purple; font-size: 18px;">
            PhonePe is a mobile payment platform using which you can transfer money using UPI, 
            recharge phone numbers, pay utility bills, etc. PhonePe works on the Unified Payment 
            Interface (UPI) system, and all you need is to feed in your bank account details and create a UPI ID.
            </div>
            """,
            unsafe_allow_html=True
        )

    # Embed a YouTube short video
    st.markdown(
        """
        <iframe width="100%" height="400" src="https://www.youtube.com/embed/mXVXlOhIQH0" frameborder="0" allowfullscreen></iframe>
        """,
        unsafe_allow_html=True
    )

    if st.markdown(
            '<a href="https://play.google.com/store/apps/details?id=com.phonepe.app&pcampaignid=web_share/" style="background-color: red; color: white; padding: 10px 20px; text-decoration: none; border-radius: 5px; font-weight: bold;">Download PhonePe</a>',
            unsafe_allow_html=True
    ):
        pass

    # Add a GIF on the left side
    st.image("phonepe_gif.gif", width=600)

    # Add a description to the right with purple color
    st.markdown(
        """
        <div style="text-align: left; color: purple;">
        Payments on PhonePe are safe, reliable and fast. One in four Indians are now using the PhonePe app to send money, recharge, pay bills and do so much more, in just a few simple clicks. PhonePe has also introduced several Insurance products and Investment options that offer every Indian an equal opportunity to unlock the flow of money, and get access to financial services.
#KarteJaBadhteJa
        </div>
        """,
        unsafe_allow_html=True
    )

    if st.markdown(
            '<a href="https://www.phonepe.com/" style="background-color: red; color: white; padding: 10px 20px; text-decoration: none; border-radius: 5px; font-weight: bold;">Phonepe Website</a>',
            unsafe_allow_html=True
    ):
        pass


if menu_choice == "About":
    # Add a custom figure/icon (e.g., using a star symbol) before "About"
    st.markdown(
        """
        <div style="display: flex; align-items: center; gap: 10px; font-size: 24px;">
            &#9733; About
        </div>
        """,
        unsafe_allow_html=True
    )
    # Title with purple color and bigger font
    st.markdown("<h1 style='{} font-size: 48px;'>PhonePe Pulse</h1>".format(purple_style), unsafe_allow_html=True)

    # Subtitle with purple color and big font
    st.markdown("<h2 style='{}'>PhonePe Pulse is a data analytics and insights platform provided by PhonePe to offer valuable information and trends based on digital transactions and payments.</h2>".format(purple_style), unsafe_allow_html=True)

    # Embed a YouTube short video
    st.markdown(
        """
        <iframe width="100%" height="400" src="https://www.youtube.com/embed/c_1H6vivsiA" frameborder="0" allowfullscreen></iframe>
        """,
        unsafe_allow_html=True
    )

    # Red button for "Phonepe Pulse" with a link
    if st.markdown(
            '<a href="https://www.phonepe.com/pulse/" style="background-color: red; color: white; padding: 10px 20px; text-decoration: none; border-radius: 5px; font-weight: bold;">PhonePe Pulse</a>',
            unsafe_allow_html=True
    ):
        pass  # Add an action here if needed

    st.markdown(
            """
            <div style="text-align: left; color: purple;">
            The Indian digital payments story has truly captured the world's imagination. From the largest towns to the remotest villages, there is a payments revolution being driven by the penetration of mobile phones and data.

When PhonePe started 5 years back, we were constantly looking for definitive data sources on digital payments in India. Some of the questions we were seeking answers to were - How are consumers truly using digital payments? What are the top cases? Are kiranas across Tier 2 and 3 getting a facelift with the penetration of QR codes?
This year as we became India's largest digital payments platform with 46% UPI market share, we decided to demystify the what, why and how of digital payments in India.

This year, as we crossed 2000 Cr. transactions and 30 Crore registered users, we thought as India's largest digital payments platform with 46% UPI market share, we have a ring-side view of how India sends, spends, manages and grows its money. So it was time to demystify and share the what, why and how of digital payments in India.

PhonePe Pulse is your window to the world of how India transacts with interesting trends, deep insights and in-depth analysis based on our data put together by the PhonePe team.
            </div>
            """,
            unsafe_allow_html=True
        )

    # Subtitle with purple color and big font
    st.markdown("<h2 style='{}'>PhonePe Pulse Github</h2>".format(purple_style), unsafe_allow_html=True)

    st.markdown(
        """
        <div style="text-align: left; color: purple;">
        PhonePe Pulse goal is to share this data with everyone (license below), so that you can build your own understanding, insights and visualization on how digital payments have evolved over the years in India.
        </div>
        """,
        unsafe_allow_html=True
    )

    if st.markdown(
            '<a href="https://github.com/PhonePe/pulse/" style="background-color: red; color: white; padding: 10px 20px; text-decoration: none; border-radius: 5px; font-weight: bold;">Pulse Github</a>',
            unsafe_allow_html=True
    ):
        pass  # Add an action here if neededhttps://github.com/PhonePe/pulse

# Define the content for the Analyze Data page
if menu_choice == "Analyze Data":
    st.markdown(
        """
        <div style="display: flex; align-items: center; gap: 10px; font-size: 24px;">
            &#x1F4C8; Analyze Data
        </div>
        """,
        unsafe_allow_html=True
    )

    # Create a dropdown box to select data type
    data_type = st.selectbox("Select Data Type", ("Transactions", "Users"))

    # Create a dropdown box to select year
    selected_year = st.selectbox("Select Year", list(range(2018, 2024)))

    # Create a dropdown box to select quarter
    selected_quarter = st.selectbox("Select Quarter", [1, 2, 3, 4])

    # Create a dropdown box to select chart type
    chart_type = st.selectbox("Select Chart Type", ("Pie Chart", "Bar Chart", "Line Chart"))

    if data_type == "Transactions":
        # Create a 1x3 grid layout for the charts
        col1, col2, col3 = st.columns(3)

        # Query the database to retrieve data from agg_transac table
        query1 = f"""
            SELECT State, Transaction_count
            FROM agg_transac
            WHERE Year = {selected_year} AND Quarter = {selected_quarter}
            ORDER BY Transaction_count DESC
            LIMIT 10
        """
        df1 = pd.read_sql_query(query1, connection)

        # Create a chart based on the selected chart type
        if chart_type == "Pie Chart":
            fig1 = px.pie(df1, values='Transaction_count', names='State',
                          title=f'Top States with Highest Transactions ({selected_year}, Q{selected_quarter})')
        elif chart_type == "Bar Chart":
            fig1 = px.bar(df1, x='State', y='Transaction_count',
                          title=f'Top States with Highest Transactions ({selected_year}, Q{selected_quarter})')
        elif chart_type == "Line Chart":
            fig1 = px.line(df1, x='State', y='Transaction_count',
                           title=f'Trend of Transactions in States ({selected_year}, Q{selected_quarter})')

        col1.plotly_chart(fig1, use_container_width=True)

        # Query the database to retrieve data from map_transac table
        query2 = f"""
            SELECT District, SUM(Amount) AS Total_Payments
            FROM map_transac
            WHERE Year = {selected_year} AND Quarter = {selected_quarter}
            GROUP BY District
            ORDER BY Total_Payments DESC
            LIMIT 10
        """
        df2 = pd.read_sql_query(query2, connection)

        # Create a chart based on the selected chart type
        if chart_type == "Pie Chart":
            fig2 = px.pie(df2, values='Total_Payments', names='District',
                          title=f'Top Districts with Highest Payments ({selected_year}, Q{selected_quarter})')
        elif chart_type == "Bar Chart":
            fig2 = px.bar(df2, x='District', y='Total_Payments',
                          title=f'Top Districts with Highest Payments ({selected_year}, Q{selected_quarter})')
        elif chart_type == "Line Chart":
            fig2 = px.line(df2, x='District', y='Total_Payments',
                           title=f'Trend of Payments in Districts ({selected_year}, Q{selected_quarter})')

        col2.plotly_chart(fig2, use_container_width=True)

        # Query the database to retrieve data from top_transac table
        query3 = f"""
            SELECT Pincode, Transaction_amount
            FROM top_transac
            WHERE Year = {selected_year} AND Quarter = {selected_quarter}
            ORDER BY Transaction_amount DESC
            LIMIT 10
        """
        df3 = pd.read_sql_query(query3, connection)

        # Create a chart based on the selected chart type
        if chart_type == "Pie Chart":
            fig3 = px.pie(df3, values='Transaction_amount', names='Pincode',
                          title=f'Top Pincodes with Highest Payments ({selected_year}, Q{selected_quarter})')
        elif chart_type == "Bar Chart":
            fig3 = px.bar(df3, x='Pincode', y='Transaction_amount',
                          title=f'Top Pincodes with Highest Payments ({selected_year}, Q{selected_quarter})')
        elif chart_type == "Line Chart":
            fig3 = px.line(df3, x='Pincode', y='Transaction_amount',
                           title=f'Trend of Payments in Pincodes ({selected_year}, Q{selected_quarter})')

        col3.plotly_chart(fig3, use_container_width=True)


    if data_type == "Users":
        # Create a 1x3 grid layout for the charts
        col1, col2, col3 = st.columns(3)

        # Query the database to retrieve data from agg_user table
        query1 = f"""
            SELECT Brands, SUM(Count) AS Total_Count
            FROM agg_user
            WHERE Year = {selected_year} AND Quarter = {selected_quarter}
            GROUP BY Brands
            ORDER BY Total_Count DESC
            LIMIT 10
        """
        df1 = pd.read_sql_query(query1, connection)

        # Create a chart based on the selected chart type
        if chart_type == "Pie Chart":
            fig1 = px.pie(df1, values='Total_Count', names='Brands',
                          title=f'Top Brands with Highest Payments ({selected_year}, Q{selected_quarter})')
        elif chart_type == "Bar Chart":
            fig1 = px.bar(df1, x='Brands', y='Total_Count',
                          title=f'Top Brands with Highest Payments ({selected_year}, Q{selected_quarter})')
        elif chart_type == "Line Chart":
            fig1 = px.line(df1, x='Brands', y='Total_Count',
                           title=f'Trend of Brands with Payments ({selected_year}, Q{selected_quarter})')

        col1.plotly_chart(fig1, use_container_width=True)

        # Query the database to retrieve data from map_user table
        query2 = f"""
            SELECT District, SUM(Registered_user) AS Total_Users
            FROM map_user
            WHERE Year = {selected_year} AND Quarter = {selected_quarter}
            GROUP BY District
            ORDER BY Total_Users DESC
            LIMIT 10
        """
        df2 = pd.read_sql_query(query2, connection)

        # Create a chart based on the selected chart type
        if chart_type == "Pie Chart":
            fig2 = px.pie(df2, values='Total_Users', names='District',
                          title=f'Top Districts with Highest Users ({selected_year}, Q{selected_quarter})')
        elif chart_type == "Bar Chart":
            fig2 = px.bar(df2, x='District', y='Total_Users',
                          title=f'Top Districts with Highest Users ({selected_year}, Q{selected_quarter})')
        elif chart_type == "Line Chart":
            fig2 = px.line(df2, x='District', y='Total_Users',
                           title=f'Trend of Users in Districts ({selected_year}, Q{selected_quarter})')

        col2.plotly_chart(fig2, use_container_width=True)

        # Query the database to retrieve data from top_user table
        query3 = f"""
            SELECT Pincode, SUM(Registered_users) AS Total_Registered_Users
            FROM top_user
            WHERE Year = {selected_year} AND Quarter = {selected_quarter}
            GROUP BY Pincode
            ORDER BY Total_Registered_Users DESC
            LIMIT 10
        """
        df3 = pd.read_sql_query(query3, connection)

        # Create a chart based on the selected chart type
        if chart_type == "Pie Chart":
            fig3 = px.pie(df3, values='Total_Registered_Users', names='Pincode',
                          title=f'Top Pincodes with Highest Registered Users ({selected_year}, Q{selected_quarter})')
        elif chart_type == "Bar Chart":
            fig3 = px.bar(df3, x='Pincode', y='Total_Registered_Users',
                          title=f'Top Pincodes with Highest Registered Users ({selected_year}, Q{selected_quarter})')
        elif chart_type == "Line Chart":
            fig3 = px.line(df3, x='Pincode', y='Total_Registered_Users',
                           title=f'Trend of Registered Users in Pincodes ({selected_year}, Q{selected_quarter})')

        col3.plotly_chart(fig3, use_container_width=True)

# Visualize Data section
if menu_choice == "Visualize Data":
    st.markdown(
        """
        <div style="display: flex; align-items: center; gap: 10px; font-size: 24px;">
            🌍 Visualize Data
        </div>
        """,
        unsafe_allow_html=True
    )

    # Create a dropdown box to select data type
    data_type = st.selectbox("Select Data Type", ("Transactions", "Count"))

    # Explore Data section
    if data_type == "Transactions":
        selected_year = st.selectbox("Select Year", list(range(2018, 2024)))
        selected_quarter = st.selectbox("Select Quarter", [1, 2, 3, 4])

        col1, col2 = st.columns(2)

        # EXPLORE DATA - TRANSACTIONS
        if data_type == "Transactions":
            st.markdown("## :violet[Aggregate State Transactions Value]")

            # Query the database to get transaction data
            query = f"""
                SELECT
                    State,
                    SUM(count) AS Total_Transactions,
                    SUM(amount) AS Total_amount
                FROM
                    map_transac
                WHERE
                    year = {selected_year}
                    AND quarter = {selected_quarter}
                GROUP BY
                    State
                ORDER BY
                    State
            """
            mycursor.execute(query)

            # Fetch data and create a DataFrame
            data = mycursor.fetchall()
            columns = ['State', 'Total_Transactions', 'Total_amount']
            df1 = pd.DataFrame(data, columns=columns)

            # Load state names from a CSV file
            df2 = pd.read_csv('States.csv')
            df1['state'] = df2['state']

            # Create a choropleth map
            fig = px.choropleth(
                df1,
                geojson="https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson",
                featureidkey='properties.ST_NM',
                locations='state',
                color='Total_amount',
                color_continuous_scale='blues'
            )

            fig.update_geos(fitbounds="locations", visible=False)
            col1.plotly_chart(fig, use_container_width=True)

    # EXPLORE DATA - COUNT
    elif data_type == "Count":

        selected_year_count = st.selectbox("Select Year for Count", list(range(2018, 2024)))
        selected_quarter_count = st.selectbox("Select Quarter for Count", [1, 2, 3, 4])


        col1, col2 = st.columns(2)  # Define col1 and col2 for the "Count" section

        # Query the database to get transaction count data
        query = f"""
            SELECT
                State,
                SUM(count) AS Total_Count
            FROM
                map_transac
            WHERE
                year = {selected_year_count}
                AND quarter = {selected_quarter_count}
            GROUP BY
                State
            ORDER BY
                State
        """
        mycursor.execute(query)

        # Fetch data and create a DataFrame
        data = mycursor.fetchall()
        columns = ['State', 'Total_Count']
        df_count = pd.DataFrame(data, columns=columns)

        # Load state names from a CSV file
        df2 = pd.read_csv('States.csv')
        df_count['state'] = df2['state']

        # Create a choropleth map for transaction count
        fig_count = px.choropleth(
            df_count,
            geojson="https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson",
            featureidkey='properties.ST_NM',
            locations='state',
            color='Total_Count',
            color_continuous_scale='greens'
        )
        st.markdown("## :green[Transaction Count by State]")

        fig_count.update_geos(fitbounds="locations", visible=False)
        col1.plotly_chart(fig_count, use_container_width=True)

    # Create a dropdown box for selecting queries
    selected_query = st.selectbox("Select Query", [
        "Top states in 2023 with the highest transactions",
        "Top states in 2023 with the highest transaction amounts",
        "Top districts in 2023 with the highest transaction counts",
        "Top districts in 2023 with the highest transaction amounts",
        "Top pincodes in 2023 with the highest transaction counts",
        "Total transaction counts by state in 2023",
        "Total transaction amounts by state in 2023",
        "Total user counts by brand in 2023",
        "Total transaction counts by district in 2023",
        "Total registered user counts by district in 2023"
    ])

    # Depending on the selected query, execute the corresponding SQL query and update the visualization
    if selected_query == "Top states in 2023 with the highest transactions":
        # SQL query for the selected query
        query = """
           SELECT State, Transaction_count
           FROM agg_transac
           WHERE Year = 2023
           ORDER BY Transaction_count DESC
           LIMIT 10;
           """
        # Execute the query and create a DataFrame
        mycursor.execute(query)
        data = mycursor.fetchall()
        columns = ['State', 'Transaction_count']
        df = pd.DataFrame(data, columns=columns)

        # Create a bar chart to visualize the data
        fig = px.bar(df, x='State', y='Transaction_count',
                     title='Top States in 2023 with the Highest Transactions')
        st.plotly_chart(fig, use_container_width=True)

    elif selected_query == "Top states in 2023 with the highest transaction amounts":
        # SQL query for the selected query
        query = """
           SELECT State, Transaction_amount
           FROM agg_transac
           WHERE Year = 2023
           ORDER BY Transaction_amount DESC
           LIMIT 10;
           """
        # Execute the query and create a DataFrame
        mycursor.execute(query)
        data = mycursor.fetchall()
        columns = ['State', 'Transaction_amount']
        df = pd.DataFrame(data, columns=columns)

        # Create a bar chart to visualize the data
        fig = px.bar(df, x='State', y='Transaction_amount',
                     title='Top States in 2023 with the Highest Transaction Amounts')
        st.plotly_chart(fig, use_container_width=True)

    elif selected_query == "Top districts in 2023 with the highest transaction counts":
        # SQL query for the selected query
        query = """
           SELECT District, SUM(Count) AS Total_Transaction_Count
           FROM map_transac
           WHERE Year = 2023
           GROUP BY District
           ORDER BY Total_Transaction_Count DESC
           LIMIT 10;
           """
        # Execute the query and create a DataFrame
        mycursor.execute(query)
        data = mycursor.fetchall()
        columns = ['District', 'Total_Transaction_Count']
        df = pd.DataFrame(data, columns=columns)

        # Create a bar chart to visualize the data
        fig = px.bar(df, x='District', y='Total_Transaction_Count',
                     title='Top Districts in 2023 with the Highest Transaction Counts')
        st.plotly_chart(fig, use_container_width=True)

    elif selected_query == "Top districts in 2023 with the highest transaction amounts":
        # SQL query for the selected query
        query = """
           SELECT District, SUM(Amount) AS Total_Transaction_Amount
           FROM map_transac
           WHERE Year = 2023
           GROUP BY District
           ORDER BY Total_Transaction_Amount DESC
           LIMIT 10;
           """
        # Execute the query and create a DataFrame
        mycursor.execute(query)
        data = mycursor.fetchall()
        columns = ['District', 'Total_Transaction_Amount']
        df = pd.DataFrame(data, columns=columns)

        # Create a bar chart to visualize the data
        fig = px.bar(df, x='District', y='Total_Transaction_Amount',
                     title='Top Districts in 2023 with the Highest Transaction Amounts')
        st.plotly_chart(fig, use_container_width=True)

    elif selected_query == "Top pincodes in 2023 with the highest transaction counts":
        # SQL query for the selected query
        query = """
           SELECT Pincode, Transaction_count
           FROM top_transac
           WHERE Year = 2023
           ORDER BY Transaction_count DESC
           LIMIT 10;
           """
        # Execute the query and create a DataFrame
        mycursor.execute(query)
        data = mycursor.fetchall()
        columns = ['Pincode', 'Transaction_count']
        df = pd.DataFrame(data, columns=columns)

        # Create a bar chart to visualize the data
        fig = px.bar(df, x='Pincode', y='Transaction_count',
                     title='Top Pincodes in 2023 with the Highest Transaction Counts')
        st.plotly_chart(fig, use_container_width=True)

    elif selected_query == "Total transaction counts by state in 2023":
        # SQL query for the selected query
        query = """
           SELECT State, SUM(Transaction_count) AS Total_Transaction_Count
           FROM agg_transac
           WHERE Year = 2023
           GROUP BY State;
           """
        # Execute the query and create a DataFrame
        mycursor.execute(query)
        data = mycursor.fetchall()
        columns = ['State', 'Total_Transaction_Count']
        df = pd.DataFrame(data, columns=columns)

        # Create a bar chart to visualize the data
        fig = px.bar(df, x='State', y='Total_Transaction_Count',
                     title='Total Transaction Counts by State in 2023')
        st.plotly_chart(fig, use_container_width=True)

    elif selected_query == "Total transaction amounts by state in 2023":
        # SQL query for the selected query
        query = """
           SELECT State, SUM(Transaction_amount) AS Total_Transaction_Amount
           FROM agg_transac
           WHERE Year = 2023
           GROUP BY State;
           """
        # Execute the query and create a DataFrame
        mycursor.execute(query)
        data = mycursor.fetchall()
        columns = ['State', 'Total_Transaction_Amount']
        df = pd.DataFrame(data, columns=columns)

        # Create a bar chart to visualize the data
        fig = px.bar(df, x='State', y='Total_Transaction_Amount',
                     title='Total Transaction Amounts by State in 2023')
        st.plotly_chart(fig, use_container_width=True)

    elif selected_query == "Total user counts by brand in 2023":
        # SQL query for the selected query
        query = """
           SELECT Brands, SUM(Count) AS Total_User_Count
           FROM agg_user
           WHERE Year = 2023
           GROUP BY Brands;
           """
        # Execute the query and create a DataFrame
        mycursor.execute(query)
        data = mycursor.fetchall()
        columns = ['Brands', 'Total_User_Count']
        df = pd.DataFrame(data, columns=columns)

        # Create a bar chart to visualize the data
        fig = px.bar(df, x='Brands', y='Total_User_Count',
                     title='Total User Counts by Brand in 2023')
        st.plotly_chart(fig, use_container_width=True)

    elif selected_query == "Total transaction counts by district in 2023":
        # SQL query for the selected query
        query = """
           SELECT District, SUM(Count) AS Total_Transaction_Count
           FROM map_transac
           WHERE Year = 2023
           GROUP BY District;
           """
        # Execute the query and create a DataFrame
        mycursor.execute(query)
        data = mycursor.fetchall()
        columns = ['District', 'Total_Transaction_Count']
        df = pd.DataFrame(data, columns=columns)

        # Create a bar chart to visualize the data
        fig = px.bar(df, x='District', y='Total_Transaction_Count',
                     title='Total Transaction Counts by District in 2023')
        st.plotly_chart(fig, use_container_width=True)

    elif selected_query == "Total registered user counts by district in 2023":
        # SQL query for the selected query
        query = """
           SELECT District, SUM(Registered_user) AS Total_Registered_Users
           FROM map_user
           WHERE Year = 2023
           GROUP BY District;
           """
        # Execute the query and create a DataFrame
        mycursor.execute(query)
        data = mycursor.fetchall()
        columns = ['District', 'Total_Registered_Users']
        df = pd.DataFrame(data, columns=columns)

        # Create a bar chart to visualize the data
        fig = px.bar(df, x='District', y='Total_Registered_Users',
                     title='Total Registered User Counts by District in 2023')
        st.plotly_chart(fig, use_container_width=True)



# Define the content for the Contact page
if menu_choice == "Contact":
    # Add a custom figure/icon (e.g., using an educated boy emoji) before "Contact"
    st.markdown(
        """

        <div style="display: flex; align-items: center; gap: 10px; font-size: 24px;">
            🎓 Contact
        </div>
        """,
        unsafe_allow_html=True
    )


    st.write("Regards,")
    st.write(
        "I am thrilled to share my successful completion of the 'Phonepe Pulse Data Visualization and Exploration' project. Leveraging technologies such as Github Cloning, Python, Pandas, MySQL, Streamlit, and Plotly, we've crafted an innovative fintech solution.")
    st.write(
        "My journey began with extracting vast data from the Phonepe Pulse Github repository, skillfully transforming and cleaning it for analysis. The data found a secure home in a MySQL database, ensuring efficient storage and retrieval.")
    st.write(
        "The true highlight of my project is the creation of an interactive geo visualization dashboard using Streamlit and Plotly. This dynamic interface offers users a wealth of insights, with over 10 dropdown options to explore different facets of the data.")
    st.write(
        "My solution isn't just efficient; it's also user-friendly and secure. I've rigorously tested it and now proudly offer a publicly accessible dashboard. It's a valuable resource for data analysis and decision-making, bringing Phonepe Pulse data to life.")
    st.write(
        "With gratitude for the support and guidance from GUVI Geek Networks and the IIT Madras Data Science Programme at IIT Madras Research Park (IITMRP), as well as the collaborative efforts of IITMDSA Zen DataScience, GUVI, we look forward to more exciting ventures ahead.")
    st.write("Best Regards,")
    st.write("🎓Rajashekhara S Gowda")
    st.write("For any inquiries or assistance, please feel free to contact me at:")
    st.write("Email: rajusgowda522000@gmail.com")
    st.write("LinkedIn:https://www.linkedin.com/in/raju-s-gowda-5f2000")

    st.write("For any inquiries or assistance, please feel free to contact us at:")