var botonfacebook = document.querySelector(".facebook")
botonfacebook.addEventListener("click", function(event){
    event.preventDefault();
    swal({
        title: "Quieres Ir A Nuestra Pagina De Facebook?",
        icon: "warning",
        buttons: true,
        dangerMode: true,
    })
    .then((redireccion)=>{
        if(redireccion){
            swal("Ok Seras Redireccionando.....",{
                icon:"success",
            });
            setTimeout( function() { 
                window.open("https://www.facebook.com/ConstrumasES/", "_blank")
            }, 1000 );
            
        }
        else{
            swal("No Seras Redireccionado",{
                icon:"error"
            })
            
        }
    })

});

var botonemail = document.querySelector(".email")
botonemail.addEventListener("click", function(event){
    event.preventDefault();
    swal({
        title: "Quieres Mandarnos Un Correo?",
        icon: "warning",
        buttons: true,
        dangerMode: true,
    })
    .then((redireccion)=>{
        if(redireccion){
            swal("Ok Seras Redireccionando.....",{
                icon:"success",
            });
            setTimeout( function() { 
                window.open("https://mail.google.com/mail/u/0/#inbox?compose=DmwnWrRnZvxxMJhMhgWCXzMvBrPpnlWCrkJNpXSFSRbLbdZSqKpHnxNWxRQvhNWVBCvKhpfDrxLq", "_blank")
            }, 1000 );
            
        }
        else{
            swal("No Seras Redireccionado",{
                icon:"error"
            })
            
        }
    })

});

var botonphone = document.querySelector(".telefono")
botonphone.addEventListener("click", function(event){
    //* preventDefault no recarga la pagina
    event.preventDefault();
    swal('Nuestro Numero De Telefono:','+503: 2213-7406');
});

var botonmaps = document.querySelector(".maps")
botonmaps.addEventListener("click", function(event){
    event.preventDefault();
    swal({
        title: "Desea Ir A Google Maps?",
        icon: "warning",
        buttons: true,
        dangerMode: true,
    })
    .then((redireccion)=>{
        if(redireccion){
            swal("Ok Seras Redireccionando.....",{
                icon:"success",
            });
            setTimeout( function() { 
                window.open("https://www.google.com/maps/place/Construmas/@13.8028584,-89.2131256,17z/data=!4m12!1m6!3m5!1s0x0:0x21ceaa716e6ce74c!2sConstrumás+el+salvador!8m2!3d13.821466!4d-89.2381774!3m4!1s0x8f633bd494cfa751:0x8fb8e746b5e374d9!8m2!3d13.8033567!4d-89.2116494", "_blank")
            }, 1000 );
            
        }
        else{
            swal("No Seras Redireccionado",{
                icon:"error"
            })
            
        }
    })

});


// Alertas Temporales por falta de contenido

var botonlineup = document.querySelector(".escenarios-contenedor")
botonlineup.addEventListener("click", function(event){
    //* preventDefault no recarga la pagina
    event.preventDefault();
    swal('Pagina En Desarollo','Estara Disponible En Breve',{
        icon:"error"
    });
});







document.addEventListener('DOMContentLoaded' ,function(){
    iniciarApp();
});

function iniciarApp(){
    navegacionFija();
    scrollNav();
}

function navegacionFija(){
    const barra = document.querySelector('.header')
    const sobre = document.querySelector('.sobre-festival')
    const body = document.querySelector('body')

    window.addEventListener('scroll', function(){
        if(sobre.getBoundingClientRect().top < 0){
            barra.classList.add('fijo');
            body.classList.add('body-scroll');
        }else{
            barra.classList.remove('fijo');
            body.classList.remove('body-scroll');
        }
    })
}

// Efecto smooth scroll
function scrollNav(){
    const enlaces = document.querySelectorAll('.navegacion-principal a');
    enlaces.forEach( enlace => {
        enlace.addEventListener('click', function(e){
            e.preventDefault();
            const seccionScroll = e.target.attributes.href.value;
            const seccion = document.querySelector(seccionScroll);
            seccion.scrollIntoView({behavior: "smooth"});
        });
    });
}

// end efecto



// Anticopy

document.oncopy = event =>{
    event.preventDefault();
    event.clipboardData.setData('Propiedad De Construmas © 2022')
}
    