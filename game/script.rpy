# Deklarasikan gambar di bawah line ini, menggunakan pernyataan image.
# cnth. image eileen happy = "eileen_happy.png"

# Deklarasikan karakter yang digunakan di game.
define mc = Character('Arda', color="#ffffff")
define spk = Character('Speaker', color="#2ecc71")
define s1 = Character('Siswa 1', color="#e74c3c")
define s2 = Character('Siswa 2', color="#e74c3c")
define s3 = Character('Siswa 3', color="#e74c3c")
define s4 = Character('Siswa 4', color="#e74c3c")
define s5 = Character('Siswa 5', color="#e74c3c")
define s6 = Character('Siswa 6', color="#e74c3c")
define s7 = Character('Siswa 7', color="#e74c3c")
define s8 = Character('Siswa 8', color="#e74c3c")
define pg = Character("Pak Guru", color="#2ecc71")
define k2 = Character('Karina', color="#e84393")
define l = Character('Lara', color="#c8ffc8")
define k = Character('Kay', color="#f1c40f")
define t = Character('Terry', color="#3498db")
define h = Character('Harris', color="#3498db")
define b = Character('Benny', color="#3498db")
define tdk = Character ('Telepon', color="#3498db")
define w = Character('Wozky', color="#3498db")

transform slightLeft:
    xalign 0.25
    yalign 1.0

transform slightRight:
    xalign 0.75
    yalign 1.0

transform slightDown:
    xalign 0.5
    yalign 0.0

transform slightRightDown:
    xalign 0.75
    yalign 0.0

transform slightLeftDown:
    xalign 0.25
    yalign 0.0    

transform toLeft0:
    xalign 0.0
    yalign 1.0

transform toRightt0:
    xalign 1.0
    yalign 1.0

# Game dimulai disini.
# Chapter 0
label start:
    scene bg rambu
    "Di malam hari yang dingin, aku pulang berjalan menuju ke rumah orang tuaku setelah meninggalkan stasiun kereta"
    "Aku berjalan tepat di jembatan dengan pemandangan yang menakjubkan di sebelahku."
    "Langit-langit gelap yang indah, udara yang sejuk menyelimuti leherku, suara arus sungai di bawah yang sangat menenangkan, rasanya aku jadi ingin tinggal di jembatan."

    "Bzzzzz Bzzzzz! Bzzzzz Bzzzzz!"

    mc "(Siapa ini? Cuman ada nomornya doang, apa belum aku simpan ya nomornya? Atau mungkin nomor baru Mamah? Karena dia pernah bilang mau ganti provider) jawab telpon"
    mc "Halo?"
    tdk "Halo, apakah ini dengan Arda"
    mc "Nama Arda banyak, buk---"
    tdk "Ardavelt Dovinie"
    mc "Ya, itu saya. Ada apa?"
    tdk "Apakah mood dan mental anda sedang baik saat ini?"
    mc "Ya, tentu saja. Aku akan bertemu dengan keluargaku dan sahabat-sahabatku lagi, mana mungkin mood dan mentalku buruk sekarang"
    tdk "Apakah tidak ada tempat yang membahayakan nyawa?"
    mc "(melihat jembatan dan arus sungai yang begitu kencang) Tidak ada"
    tdk "Ardavelt Dovinier. Sekarang anda berada dimana?"
    mc "Di trotoar (di trotoar jembatan, sebelahku ada sungai. Tidak salahkan?)"
    tdk "Saya mohon, jangan membohongi saya,  arda"
    mc "Saya gak mungkin berbohong, asli kok saya ada di trotoar"
    tdk "Kenapa aku mendengarkan ada suara arus sungai yang kencang? Apakah anda berada di atas jembatan?"
    mc "Tidak, saya berada di atas trotoar"
    tdk "ARDA!"
    mc "Aghh?!"
    mc "...."
    mc "Maaf, saya berada diatas jembatan dan betul ada sungai dibawah jembatan dengan arus yang kencang"
    tdk "Hahhh... Saya mohon maaf atas perilaku saya yang sangat memalukan. Mungkin ini bawaan dari perang Nagini"
    mc "Gak masalah, jadi... ada apa anda menelpon saya?"
    tdk "Bisakah anda berbicara dengan saya sambil berjalan?"
    mc "Bisa (arda mulai berjalan)"
    w "Sebelumnya saya mohon maaf, nama saya Wozasky Montrym, anda bisa memanggil saya dengan wozky Saya adalah rekrutan baru dari rumah sakit Ciruka"
    mc "Wozasky ya, kayak nama orang cyka blyat gitu"
    w "Anda tahu arti dari cyka blyat?"
    mc "Enggak"
    w "Ada baiknya anda jangan menggunakan kata itu sembarangan"
    mc "Kenapa? Kata kasar?"
    w "Iyaaa... benar-benar kata yang sangat jorok dan kasar di waktu yang sama"
    mc "Oh, maaf"
    w "Tidak masalah"
    w " arda sekarang anda berada dimana?"
    mc "Di luar jembatan, sekitar 2 meter jauhnya"

    w "  arda dengarkan ini baik-baik. Pertama-tama aku ingin anda bernafas dengan tenang"
    mc "Kenapa?"
    w "Lakukan saja, lakukan apa yang aku katakan"
    mc "Baiklah, hufffff... hahhhhh... (mengambil nafas dan mengeluarkan)"
    w "Ya, terus lakukan sampai anda merasa tenang"
    mc "hufffff... hahhhhh..."
    w "Bagaimana perasaan anda kali ini"
    mc "Cukup tenang"
    w "Baiklah, apakah ada tempat duduk di dekat sana?"
    mc "Tidak ada, ini di trotoarkan"
    w "Baiklah. Arda kami memiliki pesan untuk anda"
    mc "Pesan? Gak bisa dichat aja?"
    w "Mungkin lebih tepatnya berita. Saya selaku mantan ten--- Saya selaku manusia yang pernah mengalami ini merasa chat bukanlah pilihan yang tepat"
    mc "Ok..."
    w "kedua orang tuamu meninggal karena kecelakan di perempatan Jalan Mori, terjadi pada jam setengah 8 malam hari ini"
    mc "(Jadi... saat aku baru menginjakan tanah di kota ini... Ibu... Ayah... tapi mengapa?) Bagaimana dengan Harris?"
    w "!"
    w "Dia baik-baik saja di rumah, dia tidak ikut dengan kedua orang tuamu"
    mc "Salah siapa ini?"
    w "Pengemudi yang menabrak dari samping. Kedua orang tuamu adalah penumpang dimobil Pak Nadi."
    w "Saat lampu berwarna hijau, mereka jalan, akan tetapi... mobil pickup melewati lampu merah dan melaju sangat cepat dari samping, dan menabrak mereka bertiga. Pak Nadi dengan ajaib selamat, tapi orang tuamu... maaf, tidak bisa kami selamatkan..."
    mc "Terkadang dunia ini tidak adil, tapi kau harus menerimanya dan terus berdiri"
    w "Huh? Arda kita bisa membicarakan ini. Kau bisa berbicara denganku, lepaskanlah semua isi di hatimu. Aku akan mendengarkannya"
    mc "Tidak ada yang bisa dibicarakan lagi, wozky Semuanya terdengar dengan jelas, terimakasih atas kabarnya. Aku ingin bergegas ke rumah untuk bertemu dengan adikku (berjalan menuju jembatan)"
    w "Baiklah. Arda jika ada apa-apa, telepon nomor yang akan aku SMS-kan. Jaga dirimu baik-baik, tentunya dengan adikmu"
    mc "Terimakasih Wozky (menutup panggilan)"
    mc "bangsat..."

    "Tanpa habis pikir, aku pergi ke jembatan yang aku lewati"
    "Aku berjalan"
    "Berjalan..."
    "Terus berjalan..."
    "Bzzzzz Bzzzzz!"
    "Pesan, dari Wozky. Heh"
    "Satu mobil melewatiku, itu mobil pertama yang kulihat di jembatan ini. Bukankah jembatan ini terasa sangat sepi?"
    "Sama seperti jiwa ini..."

    "Kali ini aku berdiri tepat berada di tempat, di mana aku merasakan hawa ini lagi"
    "Sekarang aku melakukaknnya lagi, melihat arus sungainya lagi"
    "Bulannya sangat indah, aku masih berpikir bagaimana bulan bisa memiliki cahaya. "
    "Apakah itu dari matahari? Betapa bodohnya aku, tidak tahu sumber cahaya bulan"
    "Angin malam masih menyelimuti leherku, mukaku, tanganku, dan telapak tanganku. "
    "Angin ini seakan-akan menarikku kebawah... kebawah jembatan ini..."
    "Aku melihatnya, arus sungai itu. Sangat mendukung untuk menyeret manusia dengan cepat hingga hilang dari dunia ini"
    "Bukankah ini bagus. Bahkan alam mendukungku untuk melakukan ini, hahaha"

    mc "Bagaimana rasanya jika aku melompat dari jembatan ini?"

    "Akankah aku terbang seperti pahlawan super? Atau hanya seperti seorang pecundang?"
    "Mungkin hanya akan seperti diriku, seorang pecundang yang ingin menjadi pahlawan super..."
    "Mimpi kecilku yang takkan terwujud...Terlalu banyak bermimpi bisa menyebabkan orang gila"
    "Tapi kenapa aku tidak pernah menjadi orang gila?"
    "Aku menaiki jembatan dan berdiri di belakang penahannya"

    mc "Sambil minum susu enak kayaknya, susu stroberi hangat"
    mc "Woah, susu stroberi hangat. Inovasi terbaru"
    mc "(membuka hp Timer), timer, timer... Nahh, ketemu. Set waktu ke 5 menit, sip"
    mc "(membuka kontak Harris) Harris, gimana kabar kamu, cepet-cepet sehat ya."
    mc ". Oh iya, kakak kayaknya gak bakal bisa ketemu sama kamu lagi."
    mc "Kakak bakal tinggal sendiri di kota Barta, tenang aja kalau masalah uangmah."
    mc "Disana kakak udah dapet kerjaan kok, si Bapak Rahman orangnya baik, kakak kerja jadi orang yang nyatet-nyatet data."
    mc "Kamu tahulah namanya apa, kamukan orang paling pinter di sekolah, hehehe."
    mc "Terus berkembang bro, jangan kayak kakak kamu yang suka males ngapa-ngapain juga, hehehe."
    mc "Yaudah itu aja ya, jangan macem-macem sama diri kamu sendiri. Jaga kesehatan kamu, terus hidup, jangan mati konyol. Goodbye Harrisirta."
    mc "Lope-lope from your handsome bigbro"
    mc"..."
    mc "one “(hapus semua chat kontak Harris, artinya buat si chat diatas reverse)"
    mc "Habs 5 menit gak ada hasil"

    "Kenapa aku melakukan ini?"
    "Kenapa?"
    "tolong..."
    "Tolong..."

    "TOLONGGG!!!"
    "TOLONG AKUUUUU!!! TOLONGGGGG!!!!!"
    "AKU GAK MAU MATI!!! TOLONGGG!!!"
    "KENAPA GAK ADA ORANG YANG MENDENGARKAN AKU?!?!?!"
    "KENAPA?!?!"
    "tolong..."
    "Cukup seorang saja... tolong..."
    
    mc "Nangis? Haha-- hiks..."
    mc "Ibu... Ayah... kenapa..."
    mc "Kenapa disaat aku menginjakan tanah ini, kalian meninggalkanku..."
    mc "Kenapa..."
    mc "Nadi... Pak Nadi anjing... Si bajingan bawa-bawa orang tua gue cuman buat main-main! Gak ada kerjaan lain apa?! Emangnya gak punya temen yang lain selain Ayah sama Ibu gue?!"
    mc "bajingan..."
    mc "one: “Beepbeepbeep, beeppp beeppp, beepbeepbeep, beeppp beeppp"
    mc "(matiin alarm) Udah habis ya..."

    menu :
        "Apa yang akan kamu lakukan ?"

        "Jadilah pahlawan" :
            "Aku sudah muak... aku sudah muak dengan kehidupanku dari TK sampai SMP."
            "Rasanya seperti neraka... Mereka tahu aku biasa menyendiri, tapi kenapa mereka mengolok-olok diriku? Kenapa mereka tidak ingin mengajakku untuk makan di jam istirahat bersama-sama?"
            "Aku juga ingin memiliki teman... terakhir aku berinteraksi dengan ‘teman’, mereka membully-nya... mereka membully-nya, mereka mengancam jika dia berinteraksi denganku, maka dia akan memiliki nasib yang sama sepertiku."
            "Kenapa mereka sangat kejam pada diriku... apa salahku?"
            
            mc "APA SALAHKU?!"
            mc "apa salahku..."
            mc "bagaimana rasanya?"

            "Bagaimana rasanya jika aku jatuh dari ketinggian ini ke arus sungai yang sangat kencang?"
            "Apakah akan sakit seperti jatuh ke aspal? Atau mungkin seperti jatuh ke kolam renang?"
            "Pada momen itu, aku melepaskan peganganku dari besi jembatan itu"
            "Rasanya sangat ringan, tubuhku sangat ringan, rasanya terbang seperti pahlawan super!"
            "Semua beban dan penat di dalam diriku langsung hilang dalam sekejap"
            "Tapi tidak dengan kenangan yang tiba-tiba menyambar pikiranku."
            "Sayangnya, itu tidak akan bekerja, aku sudah merelakan semuanya. Adikku, sahabatku, impianku, semuanya sudah kutinggalkan, aku tidak memiliki rasa penyesalan..."
            "Selamat tinggal dunia..."
            "Halo neraka"
            "Aku tahu kau akan menjumpaiku"
            "Aku menerimanya..."
            


        "Jadilah pecundang":
            "Tubuhku tidak bergerak, entah kenapa aku tidak bisa melompat. Bahkan peganganku sangat kuat, bukan... ada yang memegang tanganku! Akupun berbalik dan melihat ke belakang."
            "Tidak ada siapa-siapa, tapi kenapa... kenapa rasanya seperti ada orang yang menahan tanganku untuk tidak melepaskannya."
            "Kenapa Harris harus menderita? Kenapa dia sangat lemah? Kenapa dia hanya bisa tersenyum? Kenapa... kenapa dia tersenyum? "
            "Bagaimana bisa dia memiliki senyuman itu diwajahnya walaupun dia menderita penyakit Anemia Aplastik selama 4 bulan?!"
            "Kenapa? Kenapa aku ingin meloncati jembatan ini? Kenapa? Kenapa disaat aku menginjakan tanah kota ini, kedua orang tuaku meninggal?"
            "Kenapa? Kenapa rasa bersalah ini terus menghantuiku?"
            "Bahkan ini bukan salahku, aku hanya ingin menemui keluargaku lagi... Kenapa aku tidak bisa sekuat Harris?"

            mc "Aku adalah kakaknya... tapi kenapa... kenapa aku tidak bisa kuat seperti dirinya..."

            "Jika orang tuaku sudah mati, maka tujuan hidupku selain menafkahi mereka disaat tua, apalagi? Apakah ada pilihan yang lain? "
            "Aku bisa hidup karena mereka berdua... mereka adalah salah satu alasan kenapa aku tetap hidup... aku harap mereka tiba-tiba bangun dari kematian..."

            mc "Huhh, hehe, hehehehe..."

            "Hehehehehehehehehe, aneh"
            "Mana mungkin bisa..."
            "Harris!"

            mc "Harris! Maaf maaf maaf maaf maaf maaf maaf, aku lupa aku lupa aku lupa, sialan kenapa aku bisa lupa, kenapa kenapa kenapa kenapa kenapa... kenaaapaa... KENAPA?!"

            "Harris, kali ini hanya kaulah yang kumiliki. Aku akan menjagamu, bahkan aku akan menukarkan nyawaku hanya agar kau bisa bernafas"
            "Kali ini, aku akan menjadi lelaki yang baik-baik, aku akan menjadi kakak yang baik-baik!"

            "Hah, aku juga akan menjadi sahabat yang baik"
            "Tunggu saja nanti"

            jump label_chapter1

# Chapter 1
label chapter1:
    scene bg sekolah
    "Aku berdiri tepat di depan papan pengumuman sekolah yang dimana orang-orang yang tidakku kenal juga berkumpul di satu tempat"
    "untuk mencari namanya masing-masing dan mengetahui di kelas mana mereka akan ditempatkan begitupula dengan diriku"

    mc "(Aku harap aku bisa bersama dengan teman-temanku lagi.)"
    
    show kay biasa with dissolve:
        xzoom 0.5 yzoom 0.5
        xalign 0.5

    k "Yo Arda"
    mc "Ah! Kay. Kirain siapa, nyari kelas juga lu?"
    k "Yaiyalah, lu sendiri dah nemu kelas lu?"
    mc "Belum, ini lagi nyari nih"
    k "Hohhh..."
    mc "...."
    k "...."

    show kay biasa at slightLeftDown
      
    with move

    show lara biasa at slightRight:
      xzoom 0.5 yzoom 0.5
      xalign 0.5
      yalign 0.0
    with dissolve

    show lara biasa at slightRightDown:
      xalign 0.8 
    with move

    l "Kelas 12-A"
    mc "?"
    k "Widih... dah ketemu aja kelas lu, Lar"
    l "Ya karena Lara pinter, Lara nyari dari kelas yang paling awal, tinggi, bagus, yang pastinya diawali dengan huruf A"
    k "Sombong amat"
    l "Hehehe"
    mc "Perasaan dari tadi Lara gak ada di sini deh"
    l "Lara ke sini daritadi sama si Kay, udah itu langsung nyari kelas Lara. Emangnya Arda sama Kay, malah ngobrol doang makanya gak ketemu-ketemu kelasnya"
    mc "Eh... Hehehe..."
    k "Itu namanya teman Lar, kalau berjumpa sama teman itu ada bagusnya menyapa."
    k "Emangnya lu? Udah tahu ngeliat si Arda bukannya nyapa dulu kek atau apa dulu kek, malah langsung nyari kelas sendiri."
    k "Tck tck tck, pinter doang, beradab kagak"
    l "!"
    mc "(Uhhh, kena itu kata-katanya si Kay)"
    l "Iya-iya maaf."
    l "Gimana Kay sama Arda udah ketemu kelasnya?"
    k "Belum, ini lagi nyari di kelas 12 wehhhhh... Ternyata aku di kelas 12-C"
    l "Berarti beda 2 kasta Lara sama Kay, hehehe"
    k "Sembarangan lu. Lu gimana Arda dapet kelas berapa?"
    mc "Masih nyari nih"
    k "..."
    l "..."
    mc "..."
    k "..."
    l "....."
    mc "Ketemu nih, kelas 12-F"
    k "Wihhh, jauh juga lu sama gue kelasnya"
    mc "Gue sekelas sama si Benny pula, hahaha"
    k "Buset dah, enak banget punya temen gak kek gue"
    mc "hahahaha"
    l "...."
    k "Diem mulu Lar, kenapa sih?"
    l "Ah, enggak kok"
    k "Yaudah kita ke kantin dulu yuk sebelum masuk kelas"
    spk "{i}Cek cek, cek 1 2 3. {/i}"
    spk "{i}Bagi siswa-siswi diharapkan masuk ke kelasnya masing-masing bagi yang telah menemukannya. {/i}"
    spk "{i}Untuk yang belum menemukannya, segera temukan kelas kalian. Terimakasih, NGINGGGGGGGGG!!!{/i}"
    s1 "Aduhhh"
    s2 "Asuuuu"
    s1 "HIHHHHHH"
    k "Ait ait ait"
    mc "Ugh"
    l "AAaaaAAa!"
    k "Udah gila, itu speaker belum juga diganti sama sekolah"
    mc "Ya mau gimana lagi, Pak Torresnya ngirit duit sekolah buat nanti event"
    k "Event apaan?"
    mc "Event apa ya? Kayak turnamen gitulah eventnya"
    k "Hohhh, naruhodo!"
    mc "Naruto?"
    k "Naruhodo, artinya mengerti di bahasa Jepang "
    l "Si Kay kan wibu. Dia pernah ngomong kalau waifunya lebih cantik dari dunia nyata, fufufu"
    mc "Hihhh, wibu sekarang lu ya. Ga habis thinking sih, gila gila"
    l "Udah itu aku kasih waifu dia gimana tampilannya di dunia nyata, dia malah ketakutan gara-gara matanya kebesaran, fufufu"
    k "Anzinggg, anzinggg.."
    l "Fufufu, yaudah aku mau ke kelas dulu ya"
    mc "Ohhh... Yaudah, gue mau ke kelas dulu ya"
    k "[sigh] Yoweslah gue juga mau ke kelas, bye"
    l "Dah"
    mc "Bye"

    "Aku pun mulai jalan ke kelasku yang berada di lantai 2, karena semua kelas 12 berada di lantai 2."
    "Setelah mencari kelasku, akhirnya aku menemukannya."
    "Terpampang jelas huruf F di sebelah 12 yang tertempel di tembok, aku pun memasuki kelasnya."

    "Murid lelaki, atau 'teman kelas'-ku mulai berlomba-lomba untuk menempati meja atau kursi dengan tas mereka untuk mencap bahwa mejanya adalahmeja mereka,"
    "seperti kucing yang mengencingi area dan mencap area itu menjadi miliknya."
    "Aku berjalan dan duduk di barisan ke-3. "
    "Awalnya aku ingin duduk di barisan terakhir, cuman sudah penuh, yang tesisa hanyalah barisan ke-3."
    "Akupun duduk di meja barisan ke-3,"
    "Aku tidak mengeluarkan alat tulis karena pada hari pertama sekolah, guru hanya akan menyampaikan info dan memulangkan kelas begitu saja."
    "Aku lupa membawa hpku, jadi yang kulakukan hanyalah menundukan kepala dan menguping perbincangan kelas. Walaupun terdengar tidak baik,"
    "Hanya itulah cara agar menghilangkan kebosananku di kelas (walau sebenarnya aku selalu merasa bosan dimanapun dan kapanpun)"

    s2 "Ihhh, si Kim-Jong-Cin keluar dari BOWOK udah itu ngeluarin singlenya, namanya {b} Yes Yes Yes {/b}"
    s3 "Masa sih?! Aku baru tau kalau---"

    "K-pop... ada cewek yang suka sama J-pop gak ya?"

    s3 "Nihhh, ngocok yang bener tuh jangan pelan-pelan"
    s4 "Kenceng ya ngocoknya?"
    s3 "Yoi, kalo lu mau jadi bartender harus kenceng ngocoknya. Jadi si rasanya itu bisa ke campur lebih cepat"
    "Hahhh, aku kira apaan"
    s5 "Ahhh, gapapa kok. Aku bisa di sebelah, hehehe"
    s4 "Makasih..."

    "Masih rebutan meja?"
    s6 "Busettt, cewek aja lu deketin wahahahaha"
    s7 "Bosen menjomblo si Terry"
    t "Yaiyalah bego, masa gue deketin cowok."
    t "Lagian nih ya, gue cuman bersikap baik ke dia"
    t "Kalau bersikap baik ke cewek dikira kayak yang naksir sama ceweknya, berarti lu itu tidak berpendidikan (tidak berpendidikan, anjayyyyy keren kata-kata gue)"
    s6 "Kalem man, becanda. Oh iya, lu kan suka sama anak kecil wahahahaha"
    s7 "Tolol lu kakakakakak"
    t "Hadehhh, gausah dengerin mereka. Mereka emang punya penyakit jiwa"
    s4 "Ah, ok... haha..."

    "Mereka gak mikir dulu apa sebelum bicara, mana bacotannya ga baik, di depan si cewek pula"

    s8 "Yo Arda sehat?"
    mc "Sehat (Huh, siapa dia?)"
    s8 "Si Lara gak sama lu?"
    mc "Enggak kok, beda kelas"
    s8 "Hohhh, yaudah. Take care Da"
    mc "Ok, you too"
    mc "barusan siapa ?"

    "Tak lama gurupun masuk ke kelas..."
    "Bersama Benny yang sedang loncat kodok..."

    "Hahhh, Benny... Kenapa lu harus telat di hari pertama"

    pg "Ya, sudah. Silahkan cari tempat dudukmu"
    b "Argh... baik pak"
    mc "Oy, sini Ben. Sebelah gue kosong"
    b "Wih, ok ok"
    pg "Halo, nama bapak Nadi. Sebelumnya kita lebih baik memperkenalkan diri dulu karena kita berdatangan dari kelas yang berbeda."
    pg "Hmmm kita mulai dari sana "
    pg "udah itu kesebelah ya? Perkenalkannya cukup nama dan asal kelas saja, mulai"

    s8 "Nama saya----"
    b "{i} oy, lu tau gak kalau cewek yang di belakang ngeliatin lu daritadi {/i}  "
    mc "Huh? (huh?)"
    
    "Heh, entah kenapa hatiku berdebar-debar"
    "Apa maksud dari senyuman itu?"
    "Apakah dia menyukaiku? "
    "Hahaha, aku tau itu hanyalah senyum sapaan. Senyuman itu akan menjadi koleksi di memoriku"

    b "Oy Arda"
    mc "Huh?"
    pg "Ekhm, Arda... darimana asal kelasnya?"
    mc "Ah! Arda dari kelas 11-D"
    pg "Oook, lanjut"
    b "Malah bengong lu disuruh ngenalin diri"
    mc "Sorry sorry, hehehe"
    
    "Pengenalan diri terus berlanjut"
    "Sampai..."

    s4 "Kirana, saya baru pindah kesekolah ini"
    pg "Woah, asal sekolah darimana Kirana?"
    s4 "Ahhh... dari..."
    pg "Ya ?"
    s4 "Dari SMA Barta"
    pg "Ohhh, bagus-bagus. Silahkan selanjutnya"

    "Kirana dari Barta"
    "Barta?"
    "Dari Barta ke Ciruka... Jauh sekali"
    "Setelah pengenalan diri, Pak Nadi memberikan informasi sekolah, mulai dari jadwal pelajaran, pilihan untuk kuliah atau kerja, dan lain-lain."
    "Waktu kelaspun berakhir dengan bunyinya bel"
    "Murid-murid pun keluar dari kelasnya"
    
    pg "Arda kemari sebentar!"
    mc "Ah, iya"
    pg "Si Lara sama Kay gak sekelas ya?"
    mc "Iya pak"
    pg "Ohhh, untungnya masih ada si Benny"
    mc "Iya pak, hehe"
    b "Arda mau pulang bareng sama si Lara, Kay gak?"
    mc "Iya"
    b "Yowes, gue nunggu di depan gerbang"

    "Murid-murid sudah banyak yang keluar dari kelas"
    "Tinggal tesisa aku, dan pak guru"

    pg "Arda bapak tahu kalau kamu itu hidup sendiri sama adikmu yang sakit. Bapak pengen nanya ke kamu"
    pg "mungkin rasanya gak sopan dan jadi bikin situasi aneh"
    mc "...."
    pg "Kamu mau jadi anak bapak gak? Bukan anak murid, tapi anak aja. "
    pg "Sampai disini kamu mengerti ucapan bapak gak? Takutnya gak ngerti"

    "Huh? Baru sekarang? Baru sekarang nanya-nya?"
    "Lu kemarin ada dimana? Kok gue baru ditanyain sekarang?"
    "Adik gue harus menderita dulu, baru lu nolong gitu?"

    pg "Jadi gimana? Kamu juga boleh jawab nanti kok, pertanyaannya emang membuat kamu memilih jalan hidup kamu yang baru sih"
    pg "Jadi kamu---"
    mc "Maaf pak, saya gabisa"
    mc "Saya kasihan sama adik saya yang harus beradaptasi dengan suasana yang baru"
    mc "dan juga rumah yang kami tinggali nanti gak keurus"
    pg "Ahhh, ok ok. Maaf ya kalo sekiranya bikin suasana hati gak enak"
    pg "Jangan lupa kasih tahu adik kamu ya, soalnya ini juga demi dia"
    pg "Siapa tahu dengan jawaban dia kamu berubah pikiran"
    mc "Ah, iya gak apa-apa pak ({i}bangsat...{/i})"
    pg "Kalau begitu bapak pamit duluan ya"
    mc "Ah, iya pak"

    "Dan dia keluar"
    "Manusia yang kelihatannya baru tahu kalau adikku menderita"

    mc "[inhales] Hufffff..... [exhales] haaaaaa...."

    "Akupun membuka pintu kelas dan berjalan menuju gerbang sekolah"

    "Sekolah masih ramai dengan murid-murid dan guru-guru yang berkegiatan, mau itu kegiatan ekskul, membuat tugas, berbincang, dan lain-lain"

    "Aku ingin berkegiatan seperti mereka, tapi mana bisa hahaha....."

    b "Oyyy, Ardaaa"

    "Setidaknya aku memiliki mereka"

    "Aku sangat bersyukur"
    "Aku sangat bersyukur karena masih ada yang ingin berteman dengan orang sepertiku..."
    
    "Kami berjalan di jalanan yang lurus sambil berbincang-bincang mengenai hari kami di kelas masing-masing"

    l "Lara pengen main"
    k "Huh?! Tumben lu mau main!"
    b "Yoi, setauku kamu suka baca novel kan"
    mc "Iya, sama nonton anime"
    k "!"
    l "[blush] AHAHAHA! Iyaya..."
    k "Jadi yang ngejek wibu-wibu tuh ternyata wibu juga ya...."
    l "Huh? Lara mah udah jarang-jarang nonton anime, yang lagi Lara ikutin sekarang cuman AoT season 4 aja wekkk"
    mc "Lah bukannya lu mara---"
    b "Arda Gimana nying main PES, jadi ga?"
    mc "Huh?"
    l "I-iya main PES dirumah kamu, kan pernah ngomong!"
    mc "Kapan?"
    k "I-iya main PES dirumah kamu, kan pernah ngomong!"
    mc "Yoi"
    k "Hohohohoho"
    l "Arghhhhh, iya iya Lara juga wibu.."
    k "Hihihi, gitu dong"
    mc "Mau main PES dirumah gue gak?"
    b "Anying, beneran dong ngajakin"
    l "Harghhhhh, Ardaaa"
    k "Ayolah, gasabar mau bantai-bantai pakai ipul"
    b "Sok banget, yang 5-0 lawan emyu tuh siapa ya? Huh? Huh?"
    l "Hahahaha"
    k "Asu lo, liat aja nanti gue bantai lu pada!"
    mc "[tersenyum]"

    "Akankah senyuman ini berakhir?"
    "Akankah hubungan ini berakhir?"
    "Akankah aku menjadi seorang penyendiri lagi?"
    "Akankah adikku menenangkan diriku lagi?"
    "Aku..."
    "Aku....."
    "Aku ingin yang terbaik untuk adikku dan teman-temanku..."
    "Ah, aku lupa mereka bukan temanku"
    "Mereka adalah sahabat-sahabatku....."

    k "Yosh, gue lewat sini. Bye "
    b "Yoi gue juga, bye "
    mc "Bye"
    l "Bye"

    "Benny dan Kay pun meninggalkan kami berdua di pertigaan jalan"
    "Aku dan Lara pun mulai berjalan lagi di jalan yang sama"

    l "Udah lama kita berempat gak pulang bareng"
    mc "Iya, udah 2 minggu gara-gara liburan"
    l "Iya yah "
    mc "Lar, panas?"
    l "Huh? panas?"
    mc "Itu merah muka kau "
    l "Ah-haha, Aku gak apa-apa kok"
    mc "Huh? Merah gitu kok gak apa-apa"
    l "Ah, iya aku gak kenapa-napa kok"
    mc "Hmmm"
    l "Ah, dah sampe. Aku duluan Arda bye "
    mc "Ah, bye"

    "Rumah kami bersebelahan"

    mc "Hahhhhhh, sampe juga"

    "Rumahku"
    "Rumah adikku"
    "Rumah orang tuaku"
    "Rumah keluargaku"

    mc "Hahhh, pulang"

    "Aku pun membuka sepatu dan langsung pergi ke kamar adikku"

    mc "Yo, ngapain aja cuy"
    h "Biasa, main PS sama belajar"
    mc "Wohhh, sekarang belajar jadi kebiasaan kamu ya?"
    h "Yoi dong"
    mc "Damn, beneran belajar"
    h "Hehehehehe..."
    mc "Obat udah diminum?"
    h "Iya kak, gausah di ingetin lagi napa. Aku juga ngerti kok"
    mc "Ahaha, ok ok"
    h "Sekolah kakak gimana?"
    mc "You knowlah, cuman ngasih info doang"
    h "Hih, ternyata yang gak belajar situ toh. Hahahaha"
    mc "Kampret bisa aja"

    "[flashback]"
    pg "Kamu mau jadi anak bapak gak?"
    pg "Ahhh, ok ok. Maaf ya kalo sekiranya bikin suasana hati gak enak."
    pg "Jangan lupa kasih tahu adik kamu ya, soalnya ini juga demi dia. "
    pg "Siapa tahu dengan jawaban dia kamu berubah pikiran"

    mc "Harris..."
    h "Hm?"
    mc "Enggak jadi"
    h "Hah, gajelas"
    mc "Hehehe, yaudah kakak mau ke kamar ya"
    h "Oke"

    "Akupun jalan ke kamar sebelah, yaitu kamarku sendiri"
    "Melempar tas sekolah ke lantai"
    "Masih memakai baju sekolah"
    "Aku berbaring dikasur"

    mc "Besokk.."
    "Besok mereka akan datang"
    "Mereka sahabat-sahabatku"

    return
