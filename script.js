function showSection(section){

document.getElementById("dashboard-section").style.display="none"
document.getElementById("transactions-section").style.display="none"
document.getElementById("analytics-section").style.display="none"
document.getElementById("budgets-section").style.display="none"
document.getElementById("settings-section").style.display="none"

document.getElementById(section+"-section").style.display="block"

}



async function addTransaction(){

const amount=document.getElementById("amount").value
const category=document.getElementById("category").value
const type=document.getElementById("type").value
const date=document.getElementById("date").value


await fetch("/add_transaction",{

method:"POST",

headers:{
"Content-Type":"application/json"
},

body:JSON.stringify({

amount:amount,
category:category,
type:type,
date:date

})

})


loadTransactions()
loadDashboard()

}



async function loadTransactions(){

const res=await fetch("/get_transactions")

const data=await res.json()

const table=document.getElementById("transaction-table")

table.innerHTML=""

data.forEach(t=>{

table.innerHTML+=`

<tr>

<td>${t.date}</td>
<td>${t.category}</td>
<td>${t.type}</td>
<td>₹${t.amount}</td>

</tr>

`

})

}



async function loadDashboard(){

const res=await fetch("/get_summary")

const data=await res.json()

document.getElementById("balance").innerText="₹"+data.balance
document.getElementById("income").innerText="₹"+data.income
document.getElementById("expense").innerText="₹"+data.expense

}



const ctx=document.getElementById("expenseChart")

new Chart(ctx,{
type:"doughnut",
data:{
labels:["Income","Expense"],
datasets:[{
data:[5000,2000],
backgroundColor:["green","red"]
}]
}
})



const ctx2=document.getElementById("analyticsChart")

new Chart(ctx2,{
type:"bar",
data:{
labels:["Jan","Feb","Mar","Apr"],
datasets:[{
label:"Expenses",
data:[2000,3000,2500,4000],
backgroundColor:"#3498db"
}]
}
})



loadTransactions()
loadDashboard()
