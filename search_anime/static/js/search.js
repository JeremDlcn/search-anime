// Send search url
function search() {
	let url = document.querySelector('#search-bar').value;
	url = url.replace(/ /g, '-').toLowerCase();
	window.location.href = `/search/${url}`;
}


document.querySelector('#search-now').addEventListener('click', ()=>{
	search()
});

document.querySelector('#search-bar').addEventListener('keyup', ()=>{
	if (event.key === "Enter") {
		search()
	}
});
