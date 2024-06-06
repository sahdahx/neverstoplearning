// DOM Manipulation
// document.createElement()
// document.createTextNode()
// Node.appendChild()
// Node.insertBefore()
// parentNode.removeChild()
// parentNode.replaceChild()


// buat elemen baru
const pBaru = document.createElement('p');
const teksPBaru = document.createTextNode('Paragraf Baru');
// simpan tulisan ke dalam paragraf
pBaru.appendChild(teksPBaru);

// simpan pBaru di akhir Section A
const sectionA = document.getElementById('a');
sectionA.appendChild(pBaru);


const liBaru = document.createElement('li');
const teksLiBaru = document.createTextNode('Item Baru');
liBaru.appendChild(teksLiBaru);

const ul = document.querySelector('section#b ul');
const li2 = document.querySelector('li:nth-child(2)');
ul.insertBefore(liBaru, li2);


const link = document.getElementsByTagName('a')[0];

sectionA.removeChild(link);

const sectionB = document.getElementById('b');
const p4 = sectionB.querySelector('p'); // sectionB. karena mulai cari dari sana, kalau document. maka mulai cari dari awal kode

const h2Baru = document.createElement('h2');
const teksH2Baru = document.createTextNode('New Title');

h2Baru.appendChild(teksH2Baru);
sectionB.replaceChild(h2Baru, p4);


pBaru.style.backgroundColor = 'lightpink';
liBaru.style.backgroundColor = 'lightsalmon';
h2Baru.style.backgroundColor = 'lightblue';