const ctx = document.getElementById('expenseChart');

new Chart(ctx, {
type: 'pie',
data: {
labels: ['Food','Transport','Bills','Shopping'],
datasets: [{
data: [40,20,25,15],
backgroundColor:[
'#FF8A8A',
'#7C8CF8',
'#6ED6A0',
'#BFA6FF'
]
}]
}
});
