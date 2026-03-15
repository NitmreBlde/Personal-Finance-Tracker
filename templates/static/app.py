from flask import Flask, render_template, request, redirect
from datetime import datetime

app = Flask(__name__)

transactions = []

@app.route("/", methods=["GET", "POST"])
def home():

    if request.method == "POST":

        description = request.form["description"]
        amount = float(request.form["amount"])
        ttype = request.form["type"]

        transactions.append({
            "description": description,
            "amount": amount,
            "type": ttype,
            "date": datetime.now().strftime("%d %b %Y")
        })

        return redirect("/")

    income = sum(t["amount"] for t in transactions if t["type"] == "Income")
    expense = sum(t["amount"] for t in transactions if t["type"] == "Expense")
    balance = income - expense

    return render_template(
        "index.html",
        transactions=transactions,
        income=income,
        expense=expense,
        balance=balance
    )


if __name__ == "__main__":
    app.run(debug=True)
