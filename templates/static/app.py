from flask import Flask, render_template, request, redirect, jsonify
from datetime import datetime

app = Flask(__name__)

transactions = []

def format_currency(amount):
    return f"{amount:,.0f}"

@app.route("/", methods=["GET","POST"])
def home():

    if request.method == "POST":

        description = request.form["description"]
        amount = float(request.form["amount"])
        ttype = request.form["type"]

        transactions.append({
            "id": len(transactions)+1,
            "description": description,
            "amount": amount,
            "type": ttype,
            "date": datetime.now().strftime("%d %b %Y")
        })

        return redirect("/")

    income = sum(t["amount"] for t in transactions if t["type"]=="Income")
    expense = sum(t["amount"] for t in transactions if t["type"]=="Expense")
    balance = income - expense

    sorted_transactions = sorted(transactions, key=lambda x:x["id"], reverse=True)

    return render_template(
        "index.html",
        transactions=sorted_transactions,
        income=format_currency(income),
        expense=format_currency(expense),
        balance=format_currency(balance)
    )

@app.route("/delete/<int:tid>")
def delete_transaction(tid):

    global transactions
    transactions = [t for t in transactions if t["id"]!=tid]

    return redirect("/")

@app.route("/chart-data")
def chart_data():

    income = sum(t["amount"] for t in transactions if t["type"]=="Income")
    expense = sum(t["amount"] for t in transactions if t["type"]=="Expense")

    return jsonify({
        "income": income,
        "expense": expense
    })

if __name__ == "__main__":
    app.run(debug=True)
