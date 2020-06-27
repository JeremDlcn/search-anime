let ser = document.querySelector('.ser main section');
let scrollAmount = 0;
let scrollMax = ser.clientWidth;
let scrollMin = 0;
document.querySelector('.ser').addEventListener('wheel', (e)=>{
    if (e.deltaY > 0) {
        ser.scrollTo({
            top: 0,
            left: Math.max(scrollAmount += 100, scrollMax),
            behavior: 'smooth'
        })
    }
    else if (e.deltaY < 0) {
        ser.scrollTo({
            top: 0,
            left: Math.min(scrollAmount -= 100, scrollMin),
            behavior: 'smooth'
        })
    }
});

