init:
    $ renpy.music.register_channel("nature", "voice", True)
screen inventory:
    frame:
            background Solid("#0000")
            imagebutton auto "image/music_list/bag_%s.png" action [Show("music_list"), Hide("inventory")] 
            xalign 1.0
screen music_list:
    frame:
            background Solid("#0000")
            imagebutton auto "image/music_list/bag_%s.png" action [Show("inventory"), Hide("music_list") ] 
            xalign 0.77
    frame:
        xalign 1.0
        background "image/music_list/bg_music.png"
        xmaximum 401
        ymaximum 600
    frame:
        xalign 0.95
        yalign 0.55
        style_group "music_list_bar"
        bar value Preference ("voice volume")
    frame:
        background Solid("#0000")
        xalign 0.915
        yalign 0.08
        vbox:
             style_group "music_list"
             textbutton _("No Tresspassing") action (Stop(channel='music', fadeout=None),[Play("nature", "sound/music/no_tresspassing.ogg")] )
             textbutton _("You lose me") action (Stop(channel='music', fadeout=None),[Play("nature", "sound/music/you_lost_me.ogg")] )
init -2 python:
    style.music_list_button.xpadding = 5
    style.music_list_button.background = "#0000"
    style.music_list_button_text.set_parent('default')
    style.music_list_button_text.size = 34
    style.music_list_button_text.idle_color = "#000000"
    style.music_list_button_text.hover_color = "#ccc"
    style.music_list_button_text.selected_idle_color = "#ccc"
    style.music_list_button_text.selected_hover_color = "#ccc"
    style.music_list_button_text.insensitive_color = "#000000"


    style.music_list_bar_frame.background = "#0000"
    style.music_list_bar_slider.bottom_margin = 10
    style.music_list_bar_slider.bottom_bar = "kod/games/music_bar_on.png"
    style.music_list_bar_slider.top_bar = "kod/games/music_bar.png"
    style.music_list_bar_slider.thumb = "kod/games/music_bar_VTHU.png"
    style.music_list_bar_button.xalign = 1.0
    style.music_list_bar_slider.xmaximum = 314
    style.music_list_bar_slider.ymaximum = 67
    style.music_list_bar_slider.xalign = 1.0