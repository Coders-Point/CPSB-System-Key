from flask import Flask, render_template, request
import json
import os


app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/dashboard', methods=['GET'])
def dashboard():
    username = request.args.get('username')
    password = request.args.get('password')

    if username == "CPnt" and password == "point7@coder":
        file = open("banks.json", "rt")
        banks = json.loads(file.read())
        file.close()
        return render_template('dashboard.html', banks=banks)
    
    else:
        return render_template('prompts/incorrect_credentials.html')
    
@app.route('/new-bank', methods=['GET'])
def new_bank():
    name = request.args.get('name')
    funds = request.args.get('funds')

    identity_max = 0

    with open("banks.json", "r") as file:
        banks = json.load(file)
        file.close()

    for bank in banks:
        if int(bank['ID']) > int(identity_max):
            identity_max = bank['ID']

        else: continue

    new_bank_dict = {"Name": name, "ID": str(int(identity_max) + 1), "Funds": funds}

    banks.append(new_bank_dict)

    with open("banks.json", "w") as file:
        json.dump(banks, file, indent=4)
        file.close()

    return "Bank created successfully"

@app.route('/edit-fund', methods=['GET'])
def edit_fund():
    name = request.args.get('name')
    identity = request.args.get('id')
    new_funds = request.args.get('new_funds')

    with open("banks.json", "r") as file:
        banks = json.load(file)
        file.close()


    requested_bank_index = None
    requested_bank_dict = None

    for bank in banks:
        if bank['Name'] == name and bank['ID'] == identity:
            requested_bank_index = banks.index(bank)
            banks[requested_bank_index]['Funds'] = new_funds

            with open("banks.json", "w") as file:
                json.dump(banks, file, indent=4)
                file.close()

            break

        else: continue

    if requested_bank_index is None or requested_bank_dict is None:
        return "Failed to update funds"

    else:
        return f"Updated {str(name)}-{str(identity)}'s funds to {str(new_funds)} (index: {str(requested_bank_index)})"


@app.route('/delete-bank', methods=['GET'])
def delete_bank():
    identity = request.args.get('id')
    with open("banks.json", "r") as file:
        banks = json.load(file)
        file.close()

    for bank in banks:
        if bank['ID'] == identity:
            banks.remove(bank)
            break

    with open("banks.json", "w") as file:
        json.dump(banks, file, indent=4)
        file.close()

    return "Deleted bank"



if __name__ == '__main__':
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
