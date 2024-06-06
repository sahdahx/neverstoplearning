// Event Handling
// const close = document.querySelector('.close');
// const card = document.querySelector('.card');

// close.addEventListener('click', function() {
//     card.style.display = 'none';
// });

// DOM Traversal
const close = document.querySelectorAll('.close');
const card = document.querySelectorAll('.card');

// for(let i = 0; i < close.length; i++) {
//     close[i].addEventListener('click', function() {
//         // alert('tombol ke-' + i) // buat klik
//         // card[i].style.display = 'none'; // buat hilang
//         close[i].parentElement.style.display = 'none'; // buat hilang tapi pakai parentElement
//     });
// }

// DOM Traversal Method
// - parentNode -> node
// - parentElement -> element
// - nextSibling -> node
// - nextElementSibling -> element
// - previousSibling -> node
// - previousElementSibling -> element

// const nama = document.querySelector('.nama');
// console.log(nama.parentElement.parentElement);


// DOM Traversal tapi pakai for each
close.forEach(function(el) {
    el.addEventListener('click', function(e) {
        // e.target.style.display = 'none'; // -> yg hilang cuma tanda x
        e.target.parentElement.style.display = 'none'; // -> yg hilang satu card
        // e.target.parentElement.parentElement.style.display = 'none'; // -> yg hilang semua card
        e.preventDefault(); 
        e.stockPropagation();
    });
});

// preventDefault = mencegah perilaku default dari event yang sedang terjadi. Contohnya, jika event ini adalah submit dari sebuah form, preventDefault akan mencegah form tersebut untuk dikirim.
// stockPropagation = menghentikan propagasi event ke elemen-elemen parent. Artinya, event tersebut tidak akan "membubble" ke elemen-elemen yang lebih tinggi di DOM.

// Event Bubbling 
const cards = document.querySelectorAll('.card');
cards.forEach(function(card) {
    card.addEventListener('click', function(e) {
        alert('kamu menekan card');
    });
});