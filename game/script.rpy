# Deklarasikan gambar di bawah line ini, menggunakan pernyataan image.
# cnth. image eileen happy = "eileen_happy.png"

# Deklarasikan karakter yang digunakan di game.
define mc = Character('Arda')
define spk = Character('Speaker')
define s1 = Character('Siswa 1')
define s2 = Character('Siswa 2')
define s3 = Character('Siswa 3')
define s4 = Character('Siswa 4')
define s5 = Character('Siswa 5')
define s6 = Character('Siswa 6')
define s7 = Character('Siswa 7')
define s8 = Character('Siswa 8')
define pg = Character("Pak Guru")
define k2 = Character('Karina')
define l = Character('Lara', color="#c8ffc8")
define k = Character('Kay')
define t = Character('Terry')
define h = Character('Harris')
define b = Character('Benny')

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
    "Di malam hari yang dingin, aku pergi keluar untuk menjernihkan pikiranku."
    "Aku berjalan di pinggir jalan, tepatnya di trotoar."
    "Disamping wanita bersweater ungu, tepatnya di perempatan jalan, aku melihat rambu lalu lintas yang memberikan tanda Stop (lampu merah)."
    "Untuk sementara aku mengabaikan jalanan didepan karena masih jauh sekali, aku mengangkat kepalaku keatas, melihat angkasa dan bertanya-tanya apa yang terbaik untuk adik dan diriku sendiri."

    scene bg hitam
    mc "Aku ingin menjaga adikku yang sakit di rumah, tetapi sekolah yang saat ini aku tempati rasanya terlalu jauh."
    mc "Aku takut..."
    mc "Aku takut adikku hilang dari penglihatanku saat aku pulang dari sekolah..."
    mc "Tapi..."
    mc "Aku ingin melihat sahabat-sahabatku"
    mc "Aku ingin sesekali bermain dengan mereka"
    mc "Hanya mereka lah yang mengerti diriku"
    mc "setidaknya mereka mengerti sedikit sejatinya diriku."
    mc "Apa yang harus kulakukan?"
    mc "Menjauh dari sahabatku demi adikku?"
    mc "Atau aku harus membuat adikku menunggu dirumah sendirian?"
    mc "Kakak macam apa aku? "
    mc "Aku..."
    mc "Aku... Aku... "

    menu:
      "Tidak Pindah Sekolah":
        jump tidak_pindah_sekolah

      "Pindah Sekolah":
        jump pindah_sekolah


    return

label pindah_sekolah:
    mc "Aku ingin meluangkan waktuku dengan adikku. Aku ingin dia punya teman dirumah."
    mc "Aku ingin bermain, tertawa, menonton film bersama adikku dirumah."
    mc "Aku akan mengorbankan apapun untuk adikku, karena dia adalah anggota keluargaku satu-satunya... "
    mc "Aku akan mengorbankan apapun untuk adikku, karena dia adalah anggota keluargaku satu-satunya... dan aku harus menjaga dia layaknya seorang kakak yang sayang pada adiknya."

    return

label tidak_pindah_sekolah:
    "Aku tidak ingin kehilangan sahabat-sahabatku, aku masih membutuhkan mereka."
    "Mereka adalah orang-orang yang bisa menghilangkan awan hitam di dalam pikiranku."
    "Mereka adalah orang-orang yang bisa membuka mataku untuk melihat apa yang ada di dunia ini."
    "Mereka adalah orang-orang yang berusaha untuk meyakinkan diriku bahwa dunia ini masih memiliki harapan."
    "Aku akan mencoba untuk bisa berada didekat sahabat-sahabatku."
    "Maaf adik, mungkin kakakmu ini akan pulang terlambat... lagi"

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
    k "Emangnya lu? Udah tahu ngeliat si Arda, bukannya nyapa dulu kek atau apa dulu kek, malah langsung nyari kelas sendiri."
    k "Tck tck tck, pinter doang, beradab kagak"
    l "!"
    mc "(Uhhh, kena itu kata-katanya si Kay)"
    l "Iya-iya maaf."
    l "Gimana Kay sama MC udah ketemu kelasnya?"
    k "Belum, ini lagi nyari di kelas 12 wehhhhh... Ternyata aku di kelas 12-C"
    l "Berarti beda 2 kasta Lara sama Kay, hehehe"
    k "Sembarangan lu. Lu gimana Arda, dapet kelas berapa?"
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

    s8 "Yo Arda, sehat?"
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
    
    pg "Arda, kemari sebentar!"
    mc "Ah, iya"
    pg "Si Lara sama Kay gak sekelas ya?"
    mc "Iya pak"
    pg "Ohhh, untungnya masih ada si Benny"
    mc "Iya pak, hehe"
    b "Arda, mau pulang bareng sama si Lara, Kay gak?"
    mc "Iya"
    b "Yowes, gue nunggu di depan gerbang"

    "Murid-murid sudah banyak yang keluar dari kelas"
    "Tinggal tesisa aku, dan pak guru"

    pg "Arda, bapak tahu kalau kamu itu hidup sendiri sama adikmu yang sakit. Bapak pengen nanya ke kamu"
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
    b "Arda! Gimana nying main PES, jadi ga?"
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
    l "Ah, dah sampe. Aku duluan Arda, bye "
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
