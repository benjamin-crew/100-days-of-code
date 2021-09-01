### Day 25 - Intermediate - Working with CSV Data and the Pandas Library

## Pandas

# Reading a CSV
    data = pandas.read_csv("/home/benja/Documents/Development/Python/100-days-of-code/25/weather_data.csv")

# Creating a dataframe

    missing_states_df = pandas.DataFrame(missing_states)
    missing_states_df.to_csv("25/missing_states.csv")

### See main.py for more examples.