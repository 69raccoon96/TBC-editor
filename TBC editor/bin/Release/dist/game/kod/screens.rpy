screen say:

    # Умолчания для side_image и two_window
    default side_image = None
    default two_window = False

    # Решаем, нужен ли нам двухоконный или однооконный вариант.
    if  two_window:

        # Вариант с одним окном.
        window:
            id "window"

            has vbox:
                style "say_vbox"

            if who:
                text who id "who"

            text what id "what"




    else:

        # Вариант с двумя окнами.
        vbox:
            style "say_two_window_vbox"

            if who:
                window:
                    style "say_who_window"

                    text who:
                        id "who"

            window:
                id "window"

                has vbox:
                    style "say_vbox"

                text what id "what"






    # Если есть изображение, отобразить его над текстом.
    if side_image:
        add side_image
    else:
        add SideImage() xalign 0.0 yalign 1.0

    # Использовать быстрое меню.
    #use quick_menu

screen nvl:

    window:
        style "nvl_window"

        has vbox:
            style "nvl_vbox"

        # Отображать диалог.
        for who, what, who_id, what_id, window_id in dialogue:
            window:
                id window_id

                has hbox:
                    spacing 10

                if who is not None:
                    text who id who_id

                text what id what_id

        # Отображать меню, если есть.
        if items:

            vbox:
                id "menu"

                for caption, action, chosen in items:

                    if action:

                        button:
                            style "nvl_menu_choice_button"
                            action action

                            text caption style "nvl_menu_choice"

                    else:

                        text caption style "nvl_dialogue"

    add SideImage() xalign 15 yalign 100


screen main_menu:
    on "show" action Start()
    modal True

    if persistent.mainchange :
      if persistent.complete == True:
        imagemap:

            ground "image/screens/menu/menu.png"
            hover "image/screens/menu/menu2.png"
            alpha False
            hotspot (685, 441, 527, 111):
                action [Hide("scr_list"), Start()]
            hotspot (732, 587, 435, 107):
                action ShowMenu("save_screen")
            hotspot (718, 715, 466, 122):
                action ShowMenu("preferences")
            hotspot (802, 847, 295, 131):
                action Quit(confirm=True)

      else:

        imagemap:
            ground "image/screens/menu/menu.png"
            hover "image/screens/menu/menu2.png"
            alpha False
            hotspot (685, 441, 527, 111):
                action [Hide("scr_list"), ShowMenu("game_new_prompt")]
            hotspot (732, 587, 435, 107):
                action ShowMenu("save_screen")
            hotspot (718, 715, 466, 122):
                action ShowMenu("preferences")
            hotspot (802, 847, 295, 131):
                action Quit(confirm=True)




init -2 python:

    # Сделать все кнопки главного меню одноразмерными.
    style.mm_button.size_group = "mm"

init python:
    _game_menu_screen = "main_menu"

screen choice:
    window:
        style "menu_window"
        xalign 0.5
        yalign 0.5

        vbox:
            style "menu"
            spacing 2

            for caption, action, chosen in items:

                if action:

                    button:
                        action action
                        style "menu_choice_button"

                        text caption style "menu_choice"

                else:
                    text caption style "menu_caption"

init -2 python:
    config.narrator_menu = True

    style.menu_window.set_parent(style.default)
    style.menu_choice.set_parent(style.button_text)
    style.menu_choice.clear()
    style.menu_choice_button.set_parent(style.button)
    style.menu_choice_button.xminimum = int(config.screen_width * 0.1)
    style.menu_choice_button.xmaximum = int(config.screen_width * 0.1)
##############################################################################
# Navigation
#
# Экран, включаемый в другие экраны для отображения навигации и фона.
# http://www.renpy.org/doc/html/screen_special.html#navigation
screen navigation:

    # Фон игрового меню.
    frame:
        background "#0000"
    if persistent.mainchange:
      if persistent.complete == True:
        imagemap:
            ground "image/screens/button_back.png"
            hover "image/screens/button_back_on.png"
            alpha True


            hotspot(852, 892, 243, 116) action [ShowMenu('main_menu'), Hide('preferences'), Hide('save_screen')]
      else:
        imagemap:
            ground "image/screens/button_back.png"
            hover "image/screens/button_back_on.png"
            alpha True

            hotspot(852, 892, 243, 116) clicked Return()
screen navigation2:

    modal False

    # Фон игрового меню.
    window:
        style "gm_root"

    # Кнопки.
    frame:
        style_group "g"
        background "#0000"
        xalign .99
        yalign .01
        if persistent.mainchange:
            if persistent.complete == True:
              imagemap:
                xalign .99
                yalign .01
                ground "image/screens/CL.png"
                hover "image/screens/CL_on.png"
                selected_idle "image/screens/CL.png"
                selected_hover "image/screens/CL_on.png"
                alpha True


                hotspot(0,0, 239, 120) action [ShowMenu('main_menu'), Hide('preferences'), Hide('save_screen')]
            else:
              imagemap:
                xalign .99
                yalign .01
                ground "image/screens/CL.png"
                hover "image/screens/CL_on.png"
                selected_idle "image/screens/CL.png"
                selected_hover "image/screens/CL_on.png"
                alpha True
                hotspot(0,0, 239, 120) action Return()
init -2 python:
    persistent.complete = True
    style.g_button.size_group = "gm_nav"
    style.g_button_text.font = "image/screens/fonts/MenuLight.ttf"
    style.g_button_text.size = 48
    style.g_button_text.color = "#FFF6"
    style.g_button_text.hover_color = "#FFFF"

##############################################################################
# Save, Load
#
# Экраны для сохранения и загрузки игры.
# http://www.renpy.org/doc/html/screen_special.html#save
# http://www.renpy.org/doc/html/screen_special.html#load

# Ибо сохранение и загрузка очень похожи, мы совмещаем их в один экран,
# file_picker. Потом мы используем его из экранов
# загрузки и сохранения.

screen file_picker:

    frame:
        style_group "MAX"
        background "#0000"
        left_padding 240
        top_padding 240
        ypos 0
        xpos 0

        $ columns = 4
        $ rows = 2

        frame:
            ypos 0
            background "#0000"
            top_padding 24

            grid columns rows:
                spacing 0
                style_group "MAX"

                for i in range(1, columns * rows + 1):

                    frame:
                        background "#0000"
                        xminimum 300
                        xmaximum 360
                        style_group "file_picker"
                        has vbox

                        frame:
                            background "#0000"
                            xalign 0.0
                            xfill True
                            style_group "file_picker"
                            has hbox
                            spacing 0
                            xalign 0.0
                            textbutton _("Сохр.") action FileSave(i) background "#0000"
                            textbutton _("Загр.") action (SetField(persistent, "mainchange", False), FileLoad(i)) background "#0000"
                            imagemap:
                                ground "image/screens/pust.png"
                                idle "image/screens/CL_M.png"
                                hover "image/screens/CLM_H.png"
                                selected_idle "image/screens/CL_M.png"
                                selected_hover "image/screens/CLM_H.png"
                                alpha False
                                xalign 1.5
                                yalign 0.65

                                hotspot(0, 0, 48, 48) clicked FileDelete(i)
                        add FileScreenshot(i)

                        $ file_name = FileSlotName(i, columns * rows)
                        $ file_time = FileTime(i, empty=_("Empty Slot."))
                        $ save_name = FileSaveName(i)

                        frame:
                            background "#0000"
                            xfill True

                            text "[file_name]. [file_time!t]\n[save_name!t]":
                                size 30
                                font "image/screens/fonts/MenuLight.ttf"
                                xalign 0.22
                                yalign 0.77
        $ page = FileCurrentPage()

        frame:
            xminimum 1920
            background "#0000"
            xpos 0
            bottom_margin 24
            ypadding 0
            hbox:
                spacing 0
                xalign 0.36
                yalign 0.0

                imagemap:
                    ground "image/screens/save/7.png"
                    hover "image/screens/save/7H.png"
                    selected_idle "image/screens/save/0.png"
                    selected_hover "image/screens/save/00.png"
                    alpha False
                    if FileCurrentPage() == "1":
                        hotspot(0, 0, 48, 48) clicked FilePage(5)
                    if FileCurrentPage() == "2":
                        hotspot(0, 0, 48, 48) clicked FilePage(1)
                    if FileCurrentPage() == "3":
                        hotspot(0, 0, 48, 48) clicked FilePage(2)
                    if FileCurrentPage() == "4":
                        hotspot(0, 0, 48, 48) clicked FilePage(3)
                    if FileCurrentPage() == "5":
                        hotspot(0, 0, 48, 48) clicked FilePage(4)


                frame:
                    left_padding 8
                    right_padding 8
                    background #0000
                    text "[page]":
                        size 48

                imagemap:
                    ground "image/screens/save/8.png"
                    hover "image/screens/save/8H.png"
                    selected_idle "image/screens/save/0.png"
                    selected_hover "image/screens/save/00.png"
                    alpha False
                    if FileCurrentPage() == "1":
                        hotspot(0, 0, 48, 48) clicked FilePage(2)
                    if FileCurrentPage() == "2":
                        hotspot(0, 0, 48, 48) clicked FilePage(3)
                    if FileCurrentPage() == "3":
                        hotspot(0, 0, 48, 48) clicked FilePage(4)
                    if FileCurrentPage() == "4":
                        hotspot(0, 0, 48, 48) clicked FilePage(5)
                    if FileCurrentPage() == "5":
                        hotspot(0, 0, 48, 48) clicked FilePage(1)



screen save_screen:

    modal True

    window:
        xpos 0
        ypos 0
        xalign 0.0
        yalign 0.0
        right_padding 0
        left_padding 0
        xfill True
        yfill True
        background "image/screens/SCR.png"
        style_group "tomain"
        label _("Сохранить/Загрузить"):
            style_group "save"


    use navigation2
    use file_picker

init -2 python:
    style.tomain_button.xpos = 40
    style.tomain_button.ypos = -20
    style.tomain_button.background = "#0000"
    style.tomain_button_text.color = "#FFF6"
    style.tomain_button_text.hover_color = "#FFFF"
    style.tomain_button_text.font = "image/screens/fonts/MenuLight.ttf"
    style.tomain_button_text.size = 45
    style.file_picker_frame.background = "#0000"
    style.file_picker_frame.ymaximum = 600
    style.file_picker_button.background = "#0000"
    style.file_picker_button_text.font = "image/screens/fonts/MenuLight.ttf"
    style.file_picker_button_text.size = 45
    style.file_picker_button_text.color = "#FFF6"
    style.file_picker_button_text.hover_color = "#FFFF"
    style.save_label_text.xalign = 0.5
    style.save_label_text.yalign = 0.1
    style.save_label.background = "#0000"
    style.save_label.xfill = True
    style.save_label.top_margin = 40
    style.save_label_text.color = "#FFCE4B"
    style.save_label_text.size = 84
    style.save_label_text.font = "image/screens/fonts/Menu.ttf"


##############################################################################
# Preferences
#
# Экран, позволяющий пользователю изменять настройки.
# http://www.renpy.org/doc/html/screen_special.html#prefereces

screen preferences:

    tag menu
    modal True

    window:
        xpos 0
        ypos 0
        xalign 0.0
        yalign 0.0
        right_padding 0
        left_padding 0
        xfill True
        yfill True
        background "image/screens/SCR.png"
        style_group "tomain"

        label _("Настройки"):
            style_group "MAX"

        frame:
            top_margin 240
            xalign 0.5
            background "#0000"

            hbox:
                spacing 40
                xalign 0.5
                yalign 0.5

                vbox:
                    yalign 0.0
                    frame:
                        xalign 1.0
                        style_group "pref"
                        has hbox:
                            spacing 20
                        label _("Полноэкранный режим")
                        imagemap:
                            ground "image/screens/setting/Y.png"
                            hover "image/screens/setting/YEAH.png"
                            selected_idle "image/screens/setting/YEAH.png"
                            selected_hover "image/screens/setting/YEAH.png"
                            alpha False

                            hotspot(0, 0, 48, 48) clicked Preference("display", "fullscreen")
                        imagemap:
                            ground "image/screens/setting/N.png"
                            hover "image/screens/setting/NO.png"
                            selected_idle "image/screens/setting/NO.png"
                            selected_hover "image/screens/setting/NO.png"
                            alpha False

                            hotspot(0, 0, 48, 48) clicked Preference("display", "window")



                    hbox:
                        xalign 0.5
                        frame:
                            style_group "pref"
                            has vbox:
                                spacing 20
                            vbar value Preference("sound volume")
                            add "image/screens/setting/SO.png" xalign 0.5 yalign 0.5

                        spacing 10
                        frame:
                            style_group "pref"
                            has vbox:
                                spacing 20
                            vbar value Preference ("music volume")
                            add "image/screens/setting/MU.png" xalign 0.5 yalign 0.5
                        frame:
                            style_group "pref"
                            has vbox:
                                spacing 20
                            vbar value Preference("text speed")
                            add "image/screens/setting/TE.png" xalign 0.5 yalign 0.5

    use navigation

init -2 python:
    style.MAX_label_text.xalign = 0.5
    style.MAX_label_text.yalign = 0.5
    style.MAX_label.background = "#0000"
    style.MAX_label.xfill = True
    style.MAX_label.top_margin = 100
    style.MAX_label_text.color = "#FFCE4B"
    style.MAX_label_text.size = 84
    style.MAX_label_text.font = "image/screens/fonts/Menu.ttf"
    style.pref_frame.background = "#0000"
    style.pref_vslider.bottom_margin = 10
    style.pref_vslider.bottom_bar = "image/screens/setting/VBAR_on.png"
    style.pref_vslider.top_bar = "image/screens/setting/VBAR.png"
    style.pref_vslider.thumb = "image/screens/setting/VTHU.png"

    style.pref_button.size_group = "pref"
    style.pref_button.xalign = 1.0
    style.pref_label_text.size = 84
    style.pref_label_text.color = "#ffffff"
    style.pref_label.xalign = 0.5
    style.pref_label.yalign = 0.1
    style.pref_label_text.font = "image/screens/fonts/Menu.ttf"
    style.pref_vslider.xmaximum = 64
    style.pref_vslider.ymaximum = 300
    style.pref_slider.xalign = 1.0

    style.soundtest_button.xalign = 1.0

##############################################################################
# Yes/No Prompt
#
# Экран, спрашивающий у пользователя вопрос да/нет.
# http://www.renpy.org/doc/html/screen_special.html#yesno-prompt

screen yesno_prompt:

    modal True

    window:
        background "image/screens/SCR.png"

    frame:
        style_group "yesno"
        background "#0000"

        xfill True
        xmargin .05
        ypos .1
        yanchor 0
        ypadding .05

        has vbox:
            xalign .5
            yalign .5
            spacing 90

        label _("Вы уверены?"):
            background "#0000"
            xalign 0.5

        hbox:
            xalign 0.5
            yalign 0.6
            spacing 200

            textbutton _("Да") action yes_action hover_background ("image/screens/CHOICED.png")
            textbutton _("Нет") action no_action hover_background ("image/screens/CHOICED.png")

    # Правый щелчок и escape отвечают "нет".
    key "game_menu" action no_action

init -2 python:
    style.yesno_button.size_group = "yesno"
    style.yesno_button.background = "#0000"
    style.yesno_button_text.font = "image/screens/fonts/MenuLight.ttf"
    style.yesno_button_text.size = 70
    style.yesno_button_text.color = "#FFCE4B"
    style.yesno_label_text.text_align = 1
    style.yesno_label_text.size = 90
    style.yesno_label_text.layout = "subtitle"
    style.yesno_label_text.font = "image/screens/fonts/Menu.ttf"


##############################################################################
# Quick Menu
#
# Экран, входящий в экран save и дающий некоторые полезные функции


screen scr_btns:
    imagebutton hover "Image/screens/menu/ddm_up_on_warm.png"idle "Image/screens/menu/ddm_up_off_warm.png"focus_mask True action [Show("scr_list"),Hide("scr_btns")]
    imagebutton hover "Image/screens/menu/warm/load_on_warm.png"idle "Image/screens/menu/warm/load_off_warm.png"xpos config.screen_width-100 xalign 810 yalign 0.05 ypos 10 focus_mask None  action ShowMenu('save_screen')
    imagebutton hover "Image/screens/menu/warm/settings_on_warm.png"idle "Image/screens/menu/warm/settings_off_warm.png"xpos config.screen_width-100 xalign 910 yalign 0.05 ypos 10 focus_mask None action ShowMenu('preferences')
    imagebutton hover "Image/screens/menu/warm/exit_on_warm.png"idle "Image/screens/menu/warm/exit_off_warm.png"xpos config.screen_width-100 xalign 1000 yalign 0.05 ypos 10 focus_mask None action ShowMenu('main_menu')
screen scr_list:
    imagebutton idle "Image/screens/menu/ddm_down_off_warm.png"hover "Image/screens/menu/ddm_down_on_warm.png"focus_mask True  action [Show("scr_btns"), Hide("scr_list")]





screen game_new_prompt:

    modal True

    window:
        background "image/screens/SCR.png"

    frame:
        style_group "game_new"
        background "#0000"

        xfill True
        xmargin .05
        ypos .1
        yanchor 0
        ypadding .05

        has vbox:
            xalign .5
            yalign .5
            spacing 90

        label _(""):
            background "#0000"
            xalign 0.5

        hbox:
            xalign 0.5
            yalign 0.6
            spacing 200

            textbutton _("Начать новую игру") action Start()
            textbutton _("Продолжить") action Return()

init -2 python:
    style.game_new_button.size_group = "game_new"
    style.game_new_button.background = "#0000"
    style.game_new_button_text.font = "image/screens/fonts/MenuLight.ttf"
    style.game_new_button_text.size = 70
    style.game_new_button_text.color = "#FFCE4B"
    style.game_new_button_text.hover_color = "#FFFF"
    style.game_new_label_text.text_align = 1
    style.game_new_label_text.size = 90
    style.game_new_label_text.layout = "subtitle"
    style.game_new_label_text.font = "image/screens/fonts/Menu.ttf"
