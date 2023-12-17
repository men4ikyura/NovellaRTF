label arka3:
   
    play music fon13 fadein 1.0
    
    "Себастиан после защиты диплома, едет домой в Сургут, навестить своих родных и близких."
    "{size=-5}Бабушки гордятся своим внуком, ведь теперь Себастиан с высшим образованием и может сделать много полезного для своей Родины.{/size}"

    scene bg kvartira with fade

    show s smile 2 

    s "Дом, милый дом. Как давно я тут не был!"
    s "Отдохну и отправлю резюме, пройду собеседование и буду работать."

    scene bg kvartira with fade
    
    "Спустя неделю"

    show s normal 2

    s "Пора и резюме отправить."

    menu:
        "Отправить резюме?"
        "Нет, ещё отдохну денёк":

            scene bg kvartira with fade
            "Спустя день"

            show s normal 2 

            s "Очень уютно дома, но пора работать."
            menu:
                "Отправить резюме?"
                "Надо отправлять":
                    jump conti1
                "Нет, ещё отдохну денёк":

                    play music fonend fadein 1.0

                    scene bg gameover with fade
                    pause

                    "Себастиан, так и не смог найти работу."
                    scene title1 with fade
                    pause
                    return

        "Отправить и ждать ответ":
            jump conti1


label conti1:

    scene bg kvartira with fade

    show s smile 2 

    s "Я ещё в универе хотел в Тинько пойти.
Надо изучить с какими библиотеками они работают"

    scene bg requirements with fade
                    
    s  "{size=-15}Тинько от  Python-разработчик требует умение работать с FastApi, Flask, PostgreSQL и MySQL, опыт использования Kafka, Cassandra, Clickhouse, Redis и Elasticsearch. Надо их изучить.{/size}"


    menu:
        "Как поступим?"
        "Потратить время на изучение библиотек и фреймворков":
            
            scene bg messagetinko2 with fade

            s smile 2 "Ура, я прошел!"
    

        "Вроде, больше половины знаю, смогу пройти.":

            scene bg messagetinko1 with fade

            s sad 2 "Надо было потратить время на изучение, но ещё не поздно."

            scene black with fade

            "Спустя месяц"

            s smile 2 "Вот сейчас я уверен, что смогу пройти."

            scene bg messagetinko2 with fade

            s smile 2 "Ура, я прошел!"

    
    stop music fadeout 1.0

    play music fon23 fadein 1.0

    scene black with fade

    "Спустя 5 лет"

    scene bg bar with fade

    show s normal 3 at left2
    show h normal 2 at right2

    h "Ну и как тебе Себастиан работать в Тинько?"
    s "Слушай, мне вообще всё нравиться!"
    h "А что ты там вообще делаешь?"
    s "Ну если тебе интересно, то мой распорядок такой:"

    scene bg kvartira with fade

    "Время 7:30."

    show s normal 3 at center

    s "Умыться, покушать и на работу."

    scene bg woscowstreet with fade

    "Время 8:30."

    show s normal 3 at left2

    s "Как же мне нравиться вид, когда я иду на работу."

    show bg office with fade

    "Время 9:00."

    show s normal 3 at center

    s "Так, а теперь пора и начать работать."

    scene bg tableoffice with fade

    "Время 10:30."

    show s normal 3 at left2

    s "Пора и на встречу с командой. Надо обсудить рабочие вопросы."

    scene bg office with fade

    "Время 11:00."

    show s normal 3 at center

    s "Обратно за работу."

    scene bg obed with fade

    "Время 12:30."

    show s normal 3 at left2

    s "{size=-5}Обеденный перерыв. Можно обсудить с коллегами рабочие вопросы, новости it или просто поболтать на отстранённые темы и отдохнуть.{/size}"

    scene bg office with fade

    "Время 13:30."

    show s normal 3 at center

    s "Продолжаем кодить, интересное занятие."

    scene bg obed with fade

    "Время 16:15."

    show s normal 3 at left2

    s "Небольшой перерывчик на кофе, перекус."

    scene bg tinko with fade 

    "Время 16:30."

    show s normal 3 at left2

    s "\"one to one\" диалог один на один с менеджером, где можно обсудить твою зарплату, рабочие вопросы и т.д."

    scene bg office with fade

    "Время 17:00."

    show s normal 3 at left2

    s "Ну и обратно кодить."

    scene bg woscowstreet with fade

    "Время 19:00."

    show s normal 3 at left2

    s "А вот теперь я и домой иду."

    scene bg bar with fade

    show s normal 3 at left2
    show h normal 2 at right2

    h "Ну у тебя довольно интересно. У меня только работа и перерыв на обед."
    s "Так да, очень люблю свою работу."

    stop music

    jump arka4




    









    


    




    




    







        


