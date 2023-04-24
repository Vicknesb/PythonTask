import pandas as pd
from reportlab.pdfgen import canvas

df = pd.read_csv("Property_Details.csv")
locationmean = df.groupby("Location").agg({"Price": "mean", "Square Feet": "mean"}).reset_index()
propertymean = df.groupby(["Location", "Property Type"]).agg({"Bedroom": "mean", "Bathroom": "mean"}).reset_index()
pdffile = canvas.Canvas("Property_Report.pdf")

pdffile.setFont("Helvetica-Bold", 14)
pdffile.drawString(50, 750, "Property Details")
pdffile.setFont("Helvetica-Bold", 12)
pdffile.drawString(50, 720, "Location Data")
pdffile.setFont("Helvetica", 10)

data = [["Location", "Average Price", "Average Square Feet"]]
for index, row in locationmean.iterrows():
    data.append([row["Location"], round(row["Price"], 2), round(row["Square Feet"], 2)])

col_widths = [150, 100, 100]
row_height = 20
for row in data:
    for index, item in enumerate(row):
        pdffile.drawString(50 + (index * col_widths[index]), 700 - (data.index(row) * row_height), str(item))

pdffile.setFont("Helvetica-Bold", 12)
pdffile.drawString(50, 590, "Property Data by Location and Type")
pdffile.setFont("Helvetica", 10)

data = [["Location", "Property Type", "Average Bedroom", "Average Bathroom"]]
for index, row in propertymean.iterrows():
    data.append([row["Location"], row["Property Type"], round(row["Bedroom"], 2), round(row["Bathroom"], 2)])

col_widths = [110, 110, 100, 100]
row_height = 20
for row in data:
    for index, item in enumerate(row):
        pdffile.drawString(50 + (index * col_widths[index]), 550 - (data.index(row) * row_height), str(item))

pdffile.save()
