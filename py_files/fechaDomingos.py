import datetime
import json

# Load the json file and get the value of "fecha"
with open("2023.json", 'r+') as f:
    data = json.load(f)
    for i in range(len(data)):
        
        fecha = data[i]['fecha']
        # Convert the value to a datetime object
        date = datetime.datetime.strptime(fecha, "%Y-%m-%d")

        # Get the weekday as an integer
        weekday = date.weekday()
        # Compare with the desired day of week (0 for Monday, 6 for Sunday)
        if weekday == 6: # Sunday
            data[i]['comentarios']=  "Este dia es Domingo"
    f.seek(0)        # <--- should reset file position to the beginning.
    json.dump(data, f, indent=4)
    f.truncate()
