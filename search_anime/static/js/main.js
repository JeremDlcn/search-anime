// Resize long titles
const hei = Number(window.getComputedStyle(document.querySelector('#info h1')).height.replace('px', ''));
const newSize = String(hei / 10) + 'px'
const newline = String((hei / 100) / 1.35) + 'rem'

if (hei > 250) {
	document.querySelector('#info h1').style.fontSize = newSize;	
	document.querySelector('#info h1').style.lineHeight = newline;
}
