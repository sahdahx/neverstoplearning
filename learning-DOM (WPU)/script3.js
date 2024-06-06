// DOM Events
// - Mouse Event
// - Keyboard Event
// - Resources Event
// - Focus Event
// - View Event
// - Form Event
// - CSS Animation & Transition Event
// - Drag and Drop Event, dll

// function ubahwarna(){
//     p3.style.backgroundColor = 'lightpink';
// }

// const p3 = document.querySelector('.p3');
// p3.onclick = ubahwarna;

// // addEventListener method
// const p4 = document.querySelector('section#b p');
// p4.addEventListener('click', function() {
//     const ul = document.querySelector('section#b ul');
//     const liBaru = document.createElement('li');
//     const teksliBaru = document.createTextNode('item baru');
//     liBaru.appendChild(teksliBaru);
//     ul.appendChild(liBaru);
// });

const p3 = document.querySelector('.p3');
// p3.onclick = function() {
//     p3.style.backgroundColor = 'lightpink';
// }
// p3.onclick = function() {
//     p3.style.color = 'red';
// }

p3.addEventListener('mouseenter', function() {
    p3.style.backgroundColor = 'lightpink';
})
p3.addEventListener('mouseleave', function() {
    p3.style.backgroundColor = 'lightblue';
})