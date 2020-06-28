const anime = document.querySelectorAll('.item-search');
let posters = document.querySelectorAll('.item-img-poster');

for (let i = 0; i < 2; i++) {
    let name = anime[i].children[1].children[0].textContent;
    (async () => {
        console.log("1");
        let id = await getId(name);
        console.log("2");
        let poster = await retrieveImg(id);
        console.log("3");
        posters[i].src = poster;
        console.log("4");
    })();
}

async function getId(name) {
    let response = await fetch(`https://api.jikan.moe/v3/search/anime?q=${name}&limit=1`);
    let data = await response.json();
    return data.results[0].mal_id;        
}



async function retrieveImg(id) {
    let r = await fetch(`https://api.jikan.moe/v3/anime/${id}/pictures`)
    let data =  await r.json();
    return data.pictures[data.pictures.length-1].large;
}

