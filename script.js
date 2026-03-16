const ctx = document.getElementById('expenseChart').getContext('2d');

fetch('/chart-data')
.then(response => response.json())
.then(data => {

new Chart(ctx, {

type: 'pie',

data: {
labels: ['Income', 'Expense'],

datasets: [{
data: [data.income, data.expense],

backgroundColor:[
'#6ED6A0',
'#FF8A8A'
],

borderWidth:1
}]
},

options:{
responsive:true,
plugins:{
legend:{
position:'bottom'
}
}
}

});

});
