// const nameAnime = document.title.innerHTML;

// fetch(`https://api.jikan.moe/v3/search/anime?q=${nameAnime}&limit=1`)
// .then(r => r.json())
// .then(data => {
// 	getID = data.results[0].mal_id;
// 	getIMG(getID);
// })

// // let	get_img = img['pictures'][len(img['pictures'])-1]['large']

// function getIMG (id) {
// 	fetch(`https://api.jikan.moe/v3/anime/${id}/pictures`)
// 	.then(r => r.json())
// 	.then(data => {
// 		console.log(data.pictures.length-1);
// 		// poster = data.pictures[data.pictures.length-1]
// 	})
// }