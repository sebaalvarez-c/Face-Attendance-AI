import speech_recognition as sr




def recognize_voice():


    recognizer = sr.Recognizer()



    try:


        with sr.Microphone() as source:


            print("Escuchando voz...")


            recognizer.adjust_for_ambient_noise(

                source,

                duration=0.5

            )


            audio = recognizer.listen(

                source,

                timeout=3,

                phrase_time_limit=3

            )





        text = recognizer.recognize_google(

            audio,

            language="es-ES"

        )



        text = text.lower()



        print(

            "VOZ:",

            text

        )





        palabras = [

            "presente",

            "buenos dias",

            "buen día",

            "hola"

        ]





        for palabra in palabras:


            if palabra in text:


                return {


                    "valid":

                    True,


                    "text":

                    text

                }







        return {


            "valid":

            False,


            "text":

            text

        }





    except Exception as e:



        print(

            "ERROR VOZ:",

            e

        )



        return {


            "valid":

            False,


            "text":

            "No reconocida"

        }