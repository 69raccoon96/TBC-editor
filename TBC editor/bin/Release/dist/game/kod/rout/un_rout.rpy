label un_rout:
scene bg int_dining_hall_people_sunset
"Самое главное здание в лагере? Туда, куда идут толпы людей и там, где собираются самые большие группы людей в лагере? Конечно столовая. Вот и сейчас группки пионеров тянулись вереницей к величавому зданию столовой."
"А вон и Ольга Дмитриевна, идет вместе со всеми в столовую!"
"Я рванул в ней, попутно прокручивая варианты времяпровождения после ужина."
show od_smile
show od_pion behind od_smile
show od_telo behind od_pion
me "Ольга Дмитриевна, я вас везде ищу! Вот бегунок, все заполнил."
mt "Молодец Семен, давай его."
"Она взяла бегунок и посмотрела на подписи. "
mt "Я рада, что ты выполнил всё как надо. Иди ужинай, и не забудь - после ужина на площадь, у нас костер, который для всех обязателен."
me "Угу."
scene bg int_dining_hall_people_sunset with Dissolve (0.5)
"Я понуро кивнул, ведь столько планов строил на вечер, а тут костер какой-то..."
"Сегодня на ужин давали: рис с котлетой, чай, булку с сыром \"Дружба\", куда без него? И шоколадку. "
"\"Неплохо, голодному человеку вообще все равно что есть, главное поесть\"."
"Я взял поднос с пищей, осталось выбрать место для употребления данных продуктов. Впрочем, выбирать было не из чего. Все мои знакомые сидели с кем-то, а сидеть с кем-то незнакомым не хотелось. Поэтому я выбрал двух местный столик у окна. Там пока никого не было."
"Когда я поставил поднос на стол, то взглядом зацепил знакомое лицо. Чуть в стороне сидел тот бровастый, с которым я сегодня повздорил. Может, подойти и поговорить?"
menu:
     "Да":
      jump un_rout_answered
     "Нет":
      jump un_rout_notanswered
label un_rout_answered:
$ upoints +=1
"Откладывать в долгий ящик это дело не стоит. Я поставил поднос и подошел к столику."
me "Приятного аппетита!"
pe "Спасибо…"
"Как-то без энтузиазма проговорил он."
me "Извини, пожалуйста, за тот случай в библиотеке… Не сдержался как-то…"
pe "И ты извини -  я тоже погорячился. С прозой у меня и правда не особо - я больше поэзию уважаю. А как тебя звать-то?"
me "Семеном звать."
pe "А я - Юра. Ну, что - мир?"
"Он протянул мне руку."
me "Мир."
"Пожал я в ответ."
ur "Ты уж подсаживайся давай!"
"Точно! Я совсем забыл, что собирался есть! Но перенести поднос - дело нехитрое. С Юрой по соседству сидел только один странный белобрысый пацан, ушедший весь в себя. "
me "А Петлюрой тебя почему обзывают?"
ur "Это погоняло мне еще дома дали, на Ставрополье. Там я порой вообще с полоборота драки начинаю! И многим раздаю по первое число. И по второе тоже. Так что тебе повезло еще, что мы не у меня дома… Хотя, странно, почему Петлюра - тот же Батька Махно куда большего добивался… Но тут уж ничего не сделаешь. "
"Тут неожиданно к нам подлетела Лена. "
show le_telo_3 at left 
show le_smile_3 at left 
show le_pion_3 at left 
un "О, Семен! Вот ты где! Можно подсесть?"
me "Конечно!"
un "Ой! Это же тот парнишка из библиотеки! "
"Вдруг смутилась она."
me "Не переживай. мы уже помирились. "
ur "Нормально всё!"
un "Ну. ладно."
"Она спокойно подсела за столик. "
me "Приятного аппетита. "
un "Спасибо!"
ur "Так вот, с прозой у меня, как видите, так себе, а вот стихи у меня хорошо идут. По музыку любые стихи хороши! Бывает, прочтешь что-то - и мотив уже сам просится на струны!"
me "Ты еще к Мику не записался?"
ur "Да думаю пока. Смущаюсь немного своего репертуара… На меня порой думали, что я - сиделец или детдомовец…"
me "Но ведь ты хорошо играешь на гитаре?"
ur "Ну, есть такое. "
me "Ты можешь на любые стихи мотив сочинить?"
"Он слегка призадумался над почти пустой тарелкой"
ur "Смогу."
me "Тогда зачем себя ограничивать? "
ur "Может, незачем."
me "Представь себе, как бы ты тут у нас блистал на сцене!"
ur "Может, ты и прав… Слушай, лучше я это до завтра еще обдумаю."
"Незаметно содержимое наших тарелок иссякло."
ur "И все же - это не то что дома! У нас мама порой такого борща наготовит - ух!"
"Белобрысый чуть приободрился, услышав про борщ. Юра посмотрел на него."
ur "Не кисни! И на вашей улице Первомай пройдет!"
"С этими словами он забрал поднос и ушёл."
"Моя тарелка тоже была почти чиста, а вот Лена, казалось, насильно себя кормит."
me "Может, помочь?"
un "Не надо, спасибо!"
me "Просто ты как-то с неохотой ешь."
un "У меня с детства так. "
"Организм у меня не требовательный - просит еды ровно столько, чтобы не проголодаться. Поэтому у меня бывает, что даже тарелку грибного супа съешь - а больше есть и не хочется. "
"И ведь детство у нас не особо голодное было…"
"Хотя… Мама в раннем детстве пережила блокаду. Им с бабулей всего по 3 краюшки хлеба на день было! "
"Может, это на генетическом уровне отпечаталось…"
me "Так ты из Ленинграда? "
un "Почти. Мама там прежде жила, а когда познакомилась с папой - переехала в область. "
me "Как далеко в область? "
un "Далеко. Городок небольшой, отбитый от финнов. до него и не всякая электричка доезжает. Зато хорошая природа. Лес, реки, воздух чистый…"
"На секунду возникла пауза. Я собрался было расспросить её чуть подробнее, но меня оборвали."
un "Ты не против, если я доем? "
"Заслушавшись, я не заметил, что Лена так и не притронулась к тарелке. Как нетактично с моей стороны. "
me "Да, конечно."
scene bg int_dining_hall_people_sunset
"Я взял поднос и вышел из-за стола. Белобрысый тоже куда-то делся. "
jump un_rout_after_canteen

label un_rout_notanswered:
"Да нет, еще успеется! Поесть надо как следует. "
"Я присел у окна и приступил к трапезе."
"Прыжок из зимы в лето, детский лагерь, целый хоровод новых лиц, приключение в библиотеке, крестовый поход с обходным листом…"
"На голодный желудок все эти события вертелись в голове так, будто хронику дня быстро-быстро прокручивали в надежде уложиться за 600 секунд. "
"С утолением голода этот калейдоскоп всё мерк и мерк…"
show le_telo
show le_serious
show le_pion
"Когда он окончательно померк, я вдруг заметил, что Лена села за тот же столик."
"Моя тарелка тоже была почти чиста, а вот Лена, казалось, насильно себя кормит."
me "Может, помочь?"
un "Не надо, спасибо!"
me "Просто ты как-то с неохотой ешь."
un "У меня с детства так. "
"Организм у меня не требовательный - просит еды ровно столько, чтобы не проголодаться. Поэтому у меня бывает, что даже тарелку грибного супа съешь - а больше есть и не хочется. "
"И ведь детство у нас не особо голодное было…"
"Хотя… Мама в раннем детстве пережила блокаду. Им с бабулей всего по 3 краюшки хлеба на день было! "
"Может, это на генетическом уровне отпечаталось…"
me "Так ты из Ленинграда? "
un "Почти. Мама там прежде жила, а когда познакомилась с папой - переехала в область. "
me "Как далеко в область? "
un "Далеко. Городок небольшой, отбитый от финнов. до него и не всякая электричка доезжает. Зато хорошая природа. Лес, реки, воздух чистый…"
"На секунду возникла пауза. Я собрался было расспросить её чуть подробнее, но меня оборвали."
un "Ты не против, если я доем? "
"Заслушавшись, я не заметил, что Лена так и не притронулась к тарелке. Как нетактично с моей стороны. "
me "Да, конечно."
"Я взял поднос и вышел из-за стола."
"Когда шоколадка была убрана в карман, ко мне подошла Ольга Дмитриевна, причем явно неспроста."
label un_rout_after_canteen:
scene bg int_dining_hall_people_sunset
show od_telo
show od_smile
show od_pion
with Dissolve (1.0)
if spoints >0:
    mt "Семён! Хорошо, что ты здесь! Мне неудобно тебе об этом говорить, но… "
    "Нам придётся тебя переселять к Лене."
    me "В смысле? Почему?"
    mt "Не спрашивай. Нам тут одна девочка закатила большой скандал из-за своей соседки… Хорошо, что вас там не было. У тебя ведь с собой немного вещей?"
    me "Немного. "
    mt "Отлично! Тогда вот тебе ключи от домика Лены. Если Слави на месте не будет - домик запри и ключ положи под коврик. "
    "Она передала мне новую связку ключей. "
    mt "И да, у меня есть небольшое задание."
    me "Какое?"
mt "Семен, можешь с кем-нибудь пораньше отправится на кострище? Его в порядок надо привести."
me "Не было печали... Может, не я? Почему я? А?"
mt "Ты ответственный человек, бегунок принес один из первых."
"\"Вы глубоко ошибаетесь.\""
me "Ладно, помогу, но у меня одно пожелание."
mt "Ха-хах, вот как? Смело, я слушаю."
me "Я не хочу находиться на костре. Можно после марафета уйти?"
mt "В принципе, да. Ничего страшного не произойдет. Возьми себе помощника."
me "Спасибо. И еще, я почти никого не знаю, назначьте мне помощника сами."
mt "Ну..."
"Она окинула взглядом столовую."
mt "О! Кибернетики, подь сюды."
"Ребята подошли по ближе, по их взглядам читалось разочарование в жизни."
show el_telo_2 at right behind od_telo
show el_sad_2 at right behind od_telo
show el_pion_2 at right behind od_telo
show sh_telo at left behind od_telo
show sh_norm at left
with Dissolve(0.5)
mt "Вы отправитесь с Семеном, готовить поляну для костра. И вам будет от этого бонус. Семен расскажет. Чао!"
hide od_telo
hide od_smile
hide od_pion
with Dissolve (0.5)
sh "Какой бонус?"
me "После уборки сваливаем оттуда и отдыхаем."
sh "Хоть что-то. Пошлите что ли, поляна сама себя не уберет. "
el "И то верно."
"Дружной компанией, или не очень, мы отправились к кострищу."
if spoints > 0:
    me "Стоп. Ещё в пару мест надо зайти. "
    scene bg ext_house_of_sl_day
    "Первым делом мы направились в домик к Славе. К счастью, хозяйка была дома. Я постучал в дверь"
    sl "Да-да?"
    me "Славя! Войти можно? "
    sl "Да-да, конечно!" 
    show bg int_house_of_sl_day with Dissolve(0.5)
    show sl_telo
    show sl_pion 
    show sl_norm
    with Dissolve(0.5)
    sl "Ты ведь уже переселяешься?"
    me "Ну, есть немного. Вот ключи. "
    "Я положил их на столик у окна."
    sl "Спасибо!"
    "Я быстро сложил свой нехитрый скарб в мешок и собрался на выход. "
    sl "До встречи на костре!"
    me "До встречи!"
    scene bg ext_house_of_un_day with Dissolve(1.0)
    "Потом мы бегом дошли до домика Лены."
    scene bg int_house_of_un_day with Dissolve (0.5)
    "Её нет дома. Вот и отлично…"
    show sh_telo at left
    show sh_norm at left
    show el_telo at right 
    show el_smile at right 
    show el_pion at right 
    with Dissolve(1.0)
    me "Помните, я хотел у вас на сохранение оставить одну штуку? "
    sh "Помню."
    me "Пока никого нет - самое время показать её. "
    "Из мешка я достал свой сотовый."
    el "Ух ты! Вот так штука!"
    "Шурик аккуратно взял его в руки и посмотрел."
    sh "Оно заряжается вот отсюда?"
    "Почему-то он указал на разъём для наушников."
    me "Нет, из длинной щели. "
    "Шурик быстро повернул телефон и посмотрел в разъём. "
    sh "Чудо враждебной техники! Повозиться придётся…"
    "На этой ноте он спрятал телефон к себе в карман. "
else:
    me "Стоп. ещё в одно место надо зайти."
    scene bg int_house_of_un_day with Dissolve (0.5)
    "Мы быстро добежали до домика Лены. Её нет дома. Вот и отлично…"
    "Я быстро отпер домик, нашарил в тайнике телефон и вышел с ним."
    show sh_telo at left
    show sh_norm at left
    show el_telo at right 
    show el_smile at right 
    show el_pion at right 
    with Dissolve(1.0)
    me "Помните, я хотел у вас на сохранение оставить одну штуку? "
    sh "Помню."
    me "Пока никого нет - самое время показать её. "
    "Из мешка я достал свой сотовый."
    el "Ух ты! Вот так штука!"
    "Шурик аккуратно взял его в руки и посмотрел."
    sh "Оно заряжается вот отсюда?"
    "Почему-то он указал на разъём для наушников."
    me "Нет, из длинной щели. "
    "Шурик быстро повернул телефон и посмотрел в разъём. "
    sh "Чудо враждебной техники! Повозиться придётся…"
    "На этой ноте он спрятал телефон к себе в карман. А я запер дом, и мы пошли дальше к кострищу"
label koster_un_rout:
scene bg ext_polyana_sunset with Dissolve (1.0)
show sh_telo at left behind od_telo
show sh_norm at left behind od_telo
show el_telo at right behind od_telo
show el_smile at right behind od_telo
show el_pion at right behind od_telo
with Dissolve(1.0)
"Спустя десять минут мы дошли до кострища. Нельзя сказать, что на нём было слишком сильно насорено - бытового мусора почти не было, но всяких веточек хватало. И вокруг были набросаны кирпичи. Электроник их тем временем пересчитывал."
el "…пятнадцать, шестнадцать, семнадцать."
me "Складываем их колодцем, оставим только поддувало небольшое. Шурик! Бумаги какой-нибудь не видно?"
sh "Есть немного! "
"Он пришёл с охапкой веток и какими-то испохабленными бумажными листиками. Вид у них был потрёпанный - печатные буквы растеклись по бумаге, расплывшейся небольшими волнами. Ясно - самиздат…"
show bg koster2 with Dissolve(3.0)
"За пару минут кирпичи были уложены в один ровный колодец, а все немногие лежавшие на поляне ветки были сложены в одну кучку с бумажками."
sh "Маловато будет! "
me "Не беда! За сухостоем пойдём! "
"Всякий раз, когда я гулял по лесу, меня удивляло одно: сухостой. Его всегда было МНОГО. Казалось, что если собрать хотя бы несколько поваленных деревьев, то минимум на месяц можно будет обеспечить камин топливом! Но валежник всё лежит, мшеет и просто теряется из виду, будто его и не было никогда. "
"Так, вот и первые три дерева. Одно совсем повалилось, другое - слегка косо, но стояло, третье просто стояло засохшим."
me "Сначала берём вон то лежащее, потом берёмся за покосившееся, и, если хватит сил, засохшее. "
sh "Как мы их дотащим?"
me "Я -  в середине, вы - по краям. "
el "Ясно."
"С первым деревом проблемы практически не возникло. Второе пришлось доваливать, запрыгнув сверху. Третье же даже так не далось - пришлось подпирать ребятам снизу."
me "Ребята, вы пока их переломайте, а я ещё чего-нибудь отыщу."
el "А не перебор ли будет? "
me "Не будет. "
"Три ходки спустя вдалеке от поляны уже стали слышаться голоса. "
me "Всё, тормозись!"
"Ребята облегчённо выдохнули. Уж не перегрузил ли я их? Куча получилась очень большой."
"Интересно, что там за бумажки были? Я добрал немного веток, положил в кострище и присел на корточки. "
"Из поплывшего текста можно было разобрать только один абзац:"
"\"В мире, где рабочий день короток, где каждый сыт и живёт в доме с ванной и холодильником, владеет автомобилем или даже самолётом, самая очевидная, а может быть, и самая важная форма неравенства уже исчезла. Став всеобщим, богатство перестало порождать различия…\""
"Дедушка Оруэлл, значит? Неслабо…"
show od_telo 
show od_surp 
show od_pion 
with Dissolve(0.5)
mt "Вот и пришли! Ух ты! Что это тут у нас?"
"Ольга Дмитриевна удивлённо смотрела на кучу брёвен. Кибернетики дружно посмотрели на меня. "
sh "Это всё он!"
el "Это всё он!"
mt "Семен, я знаю, что ты - ответственный и трудолюбивый, но не слишком ли много ты набрал? "
me "Не страшно! Другим отрядам ещё останется!"
mt "Ну, пожалуй, ты прав. Ладно! За ударный труд тебе и кибернетикам я выражаю благодарность!"
"Взяв под козырёк, мы втроём плюхнулись от усталости на ближайшее бревно."
"Наконец Ольга Дмитриевна попросила всех собраться поближе. Она взяла спички и подожгла бумагу. "
scene bg koster with Dissolve(2.0)
"Кто-то из толпы неожиданно запел:"
"\"Взвейтесь кострами, синие ночи...\""
"Лагерные песенки у костра. Лепота."
"Дальше подхватила наша уважаемая вожатая."
"\"Мы-пионеры, дети рабочих...\""
"И вот уже вся толпа вторила маленькой красноволосой девчонке:"
"\"Близится эра светлых веков…\""
"Текста я не помнил, поэтому просто мычал в такт. "
"«Так более можно проникнуться атмосферой, еще бы картошечки, да шашлычка с горяченьким, ммм…»"
"Я сидел и смотрел на огонь. Он был прекрасен, настолько, что им можно было наслаждаться вечно, не зря говорили что можно наблюдать за ним вечно. Он чем-то притягивал. Вокруг смеялись дети, недалеко играл парень на гитаре, кто-то пел под нее, кто-то даже умудрялся бегать по округе, в основном это были младшие отряды. "
sh "Не знаю, как вы, ребята, а я уже домой пойду."
el "Да я уж тоже отдыхать пойду. Семен, ты пойдёшь? "
menu:
     "Идём домой":
      jump un_rout_going_home
     "Остаёмся":
      jump un_rout_stay
label un_rout_going_home:
$ lpoints +=1
me "Да уж, мне тоже пора. "
"Я встал и полусонно побрёл домой."
scene bg ext_path_night with Dissolve(1.0)
"Всю дорогу меня не отпускало ощущение, что я упускаю что-то важное. Что именно, я вспомнил только у дверей домика. "
"\"Точно! Лена же со мной встретиться хотела! Надеюсь, я не припозднился ещё.\""
scene bg ext_square_night with Dissolve(1.0)
"На моё счастье, она сидела на скамейке на площади."
me "Ты меня не потеряла?"
"Она аж подпрыгнула от испуга."
show le_telo_2
show le_shocked_2
show le_pion_2
with Dissolve(0.5)
un "Да немножечко."
me "Ольга Дмитриевна меня вызвала с костром помогать."
show cg d2_evnening with Dissolve (1.0)
un "И ты не остался?"
me "Не мог же я не прийти."
un "Спасибо!"
me "А что ты тут делаешь?"
un "На звёзды смотрю."
scene anim stars with Dissolve (1.0)
"Я поднял голову. Множество огоньков - какие-то яркие, какие-то менее заметные, какие-то вообще мигающие - сияли над нами. "
"Я никогда не понимал, что можно находить в том, чтобы просто смотреть на звёздное небо, но знаю, что это как-то завораживало. "
"Отсюда, с Земли, они смотрятся маленькими светящимися точками, и вряд ли много кто может сказать, сколько небесных тел вокруг них вертится. "
"Ко времени, когда меня сюда забросило, учёные даже не могли толком сказать, обитаемы ли иные планеты или нет. "
me "Не знаешь, что в этом такого особенного - смотреть на звёзды?"
un "Не знаю. Кажется, что они пытаются поговорить со мной. Там тоже есть люди, у них - своя жизнь, наверное, лучшая, чем у нас, и они тоже вот так вот смотрят на небо и видят Землю, меня, тебя. "
me "Интересная теория. "
un "Самая обычная. "
me "Знаешь песню про белых журавлей?"
un "Знаю. Папа её очень любит."
me "Мне кажется, что все ушедшие - не только солдаты - тоже превращаются в звёзды. Видишь вот ту звезду?"
"Я показал на Рыбы, примерно туда, где была звезда ван Маанена. "
un "Вижу. "
me "А ведь она давным-давно погасла. А её свет нам всё ещё виден. Также и с человеком - память его может очень надолго пережить. Мы не видели живыми Пушкина, Шостаковича, Шаляпина - но они оставили нам многое, и поэтому мы их помним."
un "Красивая идея!"
"Ненадолго повисло молчание. Мы просто сидели и смотрели на звёздное небо. Вдруг его решила прервать Ольга Дмитриевна"
mt "Так-так… Вы тут и спать собираетесь? "
me "Нет! "
mt "Тогда поторопитесь домой - отбой скоро. "
un "Хорошо!"
mt "Доброй ночи!"
me "Доброй ночи!"
"Быстрым шагом мы дошли до дома. Лена зашла в дом первой."
jump un_rout_going_sleep
label un_rout_stay:
"Пока все предавались хоровому пению, я сидел и прокручивал все, что сегодня со мной приключилось."
scene anim intro_3
show prologue_dream
"Лужа" 
show anim intro_13
"Автобус" 
scene cg sl_bus 
show prologue_dream
"Странные голоса у меня в голове, Славя, спящая на плече,"
scene bg ext_bathhouse_evening1
show prologue_dream
"Баня"

scene koster
show prologue_dream 
"Такой эмоциональной встряски у меня уже давно не было. И что самое обидное - это то, что я ни на пиксель не приблизился к хоть какому-то логическому объяснению моего пребывания здесь. Я не из этого мира…"
"Но с другой стороны, тут довольно-таки неплохо. Нет, не так. Весело? Да, здесь весело. Мне кажется, что здесь будет много интересного, хоть это меня и пугает. Разберемся по ситуации..."
"Когда мои размышления подходили к концу, Ольга Дмитриевна уже заканчивала свою речь о долге пионеров, о прекрасном лагере, о светлом будущем коммунизма, ну и тому подобное."
mt "И самое главное, ребята. Сделайте так, чтобы от этой смены у вас остались только хорошие воспоминания. Желаю вам успехов!"
"Костер уже почти совсем погас, и становилось все холоднее..."
mt "Ну, что ж. До отбоя полчаса. Советую всем пойти подготовиться ко сну. Завтра будет очень важный день для каждого из вас. Хорошенько выспитесь!"
"Пионеры потихоньку начали строиться, а я до сих пор сидел и залипал на тлеющие угли. Из ступора меня вывела Ольга Дмитриевна."
scene koster2 with vpunch
show od_telo 
show od_smile
show od_pion 
with Dissolve(1.0)
mt "Семен, ты идёшь домой?"
me "Да, конечно. "
"Я встал и полусонно побрёл домой."
scene bg ext_path_night with Dissolve(1.0)
"Всю дорогу меня не отпускало ощущение, что я упускаю что-то важное." 
scene bg ext_house_of_un_night with Dissolve(1.0)
"Что именно, я вспомнил только у дверей домика. "
"\"Точно! Лена же со мной встретиться хотела! Какой конфуз…\""
un "Семен! Наконец-то! Что же так долго? Где ты пропадал?"
scene bg ext_house_of_un_night with vpunch
"Лена подошла так неожиданно, что я даже подпрыгнул от лёгкого испуга." 
show le_telo_2
show le_sad_2
show le_pion_2
with Dissolve(0.5)
"Смотрела она как-то понуро и разочарованно."
me "Ольга Дмитриевна меня вызвала с костром помогать."
un "А-а-а… Ладно тогда."
"Лена подошла к двери, отперла и быстро зашла внутрь."
label un_rout_going_sleep:
un "Не мог бы ты подождать тут немного? Я быстро, правда."
me "Конечно, без проблем."
scene bg ext_night_sky with Dissolve (1.0)
"Пока Лена переодевалась, я уставился на звездное небо." 
"У меня не было желания подглядывать за ней. Все мои мысли были там... среди звезд."
scene bg ext_house_of_un_night with Dissolve(0.5)
"Наконец, она приоткрыла дверь."
un "Спасибо, что подождал."
me "Ага."
scene bg int_house_of_un_night
show le_telo_2
show le_sad_2
show le_pion_2
with Dissolve(0.5)
"Зайдя внутрь, я вспомнил, что Лена почти ничего не ела. Я достал из кармана шоколадку и отдал ей."
me "Держи, а то, наверное, проголодалась после суматошного дня."
un "Спасибо большое, Семен."
hide le_sad_2
show le_smile_2
with Dissolve (0.3)
"Сказав это, она искренне по-детски улыбнулась мне."
"Таких ласковых слов мне никто не говорил. У меня приятно защемило в груди и тепло мягко разлилось по моему телу."
"Лена извлекла из своего огромного чемодана печенье и термос. Она протянула мне чай и печенье."
un "Хочешь? А то есть одной как-то неудобно."
me "Спасибо, не откажусь."
"«Полуночный перекусы, эх, молодость, молодость…»"
"Еще теплый чай и вкусное печенье были как нельзя кстати. Отличное завершение сумасшедшего дня."
me "Давай спать. Завтра будет трудный день."
un "Спокойной ночи, сладких снов."
"Я разделся и лег на кровать. Усталость накрыла меня с головой, будто цунами. Я уже не был в состоянии что-либо анализировать, поэтому я вяло сказал \"спокойной ночи\" и Морфей унес меня на своей колеснице куда-то далеко... к звездам."
