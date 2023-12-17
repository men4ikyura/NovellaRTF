
    # ПЕРВАЯ СЦЕНА
label start:    

    play music fon11 fadein 3.0

    "Урок математики. Себастиан спит."

    scene bg mathclass1

    so "Себастиан вставай, там тест раздают."

    s "Оооааа, спать хочется!"

    scene bg mathclass2 
    with fade

    "Решите тест. Не спешите и будьте внимательны!"

    menu:
        "Поставьте знак 1/25  ?  1/96"

        "<":
            "Себастиан кринжанул со знаний игрока"
        "=":
            "Себастиан кринжанул со знаний игрока"
        ">":
            $ count_test1 += 1
    menu:
        "Треугольник ABC  вписан  вокружность  с  центром .O Угол BAC  равен 32 .Найдите угол BOC. Ответ дайте в градусах."

        "64":
            $ count_test1 += 1
        "32":
            "Себастиан кринжанул со знаний игрока"
        "16":
            "Себастиан кринжанул со знаний игрока"
    menu:
        "Решите 2+2*2=?"

        "8":
            "Себастиан кринжанул со знаний игрока"
        "6":
            $ count_test1 += 1
        "2":
            "Себастиан кринжанул со знаний игрока"
    menu:
        "{size=-15}Площадь боковой поверхности треугольной призмы равна 24. Через среднюю линию основания призмы проведена плоскость, параллельная боковому ребру. Найдите площадь боковой поверхности отсечённой треугольной призмы.{/size}"

        "6":
            "Себастиан кринжанул со знаний игрока"
        "12":
            $ count_test1 += 1
        "9":
            "Себастиан кринжанул со знаний игрока"
    
    menu:
        "{size=-17}В сборнике билетов по биологии всего 25 билетов. Только в двух билетах встречается вопрос о грибах. На экзамене выпускнику достаётся один случайно выбранный билет из этого сборника. Найдите вероятность того, что в этом билете будет вопрос о грибах.{/size}"

        "0,04":
            "Себастиан кринжанул со знаний игрока"
        "0,08":
            $ count_test1 += 1
        "0,02":
            "Себастиан кринжанул со знаний игрока"
    menu:
        "Решите (2+2)*2=?"

        "8":
            $ count_test1 += 1
        "6":
            "Себастиан кринжанул со знаний игрока"
        "2":
            "Себастиан кринжанул со знаний игрока"
    menu:
        "Найдите корень уравнения 3^(x-5)=81"

        "7":
            "Себастиан кринжанул со знаний игрока"
        "6":
            "Себастиан кринжанул со знаний игрока"
        "9":
            $ count_test1 += 1
    menu:
        "Найдите корень уравнения x^2+x+1=0"

        "-1 и 1":
            "Себастиан кринжанул со знаний игрока"
        "-1":
            "Себастиан кринжанул со знаний игрока"
        "Нет решения":
            $ count_test1 += 1
    menu:
        "{size=-7}Симметричную игральную кость бросили 3 раза. Известно, что в сумме выпало 6 очков. Какова вероятность события «хотя бы раз выпало 3 очка»?{/size}"

        "0,6":
            $ count_test1 += 1
        "0,3":
            "Себастиан кринжанул со знаний игрока"
        "0,4":
            "Себастиан кринжанул со знаний игрока"
        "Решите (2+2)*2=?"

    menu:
        "Что говорит корова?"

        "Ничего":
            $ count_test1 += 1
        "Мяу":
            "Себастиан начинает мяукать и в шоке осознаёт, что коровы не мяукают"
        "Муууу":
            "Себастиан смутно догадывается, что коровы вообще не говорят, но изменить ответ уже поздно"
    "Себастиан решил тест и опять заснул."

    stop music fadeout 2
    # ВТОРАЯ СЦЕНА

    play music fon21 fadein 2

    scene bg park1
    with fade
    show h normal 1 at right2
    show s normal 1 at left2

    "Себастиан и Хиро гуляют."

    if count_test1 <= 4:
        h normal 1 "Слабенько, Себастиан, слабенько! Какие планы на будущее после такой оценки?"
        s sad 1 "Эх, да у меня еще есть время поднажать. Может быть, в Урфу повезет?"
    elif 5 <= count_test1 <= 6:
        h smile 1 "Ну, ты справился, Себастиан, но можно и лучше. Куда решил направить свои таланты?"
        s normal 1 "Нужно подтянуться, это точно. Может быть, попробую в Урфу?"
    elif 7 <= count_test1 <= 8:
        h smile 1  "Ну неплохо сдал, Себастиан, но тут еще есть куда прыгать! Какие планы на учебу?"
        s normal 1  "Да, неплохо, но есть к чему стремиться. Думаю, попробую в Урфу."
    elif 9 <= count_test1 <= 10:
        h smile 1 "Эх, Себастиан, ты просто бог математики! Куда мечтаешь попасть?"
        s smile 1 "Что поделаешь, я просто гений! Думаю, в Урфу, наверное."

    hide h with dissolve
    hide s with dissolve
    
    scene bg park2
    with fade
    show h normal 1 at right2
    show s normal 1 at left2

    h "Хмм, Урфу же в Екатеринбурге, далековато!"

    menu:
        "Есть такое":
            h  "Ну в Екб вроде не плохо."
        "Ничего страшного":
            h  "Ну в Екб вроде не плохо."
        "Терпимо":
            h  "Ну в Екб вроде не плохо."

    h  "А куда конкретнее хочешь поступить?"
    s  "{size=-7}Хочу на программиста, они зарабатывают многа деняг и это ближе к моим интересам. Да еще и профессия перспективная!{/size}"

    hide h with dissolve
    hide s with dissolve

    scene bg park3
    with fade

    show h smile 1 at right2
    show s normal 1 at left2

    h "Многа деняг? хых"
    h sad 1 "А я еще совсем не определился...."
    h normal 1 "Может на строителя или нефтяника..."
    s normal 1 "Не парься так, посмотри что тебе интереснее."
    h  "Ну мне интересно, как строят здания."
    h smile 1 "Хотелось бы небоскрёб свой построить."
    s smile 1 "А на нефтяника хочешь потому, что они много зарабатывают?"
    h smile 1 "Ага, кто бы не хотел быть богатым?"
    s normal 1 "В каждой сфере можно заработать прилично."
    s "Так что, я бы посоветовал идти на строителя."
    h "Ну да, мне это интереснее будет."
    h normal 1 "Может мне тоже тогда в Урфу поступить?"
    s smile 1 "Давай, будем вместе учиться!"

    hide h  with dissolve
    hide s with dissolve

    stop music fadeout 1
    # # ТРЕТЬЯ СЦЕНА



    play music fon31 fadein 3

    scene bg corridor
    with fade

    show s sad 1 at left31
    show so normal 1 at left3
    show h normal 1 at right32
    
    pause
    s  "Ух... страшно сдавать егэ."
    so "Не бойся мы готовились весь год, мы точно сдадим."
    h "На этом жизнь не останавливается, не волнуйтесь."

    scene bg ege
    with fade

    "Ребята заходят в кабинет и пишут экзамен."

    scene bg school
    with fade
    show s sad 1 at left31
    show so normal 1 at left3
    show h normal 1 at  right32
    

    if count_test1 <= 4:
        s sad 1 "Я точно плохо сдал!"
        so normal 1 "Ну не унывай, возможно проходной будет!"
        h normal 1 "Да, там же не так трудно было."
    elif 5 <= count_test1 <= 6:
        s sad 1"Ну вроде пойдёт, но много ошибок."
        so normal 1 "Ну хотя бы сдал, уже хорошо."
        h smile 1 "Хехе, а я вот думаю, что первую часть всю правильно написал."
    elif 7 <= count_test1 <= 8:
        s normal 1 "Почти всё сделал, последнее задание не успел."
        h  "А ты смог параметр сделать?"
        s sad 1 "Не, думаю в нём допустил ошибку..."
    elif 9 <= count_test1 <= 10:
        s smile 1 "Вообще всё изи было. Спина только болит."
        so angry 1 "По мне так сложно было!"
        h angry 1 "Непростой вариант, вторая часть все гробы!"

    scene bg room
    with fade

    "Дом Себастиана, получение результатов ЕГЭ."

    if count_test1 <= 2:
        scene bg ege11
        with fade
        "Себастиан видит 11 баллов и ему становится грустно."

        play music fonend fadein 1.0
        window hide
        scene bg gameover with fade
        pause
        "GAME OVER, Себастиан остался на второй год"
        scene title1 with fade
        pause
        return

    elif 3 <= count_test1 <= 6:
        scene bg ege66
        with fade
        "Себастиан видит 66 баллов егэ по математике  и радуется."
        s  "Дворником что ли буду?!"

    elif 7 <= count_test1 <= 8:
        scene bg ege74
        with fade
        "Себастиан видит 74 баллов егэ по математике, расстроен что не 81."
        s  "Да я мегамозг, жалко что не 81!"

    elif 9 <= count_test1 <= 10:
        scene bg ege100
        with fade
        "Себастиан видит 100 баллов егэ по математике, без эмоций смотрит на монитор!"
        s  "Пфф, как это можно не сдать!"

    stop music fadeout 1
    # СЦЕНА 4

    play sound door 

    play music fon41 fadein 3.0

    "Себастиан идет в гости"
    scene bg apartment
    with fade
    show s smile 1 at left2
    show so smile 1 at right2

    s "Привет Соня, давай проходи!"
    so "Приветик!"
    so "Эй, Себастиан, это так здорово, что мы идем в университет! Куда ты собираешься поступать?"
    menu:
        "Ага, действительно здорово!":
            s "Я думаю о поступлении в Урфу. Это же самый крутой вуз на Урале!"
        "Здорово, но немного грустно покидать школу.":
            s "Я думаю о поступлении в Урфу. Это же самый крутой вуз на урале!"

    hide so with dissolve
    hide s with dissolve

    scene bg room

    show s normal 1 at left2
    show so smile 1 at right2
    
    so smile 1 "О, Урфу звучит интересно!"
    s normal 1 "А ты, Соня, куда решила поступать?"
    so normal 1 "Я выбрала МГУ. Хочу пожить в Москве. МГУ - топ один вуз в стране, оттуда точно дураком не выпустишься."
    s smile 1 "Москва, да там будет весело."
    so angry 1 "Но, Себастиан, это означает, что мы долго не будем видеться!"
    s normal 1 "Да, я об этом подумал. Но мы всегда можем оставаться на связи и приезжать друг к другу в гости, верно?"
    so smile 1 "Конечно! Ничто не может разрушить нашу дружбу. Мы всегда будем поддерживать связь и делиться новостями."
    s smile 1 "Точно, ничто не сможет нас разлучить, даже если мы будем далеко друг от друга."


    scene bg apartment
    with fade
    show s normal 1 at left2
    show so normal 1 at right2
    so "Ну я пошла, пока пока!"
    s "Пока!"

    hide so with dissolve

    "Соня уходит домой"

    stop music fadeout 2
    # СЦЕНА 5

    scene black

    play music fon51 fadein 2
    "Хиро пишет в вк Себастиану."

    scene bg message1
    with fade

    menu:
        "Вот 10 августа собрание будет, тогда и отдам.":

            scene bg message11
            with fade
            pause
            scene bg message12
            with fade
            pause
            scene bg message13
            with fade
            pause
            scene bg message14

        "До конца августа время ещё есть, успею.":

            scene bg message21
            with fade
            pause
            scene bg message22
            with fade
            pause
            menu:
                "Оо, давай.":
                    scene bg message23
                    with fade
                    pause
                    scene bg message24
                "Почему бы и нет.":
                    scene bg message232
                    with fade
                    pause
                    scene bg message242
                    with fade
                    pause

        "Ещё не думал даже когда":

            scene bg message31 with fade
            pause
            scene bg message32 with fade
            pause
            menu:
                "Оо, давай":
                    scene bg message331 with fade
                    pause
                    scene bg message341 with fade
                    pause 
                "Почему бы и нет":
                    scene bg message332
                    with fade
                    pause
                    scene bg message342 with fade
                    pause

    stop music fadeout 2

    play music car fadein 1

    scene bg car1
    with fade

    pass

    scene bg car2
    with fade

    "Себастиан и Хиро едут подавать документы в Екатеринбург."
    "Себастиан и Хиро в Екатеринбурге."

    stop music fadeout 2.0

    play music fon51 fadein 1.0

    scene bg park1
    show s normal 1 at left2
    show h normal 1 at right2

    s "У нас ещё много времени до собрания, давай сходим медкомиссию для общежития пройдём."
    h "Да, давай!"

    scene bg obshaga9
    with fade

    show s smile 1 at left2
    show h smile 1 at right2

    h  "Ооо! Та самая 9 общага!!!"
    s  "Вау, хотел бы там жить."
    h normal 1  "Да, она одна из самых новых, там до нас почти никто не жил."

    

    scene bg obshaga11
    with fade

    pause

    show s smile 1 at left2 
    show h normal 1 at right2 

    s  "Ооo, а это 11 общага, там удобная скамейка рядом."
    h  "Ну она постарее выглядит,  коридорного типа."
    s normal 1 "Ну я скорее всего там буду, чтобы в 9 попасть надо высокие баллы по егэ."
    h normal 1 "Ну главное, чтобы в общежитие заселили, а то тут можно за 15 минут до пары проснуться и не опоздать."
    s smile 1 "Хахахаха"

    scene bg medsanchast
    with fade

    "Себастиан и Хиро заходят в медсанчасть."

    scene bg medsanchast1
    with fade

    "Себастиан и Хиро расходятся по разным кабинетам."

    scene bg medsanchast2
    with fade

    show s normal 1 at center
    
    s "Можно войти?"
    d "Да, заходи-те."
    d "Так, Себастиан, вы с Сургута, из 5469160029166829 школы?"
    d "Xммм, длинное название школы."

    menu:
        "Мне много кто так говорил":
            d "Так очень трудно запомнить."
            s smile 1 "Да чего там, всего лишь 16 чисел."
        "Промолчать":
            pass

    "Проходит некоторое время."

    d "Так, всё можете идти."
    s "Спасибо, до свидание."

    scene bg medsanchast
    with fade

    show s normal 1 at left2
    show h normal 1 at right2

    h "Как-то проще, чем я думал."

    menu:
        "Ага, я думал труднее будет.":
            show s smile 1 at left2
            h "Так, вроде уже на собрание надо идти."
        "Согласен":
            h "Так, вроде уже на собрание надо идти."

    scene bg guk1
    with fade

    "Себастиан и Хиро входят в ГУК."

    scene bg guk2
    with fade

    "Идут в актовый зал."
    
    scene bg guk3
    with fade

    "Проходит плодотворно собрание."

    scene bg guk2
    with fade

    show s smile 1 at left2
    show h  smile 1 at right2

    h "Какой там зал большой был."
    menu:
        "Так и само здание универа большое.":
            pass
        "Так оно просто гиганское.":
            pass

    h "Пойдём отнесём может оригиналы документов?"
    s normal 1 "Пойдём."

    scene black
    with fade
    
    "Себастиан и Хиро отдают документы."

    scene bg guk1
    with fade

    show s normal 1 at left2
    show h  normal 1 at right2

    h "Так, а теперь можно поехать домой или пойти гулять."
    menu:
        "Пойдём гулять":
            scene bg ekb1
            with fade

            "Топ-Топ-Топ"

            scene bg ekb2
            with fade
    
            "Топ-Топ-Топ"

            scene bg ekb3 
            with fade
            
            "Топ-Топ-Топ"

            show s smile 1 at center
            s "Так, а теперь пора и домой."
        "Поехали домой":
            pass
            
    stop music fadeout 2.0
    
    play music car fadein 1

    scene bg car1
    with fade
    
    pause

    scene bg car2
    with fade
    pause

    stop music fadeout 1

    jump arka2

    


