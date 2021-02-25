#This script changed the date format from iTunes mm/dd/yyyy to yyyy/mm/dd 
import pandas as pd

# Read the file and specify which column is the date
track_list = pd.read_excel("Track_List.xls")

# Output with dates converted to YYYY-MM-DD
track_list["Date Added"] = pd.to_datetime(track_list["Date Added"]).dt.strftime("%Y-%m-%d")
track_list["Last Played"] = pd.to_datetime(track_list["Last Played"]).dt.strftime("%Y-%m-%d")
track_list["Last Skipped"] = pd.to_datetime(track_list["Last Skipped"]).dt.strftime("%Y-%m-%d")


track_list.to_excel("Track_List_YYYY_MM_DD.xls")
