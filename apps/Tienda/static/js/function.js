const time = document.getElementById('time');
const date = document.getElementById('date');

const monthNames = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio",
    "Julio", "Agosto", "Septtiembre", "Octubre", "Noviembre", "Deciembre"
];

const interval = setInterval(() => {

    const local = new Date();
    
    let day = local.getDate(),
        month = local.getMonth(),
        year = local.getFullYear();

    time.innerHTML = local.toLocaleTimeString();
    date.innerHTML = `${day} ${monthNames[month]} ${year}`;

}, 1000);

/* Modo oscuro */
const switchButton = document.getElementById('switch');
switchButton.addEventListener('click',()=>{
    document.body.classList.toggle('dark');
    switchButton.classList.toggle('active')
})



