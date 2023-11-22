import pandas as pd

# Number of rows to read
n = 2000

df = pd.read_excel('Medicine_description.xlsx', sheet_name='Sheet1', 
        header=0, nrows=n)

# Get the unique values in the ‘Reason’ column of the data frame, 
# stores them in an array called reasons
reasons = df["Reason"].unique()
reasons_dict = {reason: i for i, reason in enumerate(reasons)}

df["Drug_Name"] = "Drug: " + df["Drug_Name"] + "\n" + "Malady:"
df["Reason"] = " " + df["Reason"].apply(lambda x: "" + str(reasons_dict[x]))
df.drop(["Description"], axis=1, inplace=True)
df.rename(columns={"Drug_Name": "prompt", "Reason": "completion"}, inplace=True)

# Convert the dataframe to jsonl format
jsonl = df.to_json(orient="records", indent=0, lines=True)

# Write the jsonl to a file

with open("drug_malady_data.jsonl", "w") as f:
    f.write(jsonl)