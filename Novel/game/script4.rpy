label arka4:
    
    play music fon4 fadein 1.0

    scene black with fade

    "Себастиан на пенсии"

    if 20 <=count_test1 < 30:
        
        scene bg moscowsity with fade

        pause

        show s normal 3 at left2

        s "Не зря я старался!"

        "Вы заработали [count_test1] баллов из 40 и вышли на первую из двух самыйх успешных концовок. Поздравляем!"
        scene title1 with fade
        pause
        return

    else:

        scene bg bali with fade

        pause

        show s normal 3 at left2

        s "Как же хорошо, на Бали."

        "Вы заработали [count_test1] баллов из 40 и вышли на первую из двух самый успешных  концовок. Поздравляем!"

        scene title1 with fade
        pause

        return 

