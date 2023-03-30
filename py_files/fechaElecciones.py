import datetime
import json

# Load the json file and get the value of "fecha"
with open("feriadosElecciones.json", 'r+') as f:
    data = json.load(f)
    for i in range(len(data)):
        descString = data[i]['nombre']
        if ( "ELECC" in descString.upper() ):
            data[i]['comentarios']=  "ESTE FERIADO ES POR ELECCIONES"
    f.seek(0)        # <--- should reset file position to the beginning.
    json.dump(data, f, indent=4)
    f.truncate()