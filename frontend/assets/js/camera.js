const video = document.getElementById("video");
const canvas = document.getElementById("canvas");
const btnReconocer = document.getElementById("btnReconocer");
const mensaje = document.getElementById("mensaje");
const inputCodigo = document.getElementById("codigoUsuario");

let procesando = false;



async function iniciarCamara() {

    try {

        const stream = await navigator.mediaDevices.getUserMedia({

            video: true,
            audio: false

        });


        video.srcObject = stream;


        mensaje.textContent =
            "Cámara activada correctamente.";


    } catch (error) {


        console.error(error);


        mensaje.textContent =
            "Error: no se pudo acceder a la cámara.";

    }

}




function obtenerUbicacion() {


    return new Promise((resolve, reject) => {


        if (!navigator.geolocation) {


            reject(
                "Tu navegador no soporta geolocalización."
            );


            return;

        }



        navigator.geolocation.getCurrentPosition(


            position => {


                resolve({

                    lat: position.coords.latitude,

                    lng: position.coords.longitude

                });


            },


            () => {


                reject(
                    "No se pudo obtener la ubicación."
                );


            },


            {

                enableHighAccuracy:true,

                timeout:10000

            }


        );


    });


}





function capturarImagen() {


    canvas.width =
        video.videoWidth;


    canvas.height =
        video.videoHeight;



    const context =
        canvas.getContext("2d");



    context.drawImage(

        video,

        0,

        0,

        canvas.width,

        canvas.height

    );



    return canvas.toDataURL(

        "image/jpeg",

        0.9

    );

}





function pintarEstado(status) {


    mensaje.className =
        "mt-4 text-lg font-semibold";



    switch(status){


        case "success":

            mensaje.classList.add(
                "text-green-400"
            );

            break;



        case "duplicate":

            mensaje.classList.add(
                "text-yellow-400"
            );

            break;



        case "unknown":

            mensaje.classList.add(
                "text-yellow-300"
            );

            break;



        case "out_of_range":

            mensaje.classList.add(
                "text-red-400"
            );

            break;



        default:

            mensaje.classList.add(
                "text-red-300"
            );

    }

}





async function iniciarReconocimiento() {



    if(procesando){

        return;

    }



    procesando = true;



    try {



        mensaje.className =
            "mt-4 text-lg text-gray-300";



        mensaje.textContent =
            "Analizando rostro...";



        const imagenBase64 =
            capturarImagen();




        const ubicacion =
            await obtenerUbicacion();




        const payload = {


            image_base64:
                imagenBase64,


            lat:
                ubicacion.lat,


            lng:
                ubicacion.lng


        };




        if(
            inputCodigo &&
            inputCodigo.value.trim()
        ){


            payload.code =
                inputCodigo.value.trim();


        }





        const data =
            await apiPost(
                "/mark-attendance",
                payload
            );





        pintarEstado(
            data.status
        );



        let mensajeFinal =
            data.message;



        if(
            data.emotion_message
        ){


            mensajeFinal +=
                " " +
                data.emotion_message;


        }




        mensaje.textContent =
            mensajeFinal;




    } catch(error){



        console.error(error);



        pintarEstado(
            "error"
        );



        mensaje.textContent =
            `Error: ${error.message}`;



    }
    finally{


        procesando=false;


    }



}






if(btnReconocer){


    btnReconocer.addEventListener(

        "click",

        iniciarReconocimiento

    );


}




iniciarCamara();