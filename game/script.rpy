# script.rpy

# Define characters
define kakek = Character("Kakek", color="#7f8c8d", image="kakek")
define rana = Character("Rana", color="#3498db", image="rana")
define pedagang = Character("Pedagang", color="#e74c3c", image="pedagang")

transform fit_screen:
    xysize (1920, 1080)

style transparent_frame:
    background None  # Removes the background

# Mulai game
label start:
    scene bg kakek with fade
    show kakek normal at right:
        zoom 0.3
    show rana doomscrolling at left:
        zoom 0.3


    kakek "Rana, kamu kelihatan bosan banget hari ini. Ada apa?"
    show rana neutral1 at left with dissolve:
        zoom 0.3
    rana "Iya, Kek. Lagi nggak tahu mau ngapain."
    kakek "Kebetulan banget, di pusat kota ada acara Nusantara Food Festival. Kamu mau ke sana?"
    show rana think at left with dissolve: 
        zoom 0.3
    rana "Food festival? Ah, kayaknya nggak deh, Kek. Pasti ramai banget."
    kakek "Ayo, cobain saja. Siapa tahu ada makanan enak yang belum pernah kamu coba."
    show rana neutral2 at left with dissolve:
        zoom 0.3
    rana "Hmm, ya sudah deh. Daripada bosan di rumah."

    hide kakek
    hide rana
    scene bg food festival2 with fade

    narrator "rana akhirnya tiba di festival kuliner. Banyak sekali stand makanan dan minuman dari berbagai daerah Nusantara."
    call screen choose_stall

    return

# Screen pemilihan stall
screen choose_stall():
    vbox:
        spacing 20
        text "Pilih stall mana yang ingin dikunjungi:" align (0.5, 0.3)
        
        hbox:
            xpos 0.5
            ypos 0.5
            anchor (0.5,0.3)
            spacing 60
            imagebutton:
                idle "stall/stall_pempek_hover.png"
                hover "stall/stall_pempek_hover.png"
                action Jump("beli_makan")
                at Transform(zoom=(0.4))
            
            imagebutton:
                idle "stall/stall_bir_pletok_hover.png"
                hover "stall/stall_bir_pletok_hover.png"
                action Jump("beli_minum")
                at Transform(zoom=(0.4))

screen pempek_grid():    
    frame :
        style "transparent_frame"
        xpos 0.5
        ypos 0.5
        anchor(0.5,0.5)
        grid 2 2:
            add "pempek/pempek adaan.png":
                zoom 0.2
            add "pempek/pempek kapal selam.png":
                zoom 0.2
            add "pempek/pempek kulit.png":
                zoom 0.2
            add "pempek/pempek lenjer.png":
                zoom 0.2

screen pempek_lenjer():
    frame :
        style "transparent_frame"
        xpos 0.5
        ypos 0.5
        anchor(0.5,0.5)
        add "pempek/pempek lenjer.png":
            zoom 0.3

screen pempek_kulit():
    frame :
        style "transparent_frame"
        xpos 0.5
        ypos 0.5
        anchor(0.5,0.5)
        add "pempek/pempek kulit.png":
            zoom 0.3

screen pempek_kapal_selam():
    frame :
        style "transparent_frame"
        xpos 0.5
        ypos 0.5
        anchor(0.5,0.5)
        add "pempek/pempek kapal selam.png":
            zoom 0.3

screen pempek_adaan():
    frame:
        style "transparent_frame"
        xpos 0.5
        ypos 0.5
        anchor(0.5,0.5)
        add "pempek/pempek adaan.png":
            zoom 0.3

# Label beli makan
label beli_makan:
    scene bg stall pempek with fade
    show rana neutral1 at left:
        zoom 0.3
    show pedagang neutral  at right:
        zoom 0.3

    rana "Pak, pempeknya yang mana yang enak ya?"

    show screen pempek_grid with dissolve
    pedagang "Wah, banyak pilihan, Teh. Ada yang lenjer, kulit, kapal selam, adaan, tekwan, dan masih banyak lagi. Teteh mau yang mana nih? Biar saya jelaskan sedikit tentang masing-masing."
  
    show rana think at left with dissolve:
        zoom 0.3
    rana "Wah, banyak banget ya. Saya bingung nih. Yang membedakan apa sih masing-masing jenis pempek itu?"
    
    hide screen pempek_grid with dissolve

    pedagang "Bedanya ada di bentuk dan isiannya, Teh."

    show screen pempek_lenjer with dissolve
    pedagang "Kalau lenjer itu panjang dan padat,"
    hide screen pempek_lenjer with dissolve

    show screen pempek_kulit with dissolve
    pedagang "kulit itu tipis dan berisi ikan,"
    hide screen pempek_kulit with dissolve

    show screen pempek_kapal_selam with dissolve
    pedagang "Kapal selam itu bulat dengan telur di dalamnya,"
    hide screen pempek_kapal_selam with dissolve

    show screen pempek_adaan with dissolve
    pedagang "Adaan itu seperti bakso ikan terbuat dari tepung kanji."
    hide screen pempek_adaan with dissolve

    pedagang "Nah, kalau Teteh suka yang pedas, ada yang bisa kita tambahkan cabe rawit."

    pedagang "Oh ya, saya punya teka-teki untuk Teteh. Bisa tebak dari mana asal pempek ini?"

    hide rana 
    hide pedagang 
    # Pertanyaan pertama menggunakan menu standar
    menu:
        "Palembang":
            $ result = "benar"
        "Jakarta":
            $ result = "salah"
        "Bandung":
            $ result = "salah"
        "Yogyakarta":
            $ result = "salah"

    if result == "benar":
        show pedagang happy at right:
            zoom 0.3
        show rana happy at left:
            zoom 0.3
        pedagang "Weits, jago banget Teh!"
    else:
        show pedagang wrong at right:
            zoom 0.3
        show rana sad at left:
            zoom 0.3
        rana "Yah, ternyata salah ya Pak?"
        pedagang "Iya, Teh. Aslinya dari Palembang."

    show pedagang neutral at right with dissolve:
        zoom 0.3
    show rana neutral1 at left with dissolve:
        zoom 0.3
    pedagang "Baik, sekarang saya punya pertanyaan tambahan. Kalau Teteh bisa menjawab dengan benar, Teteh akan mendapatkan pempek lenjer 1 gratis!"
    pedagang "Menurutmu, pempek ini awalnya dibuat oleh masyarakat apa dan dijual oleh masyarakat apa?"
    hide rana sad
    hide pedagang wrong

    # Pertanyaan kedua menggunakan menu standar
    menu:
        "Dibikin sama orang Palembang, dijual sama orang Palembang":
            $ result2 = "A"
        "Dibikin sama orang Tiongkok, dijual sama orang Tiongkok":
            $ result2 = "B"
        "Dibikin sama orang Tiongkok, dijual sama orang Palembang":
            $ result2 = "C"
        "Dibikin sama orang Palembang, dijual sama orang Tiongkok":
            $ result2 = "D"

    if result2 == "D":
        show rana happy at left:
            zoom 0.3
        show pedagang happy at right:
            zoom 0.3
        pedagang "Selamat! Teteh mendapatkan 1 bonus pempek lenjer."
        pedagang "Dengan syarat 1 pertanyaan lagi."
        show rana sad at left with dissolve:
            zoom 0.3
        pedagang "Jaman dulu, pedagang yang jualan pempek dipanggilnya apa?"

        hide rana
        hide pedagang
        # Pertanyaan ketiga menggunakan menu standar
        menu:
            "Koko":
                $ result3 = "koko"
            "Apek":
                $ result3 = "apek"

        if result3 == "koko":
            show koko_image at center
            show pedagang wrong at right:
                zoom 0.3
            pedagang "Wah, sayang sekali Teh. Jawabannya salah. Pempek gratisnya nggak jadi ya!"
            hide koko_image
            show rana sad at left:
                zoom 0.3
        elif result3 == "apek":
            show rana happy at left:
                zoom 0.3
            show pedagang happy at right:
                zoom 0.3
            pedagang "Betul sekali! Ini bonus pempek lenjer untuk Teteh."
    else:
        show rana sad at left:
            zoom 0.3
        show pedagang wrong at right:
            zoom 0.3
        pedagang "Salah, Teh. Pempek dulu dibuat sama orang Palembang dan dijual oleh orang Tingkok"

    show rana neutral2 at left with dissolve:
        zoom 0.3
    show pedagang neutral at right with dissolve:
        zoom 0.3
    pedagang "Ngomong-ngomong, Teteh tahu nggak sejarah pempek ini?"
    show rana think at left with dissolve:
        zoom 0.3
    rana "Enggak, Pak. Ceritain dong!"
    pedagang "Jadi, sejarah pempek ini dimulai dari pengaruh budaya Tiongkok di Palembang..."

    # Narasi sejarah pempek
    scene bg_pempek_story with fade
    pedagang "Dulu, pedagang Tiongkok berkeliling menjual makanan ini dan dikenal dengan sebutan 'Apek'."
    pedagang "Mereka membawa pempek yang berbahan dasar ikan tenggiri dan sagu, yang kini jadi ikon kuliner Palembang."
    jump sejarah_pempek

label sejarah_pempek:
    scene bg food festival

    pedagang "Konon, pempek dulunya adalah makanan para kaum bangsawan."
    pedagang "Bahan-bahannya nggak banyak sih. Ada ikan tenggiri, tepung sagu, air es, penyedap rasa, dan garam."

    narrator "Pada pembuatan pempek ikan tenggiri di..."
#menu ini seperti cooking mama (taya Mima untuk lebih jelas)
    menu:
        "Giling":
            jump giling_success
        "Goreng":
            jump goreng_fail
        "Presto":
            jump presto_fail

label presto_fail:
    show ikan goreng:
        zoom 0.3
        xpos 0.5
        ypos 0.5
        anchor(0.5,0.5)
    menu:
        "Goreng":
            jump goreng_fail
    jump sejarah_pempek

label goreng_fail:
    show ikan goreng:
        zoom 0.3
        xpos 0.5
        ypos 0.5
        anchor(0.5,0.5)
    pedagang "Yah, kalo digoreng mah jadi ikan goreng, Teh."
    hide ikan goreng
    jump sejarah_pempek

label giling_success:
    scene bg_dapur_pempek
    pedagang "Benar sekali! Pertama-tama, kita haluskan ikan tenggiri menggunakan blender sampai benar-benar halus."
    pedagang "Setelah itu, kita masukkan ke dalam wadah."
    menu:
        "Tambahkan air":
            show masuk_air
            narrator "Air ditambahkan ke adonan."
    jump bumbu
    # $ step = 0

    # while step < 6:
    #     menu:
    #         "Tambahkan air":
    #             if step == 0:
    #                 narrator "Air ditambahkan ke adonan."
    #                 $ step += 1
    #             else:
    #                 narrator "Langkah ini sudah dilakukan."

    #         "Tambahkan garam":
    #             if step == 1:
    #                 narrator "Garam ditambahkan ke adonan."
    #                 $ step += 1
    #             else:
    #                 narrator "Langkah ini sudah dilakukan atau belum waktunya."

    #         "Tambahkan gula":
    #             if step == 2:
    #                 narrator "Gula ditambahkan ke adonan."
    #                 $ step += 1
    #             else:
    #                 narrator "Langkah ini sudah dilakukan atau belum waktunya."

    #         "Tambahkan penyedap rasa":
    #             if step == 3:
    #                 narrator "Penyedap rasa ditambahkan ke adonan."
    #                 $ step += 1
    #             else:
    #                 narrator "Langkah ini sudah dilakukan atau belum waktunya."

    #         "Pilih tepung":
    #             if step == 4:
    #                 menu:
    #                     "Tepung terigu":
    #                         narrator "Adonan pecah. Pempek gagal dibuat."
    #                         jump presto_success
    #                     "Maizena":
    #                         narrator "Pempek terlalu lembek. Pempek gagal dibuat."
    #                         jump presto_success
    #                     "Tepung sagu":
    #                         narrator "Adonan berhasil diuleni dan dibentuk."
    #                         $ step += 1
    #             else:
    #                 narrator "Belum waktunya memilih tepung."

    #         "Rebus adonan":
    #             if step == 5:
    #                 narrator "Adonan direbus hingga matang."
    #                 $ step += 1
    #             else:
    #                 narrator "Belum waktunya merebus adonan."

    # pedagang "Pempek siap untuk dijual."
    # pedagang "Bagaimana dulu pempek dijual oleh para pedagang?"

    # menu:
    #     "Berjualan keliling":
    #         jump jualan_keliling
    #     "Menjual di ruko sendiri":
    #         show rana_confused
    #         rana "Kayaknya dulu nggak ada ruko deh.."
    #         hide rana_confused
    #         jump sejarah_pempek  #jika pemain memilih opsi selain berjualan keliling, game kembali menanyakan pertanyaan yang sama
    #     "Menjual di festival":
    #         show rana_confused
    #         rana "Kayaknya dulu nggak ada festival deh.."
    #         hide rana_confused
    #         jump sejarah_pempek

label bumbu:
    scene bg_dapur_pempek
    $ bumbu = {"garam": False, "penyedap_rasa": False, "gula": False}

    menu:
        "Garam":
            show masukin_garam
            narrator "Garam ditambahkan ke adonan."
            $ bumbu["garam"] = True
            hide masukin_garam
        "Penyedap Rasa":
            show penyedap rasa:
                zoom 0.3
                xpos 0.5
                ypos 0.5
                anchor(0.5,0.5)
            narrator "Penyedap rasa ditambahkan ke adonan."
            hide penyedap rasa
            $ bumbu["penyedap_rasa"] = True
        "Gula":
            show masukin_gula
            narrator "Gula ditambahkan ke adonan."
            hide masukin_gula
            $ bumbu["gula"] = True
    
    if bumbu["garam"] :
        menu:
            "Penyedap Rasa":
                show penyedap rasa:
                    zoom 0.3
                    xpos 0.5
                    ypos 0.5
                    anchor(0.5,0.5)
                narrator "Penyedap rasa ditambahkan ke adonan."
                hide penyedap rasa
                $ bumbu["penyedap_rasa"] = True
                menu:
                    "Gula":
                        show masukin_gula
                        narrator "Gula ditambahkan ke adonan."
                        hide masukin_gula
                        $ bumbu["gula"] = True
                jump tepung

            "Gula":
                show masukin_gula
                narrator "Gula ditambahkan ke adonan."
                hide masukin_gula
                $ bumbu["gula"] = True
                menu:
                    "Penyedap Rasa":
                        show penyedap rasa
                        narrator "Penyedap rasa ditambahkan ke adonan."
                        hide penyedap rasa
                        $ bumbu["penyedap_rasa"] = True
                jump tepung

    if bumbu["penyedap_rasa"] :
        menu:
            "Garam":
                show masukin_garam
                narrator "Garam ditambahkan ke adonan."
                $ bumbu["garam"] = True
                hide masukin_garam
                menu:
                    "Gula":
                        show masukin_gula
                        narrator "Gula ditambahkan ke adonan."
                        hide masukin_gula
                        $ bumbu["gula"] = True
                jump tepung
            "Gula":
                show masukin_gula
                narrator "Gula ditambahkan ke adonan."
                hide masukin_gula
                $ bumbu["gula"] = True
                menu:
                    "Garam":
                        show masukin_garam
                        narrator "Garam ditambahkan ke adonan."
                        $ bumbu["garam"] = True
                        hide masukin_garam
                jump tepung
    
    if bumbu["gula"] :
        menu:
            "Garam":
                show masukin_garam
                narrator "Garam ditambahkan ke adonan."
                $ bumbu["garam"] = True
                hide masukin_garam
                menu:
                    "Penyedap Rasa":
                        show penyedap rasa
                        narrator "Penyedap rasa ditambahkan ke adonan."
                        hide penyedap rasa
                        $ bumbu["penyedap_rasa"] = True
                jump tepung

            "Penyedap Rasa":
                show penyedap rasa
                narrator "Penyedap rasa ditambahkan ke adonan."
                hide penyedap rasa
                $ bumbu["penyedap_rasa"] = True
                menu:
                    "Garam":
                        show masukin_garam
                        narrator "Garam ditambahkan ke adonan."
                        $ bumbu["garam"] = True
                        hide masukin_garam
                jump tepung

label tepung:
    scene bg_dapur_pempek
    $ answer = False
    while not answer:
        menu:
            "Tepung terigu":
                show tepung terigu:
                    zoom 0.3
                    xpos 0.5
                    ypos 0.5
                    anchor(0.5,0.5)
                narrator "Adonan pecah. Pempek gagal dibuat."
                hide tepung terigu
            "Maizena":
                show tepung mizena:
                    zoom 0.3
                    xpos 0.5
                    ypos 0.5
                    anchor(0.5,0.5)
                narrator "Pempek terlalu lembek. Pempek gagal dibuat."
                hide tepung mizena
            "Tepung sagu":
                show tepung sagu:
                    zoom 0.3
                    xpos 0.5
                    ypos 0.5
                    anchor(0.5,0.5)
                narrator "Adonan berhasil diuleni dan dibentuk."
                hide tepung terigu
                $ answer = True
    show rebus_adonan
    narrator "Adonan direbus hingga matang."
    hide rebus_adonan
    jump jualan_keliling


label jualan_keliling:
    scene bg_pedagang_keliling
    pedagang "Pada zaman dahulu, sekitar abad ke-16, pada masa Sultan Badaruddin II, pempek dijual secara keliling oleh seorang Tiongkok."
    pedagang "Orang-orang biasa memanggilnya dengan sapaan 'Apek'."
    narrator "Pada awalnya, pempek dikenal dengan nama 'kelesan', yang diolah hingga dapat disimpan dalam waktu lama."

    "Setelah rana mendengarkan pemaparan tentang asal usul pempek, rana menyadari bahwa kuliner nusantara merupakan kearifan lokal yang kaya akan sejarah dan harus dilestarikan."
    rana "Wah, aku baru tahu sejarah pempek ternyata menarik banget."
    pedagang "Itulah kenapa kita harus menjaga makanan tradisional seperti ini."

    scene bg_food_festival
    pedagang "Ini pempek gratis untuk Teteh karena sudah benar menjawab pertanyaan dan mendengar cerita sejarahnya."

    return

# Label beli minum (analog dengan pempek)
label beli_minum:
    #on progess by another one

#note: ini aku baru masuki dialog script kasar dan kemungkinan akan banyak sekali error, soalnya ngandelin gpt dengan command doang T-T
#mau minta tolong untuk benerin yang error, sama custom dialog. Sketch rancangan tampilan game dan asset grafis design minta link drivenya ke Mima