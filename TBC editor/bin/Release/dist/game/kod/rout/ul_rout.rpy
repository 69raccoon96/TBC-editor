label koster_ulya:
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
"Я понуро кивнул, ведь столько планов строил на вечер, а тут костер какой-то..."
"Сегодня на ужин давали: рис с котлетой, чай, булку с сыром \"Дружба\", куда без него? И шоколадку. "
"\"Неплохо, голодному человеку вообще все равно что есть, главное поесть\"."
"Я взял поднос с пищей, осталось выбрать место для употребления данных продуктов. Впрочем, выбирать было не из чего. Все мои знакомые сидели с кем-то, а сидеть с кем-то незнакомым не хотелось. Поэтому я выбрал двух местный столик у окна. Там пока никого не было."
"Сев за столик, я начал очень быстро есть пищу, не хотелось размусоливать. Хотя торопиться некуда, после столовой - костер. На который идти совсем не хотелось, хотелось погулять по лагерю и лечь спать."
scene bg int_dining_hall_people_sunset
show ul_hitr
show ul_pion behind ul_hitr
show ul_telo behind ul_pion
us "Семен! Я к тебе сяду."
"Утвердительно сказала Ульяна."
me "Может у меня занято?"
us "Не, не занято. Ты лучше скажи – на костер идешь?"
me "Иду, конечно. "
us "Отлично! Тогда я смогу поиграть снова в твою игрушку!"
me "Какую еще игрушку?"
us "В которую я играла, когда увидела тебя…"
me "Понял тебя. "
"Резко прервал Ульяну на полуслове. Незачем окружающим знать, что было около бани."
"Ульяна хихикнула. "
me "Через сколько будет костер? И где?"
us "Можешь сразу после столовой идти на площадь, там встречаемся."
me "Угу."
"Я быстро доел свой ужин и собрался уходить, но Ульяна с набитым ртом меня остановила."
us "Подофти феня, я уфе доефла."
me "Прожуй сначала, потом уж говори."
"Я терпеливо дождался, пока Ульяна прожует и соберет грязную посуду на поднос."
"Мы вышли из столовой и Ульяна вприпрыжку понеслась к площади с Гендой во главе."
scene bg ext_square_sunset
show ul_hitr
show ul_pion behind ul_hitr
show ul_telo behind ul_pion
"А мне что оставалось делать? Идти за ней. Одному было бы скучно, а Ульяна создает вокруг себя ауру веселья и счастья, не становится грустно и одиноко."
us "Семен, что ты такой медленный?"
me "Некуда спешить, посмотри на площадь – тут пусто."
"На площади не было ни души. Только Генда гордо стоял посередине."
us "Сейчас подтянутёся! Главное мы на месте. Дай игрушку."
me "Нет. Здесь могут увидеть и тогда возникнут лишние вопросы."
us "Ну блин, и чем же заняться?"
me "Я не знаю. Пойду на скамейку и посижу."
us "Как же скучно ты проводишь время."
scene bg ext_square_sunset with Dissolve(1.0)
show od_telo
show od_surp
show od_pion
with Dissolve(0.5)
"Тут внезапно подошла Ольга Дмитриевна."
mt "Семён! Хорошо, что ты здесь! Мне неудобно тебе об этом говорить, но… "
mt "Нам придётся тебя переселять третьим."
me "В смысле? Почему?"
mt "Не спрашивай. Нам тут одна девочка закатила большой скандал из-за своей соседки… Хорошо, что вас там не было. У тебя ведь с собой немного вещей?"
me "Немного. "
mt "Отлично! Тогда иди собирайся, бери с собой вещи и ключи и подходи к администрации. "
me "Хорошо. "
mt "Ульяна! Ты идёшь со мной! Это и тебя тоже касается! "
"Они быстро скрылись из виду. "
me "Вот и отдохнули!"
if spoints == 1:
    scene bg int_house_of_sl_day
    "Я быстро добежал до домика, с которым мне предстояло попрощаться."
    "На укладку своего нехитрого скарба я затратил где-то около трёх минут. "
else:
    scene bg int_house_of_un_day
    "Я быстро добежал до домика, с которым мне предстояло попрощаться."
    "На укладку своего нехитрого скарба я затратил где-то около трёх минут. "
scene bg1
"Когда я подошёл к администрации, у дверей стояли Ольга Дмитриевна и Евгений Борисович, а из-за поворота показалась Ульянка, тащившая перед собой какую-то тележку. "
show od_telo at left
show od_surp at left
show od_pion at left
show ul_hitr
show ul_pion behind ul_hitr
show ul_telo behind ul_pion
with Dissolve(0.5)
us "Ты уже здесь! Отлично! Представляешь, как здорово? Тебя переселяют к нам в домик! Будем вместе с Алисой втроём жить!"
me "Да ну! А как вы меня там устроите?"
us "Вот для этого нам тележка и понадобится! "
ebn "Семен, хочу представиться – я директор лагеря, Евгений Борисович. Остальные меня знают, а вот с тобой как-то не пересекались еще."
"Евгений Борисович доброжелательно протянул мне свою руку, я поколебался несколько мгновений, даже не знаю почему, и пожал руку директору. "
eb "Хотя, честно признаюсь, не при таких обстоятельствах я хотел бы познакомиться. Тут такое дело, что из-за скандала с жилплощадью нам тебя приходится переселять. Прости уж, но домик придётся делить на троих. А впрочем, оно, может, и к лучшему - ты ведь парень пунктуальный, дисциплинированный. Так может, ты у этих разбойниц порядок наведёшь."
me "Евгений Борисович, я не против, но как меня там спать уложите? "
eb "Вот за этим мы и здесь. В холле стоит пара раскладных кресел - возьми одно в домик."
"Понятно теперь, зачем Ульянка тележку прикатила."
me "Хорошо. "
eb "Но прежде - поменяем ключи. "
"Я сдал свой старый комплект и сразу получил новый. Евгений Борисович строго взглянул на меня."
eb "Но учти: это - запасной комплект. Если где-нибудь посеешь - всё до последней травинки у меня осмотришь. Ясно?"
me "Ясно. "
"Евгений Борисович посмотрел на Ольгу Дмитриевну. "
eb "Я знал, что этот день настанет!"
"Самая тяжесть с креслом была не столько в его весе, столько в том, как за него надёжнее ухватиться. Снаружи меня уже хватились. "
eb "Помочь?"
me "Не надо! Я уже справился!"
"Найдя, где ухватиться, я бодро потащил кресло к выходу, и, пару раз чуть не оступившись на лестнице, осторожно водрузил его на тележку"
us "Ух ты!"
eb "Молодец! Гигант!"
scene cg1 with Dissolve(1.0)
"Катить на тележке эту дурынду было легче. Настолько, что Ульянка быстро запрыгнула на кресло, а я этого даже не почувствовал."
us "Мы едем-едем-едем в далёкие края!… "
"Странно, у меня в голове сейчас играл другой мотив. Даром что Спилберг не рядом! "
"Так припеваючи и прошла дорога до домика. "
scene bg ext_house_of_dv_day with Dissolve(1.0)
show ul_telo
show ul_hitr
show ul_pion

show dv_telo_4
show dv_smile_4
show dv_pion2_4
with Dissolve(0.5)
dv "О-о-о, кто к нам колёса катит! "
"Едва мы докатились, как Алиса бодро спрыгнула со ступеньки, наблюдая за тем, как я пытаюсь ухватить кресло, а потом ухватилась за него сама."
me "Не надо, я сам!"
dv "Ага! Вижу я, как ты \"сам\"…"
show bg int_house_of_dv_sunset
"Мне было неудобно. Как будто она меня тащила вместе с креслом. Его сразу поставили в угол напротив двери. "
dv "С собой много шмоток? "
"Я показал на оставшийся на тележке пакет. "
dv "Ясно… Тогда клади в мой ящик. "
"Пакет быстро нашёл свой приют на одной из нижних полок. "
dv "В общем, всё просто: не ныть, не нудить, не таскать что ни попади без спросу, не пытаться навязать свой устав - и будет тебе с нами счастье. ОК?"
me "ОК."
us "Ребята! Побежали скорее! Там все на костёр собираются!"
scene bg ext_square_sunset
"На площадь потихоньку собирался пионерский люд." 
scene cg lineup2
"В центр вышла глубоко уважаемая Ольга Дмитриевна и громким, властным голос приказала, по-другому ее речь нельзя расценивать, строиться парами и выдвигаться за ней."
"Я огляделся вокруг: из моего отряда, самых взрослых из пионеров, была только Славя. Но она уже встала с Ольгой Дмитриевной в первый ряд. "
scene bg ext_square_sunset
show ul_telo
show ul_smile
show ul_pion
us "Пошли со мной, Семен."
"Ульяна уже тянула меня за собой, когда я даже не успел обдумать ее предложение. "
me "Хорошо, хорошо, хватит меня уже тянуть, я сам могу идти."
scene bg ext_path_day with Dissolve(2.0)
"До костра дошли достаточно быстро, не так далеко он был, по пути Ульяна постоянно над чем-то смеялась с подружкой, которая шла позади нас, а я просто шел, переставляя ноги, словно недоработанный робот."
scene bg ext_polyana_sunset with Dissolve (2.0)
"Придя на поляну, вожатая распорядилась идти мальчикам за хворостом, а сама со Славей начала собирать из разбросанного кирпича костер."
scene bg koster2 with Dissolve(2.0)
"Я собрал парочку веток, скинул их в общую кучу и сел на самый дальний край бревна – впереди всех не было смысла садиться: дым, жар, мешали бы наслаждаться атмосферой пионерского костра."
"На улице темнело, и пора бы уже зажигать костер, и вот уже горящая спичка в руках у вожатой, направление к костру и зажигание." 
show bg koster with Dissolve (2.0)
"Вот, через пару минут костер ритмично потрескивает и освещает пионеров, которые собрались на бревнах, около костра."
"Где-то заиграла гитара, некоторые пионеры запели «Взвейтесь кострами». Я посмотрел на гитариста, это был парень лет 15. "
"«Так более можно проникнуться атмосферой, еще бы картошечки, да шашлычка с горяченьким, ммм…»"
"Я сидел и смотрел на огонь. Он был прекрасен, настолько, что им можно было наслаждаться вечно, не зря говорили что можно наблюдать за ним вечно. Он чем-то притягивал. Вокруг смеялись дети, недалеко играл парень на гитаре, кто-то пел под нее, кто-то даже умудрялся бегать по округе, в основном это были младшие отряды. Мне дико захотелось курить, такое бывает, когда я ночью засиживался за компьютером и вот сейчас как раз тот момент. Я встал с насиженного места, отошел подальше от костра, туда где он уже еле-еле освещал территорию. Достал пачку Космоса, чиркнул зажигалкой."
"Сизый дым ушел в темноту ночного неба. Как же приятно покурить, сразу становилось легко и приятно. "
show ul_telo_2
show ul_angry_2
show ul_pion_2
us "Семен! Ты что, опять куришь?"
"Позади раздался нравоучительный голос Ульяны, хоть и было всего 14, но видимо чтение о вреде курения, она не собиралась отменять."
us "Это очень вредно, мне папа знаешь что рассказывал? Если курить, то можно легкие выплюнуть!"
me "Байки."
us "Вот и нет! Я читала об этом."
me "А мне доктора говорили, что курение размягчает горло. "
us "Они - дураки."
me "Но у них - учёные степени. "
us "Тогда они - учёные дураки."
"Это заявление оказалось настолько смелым и уверенным, что я просто-таки поперхнулся дымом."
us "Вот видишь? Выкинь ее, не медля! Себе же вредишь."
me "Хорошо."
"Я затушил четверть сигареты о дерево и выкинул в кусты."
me "Довольна?"
us "Нет! Теперь пачку выкидывай в…"
"Ульяна пару секунд подумала и выдала:"
us "В костер кидай! И быстро."
me "Еще чего! Не тебе меня учить, иди вон, бегай."
us "Ну, Семен! Выкинь их, пожалуйста! Ты правда вредишь себе."
scene bg koster
show ul_telo
show ul_sad
show ul_pion
"Посмотрел на Ульяну – она и вправду была озабочена моим курением. На лице читалась молящая просьба избавиться от них. Я был, конечно, против, ведь эта привычка укоренилась во мне, похоже, навсегда, но от взгляда Ульяны становилось не по себе."
"Я подумал еще несколько минут. Серьезно, я собирался бросать курить,  ибо это сжигало мой скудный бюджет и здоровье, и получилось так, что совпало с требованием, даже, скорее, просьбой, Ульяны."
me "Хорошо! Только не думай, что это благодаря тебе."
"Буркнул я и направился к затухающему костру."
us "Спасибо!	"
"Дойдя до костра, я быстро достал пачку Космоса и бросил в красные угли. Пачка мгновенно загорелась. Недалеко стояла Ольга Дмитриевна ко мне спиной, разговаривая со Славей, та не обратила на меня внимание. "
"«Теперь точно все. День подошел к завершению, можно идти спать»."
scene bg ext_path_night
"Обратно мы шли в приподнятом настроении. Видимо, слезать с застарелой иглы будет легче. "
show ul_telo
show ul_hitr
show ul_pion
us "А когда ты мне уже дашь поиграть?"
me "Игрушка у меня в вещах. Когда дойдём - дам. "
us "Хорошо. "
me "Только чур не засиживайся с ней, хорошо? "
us "Хорошо! А что такого страшного будет?"
me "Во-первых, зарядки у меня нет - значит, надо договариваться с кибернетиками. Во-вторых, долгое сидение за ней вызывает вред чуть ли не больший, чем от курева. "
us "Да ты что!"
me "Да-да! Тебе ведь мама не разрешает сидеть долго у телевизора?"
us "Да. Она говорит, что это портит зрение."
me "Да. И на самом деле - не только это… Но не суть. С технической точки зрения - это тот же телевизор, и последствия от сидения с ней  - почти такие же. Если много времени перед ней будешь проводить - станешь как Баба Яга: старой, морщинистой и сгорбившейся!"
us "Ужас!"
me "Или станешь похожим на Кощея Бессмертного. Как я, примерно. "
"Конечно же, сначала я хотел это обернуть в шутку, но неожиданно для себя уловил, что говорю всё более и более серьёзно. Ведь и правда, я всё больше и больше костнел, бессмысленно проводя время перед компьютером и не пытаясь превратить свою отсидку во что-то более серьёзное. "
"А ведь здесь, в советских реалиях, тот же смартфон был бы куда более серьёзной штукой. Представить только - он обладает вычислительными мощностями побольше, чем у космических аппаратов \"Вояджер\" и \"Пионер\"! А памяти его хватает, чтобы чуть ли не всю Ленинку за раз загрузить! Как же мы этим бестолково распоряжались!"
us "О-о-ой… Что же тогда делать?"
me "Использовать его аккуратно и разумно, всерьёз отмерять время использования, и не тратить его память зря."
us "Хорошо! Тогда я возьму его только на полчасика, хорошо?"
me "Хорошо! Там я поставлю таймер - отдашь мне, когда он прозвенит."
us "Так там ещё и будильник есть? Здорово!"
me "Не только. Там есть и карты, и библиотека разных книг, и много всего полезного… Но опять же, это - экспериментальная разработка, и пока ещё инженеры думают над тем, как сделать её массовой. "
us "Понятно." 
show bg ext_house_of_dv_night with Dissolve(1.0)
us "О, вот мы и пришли!"
"Когда мы дошли до дома, в окнах не горел свет. Видно, Алиса уже спит. Ульяна аккуратно открыла дверь и зашла внутрь. "
us "Подожди немного."
scene bg ext_house_of_dv_night 
"Полусонно я присел на ступеньку. По ощущению прошло где-то минуты две."
show ul_telo
show ul_hitr
show ul_pion
us "Всё! Можешь заходить."
scene bg int_house_of_dv_night
"Ульянка впустила меня и быстро закрыла дверь. Я залез в свой шкаф за обещанным."
me "Тихо! Смотри, чтобы Алиса не увидела."
us "Ничего! Я с головой одеялом накроюсь. "
"И она быстро прыгнула с прибором под одеяло. На удивление, оно и в самом деле ничего не просвечивало. Да уж, это не китайский легпром."
"Тем временем я быстро разложил кресло и застелил его."
us "Спать уже будешь?"
me "Да. Устал по-чёрному."
us "Если ты уснёшь перед тем, как звонок зазвенит - я тебя разбужу."
me "Спасибо. Доброй ночи!"
"Я живенько разделся и улегся на кровать, под одеяло." 
"Сон шел очень быстро."
show blink_up with Dissolve(5.0)
"Сумбурный и тяжкий на события день сыграл свою роль." 
"Лишь в последний момент перед тем, как уснуть, меня разбудила Ульянка."
scene int_house_of_dv_night with vpunch
show ul_telo
show ul_smile2
show ul_pion
us "Семен! Время прошло!"
me "А?"
us "Я говорю, время уже вышло на игрушке!"
me "Ах да! Спасибо!"
us "Спокойной ночи!"
"Сказала она, громко зевнув после этого. "
scene int_house_of_dv_night with Dissolve(1.5)
"Прежде, чем выключить смартфон и отложить в ящик, я посмотрел на экран."
"Дисплей показывал, что ушла ровно половина от заряда батарейки."
"\"ПОТРАЧЕНО…\""
"Значит, надо будет попытаться дополнительно потрясти кибернетиков. Но это завтра. "
show blink_up with Dissolve(3.0)
"А я вновь рухнул в кресло, и Морфей лишь сильнее призывал ко мне сон..."
show black with Dissolve (2.0)