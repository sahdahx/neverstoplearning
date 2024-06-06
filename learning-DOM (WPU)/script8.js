const tubahwarna = document.getElementById('tubahwarna');
const body = document.getElementsByTagName('body')[0]
tubahwarna.onclick = function() {
    // document.body.setAttribute('class', 'aqua')
    document.body.classList.toggle('aqua')
}


const trandom = document.createElement('button');
const tekstombol = document.createTextNode('Acak Warna');
trandom.appendChild(tekstombol);
trandom.setAttribute('type', 'button');
tubahwarna.after(trandom);

// mengacak warna 
trandom.addEventListener('click', function() {
    const r = Math.round(Math.random() * 200 + 10);
    const g = Math.round(Math.random() * 100 + 10);
    const b = Math.round(Math.random() * 100 + 10);
    document.body.style.backgroundColor = 'rgb('+ r +', '+ g +', '+ b +')';
});

const smerah = document.querySelector('input[name=smerah]');
const shijau = document.querySelector('input[name=shijau]');
const sbiru = document.querySelector('input[name=sbiru]');

smerah.addEventListener('input', function() {
    const r = smerah.value;
    const g = shijau.value;
    const b = sbiru.value;
    document.body.style.backgroundColor = 'rgb(' + r + ', ' + g + ', ' + b + ')';
});

shijau.addEventListener('input', function() {
    const r = smerah.value;
    const g = shijau.value;
    const b = sbiru.value;
    document.body.style.backgroundColor = 'rgb(' + r + ', ' + g + ', ' + b + ')';
});

sbiru.addEventListener('input', function() {
    const r = smerah.value;
    const g = shijau.value;
    const b = sbiru.value;
    document.body.style.backgroundColor = 'rgb(' + r + ', ' + g + ', ' + b + ')';
});


document.addEventListener('mousemove', function(event) {
    // posisi mouse
    // console.log(event.clientX);
    // ukuran browser
    // console.log(window.innerWidth);
    const xpos = Math.round((event.clientX / window.innerWidth) * 255);
    const ypos = Math.round((event.clientY / window.innerHeight) * 255);
    document.body.style.backgroundColor = 'rgb(' + xpos + ', ' + ypos + ', 100)';
});