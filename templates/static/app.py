from flask import Flask, render_template, request, redirect

app = Flask(__name__)

transactions = []

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        description = request.form["description"]
        amount = request.form["amount"]
        ttype = request.form["type"]

        transactions.append({
            "description": description,
            "amount": amount,
            "type": ttype
        })

        return redirect("/")

    return render_template("index.html", transactions=transactions)

if __name__ == "__main__":
    app.run(debug=True)
