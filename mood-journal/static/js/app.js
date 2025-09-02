const form = document.getElementById('entry-form');
const contentEl = document.getElementById('content');
const errorEl = document.getElementById('error');
const entriesEl = document.getElementById('entries');
const ctx = document.getElementById('trendChart');
let chart;


async function fetchJSON(url, opts = {}) {
const res = await fetch(url, { headers: { 'Content-Type': 'application/json' }, ...opts });
if (!res.ok) throw new Error((await res.json()).error || res.statusText);
return res.json();
}


async function loadTrends() {
const data = await fetchJSON('/api/trends');
const labels = data.labels;
const datasets = Object.entries(data.datasets).map(([key, values]) => ({
label: key,
data: values,
fill: false,
tension: 0.25,
}));


if (chart) chart.destroy();
chart = new Chart(ctx, {
type: 'line',
data: { labels, datasets },
options: {
responsive: true,
interaction: { mode: 'nearest', intersect: false },
scales: {
y: { beginAtZero: true, suggestedMax: 1 },
},
plugins: {
legend: { position: 'bottom' },
tooltip: { callbacks: { label: (c) => `${c.dataset.label}: ${(c.parsed.y).toFixed(3)}` } }
}
}
});
}


async function loadEntries() {
const items = await fetchJSON('/api/entries');
entriesEl.innerHTML = items.map(it => {
const emoPairs = Object.entries(it.emotions).sort((a,b)=>b[1]-a[1])
}
)}