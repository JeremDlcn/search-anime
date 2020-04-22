// Send search url
function search() {
	let url = document.querySelector('#search-bar').value;
	url = url.replace(/ /g, '-').toLowerCase();
	if (document.querySelector('.switch input').checked == true) {
		window.location.href = `/v1/view/${url}`	

	}
	else {
		window.location.href = `/v2/view/${url}`
	}
	
}


document.querySelector('#search-now').addEventListener('click', ()=>{
	search()
});

document.querySelector('#search-bar').addEventListener('keyup', ()=>{
	if (event.key === "Enter") {
		search()
	}
});

