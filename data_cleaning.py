import pandas as pd

sheet_names = ['STEEL 90°', 'STEEL 100°', 'STEEL 110°', 'STEEL 120°', 'STEEL 130°', 'STEEL 140°']
data = pd.DataFrame(columns= ['Thickness', 'V-type', 'Punch', 'bend_deduction'])
for sheetName in sheet_names:
    df = pd.read_excel('Bend Deduction dataset.xlsx', sheet_name=sheetName)
    column_name = df.iloc[1]
    angle = df['HaLSpace Bending Parameter'][0]
    angle = ''.join(e for e in angle if e.isalnum()) #to remove special characters from string
    df.columns = column_name
    df = df[2:]
    df = df[['Thickness','V type','Punch','Growth bending　 曲げ伸び']]
    df['Thickness'] = df['Thickness'].fillna(method='ffill')
    df['Thickness'] = df['Thickness'].str.replace("t","")
    df["V type"] = df["V type"].str.replace("V","")
    df['Punch'] = df["Punch"].str.replace("R","")
    df.columns = ['Thickness', 'V-type', 'Punch', 'bend_deduction']
    df['angle'] = angle
    data = pd.concat([data, df])
data.to_csv('cleaned_data.csv')