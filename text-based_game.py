import time
from tkinter import *
#Defining skill variables
strength = int()
charisma = int()
intelligence = int()
luck = int()

skillpoints = int(20)

#Defining other variables
gold = int()
xp = float()
temp = float()
choice = str("")
name = str("")
weapon = 0
area = str("")
level = int()
killedC2 = int(0)
C3chest = 0
C4trap = 0
C5killed = 0
C7killed = 0
F2riddle = 0
choice = 0

rustysword = 0
diadem = 0
foot = 0


#Defining inventory slots
inventory1 = str("")
inventory2 = str("")
inventory3 = str("")
inventory4 = str("")
inventory5 = str("")

#defining visited variables
visA1 = int(0) #starting area
visA2 = int(0) #north of starting area (road with horse)
visA3 = int(0) #east of starting area (stream)
visA4 = int(0) #south of starting area (cave)
visA5 = int(0) #west of starting area (mystery...)
visE1 = int(0)
visC1 = int(0)
visC2 = int(0)
visC3 = int(0)
visC4 = int(0)
visC5 = int(0)
visC6 = int(0)
visC7 = int(0)
visC8 = int(0)
visF1 = int(0)
visF2 = int(0)

E1a = str("???")
C2a = str("???")
C3a = str("???")
C4a = str("???")
C5a = str("???")
C6a = str("???")
C7a = str("???")
C8a = str("???")
#Defining skill menu function

def buttonsmenu():
    global choice
    def button1():
        global choice
        choice = "1"
        root.destroy()
        root.quit()
    def button2():
        global choice
        choice = "2"
        root.destroy()
        root.quit()
    def button3():
        global choice
        choice = "3"
        root.destroy()
        root.quit()
    def button4():
        global choice
        choice = "4"
        root.destroy()
        root.quit()
    def button5():
        global choice
        choice = "5"
        root.destroy()
        root.quit()
    def button6():
        map()

    #the variables for changing the choices of each button
    c1 = str("1")
    c2 = str("2")
    c3 = str("3")
    c4 = str("4")
    c5 = str("5")
    c6 = str("6")

    root = Tk()
    root.title("Controller")
    root.geometry("100x26")
    root.update()
    root.deiconify()
    root.update()
    app = Frame(root)
    app.pack({"side":"left"})
    bttn1 = Button(app, command=button1)
    bttn1["text"] = c1
    bttn2 = Button(app, command=button2)
    bttn2["text"] = c2
    bttn3 = Button(app, command=button3)
    bttn3["text"] = c3
    bttn4 = Button(app, command=button4)
    bttn4["text"] = c4
    bttn5 = Button(app, command=button5)
    bttn5["text"] = c5
    bttn6 = Button(app, command=button6)
    bttn6["text"] = "map"
    bttn1.pack({"side":"right"})
    bttn2.pack({"side":"right"})
    bttn3.pack({"side":"right"})
    bttn4.pack({"side":"right"})
    bttn5.pack({"side":"right"})
    bttn6.pack({"side":"right"})
    root.mainloop()

def skillslide():
    global skillpoints,skill,choice
    def confirm(): #necissary to have this defined in here, stupid but it works
        global strength,intelligence,charisma,luck,skillpoints,skill
        if(skill == "strength"):
            strength = strength + w.get()
            skillpoints = skillpoints- w.get()
            skillslider.destroy()
            skill = str("null")
            print("Strength now: ",strength," skill points remaining: ",skillpoints,".")
            if(skillpoints>0):
                skillmenu()
                skill = str("null")
        elif(skill == "intelligence"):
            intelligence = intelligence + w.get()
            skillpoints = skillpoints- w.get()
            skillslider.destroy()
            skill = str("null")
            print("Intelligence now: ",intelligence," skill points remaining: ",skillpoints,".")
            if(skillpoints>0):
                skillmenu()
                skill = str("null")
        elif(skill == "charisma"):
            charisma = charisma + w.get()
            skillpoints = skillpoints - w.get()
            skillslider.destroy()
            skill = str("null")
            print("Charisma now: ",charisma," skill points remaining: ",skillpoints,".")
            if(skillpoints>0):
                skillmenu()
                skill = str("null")
        elif(skill == "luck"):
            luck = luck + w.get()
            skillpoints = skillpoints - w.get()
            skillslider.destroy()
            skill = str("null")
            print("Luck now: ",luck," skill points remaining: ",skillpoints,".")
            if(skillpoints>0):
                skillmenu()
                skill = str("null")
        elif(skill == "null"):
            skillslider.destroy()
            skillslider.quit()
            skillslider.exit()
    skillslider = Tk()
    skillslider.title("Slider")
    skillslider.geometry("200x75")
    skillslider.deiconify()
    w = Scale(skillslider, from_=0, to=skillpoints, orient=HORIZONTAL)
    x = Button(skillslider,command=confirm)
    w.pack()
    x["text"] = "confirm"
    x.pack({"side":"bottom"})
    skillslider.update()
    skillslider.deiconify()
    skillslider.update()
    skillslider.mainloop()
    skillslider.quit()

def skillmenu():
    global area, skillpoints, strength, charisma,intelligence,luck,choice,skill
    clear(100)
    print("Skills affect how good or bad your character is at certain things. Skills available:")
    clear(2)
    print("strength <1>, charisma <2>, intelligence <3> and luck <4>")
    clear(8)
    if(skillpoints>0):
        print("Which skill do you want to change?")
        while(choice == 0):
            buttonsmenu()
            if(choice == "1"):
                print("""
                                                                                                                                   ``
                                                                                                                                 `odmo`
                                                                                                                               `oms..sdo`
                                                 `ydyyyyyyyyyyho                                  .-:+shhyyyyyyyyhy/.        `ods.    .sd+`
                                                `hd...........omo.      `-/oyyyyyyyyyyyyyyyh+/osyyyso/-.``````````:ohh+-`  `ods.        .sd+`
                                               .dh`     ``     .odo.:+syys+:.``````````````-yNh-.``                 `.+yhsoms.   /yo.     .mh
                                              -ms`   -+hmmhs+:-.`/Ndy+-.`                    -+`                        .:sdy+-:dMMMNs.    hd
                                             :mo    sNMMMMMMMMNmhy+.                                                       `-oymMMMMMMmo.  hd
                                            /N+     hMMMMMMMMMdo-`                                                             .omMMMMMMm/ hd
                                            sm+`    hMMMMMMms:`                                                                  .omMMMMM: hd
                                             -yd+`  hMMMNy/`                                                                       .omMMM- hd
                                               -yh/`dNd+.                             .-/++/:::/+/--`                                .sNM: hd
                                                 -ymN:                       ``      +mMMMMm:..yMMMMd+`     ``                         .sdodd
                                                  +N:                       `ymh+.` :MMMMMMMs  NMMMMMMd-`./ymd:`                         .sNd.
                                                 :N+                       .dMMMMNoshMMMMMMM+  mMMMMMMMy/+mMMMMh:`                         .ym.
                                                -No                       .mMMMMmds..mMMNNmo   -smNNMMm-  .dMMMMMh:                         `my
                                               .ms                        .dMMdyy:   `+do-`      `-od+`    `hMMMMN+                          +M.
                                              `dh                          `/:-d`      `+s////////s+`        yMNs.                            my
                                              -s`   .o`                       /s         `........`          .m-                       ``     /M-
                                                    /M.                       o+                              s+                       dy      dh
                                                    /M.                       y:                              `m`                      my      :M:
                                                    /M.                       y:         `.-/++//:-.``         y+                      my       dd
                                                    /M.                       +o   .+ooo+yo:-```.-:/++++o+`    d.                      my       -M:
                                                    /M.                       -h  -h:`   osMMsdmNmNN: ./+oso` `m                       my        hy
                                                    /M.                        N  /-NMm/   `/:ssyhod-:MsyN`.s--h                       my
                                                    /M.                        d-  :MMM:              mh/M-   +o                       my
                                                    /M.                        s+   dMM`              -Mmd    h-                       my
                                                    /M.                        .d   :Ny                oh:   :h                        my
                                                    /M.                         h-  d`                  -/   d-                        my          .o.
                                                    /M.                         :y  N       .`          :y  :y                         my          ym`
                                                    /M.                          m` m`    oo/y:         :y  d.                         my         -M/
                                                    /M.                          oo o+    h: `y+        .: /s                          my         hm
                                -s`                 /M.                          `d..d    /s./`oo      ./``d.                        -yd:        -M/
                                `yd.                :No`                          /y d.   `m`o: +o     :/ +s                       -yd+`         hd
                                 `sm-                -yd+`                         h:./-:  -     .  ` `/-.d`                     -yd+`          :M:
                                   om/                 -yd/`                       -d`/:h-         `y.-:`s/                    -yd+`            dh
                                    /m+                  -yd/`                      h-:+:h         y/ :..d                   -yd+`             /M-
                                     :mo                   -yh/`                    m`-/ h:       oo  :-y:                 .sd+`               dh
                                      -my`                   :yh/`                 -h `- -h      /s   -.h:               .sd+`                /M-
                                       .dh`                    :hh/`               o+ oNh:+`.::: :` `oNh/s             .sdo.                 .my
                                        `hd.                     :hh/`             h- :MMNo .---   .dMM:.d           .sdo.               `-+yh+.
                                         `sm-                      :hh:`           :y. smy/s///::oysyms y/         .sdo.              .:syy+-`
                                           om:                       :hh:`          .y- `  .`----::- ``/y        .odo.            `./yhs/.
                                            sN/``                      :hh:`         .y:              .d`      .odo.           `-oyho-`
                                            :shyyso/-.``                 /hh:`        `s++++++++++++++s:     .ods.          ./shy/.
                                                `-:+syhyyo+:.``            /dh:                            `ods.          .yho:`
                                                       `.:/oyhhys-           /dysssssssssssssssssssssssssssds.             .
                                                               .-`             ----------------------------.
                """)
                print("Strength is the measure of physical ability and brute force. It affects how much you are able to carry. You have ",skillpoints," skill points available. How many do you wish to apply to your strength skill?")
                skill = "strength"
                skillslide()
                if(skillpoints>0):
                    choice = 0
            if(choice =="2"):
                print("""

                                                            ``
                                                         `+hyssyysyyssssssooo+++///::---..``
                                                     ``-oh+`      `````````..---:::///+ooosssssyysssy/
                                         `.-:/+osssssyNm/`                                      ````.oh/
                                        oho+/:-..```/do`                                              .sh/`
                                      -hs`        :hs.                                                  .sh/`
                                     +d:        -yy-                                                      .sh/`
                                   .hs`       .sh:                                                          .oh/`
                                  +d/        +h+`                 .                        `/`                .oh/`
                                -yy.        :m.                  `m-                       `ho                  .oh/`
                              .sy/         .m/                   .M.                        .m/                   .sy/`
                            `oh/`         `hs                    /N                          :m-                    .sy/`
                          `/ho`           sh`                    od                           +d`                     .sh/`
                         -yy.            /m.                     hs                            yy                       .sh/`
                       .sh:    .h       .m:                     .N-                            `d+                        .oy/`
                      :m+`     :N       sd       `              od                              -m:                         .sy/
                      -M`      /N       -N.     shhh/`         `m/           `:+++++/:.          /m`                          +m`
                      `M-      /N        do    .NMMMMh         /N`          -mMMMMMMMMN.         .M.                          d+
                       m+      /N        +m     ./sso:         hs           yMMMMMMMMMd.         .M`                         /m`
                       hs      /m        sh                   .N.           .shhdddyo:`          :N                         `m+
                       sh      .d+      `m+                   `:                                 /N                         +m`
                       -N-      .do      sh                                                      +d                       .sh:
                        +d`      `hy`    `hs                                                     od                     -sh:
                         hs        yh`    `m+                                                    sy                   -yh:
                         .m+        :`     :N.                                                   hs                 :hy-
                           od-             yy                                                    ho                +N-
                            -ds`          .N.                                                    m+               /m.
                              +m:         yy                                                     No              +m.
                               .yy.      -N.                                                     .odo.          od`
                                 /doossyys-+`        :/oyhhhhhyys+-                                `/yy:   .:+sdm`
                                  `-.```   do       ym+/.``````.-+my                                  .omhys+:.-yy-
                                           :N.     /M+:`    `.`   yN                                   sd.       -yy-
                                            yy     +MNMm`  -mNNh  yN                                 `yy`          -yy-
                                            .N-    `mMNM/  .NMd+ .mh                                .do              :yy-
                                             od     -hmm-   :hhhhhs`              .s`              :d/                `:ys-
                                             `m/      ``     `````                yy              /d:                   `:d+
                                              /m`                                :N.            `oh.                      :N.
                                               hs                               `do          ./sy+`                        sh
                                               -N.                           `-+yh`      `-+ys/.`                          `m+
                                                sd+/::--..```             `:oyo:.     `:oyo:.                               :N.
                                                `yMo//++oosssssooo++//:-:syo-`     ./sso-`                                   sh
                                                  om:        ``...--:://+-`        :+-`                                      `m+
                                                   +m/                                                                        :m`
                                                    :m+                                                                        N/
                                                     dh                                                                        sy
                                                    /N-                                                                        :N`
                                                    my                                                                         `N:
                                                   /N.                                                                          ys
                                                  `ms                                                                           /m
                                                  +M.                                                                           `M-
                                                  /M.                                                                            ho
                                                   dy                                                                            +m
                                                   :M-                                                                           .M.
                                                    dh                                                                            d+
                                                    :M:                                                                           ..
                """)
                print("Charisma is the measure of your social prowess. It affects how likely you are to be able to persuade people and reduces shop prices. You have ", skillpoints, " skill points available. How many do you wish to apply to your charisma skill?")
                skill = "charisma"
                skillslide()
                if(skillpoints>0):
                    choice = 0
            if(choice == "3"):
                print("""
                                                                                        `:+yyyhyyyyyysoos/`
                                                                                     oyys+:.`````````....+yy/`
                                                                                    yh-//+oss+.    `..:.   .+yy/`
                                                                                   +m`./:--../hsyyysso+syyo/.`.hy
                                                                                  :N-         ````      ``-/od/`hy`
                                                                                 .m/                         -m:`yy`
                                                                                `do                           :m-`hy
                                                                                hy      +hy.        -::.       /+ sh
                                                                               sd:.     mMM/       +NMMm`        `N:
                                                                              /m.od     .sd/       .yhh+         om
                                                                             -m: `N/      .N-     `             `m+
                                                                            .m+   +m`      ds   `ss           ` /N`
                                                                           `ds    `m+      /N` `yy`          :h-do
                                                                           yh`     +m`     `N/.hs`         .sh-:N.
                                                                          od`      `mo      sddo          /d+` hy
                                                                         /m-        /N-.`   .s:        `.yy.  .M-
                                                                        -m/          +osyso/-...-//+ossyy+    sh
                                                                       .do        `.`    `-/oyso+/:-.``      `N:
                                                                     `+d/      .+yddo                        om
                                                                    -hs`    `:sNd+-`                         N+
                                                                  `sd-    `+dNs:    :syyo`                  `N+
                                                                 /d+   `/ymm+`     +MMMMMh                   om
                                                               .hy.  `ommo-       :NMMMMm/                   /N.
                                                              .N/   :mN+`         mMMMMM`                   /N-
                                                              hy    oo`          .MMMMMd                    :N.
                                                             /N`                -dMMMMMo                     ds
                                                            `N/ /mMNh-         /MMMMMMm`      yo            `ds
                                                            hy  NMMMMM+       `NMMMMMs`     `hy            .do
                                                           +m`  :NMMMMM/      sMMMMMy      `ds            .m+
                                                          .N:    -MMMMMN      NMMMMN.     .do            .m+
                                                          ds      mMMMMM`     /mMNh-     .m+            -m/
                                                         +m`      oMMMMy       ```      -m/            :m:
                                                        .N:        -++-    ./+/`       :m:            :m:
                                                       .do            `---yNMMMm.      :-          `:sd-
                                                      -m/            :mNNNMMMMMN.  .            `:syo-`
                                                     /m:             dMMMMMMMMh. -ys`        `:syo-`
                                                    +d-              NMMMMMMMh`-ys-       `:oyo-`
                                                   sh.               oMMMMMMM+ys-       :oyo-`
                                                 `yh`                 /hmNmNNy-       `sh-`
                                                .hs`                    ./hy:        `yy`
                                              `.do                    `:yy:         :hs`
                                           `:syh+                   `/yo-         :hs:
                                         .+ys-``                  .oho.           /N.
                                      `:sy/`                    -sy+`              yh
                                    .oyo-                    `-yy:`  `-/syo        `do
                                    hy`                    `/yy-`.:+syo/.-N:        .N:
                                   -N.                   `+hs. `ys+:`     +m`        +m.
                                   hs                  .oh+``s+            yh         yh
                                  -N.              ``-sh/` `yh`            `m+        `mo
                                  -m.        ``-/ossyh:   .ds               :N.        -N+:-..````
                                  ms   ``-/oyys+:.` :o++++ms                /N:`````````-/+oydmmddo
                                  yh/oyyyo/.        `.---::`                ossssssyyssssssyy+/:-.
                                  `//.`

                """)
                print("Intelligence is the measure of your mental skill. The number of skill points gained per level. You have ",skillpoints, " skill points available. How many do you wish to apply to your intelligence skill?")
                skill = "intelligence"
                skillslide()
                if(skillpoints>0):
                    choice = 0
            if(choice =="4"):
                print("""


                                                     -/////-          .sy+`
                                                    -m+:::+N.       .sd:`od-
                                                   :m:     hy     .sd/`   do
                                                  +m-      -N.  .sd+`    .M-
                                                 +m.       :N..oNs`      om
                                                 yh        dyoh+M/       do
                                                 yh       .Nd+`         -M-
                                                 yh      :d+`           od
                                                 sh     .m/             mo
                                                 ds    .do             -M.
                                                :N.   `hs              sd
                                                ds   `yh`             +d-
                                               /N`   -y`            `sh.
                                              `do                  .hs`
                                             .om`                 :d+
                                         `-+ss+.                 +d:
                                      `:oys/.                 `.oh.
                                   ./syo-`                     `m:
                                  -mo.                          mo
                                 :m:          .:/.              sh
                                +m-          oMMMd              /N`                `````````````````
                               od.           dNNN+              `hs:`       ``.:/oyyyyyyyyyyyyyyyyyyo.`
                              od`            `..`                 -+hy+-/+syyyo+:.`                `/sho:`
                          :s/sd.                                     `/o/-.                            -oyy/.
                           -mh`      -+y.                                                                 `/yho-
                           hNsydm-   +:`                         :h`                                          -ohy:
                           hMMMy-  .:+sy/                       +m-                                              .sd/`
                           /M/-`   //-.                        sd.                                                 `odo`
                         `yydyoh.   +: +ho-                  `yh`                                                    `/hs.
                            -dms/.  `sh/`:oy`              :ohs`                                                        :hy-
                              `-/syyo:-sh:             ./yyo-`                                                            -yh/
                                  ``-+yhhNd/:.`     -oyy/.`                                                                 .sd-
                                      sh``-soosysssyo:`                                                                       :m:
                                      hy       ``..`                                                                           :m/
                                      mo                                                                                        -d+
                                      :N-                                                                                        .do
                                       +m.                                                                                        .ds
                                        sd`                                                                                        -M.
                                        `yy                                                                                         ds
                                         `do                                                                                        +N`
                                          .m+                                                                                       `N:
                                           -m:                                                                                       yh
                                            /h/.                                                                                     :M.
                                             .+ys:`                                                                                   N+
                                                -oyo-`                                                                               `M:
                                                  `:syo-`                                                                            `M-
                                                     `:yys/                                                                          -M`
                                                        :N:             `:sooo+.              ``.-:+                                 :M`
                                                      ``ds            `+h+..-.+hs:`      `/+osyyso/:`                               .hd
                                                .-/+osyyy.          `/h+`       -sy+.    yh:.`  `                                 `/d/
                                               -mo/-.`            `/ho`           `/hs:`-N.    :h` .+o                           -hy.
                                              :m:               `/ho`                -syds     /- `y/`                         `od:
                                             +m-               /ho`                    :N/:::::////////////+++++++++++++ossssssdo`
                                             :yyyhyyyyyyyyhyyyyo`                       :///////:::::::::::::-------------.....`

                """)
                print("Luck is the measure of how generally likely you are to succeed in your endeavors. How likely you are to find treasure. You have: ",skillpoints," skill points available. How many do you wish to apply to your luck skill?")
                skill = "luck"
                skillslide()
                if(skillpoints>0):
                    choice = 0
            else:
                choice = 0
                skillmenu()
    else:
        A1()

def levelup(amount):
    global area, level,skillpoints, skillpointstemp,choice
    level = level + amount
    skillpointstemp = skillpoints
    print("LEVEL UP! Level now: ", level)
    skillpoints = amount*15
    input("Press enter/return to continue to skill shop")
    skillmenu()

def clear(amount):
	print("\n "*amount)

def shop():
    global area, gold,inventory1,inventory2,inventory3,inventory4,inventory5,strength,intelligence,luck,weapon,rustysword,diadem,foot,choice
    print("Are you wanting to buy <1> or sell <2> today? (<3> to exit)")
    if(choice == "2"): #sell
        clear(4)
        print("Items: ",inventory1,"<1>, ",inventory2,"<2>, ",inventory3,"<3>, ",inventory4,"<4>, ",inventory5,"<5>")
        print("Which do you wish to sell?")
        if(choice == inventory1 or choice == inventory2 or choice == inventory3 or choice == inventory4 or choice == inventory5):
            if(choice == "1"):
                print("Bear hide is worth 250 gold (+",charisma*5," (5 extra gold per charisma level).")
                print("Are you sure you want to sell your bear hide for 250 gold? yes<1>/no<2>")
                if(choice == "1"):
                    gold = gold+250+charisma*5
                    print("Gold: ",gold)
                    time.sleep(1)
                    clear(100)
                    shop()
                    inventory1 = ("")
                if(choice == "2"):
                    shop()
            if(choice == "2"):
                print("Rusty sword worth 175 gold.")
                print("Are you sure you want to sell your rusty sword for 175 gold? <y>es/<n>o :")
                choice = input(": ")
                if(choice == "y"):
                    gold = gold+175
                    print("Gold: ",gold)
                    time.sleep(1)
                    clear(100)
                    weapon = 0
                    inventory2 = ""
                    shop()
                if(choice == "n"):
                    shop()
            if(choice == "3"):
                print("Lost Diadem worth 325 gold.")
                print("Are you sure you want to sell your Lost Diadem for 325 gold? <y>es/<n>o")
                choice = input(": ")
                if(choice == "y"):
                    gold = gold+325
                    print("Gold: ",gold)
                    time.sleep(1)
                    clear(100)
                    inventory3 = ""
                    shop()
                if(choice == "n"):
                    shop()
            if(choice == "4"):
                print("Rabbit's foot worth 75 gold")
                print("Are you sure you want to sell your lucky rabbit's foot for 75 gold? <y>es/<n>o")
                choice = input(": ")
                if(choice == "y"):
                    gold = gold+75
                    print("Gold: ",gold)
                    time.sleep(1)
                    clear(100)
                    inventory4 = ""
                    shop()
                if(choice == "n"):
                    shop()
            if(choice == "2"):
                print("Sharp sword worth 375")
                print("Are you sure you want to sell your sharp sword for 375 gold? <y>es/<n>o")
                choice = input(": ")
                if(choice == "y"):
                    gold = gold+375
                    print("Gold: ", gold)
                    time.sleep(1)
                    weapon = 0
                    inventory2 = ""
                    shop()
                else:
                    shop()
            if(choice == "2"):
                print("Sword worth 275")
                print("Are you sure you want to sell your sword for 275 gold? <y>es/<n>o")
                choice = input(": ")
                if(choice == "y"):
                    gold = gold+275
                    print("Gold: ", gold)
                    time.sleep(1)
                    weapon = 0
                    inventory2 = ""
                    shop()
                else:
                    shop()

            if(choice == "2"):
                print("Legendary sword worth 475")
                print("Are you sure you want to sell your legendary sword for 475 gold? <y>es/<n>o")
                choice = input(": ")
                if(choice == "y"):
                    gold = gold+275
                    print("Gold: ", gold)
                    time.sleep(1)
                    weapon = 0
                    inventory2 = ""
                    shop()
                else:
                    shop()

        else:
            print("That wasn't one of the options.")
            shop()
    elif(choice == "1"): #buy
        clear(4)
        print("Gold: ",gold)
        print("Items for sale: ")
        clear(1)
        if(rustysword == 0):
            print("Rusty sword <1> = 200 gold")
            clear(1)
        if(diadem == 0):
            print("Lost diadem <2> (+25 intelligence)= 350 gold")
            clear(1)
        if(foot == 0):
            print("Lucky rabbit's foot <3> (+10 luck) = 100 gold")
            clear(1)
        print("What do you wish to buy? (press enter to exit)")
        if(choice == "1" and gold>=200 and rustysword == 0):
            if(inventory2 != ""):
                print("Do you want to replace:",inventory2," with rusty sword?y<1>/n<2>")
                if(choice == "1"):
                    gold = gold-200
                    rustysword = 1
                    inventory2 = "rusty sword"
                    print("Rusty sword aquired, gold now: ",gold)
                    time.sleep(2)
                    weapon = 1
            else:
                gold = gold-200
                rustysword = 1
                inventory2 = "rusty sword"
                print("Rusty sword aquired, gold now: ",gold)
                time.sleep(2)
                weapon = 1
            clear(100)
            shop()
        if(choice == "2" and gold>=350 and diadem == 0):
            gold = gold-350
            intelligence = intelligence+25
            diadem = 1
            inventory3 = "lost diadem"
            print("Lost diadem aquired, gold now: ",gold,"  intelligence now: ",intelligence)
            time.sleep(2)
            shop()
        if(choice == "rabbit's foot" and gold>=100 and foot == 0):
            gold = gold-100
            luck = luck+10
            inventory4 = "3"
            foot = 1
            print("Lucky rabbit's foot aquired, gold now: ",gold,"  luck now: ",luck)
            time.sleep(2)
            shop()
    if(choice == "3"):
        clear(100)
    else:
        clear(100)
        shop()

def sword(a,b):
    global area, inventory2, weapon,choice
    if(inventory2 != ""):
        print("Do you want to replace",inventory2,"with",a,". yes<1>/no<2>")
        if(choice == "1"):
            print(a, "added!")
            weapon = b
            inventory2 = str(a)
    else:
        print(a," added!")
        input("Press enter/return to continue.")
        weapon = b
        inventory2 = str(a)

def alchemist():
    clear(100)
    global area, strength,intelligence,luck,charisma,gold,choice
    print("\"Welcome, Welcome\", the old shop owner calls out to you in a croaky voice, \"What can I do for you today, then?\"")
    print("buy<1> or exit<2>")
    if(choice == "1"):
        print("For sale: ")
        clear(2)
        print("Draught of the Bear (+15 strength) = 50 gold bear<1>")
        clear(1)
        print("Draught of the Owl (+15 intelligence) = 50 gold owl<2>")
        clear(1)
        print("Draught of the Sun (+20 charisma) = 50 gold sun<3>")
        clear(1)
        print("Draught of the Rabbit (+10 luck) = 50 gold rabbit<4>")
        clear(2)
        if(choice == "1"):
            if(gold>=50):
                print("Are you sure you want to buy A Draught of the Bear for 50 gold? Current Gold: " ,gold, " y<1>/n<2>")
                if(choice == "1"):
                    gold = gold-50
                    strength = strength +15
                    print("Gold now: ",gold," strength now: ",strength)
                    time.sleep(1)
                    alchemist()
            else:
                print("Not enough gold")
                time.sleep(1)
                alchmist()
        elif(choice == "2"):
            if(gold>=50):
                print("Are you sure you want to buy A Draught of the Owl for 50 gold? Current Gold: ",gold, " y<1>/n<2>")
                if(choice == "1"):
                    gold = gold-50
                    intelligence = intelligence+15
                    print("Gold now: ", gold, " intelligence now: ", intelligence)
                    time.sleep(1)
                    alchemist()
            else:
                print("Not enough gold")
                time.sleep(1)
                alechemist()
        elif(choice == "3"):
            if(gold>=50):
                print("Are you sure you want to buy A Draught of the Sun for 50 gold? Current Gold: ",gold," y<1>/n<2>")
                if(choice == "1"):
                    gold = gold-50
                    charisma = charisma + 20
                    print("Gold now: ",gold," charisma now: ", charisma)
                    time.sleep(1)
                    alchemist()
            else:
                print("Not enough gold")
                time.sleep(1)
                alchemist()
        elif(choice == "4"):
            if(gold>=50):
                print("Are you sure you want to by A Draught of the Rabbit for 50 gold? Current Gold; ",gold," y<1>/n<2>")
                if(choice == "1"):
                    gold = gold - 50
                    luck = luck +10
                    print("Gold now: ",gold," luck now: ",luck)
                    time.sleep(1)
                    alchemist()
            else:
                print("Not enough gold.")
                time.sleep(1)
                alchemist()
        else:
            print(choice, " was not for sale.")
            time.sleep(1)
            alchemist()

def map():
    global area,visE1,visC2,visC3,visC4,visC5,visC6,visC7,visC8,E1a,C2a,C3a,C4a,C5a,C6a,C7a,C8a
    if(visE1 == 1):
    	E1a = "bandits"
    if(visC2 == 1):
    	C2a = "bandits"
    if(visC3 == 1):
    	C3a = "chest"
    if(visC4 == 1):
    	C4a = "trap"
    if(visC5 == 1):
    	C5a = "dorm"
    if(visC6 == 1):
    	C6a = "door"
    if(visC7 == 1):
    	C7a = "fire"
    if(visC8 == 1):
    	C8a = "door"
    print("""                                                             -----------
                               ---------                    |   TOWN    |
                              | """,E1a,""" |--|       -----------|-----
                               ---------   |----|   NORTH   |-----------|
                                                 ------|----      -        -------------
                                                       |                  |   UPSTREAM  |
                                       --------    ---|----       ------  ----|------
                                      |  WEST  |--| START  |-----| EAST  |----|
                                       --------    ---|----       -------     |
                                                        |                     |
                                                    ----|-----           -----|--------------
                                                   |  SOUTH   |         |      DOWNSTREAM    |
                                                    -----|----           --------------------
                  -------            --------        ----|--
                 |""",C4a,"""|-------------| """,C2a,"""|------| CAVE  |
                  ---|-              ----|---        -------
                     |                   |                -
	              ---|-              -----------------|
                 |""",C5a,"""|                         | """,C3a,""" |
                  --|--                          --|---
                    |                              |
               -----|-                             |
               |""",C6a,"""|                              |
                --|-                               |
             	--|-        ------              ---|-
               |???|--------|""",C8a,"""|-------------|""",C7a,"""|
                ---          ----               -----
		""")
    input("Press enter/return to continue ")

def A1():
    clear(100)
    global area, visA1,intelligence,choice
    choice = 0
    print("""
				......................................../ss-................................../N-...........................................:M-......................
		..`..`..`..`..`..`..`..`..`..`..`..`..`.:MNN/..`..`..`..`..`..`..`..`..`..`..`.sm-.`..`..`..`..`..`..`..`..`..`..`..`..`..`..:N/`..`..`..`..`..os-:++-
		.........................................-hNdd-..............................-hh...................--........................./mo..............dMMm+om
		yho................./hyh+..................-omy.............................-mo....../+o/.........oNNhhy-......................-m+.............-y:-..-
		mNs..`..`..`..`..`..os.oN-`..`..`..`..`..`...sM:..`..`..`..`..`..`..`..`..`.-ds.`..-sN++y:...ys...-/-./N:..`..`..`..`..`..`..`../N:`...:-`..`..`..`..`
		yhmydy................om+..................../y+.............................-No..hdso.......oh........-.............../ss+..-::-om:..dNmoyys-........
		..+dNo................smo:...................................................+N-..os-................................:+mh/+.+yssm:/ms/Myyo-oM+........
		..`+Ns-.`..`..`..`..`..:+:`..`..`..`..`..`..`..`..`..`..`..`..`..`..`..`..`..ds.`..`..`..`..`..`..`..`..`..`..`..`..`yNy:..:-...y-.-/ohhs+/-ym.`..`..`
		....oydo......................--............................................-hysso+..................................:omyyhhhhyo+//++osyhmmhy/........
		......::..............-os+ohhhhh::-...........:shd+yy.........................---:sysso++/:--::::::::://++ooo++//::+hNhso+/+++dd+hho//::----..........
		..`.--/oyd+`..`..`...-dh/sd/-dmmmmh`..`..`..`.o/-/o/:...`..`..`..`..`..`..-o.`..`...:::/+hmmdyydmyyyysysssMyosssyyyyhN+//////oN:`:ohy/...`..`..`..`...
		-/sdmmmNNM+........:dyh:..-.-MmmmNd......................................-hd.............mhym+/dd//+//+//yN/+//oooooNy//+//++ms...../syo:.......:/+syd
		dmNmmmmmmM:`..`..`./d..`..`.+MmmNNmo:-...`..`..`..`..`..`..`...:ooooooooyhs-.`..`..`..`..omomy/dd////////Ny+syhhyssmm+//////yd..`..`-:ym+...:yhdmmNmmN
		mmmmmmmmmM/............-/+oymNmmMy+syhms........-.......s+//+oyho::::::::-..............:+mhsN+dh///////yMdhyo+///oNo//////oNo::://sysohdhhdNNmNmmmmmM
		mmmmmmmmmNho+/:-.......dNNNmmmmNm+//+yN:.....oyydyshy...:++++/:-...............shhyyysoyhNh+/ddmy//+//++Nho/+//+//dd/+//+//mdsoooo+/-/mNmmmmmmmmmmmmNh
		mmNmmNmmNmNNNNmd:....:oMmmNmmNmMo///oNNo.`...+:.:+/:d:..`..`..`..`..`..`...--:+Ns++oNho+/sN+/oNMy//////sN+///////oN+//////ym-`..`..`:dNNNNmmNNmNmmNNN-
		mmmmmmmmmmmmmmmNmds+yhyMNmmmmmNd/+/+mNNm:.-----........................./oydmdyo/+/dd+/+++Ny/+hMy//+//+my+//+//++my//+//++Nyh/-.....:smMNNmmNMNmmmmMs
		mmmmmmmmmmmmmmmmmmmMy+/NNmmmmNN+///hNmmNNshyhyhs-.......................NNNmNNmdyoyMyyhhhhdN+/+ho/////+M+///////yN+/////odh+ohh/-/sdmNNmmmmNMmNmmmNm`-
		mmmNNNmmNmmNmmNmmNmMs//mNmNmmMy///sMmmNNmy+///+yd/...`...:-...`..`..`...NNNmmNmNNNMdso++//+my/////////+Mo//////+Ns/////omy////sNmNNNmmNmmNmMhsMNmNM++N
		+/+NNmmmmmmmmmmmmmmMs+/dNmmmNm+//oNNmNds+/+//+//sds--/ohdmms-.........../dNmmmmmmmNm+//+//+sN+//+//+//+my+//+/+dd/+//+sms//+//hNmmmmmmmmmmNm/+NNmNNdNM
		//sMmmmmmmmmmmmmmmmMs//yMmmmMs///mMmho//////////+sNdhNNmmmmNms/++++++/:-:sMmmmmmNmho////////my/////////dh////omy/////hm+/////+MNmmmmmmmmmNMy//hMNMMNNd
		//yNNNmmNmmmmmmmmmmMs//sMmmNd///+ds+/////////+ohdho+/odNNmmmmNNNNNNNNNNNNNNmmNmNN+//////////sN+////////ym///ymo////+dd+///////mNmmmmmmmmmMMN+omMNNNNm.
		+//oymdhdMmmmmmmmmmMs+/oMmNNo/+//+//+//+//+shdho+//+//+smNmmmmmmmmmmmmmmmNNNmdhys+//+//+//+//Ny/+//+//+sN++dd+/+//omy+//+//+//oMNmmmmmmmmNNo/+mNmmNN-
		+/////o+yMNNmmmmmmmMs//+MNMh////////////ohdyo////////////yNNmmNmmmmmmmmmmNMy/////////////////sN+///////+Mymy/////sNs//////////+sydNNmmmmNNo/ommMNNN:
		dh/ohmmmsodMmmmmmmmMs+//NNN+//+//+//+//ymo+//+//+//+//hhyysdMNMNmmmmmmmmNNNNm++//+//+//+//+//oM++//+//+/Nmo/+//+yNo//+//+//+//+//++hNNmNN++/+MMMMMo
		yM++++/+/+hMmmmmmmmMs+//mMs///+//+//++hm+/+//+//+//+//ohNNNNNMMMMNmmmmmmMhdNm++++oo++//oys+//sN/+//+//+/hs//+//yNo+//+//+//+//+//+//yMNMydy//dNNMo
		ohdmo///+NNNmmNmmNmMs///yh//////////+mh//////////////sdhydNMNNMMMMNmNmmMdooohmmNNNNNhsdmhMNdydm///////////////sNmmy+//////////////+sNNMMMd+//oMN:
		+/sMs/+//hNmmmmmmmmMs+//+//+//+//+/oNs/+//+//+//+//+/omNNmNNNMMMNMMNmmNNoooooNMMMNmNNysoohNNNNd/+//+//+//+//+sNyNNNNhhhyysymdhyshmNNmmNNs/+/+dd.
		//yNo////+dMmmmmmmmN/////////////+ymo//////////////////smNmmmMMMMNNMNmMmdoooosmMNNNmMyooooNNsNy/////////////sNyoNNNmysmNNNNmmNmNNmmmmMh+///oNs
		////ods+shNNmmmmmmNh////////////+dd+/////////////////////yNNNMNMMNMNNNMMmooooooyNNmmNNooooyysMs////////////oNyoommyosmNNmmmmmmmmmmmNmsyy//sN/
		+//+omymMmmmmmmmmmMs/+//+//+//+omy+/+//+//+//+//+//+//yyo++yNMmshNNNMMMhooooooooodNNmMyooooomMo/+//+//+//+oNyooooooyNNmmmmmmmmmmmmMNmMmo+hm-
		///////+NNmNmmNmmNN//////sy+//oNs/////////////////////yNNNmddNMNdydNNMmoooooooooooyNNdNoooohMN+//////////oNMyooooohNNmmNmmNmmNmmNNNNNs/+mh`
		///+yhmNNNmmmmmmmMy/////yMMo//dd///////////////////////+hNNMNMmhydshMNshooooooooooosmhMyoosNMN//////////oNNMsoooodNmmmmmmmmmmmmmmNNy+/oNo
		+yhmNNmmmmmmmmmmmMo//+//mMN+/oN+/+//+//+//+//+//+//+//+//+hNMdoooohMMmNhoooooooooooosmMmooohMd//+//+//++mNNNooosmNmmmmmmmmmmmmmNNd+/+ym:
		mNNmmNmmNmmNmmNmNy//////mms//my/////////////////////////+//+ymhoooydhhmooooooooooooooodNooooNh/////////+MmNmooodNNmmNmmNmmNmmNNdo//+dd.
		mmmmmmmmmmmmmmNNy/+//+//++/+yN+//+//+//+//+//+//+//+//+ommdysoymhsoosmsooooooooooooooosMsoooNs//+//+//+oMmNdoooNNmmmmmmmmmmmmMy//+oms`
		ddmNNNNNNmNNmNmo//+//+//+//+Ns+//+//+//+//+//+//+//+//+/+ymMmdddNNhymsoooooooooooooooooNhssyMo//+//+//+oMmMhooyMmmmmmmmmmmmmMy+//ym+
		...---//+oshMd+////////////hm/////////////////////////////+ohddyydmNysyyyhhhhhhhhhhhhhhhyyshM+/////////oMNMyoomNmNmmNmmNmmNNh//+hd-
		`  `  `  `:dy+/+//+//+//+/+No/+//+//+//+//+//+//+//+//+//+//+ohNdhhdhys++/:::::----.-......+Ns+/+//+//+oMhdhhhMNmmmmmmmmmmNh+/omy.
		`  `  ` `omo+/////////////dm+/////////////////////////+ooyyyhyss+/:-......................+hds/////////oM---:+sydmmNNmmmmNh+/smo`
		`  `  `.yd+//////////////oNsyyys++////////////++osyyyyyso+:--....`..`..`..`..`..`..`...:shho///////////+dyso/.`..-:/+yhdmNyoym/
		`  ``-shy+//+//+//+//+//+ms``.:+shyso+/+oosyyhyss+/:-...............................-+yhs++//+//+//+//+//+osdy..........::oNd.                       -
		` `/yhs+////////////////+ms/-.`  .-/sydmds+:--.`..`..`..`..`..`..`..`..`..`..`..`.:sdyo+////////+///////////+hd:.`..`..`.:ds`                      :yN
		/odho///////////////////++osyd:  `  ``./osyo/:.................................../myoo++/////oymy//////oso+///dh........+m+                     `/hhhN
		/oNs+/+//+//+//+//+//+//+//+/ym` `  `  ` `.-+syso+/::--.........................-Nmhyydy//oyhhNMh++soooymNmhysoN+.....-sd-                    .+hy/sm:
		..+dhhh///////////////////////dy:-` `  `  `  ``.-:/+osysso++++++o+ooooo+oo+:-..../:-..omyhy+-ymoydhmosyyhmNs/+sdd...`:hh.                  `.+ds-.hh.
		...../N+/+//+//+//+//+//+//+//+oyhhy+- `  `  `  `  `  ``.-:::::::::::::::-/osyso/:-..../+-../h:../my.....-:-....-.../mo`                `-oyho- :ms`
		..../mdo++/////+/////+hhysyyyyyyyyyys: `  `  `  `  `  `  `  `  `  `  `  `  ` `-:+syyo+:-...........-...............om/              `./shy/.  `om+
		..`.-+osmyssyyhh+////+ymd+:::-.```  `  `  `  `  `  `  `  `  `  `  `  `  `  `  `  ```-/oyyso/--....`..`..`..`..`..-hd.            `-oyho:`    `yd-
		.....--.:o+//--hhyhohyyshNh/  `  `  `  `  `  `  `  `  `  `  `  `  `  `  `  `  `  `  `  ``./+syysso+/:--.........:dy`         `./shy/.      .+dy`
		++/sdNN/.......-::oms--:/+o+` `  `  `  `  `  `  `  `  `  `  `  `  `  `  `  `  `  `  `  `  `  ``.-:/+ossyyso+/:-+m+        `-oyho:`      `:ydo-
		MMMMMMM/.........:yNs.  `  `  `  `  `  `  `  `  `  `  `  `  `  `  `  `  `  `  `  `  `  `  `  `  `  `  ```-:/+sNm-      `/smh+.        -ody:`
		MMssMMMm+......-dMMMMm` `  `  `  `  `  `  `  `  `  `  `  `  `  `  `  `  `  `  `  `  `  `  `  `  `  `  `  `  .hh`   `-+yho/yyys+/-```+hd+.
		MMNNMMMMy..`../dNMNMMd` `  `  `  `  `  `  `  `  `  `  `  `  `  `  `  `  `  `  `  `  `  `  `  `  `  `  `  ` :mo  `/shy/. `  ``.:+smmms-
		MMNs/syo....../MMy`NMMmo.` `` `` `` `` `` `` `` `` `` `` `` `` `` `` `` `` `` `` `` `` `` `` `` `` `` `` `+N/-+hho-` `` `` `` .+hy:
		/+-............mMMNMMMd+do`` `` `` `` `` `` `` `` `` `` `` `` `` `` `` `` `` `` `` `` `` `` `` `` `` `` `yMhdy/. `` `` `` ``/hd+`
		..`..`..`..`..`/hs:---.:m+ `  `  `  `  `  `  `  `  `  `  `  `  `  `  `  `  `  `  `  `  `  `  `  `  `  ` `ho-`  `  `  `  ``sds-

	""")
    if(visA1 == 0):
        clear(2)
        print("You wake up in a dark, damp forest. You remember nothing but your name: ",name,". Your head is resting upon the soft most of the forest floor. In your pockets you have nothing but an old, metal compass, cold against your leg. You decide your first objective should be to find out what it is you're doing in this place. In all directions you can see very little for the density of the trees and their canopy, however, you can hear:")
        clear(2)
        print("To the north<1> you can hear the soft sound of horse shoes on mud. Perhaps a road? You think to yourself")
        clear(2)
        print("To the east<2> you can hear the quiet trickling of water.")
        clear(2)
        print("To the south<3> you can hear a repetitive dripping sound, echoing through what you think may be a cave")
        clear(2)
        print("To the west<4> you hear nothing at all. Perhaps there is nothing there, the sound is muffled by the trees, or something much more sinister...")

        if(intelligence >=8):
            print("However, due to your vast intelligence, you see the tracks of a large animal, similar to a bears but much larger. you shudder with the thought of what must lie ahead to the west<4>")
        clear(2)
        print("Which way do you go?")
        visA1 = 1
        buttonsmenu()
    elif(visA1 == 1):
        print("You return, again, to the dark, damp patch of forest where you originally woke up. Once again you can see very little however you still hear:")
        clear(2)
        if(visA2 == 0):
            print("To the north<1> you can hear the soft sound of horse shoes on mud. Perhaps a road? You think to yourself")
        else:
            print("To the north<1> is the plump trader you met previously.")
        clear(2)
        if(visA3 == 0):
            print("To the east<2> you can hear the quiet trickling of water.")
        else:
            print("To the east<2> lies the stream.")
        clear(2)
        if(visA4 == 0):
            print("To the south<3> you can hear a repetitive dripping sound, echoing through what you think may be a cave")
        else:
            print("To the south<3> is the large cave you visited previously")
        clear(2)
        if(visA5 == 0):
            print("To the west<4> you hear nothing at all. Perhaps there is nothing there, the sound is muffled by the trees, or something much more sinister...")
        #else something, i dunno yet
        clear(2)
        print("Which way do you go?")
        buttonsmenu()

    if(choice == "1"):
        A2()
    elif(choice == "3"):
        A4()
    elif(choice == "2"):
        A3()
    elif(choice == "4" and visA5 ==0):
        A5()
    elif(choice == "map"):
        map()
        A1()
    else:
        print("that was not one of the options. Options written with \"<>\" around them.")
        visA1 = 0
        A1()

def A2():
    clear(100)
    print("""
        NNhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhmM
        hd                                                                                                                                                  +M
        hd                                                                                                                                                  +M
        hd                                                                                                                                                  +M
        hd                                                                                                                                                  +M
        hd                                                                                                                                                  +M
        hd                                                                                                                                                  +M
        hd                                                                `                                                                                 +M
        hd                                      ``...---::://++ooosssyyyyyyyyysso+/:-..`                                                                    +M
        hd                                     +dysssssoo+++//::--.....``````..-:/++ossyyyysso/::-..`                                                       +M
        hd                                 `:+sMhooooooooooooooo:`           .----------::://+osyhddmddyso+:.                      .ss.                     +M
        hd                                 :M+/:--------------+Ndyy/. `-:/osyysssssssssssssssssssssyyyyyyhmNmh+-            -+.    `dMmo.                   +M
        hd                                 :M-+o/-.`          `/hy/+yydhhyyyhhyyyyyyyyyyyyyyyyyyyyyyyyyyyyhmmmmN:           yMm:    yMMMmo`                 +M
        hd                                 :M/M+/osyh`  `````   `+hs.sMddhysooossyyssssssssssssssssssssssssshNdd:           sMMNs-/sMMMMMN-                 +M
        hd                                 :M/M-   -M- :dsssysysssym:sNsooo++//:://///////////////////:::::::Mo`           -hMMMMNMMMMMMM/                  +M
        hd                                 :M/M-   .M- +N` `````...` sm         dhyyyyyyyyyyyyyyyyyyyd/      No          `hNMMMMMMMMMMMMMs`                 +M
        hd                                 :M/M-   .M- +N            sm        `M/   ````+dddds      ms      No          sMMMhsoMMMMd:/hMMm/                +M
        hd                                 :M/M-   .M- +N            sm        `M/   :yyyNMMMMMo-    ms      No         :MMMm  .mMMMh  /MMMMo               +M
        hd    --.``                        :M/M-   .M- +N            sm        `M/     `oMMMMN+:.    ms      No        -mMMMo   `hNy-  `hNMN`               +M
        hd    +syhyso+:..``                :M/M-   .M- +N            sm        `M/    `.dMMNm:       ms      No       .mMMMMo    `.      :Ny                +M
        hd        `-:/oyyhyso/:.``         :M/M-   .M- +N            sm        `M/.+shdNMMMmo:-      ms      No      .dMMMMNMo`.:.`       /dy-              +M
        hd                `-:+oyhhyo+:.``  :M/M-   .M- +N            sm        `ModMMMMMMMMMMMN::::::mo      No     `dMMMM++MMdNMNho-`     `yNs`            +M
        hd                       `.:/oyhhyosM/M-   .M- +N            sm         so++++++++++++++++++oo-``````No`````hMMMMd  +ymMMMMMMd-`..  +Md-            +M
        hd                               .:sM/M:   .M- +N            sm                       ``.:+syhysyyyyyhhhhyyhmoNMMN    `:syo:mMmhMM. .No             +M
        hd                                 :M/M-   -M: +N            sm                      :hys+:.`      :osyy/ `   yMMM.         hMs:sy+yds:             +M
        hd                                 :M/M-   .M- +N`           sm                    .yd:           -N+`   `m/  oMMM+         dMN.  --                +M
        hd                                 :M/M-   .M- +N            sm                   +mo+s.         `No      ym` -hMMm/`       mMMh                    +M
        hd                                 :M/M-   .M- +N            sm                 -dy.sMMm`        :M`     `mM-   .sNMNo:---..mMMN+                   +M
        hd                          .smhhhhNM+M-   .M- +N            sm                /N: hMMMMd`   :ho oN      +MM`     `oNMMMMMMMMMs-dh.                 +M
        hd                        .sm+.h-  :NNymo` .M- +N            sm                /M` NMMMNs``+mMM/ hm      dMMs.       ``.--::/-  sN.                 +M
        hd                       .Ny` `M:  smym/omo-M- +N            sm                -M- mMMM.-yNMMMN`+Mm       /dMMy:            ``./N-                  +M
        hd                       yMm` `M: .M/ /mo.omh. /N:  `/dmo.   sm                `M/ mMMMdMMMMMMs-MMd         /dMMdooosyyhdmmNNMmdN.                  +M
        hd                      -M/mo `M: yd   .hd``    :m+sdodd+hy- sm               `.No mMMMMMmdys+.sMMh    .o-   `/yyyyyyyyyyyyss:` ym.                 +M
        hd                      hd :N-`M:-M:   `+Mo      -mN. yh `+N./N:    .-:/osyydmNNMmyhyo/-```  ./dMMN/  +NMs                      /M`                 +M
        hd                     :M:  yd.M:hh  `+dyMNs.`   `N+  yh   yd`hh `+dso+/:dddyyo+///+osyyyyyyyhymMMMN+hMMM/       --        ``   oN                  +M
        hd                     dNy. .NsMsM-`/ds.-M:osyyyshd   yh   yMy:Mods.     .``:mysoomd:..``````` .dMMMMMMMM.     `sNN`   `  :m+ .sd/                  +M
        hd                    `Ns+hs.+MMMh/ds-  .M-  ``.oM:   yh  +m:NyNs.         :No`  -.smh:        :dMMMMMMMM-     oMMM/:+dmshy:-sNy`                   +M
        hd                     dy `/hyNMMmy-    .M-.-/+smNy.  yh /N: :MhyyyyyyyyyyymM.  /m-hNMM/-.```/dNMMMMh:dMMm`    /MMMNmNMMM:  hMM:                    +M
        hd                     yNsoo+hMMMmssssssyMhys+/-mhsd: yh-N/   ym```````````+N` `modd-NMMNNmmmMMMMMd:``mshMy`   :MdhdddMMm   -Nd`                    +M
        hd                     oN.-:+mMMNmy:..../M-     ym`/mohmmo .-/dd+++++++++++yd `sm-M/ hMMMMMMMMMMNN:  sd``dMmh` .M/``.-dMy  :mmyso/:--.``            +M
        hd                     /M`.ohhMdm.odo.  hm......oM. -dMMNsyyo/Ny+++++++++++Ns-ds.+M. ddhMMMMMMMM/+m//N-  .mMM: `N+    oM+ +m+..-:/oosyyyyysso+//:--.oM
        hd                     -Myho.hh:M- .odo/MhyyyyyyyMo/sdMMm:.  .MyyyyddyyyhhdM+-oohNo  dh`NMMMMMyM+/sNNd//::sMmd  ms    :MmhN-          ```..--:/+oossdM
        md.                    `My. -M: No   .oNh        dmo:dMmsd/` /M.```+M..sdsNNhmh:ym  .NN-dMMMMd/M/+dNNs//++hM-M/.dd.   -MMMM:                        +M
        dNyyo/-`                Mo  yd  yd    :M-        sN`ydhd -yh:sN    .M:`+. dh-/o`No .mMMddMMMMo/M.sd-/m:   dh hNNMMm:  /MMMMm`                       +M
        hd`.:oyyy+:.`           sm--M:  /M`   dy         :Mhd.sd   :hNh     Ns`   :/ `:sN.`dMMM.-MMMMs:Mdh.  /m/ +N. -MMMMM-  yMMMNs`                       +M
        hd     `-/syys/.`        omdd   `M/  /N.         .MN. om    .M+     -yho///+sys/- sMMMm  yMMMd+Ms`    /m+N+ .yMMNmy   oMMN/                         +M
        hd          .:oyys+-.     +Ns````dy`om/           sm. om    -M-       -////+-`    sMMMh   +NMMNMs-`   `+Mh :mMMN:`    :MMo                          +M
        hd              `-/shyo:.` :syyyyddyd-            `dh om   .ym`                   sMMm:   `NMMMMMdyoosyyd-`oMMM:     `+MMs                          +M
        hd                   ./shyo/..```````              .N+oN .odo.                    yMMh/`  `NMMMMM.-+-.`  smMMMd     -mMMMy                          +M
        hd                       .:ohhs/.`                  :ddmsdo.                      yNNNNd`  yMMMMMs.     `MMMMMy     `dMMMh                          +M
        hd                           .:ohho:``                `..`                         -----   /MMMMMMN     .dMMMMo     .mMMMN:`                        +M
        hd                               .:shho:`                                                  `//////:      `+yhd:      /mMMMMy                        +M
        hd                                   ./sdy+-`                                                                         `::::-                        +M
        hd                                       -+ydy/.                                                                                                    +M
        hd                                           -ohds:`                                                                                                +M
        hd                                              `:sdho-                                                                                             +M
        mNyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyhNMNhyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyydM
	""")
    global area, visA2,visE1,choice
    if(visA2 == 0):
        print("Crashing your way through the branches in the direction of the horse you eventually come breaking through into the sunight of an opening: ")
        print("You try to locate the sound you heard previously, the horse, once your eyes adjust to the brightness of day.")
        print("You see a small black horse pulling a wooden carridge. Atop the wooden carridge is a plump, friendly looking man. His purple clothes and emblem suggest a trader to you, though you haven't a clue why, you've never seen this man before in your life.")
        print("\"I've got all sorts of goods: maps, weapons... well that's it really... and only the one map...\", he mutters to himself,dissapointedly,\"Well I s'pose I've got a map and some weapons if you've got the coin! \", he calls out to you with a chuckle in his voice, \"you can also trade with me if you've not any gold to spare\"")
        if(gold == 0):
            print("\"Sorry, I don't have any gold on me. I'll come back when I do though!\", you shout out to him,")
            if(inventory1 == "" and inventory2 == "" and inventory3 == "" and inventory4 == "" and inventory5 == ""):
                print("\"I don't have nothing for trading neither\", you say.")
                print("\"ah, well\", he says, \"I'll be waiting here for you when you do\"")
                clear(2)
                print("Thoroughly dissapointed that you had no money or anything of value you decide to explore further.")
                clear(2)
                print("To the west<1> the muddy road continues, though you can't see where it leads as it turns a corner.")
                clear(2)
                print("To the east<2he muddy road continues straight, slowly transitioning to a more well made, cobbled path. A rotting wooden sign points in that direction it reads: \"Zollfeld\".")
                print("You ask the trader about it and he tells you, \"Well it's the biggest town for miles around! How is it that you're not knowing that?...\", before he can ask you where your from you hastily leave with no answer ready")
                clear(2)
                print("To the south<3the same area of dark forest where you originally woke up")
                clear(2)
                print("Which way do you go?")
            else:
                print("\"I can trade with ye though!\", you shout with glee at your good fortune to have met this trader,")
                print("\Wonderful, simply wonderful!\", he calls out, genuine joy in his every word.")
                clear(2)
                shop()
                print("After talking with the kind trader for quite some time you decide it's time to leave")
                clear(2)
                print("To the west<1> the muddy road continues, though you can't see where it leads as it turns a corner.")
                clear(2)
                print("To the east<2> the muddy road continues straight, slowly transitioning to a more well made, cobbled path. A rotting wooden sign points in that direction it reads: \"Zollfeld\".")
                print("You ask the trader about it and he tells you, \"Well it's the biggest town for miles around! How is it that you're not knowing that?...\", before he can ask you where your from you hastily leave with no answer ready")
                clear(2)
                print("To the  south<3>	is the same area of dark forest where you originally woke up")
                clear(2)
                print("Which way do you go?")
                buttonsmenu()
        else:
            print("\"What have you for sale?\", you ask him a grin on your face.")
            time.sleep(2)
            shop()
        visA2 = 1
    else:
        clear(100)
        print("You return to the road with the plump trader. He greets you by grabbing your hand in his two large ones and shakes your hand excitedly so you feel as though your arm may rip from it's socket.")
        print("\"Do you have gold or anything to trade ",name,"?\", he asks you hopefully.")
        if(gold>0):
            shop()
            print("After talking with the kind trader for quite some time you decide it's time to leave")
        elif(gold==0):
            print("\"No, sir, sorry\", you say to him, as thoroughly upset at your lack of gold as he.")
            clear(4)
        if(inventory1 == "" and inventory2 == "" and inventory3 == "" and inventory4 == "" and inventory5 == ""):
            print("\"I've nothing to trade right now mister but I'm sure I soon will.\", you say to him sadly")
            clear(4)
        else:
            print("\"As a matter of fact I do! \", you say as overjoyed as him at your chance to sell what you have collected")
            shop()


        print("To the west<1> the muddy road continues, though you can't see where it leads as it turns a corner.")
        clear(2)
        print("To the east<2> the muddy road continues straight, slowly transitioning to a more well made, cobbled path. A rotting wooden sign points in that direction it reads: \"Zollfeld\".")
        print("You ask the trader about it and he tells you, \"Well it's the biggest town for miles around! How is it that you're not knowing that?...\", before he can ask you where your from you hastily leave with no answer ready")
        clear(2)
        print("To the south<3> is the same area of dark forest where you originally woke up")
        clear(2)
        print("Which way do you go? ")

    if(choice == "1"):
        B1()
    elif(choice == "2" and visE1 == 0):
        E1()
    elif(choice == "3"):
        A1()
    elif(choice == "4"):
        map()
        A2()
    else:
        print("please choose one of the options.")
        A2()

def A3():
    clear(100)
    print("""
        oooooooooosMmoooooooomMoooooooooooooNMsoooooosMdooooomMsooooohMmydMmsoohMhoooooooooooMMdMhoooodMmMhooomMmMNdhhmMdooooooooooooooooooosNMdMMmhhhhdNNhooomMdhhhdMdoooooMMhhhMNdNNmdhmNNsooohMmhhhmMoooooooo
        oooooooooomMsoooooooohMyooooooooooodMyooooomNdMmooooodMyoooooosmMmsooNNNMsoooooooooooNMhMmooooNMhMyooosMmyNMdhhdMNsooooooooooooooooomMddMmMNdhhhhmMmsyMNhhhdMmooooooNMhhhmmNddhdNMhoooooyMmhhhmMoooooooo
        oossssssshMmyyyyyyyyydMmhhhhhyssooyMmoooooooydMmooooohMyooooooohMhooosNMmoohhoooooooomMdNNooosMmdMsoooohMhsmMmhhdNNyooooooooooooooodMmhNNosmMmhhhhhmMMMdhhdNNsoooooomMdhhhhhhdmMdsooooooyMNhhhmMoooooooo
        mNmmmmmddmmdddddhdhhhhhyhhhhhddmNNMMmhhyysooooNNoooooyMhooooooohMyoooosNNsdMhoooooooodMdmMsoohMmNMoooooomMsohMNdhhmMhoooooooooooooyMNhNMsooohNNdhhhhdNmhhhmMyooooooomMdhhhhhdNNyoooooooosMNhhhmMoooooooo
        +++++///////////////////////////+/ossyhdmmNNNmMMhyysosMdooooooodMyooooosNMMyooooooooohMmdMyoomMhMNoooooosMmosmMMmhhmMmooooooooooosNNddMhooooosmMmhhhhdhhhhMNoooooooodMdhhhhNMhoooooooooooMNhhhmMsooooooo
        /////////////////////////////////////////+++oosyhddmmNMNddhyyssmMsooooooNMyoooooooooohMmhMdosMNhMmooooooodMydMydMNdhdNNsooooooooomMddMmoooooooohMNdhhhhhhdMhoooooooodMdhhhhMdooooooooooooNMhhhmMsooooooo
        ///////////////////////////////////////////////////++++osyhhdmmNMmddyssmNyoooooooooooyMmhMmohMmhMdooooooooNNNMooyNMdhdNNyooooooodMmhNMsooooooooosNMdhhhhhNNooooooooohMmhhhhMdoooooooooooomMhhhmMsooooooo
        /////////////////////////////////////////////////////////////++++osydNNMyoooooooooooosMNhNMomMddMhooooooooyMMNooosmMmhhmMdoooooyMNdmMhooooooooooosmMmhhhdMhooooooooohMmhhhhMdoooooooooooomMdhhmMsooooooo
        ////////////////////////////////////////////////////////////////////+oymNdyoooooooooosMNhmMsMNhmMyooooooooomMdooooohNNdhdMmsoosMNddMmoooooooooooooohMNhhmMyoooooooooyMmhhhhMdoooooooooooodMdhhmMsooooooo
        ////ssoo+//////////////////////////////////////////////////////////////+ohmNdyooooooooMNhdMmMmhmMsooooooooohMyoooooosmMmhdNNyoNMdhNNsooooooooooooooomMdhhMdoooooooooyMmhhhhMmoooooooooooohMmhhmMsooooooo
        ////hddmmNddhysso++///////////////////////////////////////////////////////+shmNdyoooooNMhhMMMdhmMoooooooooohMyooooooosdMNddNNmMmhmMyoooooooooooooooohMmhhNNooooooooosMNhhhhMmooooooooooooyMmhhmMsooooooo
        dy+///++++osyhdddmmmdhyysoo++////////////////////////////////////////////////+shmNdsoomMdhMMNdhMNoooooooooohMhoooooooooyNNdhmMNddMdooooooooooooooooosMNhhmMyoooooooosMNhhhhMmooooooooooooyMmhhmMsooooooo
        hNdo///////////++++osyydddmmNmdhysoo++//////////////////////////////////////////+sdmmhmMdhNMdhhMmoooooooooohMhoooooooooosmMmhddhdMsoooooooooooooooooomMdhhMdoooooooooMNhhhhMmoooooooooooosMNhhmMyooooooo
        /omNy+///////////////////++++osyhddmmNmdhyyso++////////////////////////////////////+sdNMdhmMdhhMdooooooooooyMhooooooooooooNMhhhhdMyoooooooooooooooooohMmhhNNoooooooooMMhhhhMmoooooooooooooMNhhmMyooooooo
        //+yNdo///////////////////////////odMmhdmNMMNNNmmdhysoo++/////////////////////////////hMmhdMmhdMhooooooooooyMhoooooooooooomMdhhhhMdoooooooooooooooooosMNhhmMyooooooooNMhhhhMmoooooooooooooMMhhmMyooooooo
        ////omNy+//////////////////////oymNdo+//++osydmMmyyhddmmmmdhyysoo++///////////////////yMNddMNdmMyoooooooooosmhoooooooooooohMmhhhhNNoooooooooooooooooooNMdhdMdoooossssNMddddMNhhddddmmmmmmmMMNNNMmdddhhhh
        /////+yNmo////////////////////+NMy+///////////+smmy+//++oosyhddmmdmmdyhysssooo+++/////ohNMMMNmdyooooooooooooooooooooooooooyMmhhhhmMdddddddddddddddddddNMNmNMNmmmmmmmmmmddddhhhyyysssooooo+ooooosssyyyyyh
        ///////omNy+//////////////////+NM+//////////////+hNmo//////////+++ooydNMMmmdmmddmmmdddmmdhmNNdysoooooooosssooosmmmmmmmmmmmmMNhhhhdMmyyyyyyyyyyyyyyyyhdMMmdsooooo+++++++/////////////////////////////////
        ////////+yNmo//////////////////yMh////////////////odNh+///////////////+sdmmys+++ooossyo+///+yNMmoooooosmmddmmdhMMhssooooo+oMMhhhhhMm////////////+ohmmdyo+///////////////////////////////////////////////
        //////////omNy+////////////////+NN+/////////////////smNy+////////////////+shmmho+/////////+hNNdsosyhdmmd+--:/oosmMmmddmmdhyNMdhhhhNM////////+osdmmds+///////////////////////////////////////////////////
        ///////////+sNmo////////////////hMy//////////////////+sNms+/////////////////+yMMmhsooossydNmhyhmmddyo/:.........hMyhysssyhNMMdhhhhmMs////+oymmmyo+////////////////////+ohyso++//////////////////////////
        /////////////odNy+//////////////+Mm////////////////////+hNdo//////////////////hMmhmNMMmhyyyddhs+:-.......-:/os+:omNNNmddddmmNmdhhhdMh/osdmmds+//////////////////////+ymmmhmmmddhyso++///////////////////
        //////////////+yNmo//////////////dMs/////////////////////omNh+/////////////////hMy+ohmdh+:-:-..........+dmmdhydmddy+/::::-.-yMNNmdhMNsmmyo///////////////////////+sdmms+///+oosyhmmmdmhy////////////////
        ////////////////sNNhso+//////////oMd//////////////////////+yNms+///////////////+dMs//+oydmdy+:-......../MmyyyhhdmMMNd/..../dNyoyddmNNdNdhyysoo++++////////////+ohmmyo/////////////++smMm+///////////////
        /////////////////+yNMNddyo++//////mMo///////////////////////+yNms///////////////+ys//////+oydmdy+:......oyssooo++++//-..:yNd+////++osyhdyhhdmmmmddddhyysoo++oymmho/////////////////sNNs/////////////////
        ///////////////////+mMyyhmmmhso+//sMh/////////////////////////odNh+////////////////////+osossydNMNd/..................-oNNy+osyhdddmmmdh+/////+++ossyhhdmmNmNds//////////////////odNh+//////////////////
        ////////////////////+mNs//+sydNmdysNM+//////////////////////////sMNhyyyyyyyyyyyyysssssyNMNhyyyssso+:...............-oydNymmmmdhysso++////////////////////+dMh+//////+oooossssoosyNmo////////////////////
        /////////////////////oNNs/////+oshmNMy+++/////////////////////+ymmssssssssssyyyyyyyyyyyyyo.......................-ommso+/++//////////////////////////+oyhmmNNdooo+yhNMNNNNmNmmmmms+/////////////////////
        /////////////////++ydNmmNs+////////+NNNNdo++++++++/+++++++oosymNy-.............................................-omNs////////////////////////////++shdNMMMdo/osddmNmmmmmNNNNNNNmmNmho+///////////////////
        +++////+shdyso+oymNmyo/+mNdhso+////++++yNMmddddddddddmmmmmdhhyo:..............................................:mNs///////++++++o++/////////++sydmmdNMNmhymNdyhhhhyyhhhhhhhyyydhooshNmds/////////////////
        NmdhyydmNhyhdmNNNs+/////+oshdNmdyyhdmmmdhs+/::::://::--..............-:-.....................................-+NNhyyhhddddmmmNNNmddyo+++oydmmds+:-hMh+////oNMMdyyyyyyyyyyyyyyyhmmdyodMd/////////////////
        +osydmyo///////+o///////////+sNNdh+/:.......................:--...-ohNNNs-...........................-:....-hMmddhhyysssooo++///+oydmMmNmyo/..../mNs//////+MNyNds+/////////////+odMMNh//////////////////
        hmddmdddddddddhhhhhhhyyyyyyymNy:........................-/ydNNNmddMMNyshNNy-....................-....-//:-/NMs+/////////////////////+NM-.......sMd+///////oMd/ohNmy+//////+/oydmNmys+///////////////////
        --:::://////++++++ooooosssyyy:.....................-.-ohNNhs+//+oosyyhdmmmNNmddhysso+/:-.......-///-...-//ohmNmhyo+///+++o++/////////hM+.....:dMy/////////sMd///+ymNh+++yhmNMMMNdhhhhhhhys//////////////
        ...............................................:--:/-:hdmmNmmy//////////////+oossyyhddmMh/........://:...-//:-:oydNmddmNNdNmdyo+////+dMs....+Nm+//////////oMd///+shNNNNNho/////+++oyhhddMNsoooooo++oooo+
        .........................................-/symNNmNNNmddo//:+Md/////////////////////////+hNms:.......-///-..://.....:+/-....:+ymNddmNNm/....oMMhhyyysyyssssyMdshmNds/.:-......:+shmNmdddddmddddmmmmmmmmmN
        ..................::....-...........-oshNNdhyo//////+odM+://Mmoossysyyyhhdddhys++/////////sdMh/........:/:..//-................-+/:........./ooosssssyyyhhhddds/.......:+shmNmhys+//////////////////////
        .................:/:..://...://..-odMmys+///////++oyyhdMM::-oddhhyysssoo++/+oyhmNNmdhso+++++ohNmo-......//..//......................................................+dMNdys+////////////////////////////
        .................//-..//...-/:..sMNy/+ossyhdmmNNmdhyso+/-........................-:+sydNNNNNNNNNNN-.........::....................................................:dMMh/////////////////////////////////
        .................:/:..//...:/:..:dMNNmdhyso+/:......-:-...........................://:........--::://-...........................................................oMm+yMd+///////////////////////////////
        do:...............:-..//-..-/:....-.................-:///:.......................//-...-:://///::---..................................................--..-/-...-NM+//sMm+//////////////////////////////
        sdNds:.................-....::-.........................-//:....................-/:..://:--..-:::.-+++++++///////////////::::::::::----------.........://:-//:..yMs////oNNo/////////////////////////////
        //+sdmmy/.........-:-------.-:///:-.....-/:...............-//-..................:/:.:/:..::///:/ohNmhhhhddddhhddddddddddmmmddddddmmmmmmmmmmmmmmmmNNms/..-:////-/Mm//////oNN+////////////////////////////
        ++++ooymMNh+.......:::::::///:---::///::-//:................--..........:::-.....---//.-//--:sdNdy++/////////////////+sdNNmmdhhyssoo+++++++++++++++shmmy/.:////mMooo/////yMh////////////////////////////
        mdddddddddh+................-:://:-----:::/:-........................-://--..----..-:-..-/smNhs+///////////////////ohNNho++osyyhhdmmNmo//////////////+hMN/:///+NNmNM/////+NM+///////////////////////////
        ................................-:://::::://-.......................:/:-..:///::::..../smmhs+////////////////////ymNhs+///////////++oNNo//////////+sdNdo-.:/://---mM//////sMdso+////////////////////////
        .................................--.---:::-....................:::://-..-//-.......+yNNds++oooo++++++ossyso+////odNNhs+++++++++++++++oNNs+ossyhddmNms:....:/-//...smNdyo+/+shdmmNdhyso+/////////////////
        ................................::////:::---...................-::::....//-.......+mmmmmmNNNmmdmmmmNNNmdhdmmNdhyoooshmNmmmNNNNmmmdddddmmmddhyyo+/:--.........--....-:+ydNdysssssyhdNMNNmhssssssssooooooo
        .....................................---:::///:--.............-....--...-..........---:sNMdo+++++++ohNmy+/++osyddmNdhys+++ohmNy:----------.............................--+yhyhyhhhhhhhhhhhhhhhhhhhhhhhhh
        .................:+shy-......................-:://:..-::.-/:.-//-.//:.............../smmy+///////////+ymNyo+////+++syho////+yNN/...............................................-oys/-...................
        ...........-:+sdmddhmM/..........................-:-..://-://--//://.............-odNdo+///////////////+smmmmdhyoo//////+odNds:...-:-........................................:ymmyhmmy+:................
        ..........omNMMNmmmmNN/................................:/:.-//..:///.........../ymmy+////////////////////+++osyddmmdhyshmms:-....//:-..................:-.................-+dNdo+//+oydmds/-............
        -........./ysoo+//:::-.................................:/-.-//..-/::..........omMNdhyssoo+++//////////////+oossydmNNNmdy/-......:/:....--///:-......./dmdddhso+/:-......-ommho////////++sdNmy..../yhdddd
        dh/....................................................---..--.................::/+osyhddddmddhyysoosyhdmmmddhyso/::--.........-//...-//::----.....+dNho+oosyhdddms:..:ymNho+/////+++oosdmmy+...:Nmsoooo
        ohmd+-..................................................:///////::-.....................--::/+osyhddhyo+/:--...................-//...:/:.........+mNh+//////////+sdmdosmmdddmdyhdmddddhhy:-....-mMo+++os
        //ohmd+-.......................................................--:///-.........................................................-/:...:/-......-+mNy+///////////////+sdmmy/--:oyo/::--..........-+mdddmdh
        ////+ymmo-..........................................................-...........................................................-....:/-....-ommy+///+ooooooooooo+++++oydmdo-....................---::..
        //////+smmo-..............................................................................................................................-ommyoosyddddddddddddddddddddddNMM+...........................
        ////////+yNm:..................................................-........................................................................-omMNdmddhyo/:-....---..----:::://++::..........................
        +osyhdyso+mM..................................................-//-........................./:................................--.........smdhs+/:.....................--/://::-..----....................
        dddyooydddMd....................................................://:-.....................-//................................-//:-.......-..........................:/::-...-:://///:...................
        -.......-:/-......................................................-://:-..................:/:..................................-://:-..............................-//.....:/:-.....::--------..........
        .....................................................................-://:-...............:/:.....................................-://::---........------..........-//.....//-..../ymmddddddddddhhhhhyyy
        ........................................................................--///:-...........:/:........................................--:://///::::///////...........--.....//....+NNo+++++o++ooooossssss
        ............................................................................-://:-........:/:................................................--------:::::////:::----------//:...:hmmhso+///////////////
        ...............................................................................-:///-.....:/:.....................................................-//:----------::////::::::::.....-+MMNs///////////////
        ...................................................................................//-....-/:.....................................................................................:hNMy+////////////////
        ....................................................................................//.....//......................................................................................ymmdso+++++++++++++++
        ....................................................................................:/-....-:........................................................................................:ohNmmmmddddmmddddd
        .-+yyo+:-................................................................................................................................................................................:-----:::::::::
        hNmyyhdmNmhyo+:-........................................................................................................................................................................................
        so///////+oyhdmNmhyo+:-.................................................................................................................................................................................
        ////////////////+oyhdmNmdyo+:-..........................................................................................................................................................................
        ///////////////////////+oyydmNmdyo+:-...................................................................................................................................................................
        //////////////////////////////+oshdmNmdys+:-............................................................................................................................................................
        /////////////////////////////////////+oshdmNNdhs+:-.....................................................................................................................................................
        """)
    global area, visA3,F2riddle,choice
    visA3 = 1
    area = "A3"
    print("You arrive at a small stream. It's water trickling gently by. Do you:") #breaking it's glistening surface you seem a strange object.
    #print("<look at> the strange object,")
    if(F2riddle == 0):
        print("move north<1>, in the opposite direction of the current to the water's source,")
    if(visF1 == 0):
        print("travel south<2>, moving in the same direction as the stream or")
    print("return west<3> to where you started this adventure.")
    buttonsmenu()

    # if(choice == "look at"):
    #     print("What can this strange device be?")
    #     time.sleep(2)
    #     print("When you touch it, it brings forth a sound")
    #     time.sleep(3)
    #     print("It's got wires that vibrate, and give music")
    #     time.sleep(3)
    #     print("What can this thing be that you've found?")
    #     clear(1)
    #     time.sleep(2)
    #     print("You can't wait to share this new wonder")
    #     time.sleep(3)
    #     print("The people will all see it's light")
    #     time.sleep(2)
    #     print("Let them make their own music")
    #     time.sleep(2)
    #     print("The Priests praise my name on this night.")
    #     clear(1)
    #     time.sleep(3)
    #     print("...Instead of the grateful joy that I expected, they were words of quiet rejection!")
    #     time.sleep(4)
    #     print("Instead of praise, sullen dismissal.")
    #     time.sleep(2)
    #     clear(2)
    #     print("Your spirits are low, in the depths of dispair")
    #     time.sleep(3)
    #     print("My lifeblood...")
    #     time.sleep(3)
    #     print("...Spills over")
    #     time.sleep(4)
    #     print("GAME OVER (you died)")
    #     exit(2)
    if(choice == "1" and F2riddle == 0):
        F2()
    elif(choice == "2" and visF1 == 0):
        F1()
    elif(choice == "3"):
        A1()
    elif(choice == "map"):
        map()
        A3()
    else:
        print(choice," was not one of the options.")

def A4():
    global area, visA4,intelligence,choice
    clear(100)
    print("As the cave comes into view you only now get a grasp of how vast it must truly be.")
    print("You drop a stone down it and don't here it land for several seconds.")
    print("Do you:")
    clear(1)
    print("<climb> into the cave with a rope that you spotted hanging from a nearby tree")
    clear(1)
    print("<jump> into the cave, blindly.")
    clear(1)
    print("Return <north> to where you started this adventure.")
    clear(1)
    buttonsmenu()

    if(choice == "climb"):
        C1()
    elif(choice == "jump"):
        print("You leap into the dark abyss of the cave.")
        time.sleep(2)
        print("...")
        time.sleep(2)
        print("As you fall it dawns on you that maybe this was not the best approach.")
        time.sleep(2)
        print("...")
        time.sleep(2)
        print("Your body smashes into the cold floor of the cave.")
        time.sleep(2)
        print("GAME OVER, you died (what did you expect, i mean really?)")
        time.sleep(4)
        quit()
    elif(choice == "north"):
        A1()
    elif(choice == "map"):
        map()
        A4()
    else:
        print("That was not one of the options.")
        A4()
    visA4 = 1

def A5():
    clear(100)
    global area, inventory1,visA5,choice
    if(intelligence>=8):
        print("Cautiously you follow the \"bear\" tracks,")
    else:
        print("You stumble, blindly in the direction where you could hear nothing,")
    print("As you walk on further you start to see large dead animals, deer, cattle and horses are among them")
    print("You jump at every sound, whether a snapping twig or the rustling of leaves")
    clear(2)
    time.sleep(4)
    print("...")
    time.sleep(2)
    print("...")
    time.sleep(2)
    print("You see it!")
    clear(2)
    print("Ahead of you crouched low over it's meal, a horse, is a colossal creature.")
    print("At least three times your height, it smells the air, perhaps for your scent before locating you.")
    print("It turns around and stands up, it stares at you, it's nostrils flared")
    print("Do you:")
    clear(2)
    print("attack<1> it (requires 30+ strength or a good weapon),")
    clear(2)
    print("attempt to ride<2> it,")
    clear(2)
    print("Or run, east<3>, back to where you began your adventure.")
    clear(2)
    print("What do you do? ")
    buttonsmenu()
    if(choice == "1" and strength>=30):
        clear(100)
        print("You overpower the creature with your overwhelming strength. You pick it up and throw it into a tree.")
        print("Dazed, the creature turns around slowly but as it does you leap onto it's back and blind it.")
        print("Wildly, the creature swats at you with it's arms but you dodge it's attacks easilyl.")
        print("As it falls to the ground in pain, you emerge, victorious.")
        clear(2)
        print("Bear hide added")
        inventory1 = "bear hide"
        levelup(2)
        clear(100)
        visA5 = 1
        A1()
    elif(choice == "1" and  weapon >2):
        print("As the creature lunges at you with its enormous paws you slice it's hands clean off with your weapon")
        print("It opens it's massive jaws and tries to devour you. You plunge your weapon into the beast's throat.")
        print("Bear hide added!")
        levelup(2)
        inventory1 = "bear hide"
        clear(100)
        visA5 = 1
        A1()

    elif(choice == "2"):
        clear(100)
        print("You walk slowly towards the creature with your hands out in front of you as a sign of respect.")
        time.sleep(2.5)
        print("The beast swats you away with it's enormous paws, knocking you aside like a ragdoll.")
        time.sleep(2.5)
        print("Your limp body smashes into a nearby tree.")
        time.sleep(1.5)
        print("You die instantly.")
        time.sleep(2)
        print("GAME OVER, what did you expect?")
        exit()
    elif(choice == "1" and strength<30):
        clear(100)
        print("You run at the beast with all the speed and confidence you can muster.")
        time.sleep(2)
        print("The beast swats you away with it's enormous paws")
        time.sleep(2)
        print("You die instantly.")
        time.sleep(2)
        print("GAME OVER, seriously, you attacked the bear?")
        exit()
    elif(choice == "3"):
        A1()
    elif(choice == "map"):
        map()
        A5()

    else:
        print(choice, " was not an option, please pick one of the options in \"<>\"")
        A5()

def B1():
    global area, choice
    buttonsmenu()
    print("You walk on the path for quite some time until eventually you see a beautifully painted sign above a large arch that reads: \"Zollfeld\"")
    print("You walk around the small town for a while looking for shops that may be useful to you but only see one. An alchemist.")
    print("Do you:")
    clear(2)
    print("Enter the <alchemist> or,")
    clear(1)
    print("Go <back> to the trader.")
    choice = input(": ")
    if(choice == "alchemist"):
        alchemist()
        input("Press enter/return to exit Zolfeld and return to the trader.")
        A2()
    elif(choice == "back"):
        A2()
    elif(choice == "map"):
        map()
        B1()
    else:
        print("That wasn't an option")
        B1()

def E1():
    global area, weapon, gold, visE1,inventory2,choice
    buttonsmenu()
    visE1 = 1
    print("You walk down the muddy road and turn the corner.")
    time.sleep(1)
    print("The second you see what's there you regret your decision.")
    time.sleep(1)
    print("A gang of bandits all stare at you simultaniously")
    time.sleep(1)
    print("They walk towards you")
    time.sleep(1)
    print("Do you:")
    clear(1)
    print("<attack>")
    clear(1)
    print("<run> back to the trader")
    clear(1)
    choice = input(": ")
    if(choice == "attack"):
        if(weapon >= 1):
            print("Three of the bandits run in your direction,")
            print("\"Your money or your life!\", one shouts out to you,")
            print("You draw your weapon and slice the biggest one's head clean off before the others can react.")
            print("They look at eachother stunned, fear in their eyes.")
            print("One runs for his life,")
            print("While the other is frozen in fear, watching after his deserting friend you plunge your weapon into his back,")
            print("He falls, limp, to the ground as the rest of the bandits flee to the shadows of the forest.")
            clear(2)
            print("You loot the two bandits' corpses and find 200 gold in their bags.")
            gold = gold+200
            input("press Return/Enter to contine")

            A2()
            levelup(1)
        elif(luck >=10):
            print("Three of the bandits run in your direction,")
            print("\"Your money or your life\", one shouts out to you,")
            print("Luckily as he says that he slips on the muddy ground, impaling himself on his own sword.")
            print("The rest of the bandits flee, fearing your mind powers.")
            print("You loot the fallen bandit's corpse and take his weapon:")
            clear(1)
            sword("rusty sword", 1)
            input("press Return/Enter to contine")
            A2()
            levelup(1)

        elif(strength >=30):
            print("Three of the bandits run in your direction,")
            print("\"Your money or your life!\", one shouts out to you,")
            print("Due to your immense strength as one attempts to attack you, you pick him up in your hands and tear him clean in half.")
            print("\"FEAR ME!\", you bellow. The rest of the bandits run for their life into the forest. You throw the two halves of the dead bandit into the forest. You estimate they land around a kilometer away.")
            input("press Return/Enter to contine")
            A2()
            levelup(1)
        else:
            print("The bandits walk towards you, you try to attack them but without a weapon or any strength to speak of the biggest of the them kills you with one swipe of their sword. You see them loot your body as you slowly bleed out")
            time.sleep(3)
            print("GAME OVER, you seriously suck")
            time.sleep(8)
            visE1 = 1
            exit()
    elif(choice == "run"):
        A2()
    elif(choice == "map"):
        map()
        E1()
    else:
        print("that wasn't an option")
        E1()

def F1():
    global area, visA1, inventory2, weapon,choice
    clear(100)
    print("You follow the stream, eventually as it widens and flows into the ocean you reach a small beach.")
    print("In the water you spot a skeletal hand with a sharp sword, glistening in the light.")
    print("Do you: ")
    clear(1)
    print("Turn your back on the mysterious hand and <leave> or")
    clear(1)
    print("Wade into the cold waters and <take> the sword from the skeletal hand")
    clear(1)
    choice = input(": ")
    if(choice == "leave"):
        print("As you turn to walk away, you hear a clatter at your feet. The sword!")
        print("You look into the lake and the dead hand is gone from the glistening surface.")
        sword("sharp sword",3)
        A3()
        visF1 = 1
    elif(choice == "take"):
        print("As you attempt to retrieve the sword you feel the hand's cold fingers tighten around your wrist. Before you can react it drags you under the waves.")
        time.sleep(3)
        clear(2)
        print("GAME OVER, you died. (You got too greedy)")
        exit()
    elif(choice == "map"):
        map()
        F1()
    else:
        print(choice, " was not an option.")
        time.sleep(2)
        F1()

def F2():
    clear(100)
    global area, F2riddle,strength,choice,visF1
    print("You follow the stream in the opposite direction of it's flow and find a waterfall.")
    print("You notice a small lever built into the stone of the cliff.")
    print("Do you: ")
    clear(2)
    print("Flick the <switch> or")
    clear(1)
    print("Go <back>")
    clear(2)
    choice = input(": ")
    if(choice == "back"):
        A3()
    elif(choice == "switch"):
        print("A platform forces it's way through the flowing waterfall causing the water to flow around it and allowing you to walk through into a small chamber in the side of the cliff face.")
        print("Inside the chamber is a shrine upon it is the word:")
        clear(1)
        print("\"sdvvzrug\"")
        clear(1)
        print("Below it a message in English, to help decypher it, it reads: ")
        clear(1)
        print("\"subtract four\"")
        clear(1)
        print("Below that another piece of text:")
        clear(1)
        print("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
        print("DEFGHIJKLMNOPQRSTUVWXYZABC")
        clear(1)
        print("To crack the code input the decyphered message. To go <back> down the river type <back>")
        choice = input(": ")
        if(choice == "back"):
            A3()
        elif(choice == "password"):
            print("You feel an ancient blessing being placed upon you as you input the correct answer.")
            strength = strength+30
            print("+30 strength. Strength now: ", strength)
            print("As you exit the chamber you hear the waterfall reform behind you.")
            F2riddle = 1
            input("Press return/enter to continue")
            visF1 = 1
            A3()
        elif(choice == "map"):
            map()
            F2()
        else:
            print("That wasn't one of the options")
            time.sleep(1.5)
            F2()
    elif(choice == "map"):
        map()
        F2()
    else:
        print("That wasn't one of the options")
        time.sleep(1.5)
        F2()

def C1():
    clear(100)
    global area, visC1,choice
    if(visC1 == 0):
        print("As you slowly make your way into the mouth of the cave you hear a noise slowly louden, only once you get to the cold stone floor at the bottom of the cave do you realise what it is. Music.")
        print("You see an entrance to more of the cave up ahead. Above it is a shoddily made sign it reads: \"Bandit's Guild\". Do you:")
    else:
        print("You return to the bottom of the cave, with the entrance to the Bandit's Guild. Do you:")
    clear(1)
    print("<enter> the Bandit's Guid or")
    clear(1)
    print("<ascend> back up the rope to the surface")
    clear(2)
    choice = input(": ")
    if(choice == "enter"):
        visC1 = 1
        C2()
    elif(choice == "ascend"):
        visC1 = 1
        A4()
    elif(choice == "map"):
        map()
        C1()
    else:
        print("That was not an option")
        time.sleep(1.5)
        C1()

def C2():
    clear(100)
    global area, visC2, killedC2,choice
    visC2 = 1
    if(killedC2 != 1):
        print("As you enter the Bandit's Guild you see two guards, ")
        print("\"Halt!\", they shout, raising their weapons, \"What business do you have with us?\"")
        print("Do you:")
        clear(2)
        #print("Say: \"I wish to <join> the Bandit's Guild\"")
        #clear(1)
        print("Say: \"Nothing, Nothing\", and go <back> to the start of the cave")
        clear(1)
        print("<attack> both of the guards")
        clear(2)
        choice = input(": ")
        if(choice == "back"):
            C1()
        elif(choice == "attack"):
            if(strength>20):
                print("You walk up to the guards confidently, with two small pebbles in your hands held behind your back.")
                print("They look at you angrily, \"This is your last warning\", they say, \"We will attack.\"")
                print("You hurl the pebbles with your immense strength at the guards' heads.")
                print("They soar at such a great speed that they fly directly through the guards' heads killing them both instantly")
                killedC2 = 1
                visC2 = 1
                clear(2)
                levelup(2)
                input("Press Enter/Return to continue...")
            elif(weapon >1):
                print("You walk up to the guards confidently, as they move to block you from entering further you slay them both with one swipe of your ", inventory2)
                print("You see one of their weapons: A sword!")
                sword("sword",2)
                visC2 =1
                killedC2 =1
                levelup(2)
                clear(2)
            elif(intelligence > 8):
                print("You walk up to the guards confidently, because of your superior intelligence, you notice that both their swords have weakspots in the same place.")
                print("As they swing their weapons in your direction you are able to snap them both clean in half.")
                print("The bandits run away in fear.")
                levelup(2)
            else:
                print("You walk up to the guards confidently, with one quick movement of his sword one chops your head clean off. You die instantly")
                time.sleep(2)
                print("GAME OVER! you died.")
                exit()
        elif(choice == "map"):
            map()
            C2()
        else:
            print("That was not an option.")
            time.sleep(2)
            C2()
    print("Do you: ")
    clear(1)
    print("go <back> to the entrance to the cave, ")
    clear(1)
    print("continue further into the cave down a passage to your <left> or ")
    clear(1)
    print("walk down a passage to your <right>")
    clear(2)
    choice = input(": ")
    if(choice == "back"):
        C1()
    elif(choice == "left"):
        C3()
    elif(choice == "right"):
        C4()
    elif(choice == "map"):
        map()
    else:
        print("That was not an option")
        time.sleep(2)
        C2()

def C3():
    clear(100)
    global area, C3chest,choice
    visC3 = 1
    print("You walk through the door into a small room. In the centre of the room is a large wooden chest.")
    print("Do you: ")
    clear(2)
    print("<open> the chest,")
    clear(1)
    print("<continue> through the cavern, leaving the chest behind or")
    clear(1)
    print("go <back>")
    clear(1)
    buttonsmenu()
    choice = input(": ")
    if(choice == "open" and C3chest == 0):
        print("Inside the chest you find a legendary sword.")
        sword("legendary sword",4)
        C3chest = 1
        C3()
    elif(choice == "open" and C3chest == 1):
        print("The chest has already been looted")
        C9()
    elif(choice == "continue"):
        C7()
    elif(choice == "back"):
        C2()
    elif(choice == "map"):
        map()
        C3()
    else:
        print("That was not an option.")
        C3()

def C4():
    clear(100)
    global area, C4trap,choice
    visC4 = 1
    print("You enter a thin corridor, it's emptiness surprises you")
    if(intelligence>=10):
        print("Due to your immense intelligence you notice an anommaly in the roof, a trap.")
    print("Do you:")
    clear(1)
    print("<continue> walking down the corridor,")
    clear(1)
    if(intelligence>=10):
        print("<disarm> the trap,")
        clear(1)
    print("or, go <back>")
    clear(2)
    choice = input(": ")
    buttonsmenu()
    if(choice == "disarm" and intelligence>=10):
        clear(100)
        print("Trap disarmed,")
        print("Do you:")
        clear(1)
        C4trap = 1
        print("<continue> down the corridor, now that the trap is disarmed or,")
        clear(1)
        print("Go <back>.")
        choice = input(": ")
        if(choice == "continue"):
            C5()
        elif(choice == "back"):
            C2()
    elif(choice == "continue"):
        if(C4trap == 0):
            print("You don't notice the trap on the ceiling as you walk through the corridor due to your lacking intelligence.")
            time.sleep(2.5)
            print("A colossal boulder falls from the roof and crushes you into the floor.")
            time.sleep(1)
            print("You die instantly.")
            time.sleep(0.5)
            print("GAME OVER, didn't the empty corridor seem a bit suspicious?")
            exit()
        else:
            C5()
    elif(choice == "back"):
        C2()
    elif(choice == "map"):
        map()
        C4()
    else:
        print(choice, " was not one of the options.")
        time.sleep(1)
        C4()

def C5():
    clear(100)
    global area, C5killed,choice
    visC5 = 1
    print("You enter a large room, bunk-beds run along all walls. Some kind of dormitory for the bandits, you think to yourself.")
    if(C5killed == 0):
        print("Around the room you spot a total of eight bandits, you are going to need a very good weapon to get past them all.")
        print("Do you:")
        clear(2)
        print("<attack> all eight of the banits (good weapon or high strength),")
        clear(1)
        print("attempt to <trick> the bandits into letting you past (high charisma),")
        clear(1)
        print("<run past> the bandits and continue on your current path")
        clear(1)
        print("run <back> down the corridor in the direction of the cave's entrance.")
        clear(2)
        buttonsmenu()
        choice = input(": ")
        if(choice == "attack"):
            if(weapon>=4):
                clear(100)
                C5killed = 1
                print("In the blink of an eye, before many of the bandits notice you, they are all dead on the ground. Your incredible weapon feels as though it gives you the power of a god.")
                print("Do you:")
                clear(2)
                print("<continue> down the path or")
                clear(1)
                print("<back> down the corridor in the direction of the cave's entrance.")
                clear(2)
                choice = input(": ")
                if(choice == "continue"):
                    C6()
                else:
                    C4()
            elif(strength>40):
                print("One by one the bandits run towards you but due to your incredible strength you knock each of them unconcious in a second.")
                print("Do you:")
                clear(2)
                print("<continue> down the path or")
                clear(1)
        elif(choice == "trick"):
            print("The bandits let you past without too much questioning.")
            time.sleep(1.5)
            C6()
        elif(choice == "run past"):
            print("As you attempt to run past the bandits one hits you in the knees with the flat of his sword. You fall onto the floor.")
            if(luck>25):
                print("Luckily, at that exact moment an earthquake hit, knocking the rest of the bandits down.")
                print("You already being on the ground gave you a headstart against the others who were stunned by their misfortune.")
                print("You manage to slip past all the fallen bandits and make it to the exit of the chaber.")
                C6()
            else:
                print("The bandit drives his sword into your chest.")
                time.sleep(1)
                print("GAME OVER! you died")
        elif(choice == "back"):
            C4()
        elif(choice == "map"):
            map()
            C5()
        else:
            print("That wasn't an option")
            C5()

    else:
        print("The floor is littered with the eight dead bandits you killed earlier.")
        print("Do you:")
        clear(2)
        print("go <back> towards the cave's entrance or,")
        clear(1)
        print("<continue> on your current path")
        clear(2)
        choice == input(": ")
        buttonsmenu()
        if(choice == "back"):
            C4()
        elif(choice == "continue"):
            C6()
        elif(choice == "map"):
            map()
            C5()
        else:
            print("That wasn't an option.")
            C5()

def C6():
    clear(100)
    global area, strength,choice
    visC6 = 1
    print("Ahead of you is a large Iron gate. The gate has no hinges or any way past other than to break through it.")
    print("Do you:")
    clear(1)
    print("<break> (40 or greater strength or legendary sword required)")
    clear(1)
    print("go <back> in the direction of the cave's entrance.")
    choice = input(": ")
    buttonsmenu()
    if(choice == "break"):
        if(strength >= 40):
            print("You smash the gate down with your incredible strength.")
            time.sleep(2)
            C9()
        elif(inventory2 == "legendary sword"):
            print("Your magical sword of legend carves through the iron gate as though it were butter.")
            time.sleep(2)
            C9()
        else:
            print("You don't have enough strength right now, 40 or greater is required.")
            time.sleep(2)
            C5()
    elif(choice == "back"):
        C5()
    elif(choice == "map"):
        map()
        C6()
    else:
        print(choice, " was not one of the options.")
        C6()

def C7():
    clear(100)
    global area, C7killed,weapon,choice
    visC7 =1
    if(C7killed ==0):
        print("You enter a small, dark room with three bandits hunched low over a campfire cooking a meal.")
        print("Do you:")
        clear(1)
        print("<sneak> past them to the room ahead.")
        clear(1)
        print("<attack> the bandits")
        clear(1)
        print("go <back> in the direction of the cave's entrance.")
        choice = input(": ")
        if(choice == "sneak"):
            print("You silently creep your way through the shadows.")
            time.sleep(1.5)
            C8()
        elif(choice == "attack"):
            if(weapon >1):
                print("You sneak up behind the first two bandits slitting their throats as the third is distracted, cooking.")
                print("You throw a small stone behind him. When he turns to investigate, you stab him in the back.")
                clear(2)
                C7killed = 1
                print("Do you: ")
                clear(1)
                print("Go <back> in the direction of the cave's entrance or")
                clear(1)
                print("<continue> in the opposite direction of the caves entrance.")
                choice = input(": ")
                if(choice == "back"):
                    C3()
                else:
                    C8()
        elif(choice == "back"):
            C3()
        elif(choice == "map"):
            map()
            C7()
        elif(choice == "continue"):
            C8()
        else:
            print(choice, " was not one of the options.")
            time.sleep(1.5)
            C7()
    else:
        print("You return to the campfire and the three, now dead, bandits.")
        print("Do you:")
        clear(1)
        print("Go <back> in the direction of the cave's entrance or")
        clear(1)
        print("<continue> in the opposite direction of the cave's entrance.")
        choice = input(": ")
        if(choice == "back"):
            C3()
        elif(choice == "map"):
            map()
            C7()
        elif(choice == "continue"):
            C8()
        else:
            C8()

def C8():
        clear(100)
        global area, strength,choice
        visC8 =1
        print("Ahead of you is a large Iron gate. The gate has no hinges or any way past other than to break through it.")
        print("Do you:")
        clear(1)
        print("<break> (40 or greater strength or legendary sword required)")
        clear(1)
        print("go <back> in the direction of the cave's entrance.")
        choice = input(": ")
        if(choice == "break"):
            if(strength >= 40):
                print("You smash the gate down with your incredible strength.")
                time.sleep(2)
                C9()
            elif(inventory2 == "legendary sword"):
                print("Your magical sword of legend carves through the iron gate as though it were butter.")
                time.sleep(2)
                C9()
            else:
                print("You don't have enough strength right now, 40 or greater is required.")
                time.sleep(2)
                C7()
        elif(choice == "back"):
            C7()
        elif(choice == "map"):
            map()
            C8()
        else:
            print(choice, " was not one of the options.")
            C6()

def C9():
    global area, inventory2,strengthprint,choice
    print("You enter an enourmous, circular room, when you do you notice the door closes behind you.")
    print("In the centre of it stands a giant. At least 25 feet tall his towering stature is intimidating to say the least.")
    print("how do you defeat it:")
    clear(2)
    print("<climb> up it's back,")
    clear(1)
    print("Attack it's <legs>,")
    clear(1)
    if(inventory2 == "legendary sword"):
        print("<throw> your sword at it's head,")
        clear(1)
    choice = input(": ")
    if(choice == "climb"):
        print("As you clamber up it's back it roars with fury.")
        print("Do you:")
        clear(2)
        if(inventory2 != ""):
            print("Cut it's <throat> with your sword")
            clear(1)
        print("<snap> it's neck with your bear hands")
        clear(1)
        print("<strangle> it with your immense strength (requires 40 or greater strength)")
        choice = input(": ")
        if(choice == "throat" and inventory2 != ""):
            print("When you cut the giants throat it falls to the ground with a thud, throwing dust into the air")
            print("CONGRATULATIONS! game completed.")
            time.sleep(8)
            exit()
        elif(choice == "throat" and inventory2 == ""):
            print("No sword, please choose another option.")
            C9()
        elif(choice == "snap"):
            print("Wit a loud crack the giant's neck is broken. You ride it to the ground as it falls. It hits the ground with a loud thud throwing a cloud of dust into the air.")
            print("CONGRATULATIONS! game completed.")
            time.sleep(8)
            exit()
        elif(choice == "strangle" and strength >=40):
            print("The giant struggles against your grasp around it's throat but it is no match for your might. It falls to the ground with a loud thud throwing a cloud of dust into the air.")
            print("CONGRATULATIONS! game completed.")
            time.sleep(8)
        elif(choice == "strangle" and strength <40):
            print("Not enough strength, please choose another option.")
            C9()
        else:
            print("That wasn't an option.")
            time.sleep(1)
            C9()
    if(choice == "legs"):
        print("You knock the legs out from under the colossal creature. It falls to the ground with a loud thud. throwing a cloud of dust into the air.")
        time.sleep(3.5)
        print("As you walk up to it to kill it, it grabs your legs and lifts you into the air.")
        print("Do you:")
        clear(2)
        print("<swing> your body back and forth to break free")
        clear(1)
        print("Cut the giant's <hands> off with your sword (requires sword)")
        clear(2)
        choice = input(": ")
        if(choice == "swing"):
            print("The giant looks confused at your writhing to break free. It's expression changes from confusion to anger and fear however, when you break free from it's grasp and leap towards it's face.")
            time.sleep(3)
            print("With all the strength you can muster you wrap your arms around it's throat, strangling it. As it hits at you to get you off you only hold on tighter. Fearful for your life.")
            time.sleep(3)
            print("The giant falls to the ground with a loud thud. Dead.")
            time.sleep(1.5)
            print("CONGRATULATIONS! game completed")
            time.sleep(8)
            exit()
        elif(choice == "hands" and inventory2 != ""):
            print("The giant screams in pain as you fall to the ground with it's disembodied hands. As it lies on the ground in pain you walk up behind it and slit it's throat.")
            time.sleep(3.5)
            print("CONGRATULATIONS! game completed")
            time.sleep(8)
            exit()
        elif(choice == "hands" and inventory2 ==""):
            print("You have no sword to cut youself free.")
            C9()
        else:
            print("That wasn't an option")
            time.sleep(1)
            C9()
    if(choice == "throw"):
        if(inventory2 == "legendary sword"):
            print("The giant catches your sword in it's hands as it soars towards it's head.")
            print("Do you:")
            clear(2)
            print("Throw a <rock> at the sword in it's hands to knock it free.")
            clear(1)
            print("<will> your magic sword to come back to you")
            clear(2)
            choice = input(": ")
            if(choice == "rock"):
                print("The rock knocks the sword clean out of the giant's hands the sword soars through the air and lodges itself in the giant's neck.")
                time.sleep(3)
                print("CONGRATULATIONS! game completed.")
                time.sleep(8)
                exit()
            elif(choice == "will"):
                print("With all the power you can muster you focus entirely on the magic sword. You imagine it being back in your hands.")
                time.sleep(2)
                print("As you imagine it's weight in your hands and it's cold hilt suddenly it appears.")
                time.sleep(2)
                print("With your new found mastery of your sword you will it to fly into the air and kill the giant.")
                time.sleep(2)
                print("With a loud thud the giant falls to the ground throwing a large dust cloud into the air.")
                time.sleep(5)
                print("CONGRATULATIONS! game completed")
                time.sleep(8)
                exit()
            else:
                print("That wasn't one of the options.")
                time.sleep(1.5)
                C9()
        else:
            print("No sword to throw.")
            time.sleep(1.5)
            C9()

#The entire game
print("Best viewed in fullscreen.")
time.sleep(2)
clear(100)
print("What is your name adventurer?  ")
name = input(": ")
clear(2)
print("Choices are written with \"<>\" around them like <choice>.")
time.sleep(2)
skillmenu()
A1()

if(skillpoints>0):
    skillmenu()
