// DOM Selection (Part 1)

// document.getElementById() -> mengembalikan element
const judul = document.getElementById('judul')
judul.style.color = 'purple';
judul.style.backgroundColor = 'pink';
judul.innerHTML = 'Sahdahx';

// document.getElementsByTagName() -> mengembalikan HTMLCollections
const p = document.getElementsByTagName('p');

for( let i = 0; i < p.length; i++) {
    p[i].style.backgroundColor = 'lightblue';
}

const h1 = document.getElementsByTagName('h1')[0];
h1.style.fontSize = '50px';

// document.getElementsByClassName() -> mengembalikan HTMLCollections
const p1 = document.getElementsByClassName('p1');
p1[0].innerHTML = 'Ini diubah menggunakan javascript';