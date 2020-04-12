import pandas as pd


marketing_analyst_names = pd.read_excel("Airbnb_October_2019.xlsx")
sales_rep_names = pd.read_excel("Airbnb_October_2019_1.xlsx")
sal =pd.read_excel("Airbnb_October_2019_2.xlsx")
#senior_leadership_names = pd.read_excel("SeniorLeadershipNames.xlsx")

# Create a list of the files in order you want them appended
all_df_list = [marketing_analyst_names, sales_rep_names, sal]

# Merge all the dataframes in all_df_list
# Pandas will automatically append based on similar column names
appended_df = pd.concat(all_df_list)

# Write the appended dataframe to an excel file
# Add index=False parameter to not include row numbers
appended_df.to_excel("AllCompanyNames.xlsx", index=False)