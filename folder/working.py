import re
import pandas as pd

file_path = "./17052023.txt"

with open(file_path, "r") as file:
    text = file.read()

data = []
pattern = r"UPTIME TOTALS FOR ATM (\d{4})\n+.*?(?:(No totals received)|(?:Online\s+\d\s+\d{2}:\d{2}.\d{2}\s+(\d{2}\.\d{2})))"
matches = re.findall(pattern, text, re.DOTALL)
print(matches)
for match in matches:
    atm_number = match[0]
    if match[1]:
        online_percentage = None
    else:
        online_percentage = match[2]
    # print("ATM Number:", atm_number)
    # print("Online Percentage:", online_percentage)
#     data.append({'ATM Number': atm_number, 'Online Percentage': online_percentage})

# df = pd.DataFrame(data)

# # Export the DataFrame to an Excel file
# df.to_excel('atm_data.xlsx', index=False)


# the environment =  .\env_name\Scripts\activate