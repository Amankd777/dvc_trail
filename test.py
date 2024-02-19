import pandas as pd

Data=[
    {"name":"Aman", "age":20, "city":"Bengaluru"},
    {"name":"Vignesh", "age":21, "city":"Bengaluru"},
    {"name":"Kundeti", "age":20, "city":"Machilipatnam"},
    {"name":"John", "age":23, "city":"Missouri"}
]

Data=pd.DataFrame(Data)

Data.to_csv("data/data.csv", index=False)