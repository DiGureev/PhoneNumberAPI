from flask import Flask
import os
import json
from script import main

app = Flask(__name__)

@app.route("/<phone_number>")
def home(phone_number):
    username = phone_number.replace("+", "")
    result = main(phone_number)
    
    if os.path.exists(f"./reports/{username}.json"):
        print("Exist")
        with open(f"./reports/{username}.json","r") as f:
            result = json.load(f)
        return result, 200
    else:
        print("Does not Exist")
        result = main(phone_number)
        with open(f"./reports/{username}.json", "w") as f:
            json.dump(result, f)
        return json.dumps(result), 200

if __name__ == "__main__":
    app.run(debug=True)