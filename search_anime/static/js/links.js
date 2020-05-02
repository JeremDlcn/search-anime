let links = document.querySelectorAll('main a');

document.querySelector('.switch input').addEventListener('click', ()=>{
	if (document.querySelector('.switch input').checked == true) {
		version(1);
		console.log('premier')
	}
	 else {
	 	version(2);
	 	console.log('second')
	}
});


function version(nb) {
	for (let i = 0; i < links.length; i++){
		links[i].href = links[i].href.replace('/v1',``)
		links[i].href = links[i].href.replace('/v2',``)
		links[i].href = links[i].href.replace('/view/',`/v${nb}/view/`)
		links[i].href = links[i].href.replace('http://127.0.0.1:5000',``)
	}
}