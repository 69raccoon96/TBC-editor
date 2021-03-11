init:
    $ five_gape = False

label game_kn:
$ b = 0
screen one_gape_krest:
    frame:
          background Solid("#0000")
          add "kod/games/game_kn/game_kn_krest.png":
             pos (660, 138)
screen two_gape_krest:
    frame:
          background Solid("#0000")
          add "kod/games/game_kn/game_kn_krest.png":
             pos (900, 138)

screen three_gape_krest:
    frame:
          background Solid("#0000")
          add "kod/games/game_kn/game_kn_krest.png":
             pos (1143, 138)
screen four_gape_krest:
    frame:
          background Solid("#0000")
          add "kod/games/game_kn/game_kn_krest.png":
             pos (660, 380)
screen five_gape_krest:
    frame:
          background Solid("#0000")
          add "kod/games/game_kn/game_kn_krest.png":
             pos (900, 380)
screen six_gape_krest:
    frame:
          background Solid("#0000")
          add "kod/games/game_kn/game_kn_krest.png":
             pos (1143, 380)
screen seven_gape_krest:
    frame:
          background Solid("#0000")
          add "kod/games/game_kn/game_kn_krest.png":
             pos (660, 620)
screen eight_gape_krest:
    frame:
          background Solid("#0000")
          add "kod/games/game_kn/game_kn_krest.png":
             pos (900, 620)
screen nine_gape_krest:
    frame:
          background Solid("#0000")
          add "kod/games/game_kn/game_kn_krest.png":
             pos (1143, 620)
$ one_gape = False
$ two_gape = False
$ three_gape = False
$ four_gape = False
$ six_gape = False
$ seven_gape = False
$ eight_gape = False
$ nine_gape = False

scene black
"hello"
call screen game_kr_nol
screen game_kr_nol:
    add "kod/games/game_kn/bg_game_kn.png"
    frame:
        yalign 0.2
        imagemap:
             ground "kod/games/game_kn/bg_game_kn.png"
             hover "kod/games/game_kn/bg_game_kn_hover.png"
             if one_gape == False:
                  hotspot (687, 159, 228, 238)focus_mask True action Jump("kn_one")
             if two_gape == False:
                  hotspot (927, 159, 230, 240)focus_mask True action Jump("kn_two")
             if three_gape == False:
                  hotspot (1170, 159, 227, 240)focus_mask True action Jump("kn_three")
             if four_gape == False:
                  hotspot (688, 410, 225, 224)focus_mask True action Jump("kn_four")
             if six_gape == False:
                  hotspot (1170, 410, 227, 221)focus_mask True action Jump("kn_six")
             if seven_gape == False:
                  hotspot (688, 646, 225, 225)focus_mask True action Jump("kn_seven")
             if eight_gape == False:
                  hotspot (930, 647, 227, 220)focus_mask True action Jump("kn_eight")
             if nine_gape == False:
                  hotspot (1173, 646, 225, 218)focus_mask True action Jump("kn_nine")
             if five_gape == False:
                  hotspot (928, 412, 229, 220)focus_mask True action Jump("kn_nine")
label kn_one:
$ one_gape = True
show screen game_kr_nol
show screen one_gape_krest
jump game_kn_continue
label kn_two:
$ two_gape = True
show screen game_kr_nol
show screen two_gape_krest
jump game_kn_continue
label kn_three:
$ three_gape = True
show screen game_kr_nol
show screen three_gape_krest
jump game_kn_continue
label kn_four:
$ four_gape = True
show screen game_kr_nol
show screen four_gape_krest
jump game_kn_continue
label kn_five:
$ five_gape = True
show screen game_kr_nol
show screen five_gape_krest
jump game_kn_continue
label kn_six: 
$ six_gape = True
show screen game_kr_nol
show screen six_gape_krest
jump game_kn_continue
label kn_seven:
$ seven_gape = True
show screen game_kr_nol
show screen seven_gape_krest
jump game_kn_continue
label kn_eight:
$ eight_gape = True
show screen game_kr_nol
show screen eight_gape_krest
jump game_kn_continue
label kn_nine:
$ nine_gape = True
show screen game_kr_nol
show screen nine_gape_krest
jump game_kn_continue



label game_kn_continue:
$ random.seed([], version=2)
if b<10:
    $ komp_xod = random.randint(1,9)
    if one_gape == True and komp_xod == 1:
        $ komp_xod = random.randint(1,9)
    elif two_gape == True and komp_xod == 2:
        $ komp_xod = random.randint(1,9)
    elif three_gape == True and komp_xod == 2:
        $ komp_xod = random.randint(1,9)
    elif four_gape == True and komp_xod == 2:
        $ komp_xod = random.randint(1,9)
    elif five_gape == True and komp_xod == 2:
        $ komp_xod = random.randint(1,9)
    elif six_gape == True and komp_xod == 2:
        $ komp_xod = random.randint(1,9)
    elif seven_gape == True and komp_xod == 2:
        $ komp_xod = random.randint(1,9)
    elif eight_gape == True and komp_xod == 2:
        $ komp_xod = random.randint(1,9)
    elif nine_gape == True and komp_xod == 2:
        $ komp_xod = random.randint(1,9)
    $ b +=1
    jump game_kn_continue

