#This script changed the date format from iTunes mm/dd/yyyy to yyyy/mm/dd
#will also strip date time
import pandas as pd
import os

file = input("Enter name of file to convert:")

# Read the file and specify which column is the date
track_list = pd.read_csv(file)

# Output with dates converted to YYYY-MM-DD
track_list["Date Added"] = pd.to_datetime(track_list["Date Added"]).dt.strftime("%Y-%m-%d")
track_list["Last Played"] = pd.to_datetime(track_list["Last Played"]).dt.strftime("%Y-%m-%d")
track_list["Last Skipped"] = pd.to_datetime(track_list["Last Skipped"]).dt.strftime("%Y-%m-%d")

output = input("Name of file for output:")

track_list.to_csv(output)
