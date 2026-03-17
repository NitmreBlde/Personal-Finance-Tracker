from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

transactions = []

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/add_transaction", methods=["POST"])
def add_transaction():

    data = request.json

    transactions.append(data)

    return jsonify({"message":"Transaction added"})


@app.route("/get_transactions")
def get_transactions():
    return jsonify(transactions)


@app.route("/get_summary")
def get_summary():

    income = 0
    expense = 0

    for t in transactions:

        amount = int(t["amount"])

        if t["type"] == "Income":
            income += amount
        else:
            expense += amount

    balance = income - expense

    return jsonify({
        "income": income,
        "expense": expense,
        "balance": balance
    })


if __name__ == "__main__":
    app.run(debug=True)
