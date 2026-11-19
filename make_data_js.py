import json

data_content = """// ==========================================================================
// DATA MODUL PRAKTIKUM MINERALOGI & PETROLOGI
// Program Studi S1 Teknik Pertambangan - Fakultas Teknik UNIKARTA
// Dosen Pengampu: Sundyo, S.T., M.T. | Asisten: Al Disa Eka S. & Amalia Azis
// ==========================================================================

const MODULE_META = {
  courseTitle: "Praktikum Mineralogi dan Petrologi",
  institution: "Program Studi Teknik Pertambangan, Fakultas Teknik",
  university: "Universitas Kutai Kartanegara (UNIKARTA)",
  academicYear: "Semester Ganjil 2025/2026",
  lecturer: "SUNDYO, S.T., M.T.",
  assistants: ["Al Disa Eka Saputri", "Amalia Azis"],
  quote: "Bagi seorang insinyur pertambangan, batuan dan mineral bukan sekadar batu di pinggir jalan; mereka adalah kunci cadangan bijih, stabilitas lereng tambang, dan masa depan industri!",
  stats: {
    totalChapters: 9,
    totalMohs: 10,
    totalCrystalSystems: 7,
    totalFlashcards: 60,
    totalQuizQuestions: 60
  }
};

const CHAPTERS_DATA = [
  {
    id: "tata-tertib",
    number: "00",
    title: "Tata Tertib & Sanksi Laboratorium",
    badge: "Etika & Prosedur",
    icon: "fa-clipboard-check",
    color: "#e11d48",
    overview: "Kewajiban, larangan, dan tingkatan sanksi disiplin praktikan Laboratorium Geologi & Tambang FT-UNIKARTA.",
    lecturerNote: "Disiplin di laboratorium tambang adalah cerminan K3 (Keselamatan dan Kesehatan Kerja) di dunia pertambangan nyata. Kelalaian kecil dapat merusak spesimen langka atau membahayakan rekan kerja!",
    sections: [
      {
        heading: "I. Kewajiban Praktikan (13 Poin Wajib)",
        points: [
          "1. Sudah membayar praktikum dan mengumpulkan bukti pembayaran ke lab.",
          "2. Berpakaian rapi & sopan (DILARANG memakai kaos oblong, bersandal, atau celana sobek).",
          "3. Mengisi Surat Pernyataan Mentaati Tata Tertib Laboratorium.",
          "4. Wajib memiliki Buku Panduan Praktikum resmi.",
          "5. Hadir 10 menit sebelum praktikum dimulai (disiplin waktu tambang).",
          "6. Menandatangani daftar hadir sebelum praktikum dilaksanakan.",
          "7. Jika berhalangan hadir, wajib lapor ke Ka. Lab; ketidakhadiran tanpa izin resmi = DIANGGAP GUGUR.",
          "8. Hanya boleh meninggalkan ruang praktikum atas izin Ka. Lab / Teknisi / Asisten Dosen.",
          "9. Berlaku sopan, bertanggung jawab, berinisiatif, dan kreatif terhadap tugas yang diberikan.",
          "10. Tas dan barang lain yang tidak dibutuhkan diletakkan di loker/tempat yang disediakan.",
          "11. Menjaga kebersihan dan ketertiban laboratorium setiap saat.",
          "12. Mentaati aturan penggunaan alat & bahan. Merusak peralatan akibat kelalaian WAJIB mengganti/memperbaiki sesuai perintah Ka. Lab dalam Berita Acara kejadian.",
          "13. Setelah praktikum selesai, wajib melapor dan mengembalikan seluruh fasilitas lab ke Teknisi dalam keadaan baik."
        ]
      },
      {
        heading: "II. Larangan Keras bagi Praktikan",
        points: [
          "1. DILARANG berada dalam pengaruh minuman keras (alkohol) dan narkoba.",
          "2. DILARANG merokok, mengobrol santai, membuat kegaduhan, ribut, atau mengacau selama praktikum.",
          "3. DILARANG pindah kelompok tanpa persetujuan Ka. Lab.",
          "4. DILARANG melakukan aktivitas lain tanpa izin Ka. Lab, serta DILARANG KERAS membawa fasilitas lab keluar lab tanpa izin tertulis Ka. Lab."
        ]
      },
      {
        heading: "III. Tingkatan Sanksi Disiplin (5 Kriteria)",
        table: {
          headers: ["No", "Jenis Sanksi", "Kriteria Pelanggaran"],
          rows: [
            ["1", "Peringatan secara lisan / teguran", "Kriteria A"],
            ["2", "Peringatan secara tertulis", "Kriteria B"],
            ["3", "Pengurangan Nilai Praktikum", "Kriteria C"],
            ["4", "Tidak Lulus Praktikum", "Kriteria D"],
            ["5", "Dikeluarkan sebagai mahasiswa Jur. Teknik Pertambangan FT-UNIKARTA", "Kriteria E (Pelanggaran berat / pidana)"]
          ]
        }
      }
    ]
  },
  {
    id: "mineralogi-dasar",
    number: "01",
    title: "Mineralogi Dasar & Genesa Mineral",
    badge: "Konsep Dasar",
    icon: "fa-gem",
    color: "#2563eb",
    overview: "Definisi mineral, keteraturan atom, cabang ilmu geologi, dan lingkungan pembentukan (Genesa) mineral di alam.",
    lecturerNote: "Mineral adalah unit pembangun kerak bumi dan bijih tambang. Memahami genesa (asal-usul) mineral memudahkan kita memprediksi zona mineralisasi ekonomis seperti emas hidrotermal atau bauksit residual!",
    sections: [
      {
        heading: "Pengertian Mineralogi & Mineral",
        points: [
          "Mineralogi: Cabang ilmu geologi yang mempelajari secara detail mengenai apa-apa saja yang bersangkutan dengan kristal, klasifikasi mineral logam dan non-logam, pembentuk mineral, serta penamaannya.",
          "Definisi Mineral: Suatu benda padatan yang homogen, terjadi secara alamiah, terbentuk dari bahan anorganik, mempunyai komposisi kimia dan susunan atom tertentu.",
          "Keteraturan Atom: Mineral terbentuk dari atom dan molekul yang tersusun dalam pola teratur berulang 3 dimensi, yang menjadikan mineral memiliki sifat dalam yang teratur.",
          "Kuantitas di Alam: Hingga saat ini telah diketahui lebih dari 2.300 jenis mineral, dan terus bertambah dengan laju penemuan maksimal ~25 mineral per tahun.",
          "Relevansi Tambang: Dalam industri tambang, kita selalu bersentuhan langsung dengan mineral ekonomis (ore) maupun batuan samping (gangue/waste)."
        ]
      },
      {
        heading: "Tiga Lingkungan Utama Pembentukan Mineral",
        points: [
          "1. Magmatik: Terbentuk dari aktivitas magma di dalam bumi, lelehan, erupsi, pneumatolitik, hidrotermal (larutan gas berair panas), dan hot spring (mata air panas). Contoh: Feldspar, Biotit, Amfibol, Piroksen, Olivin, Nefelin, Kuarsa, Gelas, Muskovit.",
          "2. Metamorfosa: Terbentuk melalui proses rekristalisasi dan isokimia pada fase padat akibat tekanan (P) dan temperatur (T). Contoh: Andalusit, Kordierit, Epidot, Garnet, Feldspar, Amfibol, Glaukofan, Grafit, Kianit, Silimanit, Staurolit, Tremolit, Aktinolit, Wolastonit, Mika, Kuarsa.",
          "3. Sedimen: Terbentuk hanya di permukaan bumi melalui proses evaporit (penguapan larutan pekat) dan presipitasi (larutan mengkristal dengan sendirinya). Contoh: Kuarsa, Karbonat, Mineral Lempung, Anhidrit, Glaukonit, Gipsum, Halit (batu garam)."
        ]
      },
      {
        heading: "Proses Keterbentukan (Genesa) Mineral Lainnya",
        points: [
          "• Sublimasi (dari fasa gas fumarola/solfatara)",
          "• Sedimentasi mekanis dan kimiawi",
          "• Evaporasi (pengeringan cekungan tertutup)",
          "• Proses Hidrothermal (sirkulasi fluida panas magmatik)",
          "• Konsentrasi Mekanika dan Residual (placer/endapan letakan)",
          "• Metamorfisme regional / kontak",
          "• Kristalisasi magma (Deret Bowen)",
          "• Oksidasi dan Pengkayaan Supergen (enrichment zona gossan/tembaga)",
          "• Metasomatisme Kontak (skarn pada kontak magma & batugamping)"
        ]
      },
      {
        heading: "Klasifikasi Berdasarkan Peran dalam Batuan",
        points: [
          "• Mineral Primer: Penyusun utama batuan hasil kristalisasi magma (contoh: Hornblenda, Piroksen, Olivin, Plagioklas).",
          "• Mineral Sekunder: Terbentuk akibat perubahan/pelapukan/alterasi dari mineral primer (contoh: Laumontite, Klorit, Serisit, Kaolinit).",
          "• Mineral Aksesoris: Mineral tambahan yang hadir dalam jumlah sangat sedikit (<5%) namun khas (contoh: Zirkon, Apatit, Turmalin)."
        ]
      }
    ]
  },
  {
    id: "sifat-fisik-mineral",
    number: "02",
    title: "Sifat Fisik Mineral & Skala Mohs",
    badge: "Uji Lapangan",
    icon: "fa-microscope",
    color: "#059669",
    overview: "Parameter identifikasi megaskopis mineral: Warna, Kilap, Pecahan, Belahan, Tenacity, Kemagnetan, Berat Jenis, dan Skala Kekerasan Mohs 1-10.",
    lecturerNote: "Di lapangan eksplorasi tambang, Anda tidak selalu membawa laboratorium canggih. Loupe, kuku, uang koin, pisau saku, kikir, dan kawat magnet adalah senjata utama identifikasi mineral!",
    sections: [
      {
        heading: "1. Warna & Cerat (Streak)",
        points: [
          "Warna (Colour): Spektrum cahaya yang dipantulkan mineral. Warna penting untuk membedakan pengotor vs warna asli. Contoh: Azurit selalu biru khas, Epidot berwarna kuning-hijau.",
          "Gores / Cerat (Streak): Warna serbuk mineral saat digoreskan pada pelat porselen putih tidak berglasur. Warna cerat lebih konstan daripada warna permukaan luar (misal: Pirit berwarna kuning emas tetapi ceratnya hitam kehijauan; Hematit berwarna perak/abu-abu tetapi ceratnya cokelat kemerahan)."
        ]
      },
      {
        heading: "2. Kilap (Luster) - 2 Kelompok Besar & 8 Jenis",
        points: [
          "Kilap ditimbulkan pantulan cahaya pada permukaan mineral, berkaitan erat dengan indeks bias (n).",
          "A. Kilap Logam (Metallic Luster): Mineral opaque (kedap cahaya) dengan indeks bias n >= 3, memberi kesan gelap/logam. Contoh: Galena, Native Metal, Sulfit, Pirit.",
          "B. Kilap Non-Logam (Non-Metallic Luster): Memantulkan warna-warna muda/terang. Terdiri atas:",
          "  1. Kilap Kaca (Vitreous): Menyerupai pantulan kaca. Contoh: Kuarsa, Kalsit.",
          "  2. Kilap Intan (Adamantine): Cemerlang berkilau tinggi seperti intan. Contoh: Intan.",
          "  3. Kilap Sutera (Silky): Lembut bergaris sutera pada mineral berserat. Contoh: Asbes, Aktinolit, Gipsum.",
          "  4. Kilap Damar (Resinous): Seperti getah damar atau kekuning-kuningan. Contoh: Spalerit, Sulfonit.",
          "  5. Kilap Mutiara (Pearly): Menyerupai mutiara atau bagian dalam kulit kerang. Contoh: Muskovit, Talk, Dolomit.",
          "  6. Kilap Lemak (Greasy): Memberikan kesan licin seperti lemak atau sabun. Contoh: Serpentinit.",
          "  7. Kilap Tanah (Earthy / Dull): Memberikan kesan kusam seperti lempung/tanah basah. Contoh: Kaolin, Limonit, Bauksit."
        ]
      },
      {
        heading: "3. Pecahan (Fracture) - 5 Tipe",
        points: [
          "Pecahan adalah kenampakan permukaan saat mineral pecah tidak mengikuti bidang belahannya:",
          "1. Pecahan Konkoidal (Conchoidal): Memperlihatkan undulasi/gelombang lengkung seperti bagian luar kulit kerang atau pecahan kaca botol. Contoh: Kuarsa, Kalsedon.",
          "2. Pecahan Serat (Splintery / Fibrous): Menunjukkan kenampakan seperti serat kayu atau daging. Contoh: Serpentinit, Asbes, Augit.",
          "3. Pecahan Tidak Rata (Uneven): Permukaan tidak teratur, kasar bergelombang.",
          "4. Pecahan Runcing (Hackly): Permukaan kasar dengan tonjolan tajam dan runcing.",
          "5. Pecahan Rata (Even): Permukaan pecahan relatif rata dan cukup halus. Contoh: Lempung."
        ]
      },
      {
        heading: "4. Belahan (Cleavage) & Sifat Dalam (Tenacity)",
        points: [
          "Belahan: Kecenderungan mineral pecah melalui bidang kristalografis rata, licin, dan berpasangan.",
          "Tingkat Belahan: Sempurna (mika), Baik (Kalsit, Orthoklas, Gipsum), Jelas / Distinct (Hornblende), Tidak Jelas / Indistinct (Plagioklas), Tidak Sempurna (Apatit, Native Metal), Tidak Tentu / Tanpa Belahan (Kuarsa, Opal).",
          "Arah Belahan: 1 arah (mika), 2 arah (feldspar), 3 arah (kalsit, halit rhombohedral/kubik), 4 arah (fluorit).",
          "Ketahanan / Sifat Dalam (Tenacity):",
          "• Brittle: Rapuh, mudah hancur menjadi bubuk halus saat dipukul.",
          "• Fleksibel: Dapat dibengkokkan tetapi TIDAK kembali ke bentuk semula.",
          "• Elastisitas: Dapat dibengkokkan dan KEMBALI ke bentuk semula saat dilepas (contoh: Muskovit).",
          "• Daktil (Ductile): Dapat dibentuk menjadi kawat panjang (contoh: Tembaga murni).",
          "• Sektil (Sectile): Dapat diiris tipis dengan pisau tanpa hancur.",
          "• Malleable: Dapat ditempa dan digencet menjadi lempengan pipih."
        ]
      },
      {
        heading: "5. Skala Kekerasan Mohs 1-10 & Alat Penguji Lapangan",
        table: {
          headers: ["Skala", "Nama Mineral", "Rumus Kimia Unsur", "Alat Uji Lapangan Setara"],
          rows: [
            ["1", "Talk", "H2Mg3(SiO4)3", "Bisa digores sangat mudah dengan kuku jari"],
            ["2", "Gips", "CaSO4 · 2H2O", "Kuku Jari (Skala 2,5)"],
            ["3", "Kalsit", "CaCO3", "Jarum Baja (Skala 3,0) / Uang Logam (3,5)"],
            ["4", "Fluorit", "CaF2", "Paku Besi (Skala 4,5)"],
            ["5", "Apatit", "Ca5(PO4)3F", "Pisau Baja (Skala 5,5) / Kaca Jendela (5,5 - 6,0)"],
            ["6", "Felspar (Ortoklas)", "K(AlSi3O8)", "Kikir Baja (Skala 6,0 - 7,0)"],
            ["7", "Kwarsa", "SiO2", "Dapat menggores kaca & kikir baja dengan mudah"],
            ["8", "Topaz", "Al2SiO4", "Ampelas Karborundum (Skala 8,0 - 9,0)"],
            ["9", "Korundum", "Al2O3", "Ampelas Intan / Korundum"],
            ["10", "Intan", "C (Karbon murni)", "Mineral terkeras di bumi, hanya digores intan lain"]
          ]
        }
      }
    ]
  },
  {
    id: "sistem-kristal",
    number: "03",
    title: "Bentuk Kristal & 7 Sistem Kristalografi",
    badge: "Kristalografi",
    icon: "fa-cube",
    color: "#7c3aed",
    overview: "Tingkat kesempurnaan kristal (Euhedral, Subhedral, Anhedral) dan 7 sistem kristalografi lengkap dengan rasio sumbu, sudut, dan contoh mineral.",
    lecturerNote: "Sistem kristal adalah geometri atomik 3D yang mendasari bentuk belahan dan kekuatan kompresi batuan. Ingat rumus rasio sumbu dan sudut kristalografinya untuk ujian lisan!",
    sections: [
      {
        heading: "Tingkat Kesempurnaan Bangun Kristal",
        points: [
          "1. Euhedral: Kristal sempurna dengan bidang muka kristal dibatasi oleh bidang kristal itu sendiri secara tegas dan teratur.",
          "2. Subhedral: Kristal sebagian dibatasi bidang sendiri dan sebagian dibatasi oleh bidang kristal mineral di sekitarnya.",
          "3. Anhedral: Kristal tidak sempurna, seluruh permukaannya dibatasi oleh kristal lain karena keterbatasan ruang tumbuh.",
          "Faktor Pembentuk Kesempurnaan: (1) Sifat alamiah fasa cair/gas asal, (2) Ruang/tempat pembentukan yang leluasa, (3) Temperatur dan tekanan saat pembekuan."
        ]
      },
      {
        heading: "Rangkuman 7 Sistem Kristalografi",
        table: {
          headers: ["No", "Sistem Kristal", "Rasio Sumbu (Axial Ratio)", "Sudut Kristalografi", "Contoh Mineral Tambang"],
          rows: [
            ["1", "Isometrik (Reguler/Kubik)", "a = b = c (3 sumbu sama panjang)", "α = β = γ = 90° (saling tegak lurus)", "Emas (Gold), Pirit, Galena, Halit, Fluorit"],
            ["2", "Tetragonal", "a = b ≠ c (sumbu vertikal berbeda)", "α = β = γ = 90° (semua 90°)", "Rutil, Autunit, Pirolusit, Leusit, Skapolit"],
            ["3", "Hexagonal", "a = b = d ≠ c (4 sumbu kristal)", "α = β = 90°, γ = 120° (bidang dasar 120°)", "Kuarsa, Korundum, Hematit, Kalsit, Dolomit, Apatit"],
            ["4", "Trigonal (Rhombohedral)", "a = b = d ≠ c (4 sumbu kristal)", "α = β = 90°, γ = 120°", "Turmalin, Sinabar (Cinabar)"],
            ["5", "Orthorhombik (Rhombis)", "a ≠ b ≠ c (3 sumbu berbeda panjang)", "α = β = γ = 90° (semua saling tegak lurus)", "Stibnit, Krisoberil, Aragonit, Witerit"],
            ["6", "Monoklin", "a ≠ b ≠ c (3 sumbu berbeda panjang)", "α = β = 90° ≠ γ (sudut γ miring/oblique)", "Azurit, Malakit, Kolemanit, Gipsum, Epidot"],
            ["7", "Triklin", "a ≠ b ≠ c (3 sumbu tidak ada yang sama)", "α ≠ β ≠ γ ≠ 90° (ketiga sudut tidak tegak lurus)", "Albit, Anortit, Labradorit, Kaolinit, Mikroklin, Anortoklas"]
          ]
        }
      }
    ]
  },
  {
    id: "silika-nonsilika",
    number: "04",
    title: "Mineral Silika vs Non-Silika",
    badge: "Komposisi Kimia",
    icon: "fa-atom",
    color: "#d97706",
    overview: "Pembagian mineral silikat (Ferromagnesian vs Non-Ferromagnesian), variasi kuarsa, dan 7 kelompok mineral Non-Silika bernilai ekonomis tinggi.",
    lecturerNote: "Bijih tembaga, emas, besi, dan timbal di dunia tambang sebagian besar berasal dari kelompok Non-Silika (Sulfida & Oksida), sedangkan batuan dinding galian tambang umumnya tersusun oleh mineral Silika!",
    sections: [
      {
        heading: "1. Mineral Silika (Silikat)",
        points: [
          "Unsur utama adalah silika (SiO2) hasil pembekuan magma. Membentuk mayoritas batuan beku, sedimen, dan metamorf.",
          "A. Ferromagnesian Silikat: Mengandung ion Besi (Fe) dan/atau Magnesium (Mg). Berwarna GELAP (hijau tua - hitam), Berat Jenis tinggi (3,2 - 3,6). Contoh: Olivin ((Mg,Fe)2SiO4), Piroksen/Augit (CaMgSi2O6), Amfibol/Hornblende (Ca2(Mg,Fe)5(Si,Al)8O22(OH)2), Biotit.",
          "B. Non-Ferromagnesian Silikat: TIDAK mengandung Fe dan Mg. Berwarna TERANG (putih, merah muda, bening), Berat Jenis lebih ringan (rata-rata 2,7). Contoh: Kuarsa (SiO2), Feldspar/Ortoklas (KAlSi3O8), Muskovit (KAl2(AlSi3O10)(OH)2).",
          "Karakteristik Kuarsa: Hanya tersusun dari Si dan O (SiO2) dengan ikatan kovalen 3 dimensi yang sangat kuat. Tidak punya bidang belahan (pecahan konkoidal), sangat keras (Mohs 7), tahan pelapukan.",
          "Variasi Warna Kuarsa: Kuarsa susu (putih), kuarsa asap (abu-abu kehijauan), kuarsa rose (merah muda), ametis (ungu), dan kristal batuan / rock crystal (jernih tanpa warna)."
        ]
      },
      {
        heading: "2. Mineral Non-Silika (7 Kelas Utama)",
        points: [
          "1. Elemen Asli (Native Elements): Unsur murni tanpa ikatan unsur lain. Contoh: Emas (Au), Perak (Ag), Tembaga murni (Cu), Platinum (Pt). Kegunaan: Perhiasan, konduktor elektronik, mata uang.",
          "2. Karbonat (CO3): Mengandung gugus karbon & oksigen. Contoh: Kalsit (CaCO3) dan Dolomit (CaMg(CO3)2). Kegunaan: Bahan baku utama semen portland, fluks peleburan bijih besi.",
          "3. Oksida (O): Ikatan ion oksigen dengan logam positif. Contoh: Hematit (Fe2O3), Magnetit (Fe3O4), Korundum (Al2O3). Kegunaan: Bijih besi primer, refraktori, amplas industri pesawat.",
          "4. Halida (X-): Garam halogen (F, Cl, Br, I) dengan kation Na, K, Ca. Contoh: Fluorit (CaF2), Halit (NaCl), Silvit (KCl). Kegunaan: Bahan kimia, deterjen, fluks peleburan fluorspar.",
          "5. Sulfida (S): Ikatan sulfur dengan logam berharga. Contoh: Galena (PbS - timbal), Kalkosit (Cu2S - tembaga), Pirit (FeS2 - besi). Kegunaan: Sumber logam industri baterai dan elektronik.",
          "6. Sulfat (SO4): Sulfur berikatan dengan oksigen dan logam. Contoh: Gipsum (CaSO4·2H2O), Anhidrit (CaSO4). Kegunaan: Pembuatan sheetrock/plafon gipsum, retarder semen.",
          "7. Fosfat (PO4): Contoh: Apatit (Ca5(PO4)3(OH,F,Cl)). Kegunaan: Pupuk pertanian fosfat."
        ]
      }
    ]
  },
  {
    id: "petrologi-batuan-beku",
    number: "05",
    title: "Petrologi Umum & Batuan Beku",
    badge: "Batuan Beku",
    icon: "fa-fire",
    color: "#dc2626",
    overview: "Genesa batuan beku, intrusif vs ekstrusif, parameter tekstur mikroskopis/makroskopis, dan 4 klasifikasi batuan beku.",
    lecturerNote: "Dalam geoteknik tambang terbuka, batuan beku intrusif seperti Granit atau Diorit umumnya memiliki kuat tekan batuan utuh (UCS) yang sangat tinggi, sangat kokoh untuk lereng tambang tinggi!",
    sections: [
      {
        heading: "Pengertian Petrologi & Batuan",
        points: [
          "Petrologi (Yunani: petra = batu): Ilmu yang membahas proses pembentukan batuan, mencakup struktur, tekstur, komposisi mineral, kandungan fosil, umur, dan evolusinya.",
          "Definisi Batuan: Agregat satu atau beberapa mineral anorganik dan material organik yang terjadi secara alamiah menyusun kerak bumi. Tanah dan bahan lapuk lepas TIDAK termasuk batuan.",
          "3 Golongan Batuan: Batuan Beku (Igneous), Batuan Sedimen, dan Batuan Metamorf.",
          "Batuan Beku (Latin: igneus = api): Batuan hasil pembekuan lelehan silikat pijar (magma). Terbagi menjadi: (1) Intrusif/Plutonik (membeku di dalam bumi, membentuk pluton/dike/sill), dan (2) Ekstrusif/Vulkanik (membeku di permukaan bumi sebagai aliran lava atau endapan piroklastik)."
        ]
      },
      {
        heading: "5 Parameter Tekstur Batuan Beku",
        points: [
          "1. Derajat Kristalisasi: Holokristalin (seluruhnya kristal), Hipokristalin (campuran kristal dan kaca/gelas), Holohyalin (hampir seluruhnya kaca/gelas vulkanik).",
          "2. Ukuran Butir: Faneritik (butiran kasar dapat dilihat mata langsung tanpa mikroskop), Afanitik (butiran sangat halus tidak dapat dibedakan dengan mata).",
          "3. Bentuk Kristal: Euhedral (bidang muka kristal sempurna), Subhedral (bidang kristal kurang sempurna), Anhedral (tidak beraturan).",
          "4. Kombinasi Bentuk Kristal: Panidiomorf/Unidiomorf (didominasi euhedral), Hipidiomorf (didominasi euhedral dan subhedral), Alotriomorf (didominasi anhedral).",
          "5. Keseragaman Ukuran Butir: Equigranular (ukuran butir seragam), Inequigranular (ukuran butir tidak seragam, misal tekstur porfiritik: fenokris di dalam massa dasar)."
        ]
      },
      {
        heading: "4 Klasifikasi Batuan Beku",
        points: [
          "A. Berdasarkan Tempat Terbentuk: Plutonik (jauh di dalam mantel/kerak bumi), Hipabisal (dekat permukaan bumi/retas), Vulkanik (keluar di permukaan bumi).",
          "B. Berdasarkan Warna Mineral: Mineral Mafik (gelap: olivin, piroksen, amfibol, biotit) dan Mineral Felsik (terang: feldspar, muskovit, kuarsa, feldspatoid).",
          "C. Berdasarkan Indeks Warna (Kandungan Mineral Mafik):",
          "  • Leucocratic: mineral mafik < 30%",
          "  • Mesocratic: mineral mafik 30% - 60%",
          "  • Melanocratic: mineral mafik 60% - 90%",
          "  • Hypermelanic: mineral mafik > 90%",
          "D. Berdasarkan Kandungan Kimia (Kadar Silika SiO2):",
          "  • Batuan Beku Asam (Acid): SiO2 > 65%. Contoh: Granit (Plutonik), Riolit (Vulkanik).",
          "  • Batuan Beku Menengah (Intermediate): SiO2 52% - 65%. Contoh: Diorit (Plutonik), Andesit (Vulkanik).",
          "  • Batuan Beku Basa (Basic): SiO2 45% - 52%. Contoh: Gabro (Plutonik), Basalt (Vulkanik).",
          "  • Batuan Beku Ultra Basa (Ultra Basic): SiO2 < 45% (di modul tertera < 30%). Contoh: Peridotit, Dunit."
        ]
      }
    ]
  },
  {
    id: "batuan-sedimen",
    number: "06",
    title: "Batuan Sedimen Klastik & Non-Klastik",
    badge: "Batuan Sedimen",
    icon: "fa-layer-group",
    color: "#0284c7",
    overview: "Proses pengerjaan kembali (reworking), 3 komponen pembentuk, 7 parameter tekstur klastik Wentworth, dan 6 klasifikasi Koesoemadinata (1981).",
    lecturerNote: "Di Kalimantan Timur (lokasi kampus UNIKARTA), batuan sedimen mendominasi cekungan Kutai! Batubara, batupasir kuarsa, dan serpih adalah formasi utama yang wajib dikuasai insinyur tambang batu bara!",
    sections: [
      {
        heading: "Genesa Sedimen Klastik & 3 Komponen Pembentuk",
        points: [
          "Sedimen Klastik: Batuan hasil pengerjaan kembali (reworking) batuan yang telah ada melalui: Pelapukan -> Erosi -> Transportasi (air, angin, es, gravitasi) -> Redeposisi (pengendapan kembali) -> Litifikasi (pembatuan).",
          "3 Komponen Pembentuk Batuan Klastik:",
          "1. Butiran (Grain): Fragmen mineral, fosil, atau pecahan batuan (litik) yang tertransportasi.",
          "2. Masa Dasar (Matrix): Material halus (< 1/16 mm) yang diendapkan bersamaan dengan butiran.",
          "3. Semen (Cement): Material sangat halus pengikat butir dan matriks yang diendapkan belakangan dari larutan kimia (semen karbonat, silika, oksida besi, lempung)."
        ]
      },
      {
        heading: "7 Parameter Tekstur Batuan Sedimen Klastik",
        points: [
          "1. Besar Butir (Grain Size): Mengikuti Skala Wentworth. Menunjukkan energi pengendapan (pelapukan kimia = halus; pelapukan mekanis = kasar).",
          "2. Pemilahan (Sorting): Derajat keseragaman butir: Terpilah sangat baik, baik, sedang, buruk, sangat buruk.",
          "3. Kebundaran (Roundness): Derajat keausan/ketajaman sudut butir akibat abrasi: Sangat menyudut (very angular), Menyudut (angular), Menyudut tanggung (sub-angular), Membundar tanggung (sub-rounded), Membundar (rounded), Sangat membundar (well-rounded).",
          "4. Kemas (Fabric): Orientasi dan kontak antar-butir. Terbagi: Kemas Terbuka (butir mengambang dalam matriks, tidak bersentuhan) dan Kemas Tertutup (butir saling bersentuhan / grain supported).",
          "5. Porositas: Rasio volume pori rongga terhadap volume total batuan (%). Uji tetes air: Baik (air meresap cepat), Sedang, Buruk (air tidak meresap). Jenis: Intergranular, microporosity, dissolution, fracture.",
          "6. Warna Batuan Sedimen: Merefleksikan lingkungan pengendapan. Merah = lingkungan oksidasi terbuka; Hitam/Gelap = lingkungan reduksi tergenang. Dipengaruhi pula oleh mineral dominan (kuarsa = putih), semen (oksida besi = cokelat/merah), selubung (glaukonit = hijau), dan derajat kehalusan butir.",
          "7. Kekompakan: Sifat ketahanan fisik: Dense (sangat padat), Hard (keras padat), Medium hard (agak keras, bisa digores jarum baja), Soft (lunak, mudah tergores), Friable (keras tapi dapat diremas dengan jari tangan), Spongy (berongga)."
        ]
      },
      {
        heading: "6 Golongan Batuan Sedimen (Koesoemadinata, 1981)",
        points: [
          "1. Golongan Detritus Kasar: Diendapkan secara mekanis di lingkungan sungai, danau, atau laut dangkal berenergi tinggi. Contoh: Breksi (fragmen meruncing), Konglomerat (fragmen membundar), Batupasir.",
          "2. Golongan Detritus Halus: Diendapkan di lingkungan air tenang, laut dangkal hingga laut dalam. Contoh: Batu lanau, Serpih (shale), Batu lempung, Napal (marl / nepal).",
          "3. Golongan Karbonat: Terbentuk dari cangkang organisme laut (moluska, algae, foraminifera) di laut litoral-neritik atau pengendapan klastik karbonat di neritik-batial. Contoh: Batugamping, Dolomit.",
          "4. Golongan Silika: Hasil kombinasi pengendapan organik biogenik dan presipitasi kimiawi. Contoh: Rijang (chert), Radiolaria, Tanah Diatom. Keterdapatan terbatas di alam.",
          "5. Golongan Evaporit: Terbentuk akibat penguapan tinggi air laut/danau tertutup dengan konsentrasi garam pekat. Contoh: Gipsum, Anhidrit, Batu Garam (Halit).",
          "6. Golongan Batubara: Terbentuk dari akumulasi material organik tumbuhan rawa purba yang mati dan tertimbun cepat tanpa kontak oksigen bebas (mencegah pembusukan/pelapukan)."
        ]
      }
    ]
  },
  {
    id: "struktur-sedimen",
    number: "07",
    title: "Struktur Batuan Sedimen Lengkap",
    badge: "Struktur Sedimen",
    icon: "fa-water",
    color: "#0d9488",
    overview: "Kelainan perlapisan sedimen akibat energi pengendapan: Singenetik, Epigenetik, dimensi perlapisan, dan 18+ struktur sedimentasi khas wajib hafal.",
    lecturerNote: "Mengenali struktur sedimen seperti cross bedding, flute cast, dan graded bedding memungkinkan kita mengetahui 'top and bottom' (bagian atas dan bawah) lapisan batubara atau lapisan pembawa emas purba!",
    sections: [
      {
        heading: "Klasifikasi Berdasarkan Waktu & Dimensi Perlapisan",
        points: [
          "Struktur Primer (Singenetik): Terbentuk bersamaan dengan proses sedimentasi oleh energi mekanis arus fluida.",
          "Struktur Sekunder (Epigenetik): Terbentuk setelah pengendapan, sebelum atau selama proses diagenesa/pembebanan batuan.",
          "Struktur Organik: Terbentuk oleh aktivitas biologis (moluska, jejak cacing/bioturbasi, terumbu bioherm).",
          "Dimensi Ketebalan Lapisan:",
          "• Laminasi: Tebal perlapisan < 1 cm (energi konstan, suspensi halus).",
          "• Stratum: Tebal perlapisan > 1 cm.",
          "• Beds: Kumpulan dari beberapa lapisan laminasi dan stratum.",
          "• Masif (Massive): Lapisan tanpa struktur internal dengan ketebalan > 120 cm."
        ]
      },
      {
        heading: "18+ Struktur Sedimentasi Khas (Kamus Struktur Tambang)",
        points: [
          "1. Graded Bedding: Lapisan bersusun dengan gradasi ukuran butir vertikal; normal grading = butir kasar di bawah dan menghalus ke arah atas.",
          "2. Cross Lamination & Cross Bedding: Perlapisan silang siur bersudut miring akibat migrasi arus pasir/duna. Cross lamination tebal < 5 cm; Cross bedding tebal > 5 cm.",
          "3. Clastic Imbrication: Fragmen batuan pipih tersusun saling menumpuk (overlapping) miring searah hulu arus pada aliran sungai fluvial berbatu.",
          "4. Primary Current Lineation: Struktur garis-garis sejajar memanjang di dalam batuan pasir oleh arus utama kecepatan tinggi.",
          "5. Fosil Orientation: Kumpulan fosil bercangkang memanjang yang terorientasi searah arah aliran arus sedimentasi.",
          "6. Load Cast: Lekukan tonjolan ke bawah pada batas perlapisan akibat pembebanan massa pasir di atas lapisan lumpur lembek.",
          "7. Flute Cast: Celah terputus berbentuk kantong memanjang (2 - 10 cm) akibat gerusan pusaran air turbulen yang terisi pasir di batuan dasar.",
          "8. Mud Cracks: Retakan bersegi lima pada permukaan lumpur basah yang mengering akibat penyusutan suhu dan penguapan.",
          "9. Tool Marks: Jejak goresan benda/fragmen keras yang terbawa arus menggores lapisan lumpur lunak.",
          "10. Rain Print: Lubang kecil lingkaran atau elips bekas tetesan air hujan pada lapisan lumpur basah yang belum mengeras.",
          "11. Flame Structure: Struktur tonjolan lidah lumpur basah yang mencuat ke atas menembus lapisan batupasir akibat tekanan lateral dan beban.",
          "12. Ball, Pillow / Pseudonodule: Gumpalan batupasir membundar seperti bantal yang amblas ke dalam lapisan serpih lunak di bawahnya.",
          "13. Convolute Bedding: Perlapisan yang meliuk-liuk rumit dengan ketebalan 2 - 25 cm akibat deformasi plastis sebelum litifikasi sempurna.",
          "14. Scours: Jejak gerusan saluran lokal yang terpotong oleh arus sedimentasi berikutnya.",
          "15. Channels: Struktur pengisian saluran/palung purba berkelok-kelok dengan energi erosi tinggi.",
          "16. Dish and Pillow: Struktur berbentuk mangkok dan bantal pasir yang amblas tertekan beban sedimen di atasnya.",
          "17. Low Relief Erosion Surface: Relief erosi bertingkat rendah pada permukaan tubuh sedimen sebelum lapisan baru terendapkan.",
          "18. Syndepositional Fold & Slumps: Lipatan kecil dan luncuran pada batupasir yang terjadi saat lapisan sedimen belum terkonsolidasi sempurna.",
          "19. Hard Ground Mass: Akumulasi sedimen khas padat di dalam massa sedimen lain yang relatif lunak.",
          "20. Biostromes & Bioherm: Biostromes = struktur batugamping terumbu berlapis mendatar; Bioherm = gundukan bukit terumbu gamping organik terbatas."
        ]
      }
    ]
  },
  {
    id: "batuan-metamorf",
    number: "08",
    title: "Batuan Metamorf: Struktur & Tekstur",
    badge: "Batuan Metamorf",
    icon: "fa-mountain",
    color: "#4f46e5",
    overview: "Pengertian metamorfisme fase padat, 4 struktur foliasi, 4 struktur non-foliasi, tekstur kristaloblastik, dan tekstur khusus batuan metamorf.",
    lecturerNote: "Batuan metamorf membentuk batuan dasar (basement) kerak bumi. Memahami apakah batuan itu Foliasi (berlapis planar lemah) atau Non-Foliasi (masif padat) sangat krusial dalam merancang terowongan tambang bawah tanah (underground mining tunnel)!",
    sections: [
      {
        heading: "Pengertian & Genesa Metamorfisme",
        points: [
          "Batuan Metamorf: Batuan yang berasal dari batuan induk (beku, sedimen, atau metamorf sebelumnya) yang mengalami perubahan tekstur dan komposisi mineral pada FASE PADAT akibat perubahan tekanan (P), temperatur (T), atau keduanya.",
          "Bila batuan meleleh sempurna, ia kembali menjadi magma dan saat membeku menjadi batuan beku baru.",
          "Contoh Metamorfisme Klasik: Batu lempung -> Slate (batusabak) -> Filit -> Sekis -> Gneis; Batugamping -> Marmer/Pualam; Batupasir kuarsa -> Kuarsit."
        ]
      },
      {
        heading: "Struktur Foliasi (Kenampakan Planar Berlapis)",
        points: [
          "Terjadi karena penjajaran mineral pipih/prismatik akibat tekanan diferensial terarah:",
          "a. Slaty Cleavage: Berbutir sangat halus (mikrokristalin) dengan bidang belah planar sangat rapat, teratur, dan sejajar. Batuannya: Slate (Batusabak).",
          "b. Phyllitic: Menyerupai slaty cleavage tetapi ukuran kristal rekristalisasi lebih besar, mulai ada pemisahan mineral pipih dan granular, serta memiliki kilap sutera (silky luster). Batuannya: Phyllite (Filit).",
          "c. Schistosic (Sekistosa): Susunan paralel mineral-mineral pipih, prismatik, atau lentikular (umumnya mika/klorit) berukuran butir sedang hingga kasar. Batuannya: Schist (Sekis).",
          "d. Gneissic (Gneissose): Perselingan lapisan penjajaran mineral granular (kuarsa, feldspar) berselang-seling dengan mineral tabular/prismatik gelap (ferromagnesian) yang tidak menerus/terputus-putus. Batuannya: Gneiss (Gneis)."
        ]
      },
      {
        heading: "Struktur Non-Foliasi (Granular / Equidimensional)",
        points: [
          "Terbentuk oleh mineral berbutir seragam tanpa orientasi planar terarah:",
          "a. Hornfelsic / Granulose: Mosaik mineral equidimensional dan equigranular berbentuk poligonal akibat metamorfosa termal kontak. Batuannya: Hornfels (Batu Tanduk).",
          "b. Kataklastik (Cataclastic): Tersusun oleh pecahan/fragmen batuan kasar yang membentuk kenampakan breksiasi akibat tegasan deformasi sesar geser. Batuannya: Cataclasite (Kataklasit).",
          "c. Milonitic (Mylonitic): Penggerusan mekanik hebat, berbutir sangat halus, menunjukkan goresan searah dan belum terjadi rekristalisasi mineral primer. Batuannya: Mylonite (Milonit).",
          "d. Phylonitic (Filonitik): Mirip dengan struktur milonitik tetapi telah mengalami rekristalisasi lanjut dan menampakkan kilap sutera. Batuannya: Phyllonite (Filonit)."
        ]
      },
      {
        heading: "Tekstur Batuan Metamorf (Bentuk Kristal, Mineral & Khusus)",
        points: [
          "1. Tekstur Ketahanan:",
          "• Relict / Palimpsest / Sisa: Masih memperlihatkan sisa tekstur batuan asalnya.",
          "• Kristaloblastik: Tekstur baru hasil proses rekristalisasi metamorfosa (berakhiran -blastik).",
          "2. Tekstur Berdasarkan Ukuran Butir: Fanerit (bisa dilihat kasat mata) & Afanitik (tidak bisa dilihat mata).",
          "3. Tekstur Bentuk Individu Kristal: Idioblastik (mineral euhedral sempurna) & Xenoblastik / Hypidioblastik (mineral anhedral/subhedral).",
          "4. Tekstur Bentuk Mineral:",
          "• Lepidoblastik: Didominasi mineral berbentuk pipih/tabular (seperti mika, klorit).",
          "• Nematoblastik: Didominasi mineral berbentuk prismatik/jarum (seperti amfibol, silimanit).",
          "• Granoblastik: Didominasi mineral butiran granular equidimensional (kuarsa, kalsit), batas sutured (tidak teratur) atau unsutured (teratur).",
          "5. Tekstur Khusus Lainnya:",
          "• Porfiroblastik: Kristal mineral berukuran besar (porfiroblas) berada di dalam massa dasar mineral yang lebih halus.",
          "• Poikiloblastik (Sieve Texture): Porfiroblas besar melingkupi/mengepung kristal-kristal mineral yang lebih kecil seperti saringan.",
          "• Mortar Texture: Fragmen mineral besar dikelilingi oleh massa dasar hancuran kristal dari mineral yang sama akibat penghancuran mekanik (crushing).",
          "• Decussate Texture: Tekstur kristaloblastik polimineralik tanpa orientasi teratur.",
          "• Saccharoidal Texture: Tekstur kenampakan butir menyerupai butiran gula pasir.",
          "• Homeoblastik: Batuan metamorf yang hanya tersusun oleh satu macam tekstur saja."
        ]
      }
    ]
  }
];

const MOHS_SCALE_DRILL = [
  { scale: 1, name: "Talk", formula: "H2Mg3(SiO4)3", tool: "Sangat mudah digores kuku jari", hint: "Mineral terlunak, terasa licin seperti sabun (kilap lemak)" },
  { scale: 2, name: "Gips", formula: "CaSO4 · 2H2O", tool: "Kuku Jari (Skala 2,5)", hint: "Bisa digores oleh kuku jari, bahan baku sheetrock semen" },
  { scale: 3, name: "Kalsit", formula: "CaCO3", tool: "Jarum / Uang Logam (Skala 3,0 - 3,5)", hint: "Reaktif berbuih jika ditetesi HCl 0.1 M, belahan rhombohedral" },
  { scale: 4, name: "Fluorit", formula: "CaF2", tool: "Paku Besi (Skala 4,5)", hint: "Belahan 4 arah oktahedral, sistem isometrik" },
  { scale: 5, name: "Apatit", formula: "Ca5(PO4)3F", tool: "Pisau Baja / Kaca (Skala 5,5)", hint: "Bisa digores pisau baja tajam, sumber pupuk fosfat" },
  { scale: 6, name: "Felspar", formula: "K(AlSi3O8)", tool: "Kikir Baja (Skala 6,0 - 7,0)", hint: "Mineral pembentuk kerak bumi melimpah (Ortoklas/Plagioklas)" },
  { scale: 7, name: "Kwarsa", formula: "SiO2", tool: "Menggores Kaca & Kikir Baja", hint: "Pecahan konkoidal, tanpa belahan, sangat resisten pelapukan" },
  { scale: 8, name: "Topaz", formula: "Al2SiO4", tool: "Ampelas Karborundum (Skala 8,0)", hint: "Batu permata keras, kristal orthorhombik" },
  { scale: 9, name: "Korundum", formula: "Al2O3", tool: "Ampelas Intan / Korundum", hint: "Hanya kalah keras dari intan, batu ruby & safir" },
  { scale: 10, name: "Intan", formula: "C", tool: "Hanya digores intan lain", hint: "Zat padat alami terkeras di bumi, ikatan karbon kovalen tetrahedral" }
];

const FLASHCARDS = [
  {
    id: 1,
    category: "Tata Tertib",
    front: "Kapan praktikan wajib hadir di laboratorium sebelum praktikum dimulai?",
    back: "Hadir 10 menit sebelum praktikum dimulai (Kewajiban no. 5). Menandatangani absensi sebelum mulai."
  },
  {
    id: 2,
    category: "Tata Tertib",
    front: "Apa sanksi untuk kriteria pelanggaran 'E' di Laboratorium FT-UNIKARTA?",
    back: "Dikeluarkan sebagai mahasiswa Jurusan Teknik Pertambangan FT-UNIKARTA (untuk pelanggaran berat / pidana)."
  },
  {
    id: 3,
    category: "Tata Tertib",
    front: "Bagaimana aturan jika praktikan merusak alat laboratorium akibat kelalaian?",
    back: "Praktikan WAJIB mengganti atau memperbaiki sebagaimana perintah Ka. Lab dan dinyatakan dalam Berita Acara kejadian (Poin 12)."
  },
  {
    id: 4,
    category: "Mineralogi Dasar",
    front: "Apa definisi resmi 'Mineral' menurut modul praktikum?",
    back: "Suatu benda padatan homogen, terjadi secara alamiah, terbentuk dari bahan anorganik, mempunyai komposisi kimia dan susunan atom tertentu."
  },
  {
    id: 5,
    category: "Mineralogi Dasar",
    front: "Berapa perkiraan jumlah mineral yang telah diketahui dan laju penemuan per tahunnya?",
    back: "Lebih dari 2.300 mineral telah ditemukan, dan bertambah dengan laju maksimal 25 mineral per tahunnya."
  },
  {
    id: 6,
    category: "Mineralogi Dasar",
    front: "Sebutkan 3 lingkungan utama pembentukan mineral beserta contohnya!",
    back: "1. Magmatik (Feldspar, Olivin, Piroksen, Kuarsa)\\n2. Metamorfosa (Andalusit, Garnet, Kianit, Mika)\\n3. Sedimen (Evaporit & Presipitasi: Gypsum, Halit, Kalsit, Lempung)."
  },
  {
    id: 7,
    category: "Sifat Fisik",
    front: "Apa perbedaan mendasar antara Kilap Logam dan Kilap Non-Logam?",
    back: "Kilap Logam: Mineral opaque dengan indeks bias n >= 3, umumnya berwarna gelap/hitam (Galena, Pirit).\\nKilap Non-Logam: Memantulkan warna muda/terang dengan n < 3 (Kaca, Intan, Sutera, Damar, Mutiara, Lemak, Tanah)."
  },
  {
    id: 8,
    category: "Sifat Fisik",
    front: "Sebutkan contoh mineral dengan Kilap Sutera (Silky) dan Kilap Lemak (Greasy)!",
    back: "Kilap Sutera: Asbes, Aktinolit, Gipsum.\\nKilap Lemak: Serpentinit (kesan seperti sabun saat kena cahaya)."
  },
  {
    id: 9,
    category: "Sifat Fisik",
    front: "Apa yang dimaksud dengan Pecahan Konkoidal dan apa contoh mineralnya?",
    back: "Pecahan yang memperlihatkan gelombang melengkung menyerupai permukaan luar kulit kerang atau botol kaca pecah. Contoh: Kuarsa dan Kalsedon."
  },
  {
    id: 10,
    category: "Sifat Fisik",
    front: "Sebutkan istilah ketahanan mineral (Tenacity): Brittle, Fleksibel, Elastisitas, Daktil, Sektil, Malleable!",
    back: "• Brittle: pecah jadi bubuk\\n• Fleksibel: dibengkokkan tak kembali\\n• Elastisitas: dibengkokkan kembali ke awal\\n• Daktil: dibentuk kawat\\n• Sektil: diiris tipis\\n• Malleable: ditempa dengan palu"
  },
  {
    id: 11,
    category: "Skala Mohs",
    front: "Hafalkan rumus kimia untuk mineral Skala Mohs 1 sampai 5!",
    back: "1. Talk: H2Mg3(SiO4)3\\n2. Gips: CaSO4 · 2H2O\\n3. Kalsit: CaCO3\\n4. Fluorit: CaF2\\n5. Apatit: Ca5(PO4)3F"
  },
  {
    id: 12,
    category: "Skala Mohs",
    front: "Hafalkan rumus kimia untuk mineral Skala Mohs 6 sampai 10!",
    back: "6. Felspar: K(AlSi3O8)\\n7. Kwarsa: SiO2\\n8. Topaz: Al2SiO4\\n9. Korundum: Al2O3\\n10. Intan: C"
  },
  {
    id: 13,
    category: "Skala Mohs",
    front: "Berapa skala kekerasan alat uji lapangan untuk: Kuku Jari, Uang Logam, Pisau Baja, Kaca, dan Kikir Baja?",
    back: "• Kuku Jari = 2,5\\n• Uang Logam = 3,5\\n• Pisau Baja = 5,5\\n• Kaca = 5,5 - 6,0\\n• Kikir Baja = 6,0 - 7,0"
  },
  {
    id: 14,
    category: "Sistem Kristal",
    front: "Jelaskan rasio sumbu kristal (axial ratio) dan sudut kristalografi untuk Sistem Isometrik!",
    back: "Rasio sumbu: a = b = c (3 sumbu sama panjang).\\nSudut kristalografi: α = β = γ = 90° (saling tegak lurus).\\nContoh: Gold, Pirit, Galena, Halit, Fluorit."
  },
  {
    id: 15,
    category: "Sistem Kristal",
    front: "Jelaskan rasio sumbu dan sudut kristalografi untuk Sistem Hexagonal dan Trigonal!",
    back: "Rasio sumbu: a = b = d ≠ c (4 sumbu kristal).\\nSudut kristalografi: α = β = 90°, γ = 120°.\\nContoh Hexagonal: Kuarsa, Korundum, Kalsit.\\nContoh Trigonal: Turmalin, Sinabar."
  },
  {
    id: 16,
    category: "Sistem Kristal",
    front: "Jelaskan perbedaan sudut kristalografi antara Orthorhombik, Monoklin, dan Triklin!",
    back: "Ketiganya memiliki panjang sumbu a ≠ b ≠ c.\\n• Orthorhombik: α = β = γ = 90°\\n• Monoklin: α = β = 90° ≠ γ (γ miring)\\n• Triklin: α ≠ β ≠ γ ≠ 90° (ketiganya tidak saling tegak lurus)"
  },
  {
    id: 17,
    category: "Silika vs Non-Silika",
    front: "Apa ciri pembeda utama mineral silikat Ferromagnesian dan Non-Ferromagnesian?",
    back: "Ferromagnesian: Mengandung Fe & Mg, warna GELAP (hitam/hijau tua), BJ 3,2 - 3,6 (Olivin, Piroksen, Amfibol, Biotit).\\nNon-Ferromagnesian: Tanpa Fe & Mg, warna TERANG, BJ ~2,7 (Kuarsa, Ortoklas, Muskovit)."
  },
  {
    id: 18,
    category: "Silika vs Non-Silika",
    front: "Sebutkan macam-macam variasi warna mineral Kuarsa!",
    back: "Kuarsa susu (putih), kuarsa asap (abu-abu), kuarsa rose (merah muda), ametis (ungu), dan kristal batuan / rock crystal (jernih)."
  },
  {
    id: 19,
    category: "Silika vs Non-Silika",
    front: "Sebutkan 7 kelas mineral Non-Silika beserta satu contoh mineralnya!",
    back: "1. Elemen Asli (Emas - Au)\\n2. Karbonat (Kalsit - CaCO3)\\n3. Oksida (Hematit - Fe2O3)\\n4. Halida (Halit - NaCl / Fluorit - CaF2)\\n5. Sulfida (Galena - PbS / Pirit - FeS2)\\n6. Sulfat (Gipsum - CaSO4·2H2O)\\n7. Fosfat (Apatit)"
  },
  {
    id: 20,
    category: "Petrologi Umum",
    front: "Apa asal kata 'Petrologi' dan definisinya?",
    back: "Berasal dari bahasa Yunani 'petra' yang berarti batu. Petrologi adalah ilmu yang membahas proses pembentukan batuan, mencakup struktur, tekstur, komposisi mineral, kandungan fosil, umur, dan evolusinya."
  },
  {
    id: 21,
    category: "Batuan Beku",
    front: "Apa perbedaan Batuan Beku Intrusif (Plutonik) dan Ekstrusif (Vulkanik)?",
    back: "Intrusif/Plutonik: Magma membeku di bawah tanah sebelum capai permukaan bumi (disebut pluton, pendinginan lambat, butir kasar/faneritik).\\nEkstrusif/Vulkanik: Magma keluar ke permukaan bumi menjadi lava/piroklastik (pendinginan cepat, butir halus/afanitik atau gelas)."
  },
  {
    id: 22,
    category: "Batuan Beku",
    front: "Jelaskan istilah derajat kristalisasi: Holokristalin, Hipokristalin, dan Holohyalin!",
    back: "• Holokristalin: Seluruhnya tersusun oleh kristal.\\n• Hipokristalin: Tersusun oleh campuran kristal dan gelas/kaca vulkanik.\\n• Holohyalin: Hampir seluruhnya tersusun oleh gelas vulkanik."
  },
  {
    id: 23,
    category: "Batuan Beku",
    front: "Sebutkan klasifikasi batuan beku berdasarkan kandungan kimia silika (SiO2)!",
    back: "• Asam (Acid): SiO2 > 65% (Granit, Riolit)\\n• Menengah (Intermediet): SiO2 52% - 65% (Diorit, Andesit)\\n• Basa (Basic): SiO2 45% - 52% (Gabro, Basalt)\\n• Ultra Basa: SiO2 < 45% (di modul tertera < 30%, Peridotit)"
  },
  {
    id: 24,
    category: "Batuan Beku",
    front: "Sebutkan 4 tingkatan batuan beku berdasarkan persentase mineral mafik!",
    back: "1. Leucocratic: mineral mafik < 30%\\n2. Mesocratic: mineral mafik 30% - 60%\\n3. Melanocratic: mineral mafik 60% - 90%\\n4. Hypermelanic: mineral mafik > 90%"
  },
  {
    id: 25,
    category: "Batuan Sedimen",
    front: "Sebutkan 3 komponen pembentuk batuan sedimen klastik!",
    back: "1. Butiran (Grain): fragmen mineral, fosil, atau fragmen batuan (litik).\\n2. Masa Dasar (Matrix): butiran halus (< 1/16 mm) terendap bersamaan.\\n3. Semen (Cement): pengikat butir dan matriks yang diendapkan setelahnya (karbonat, silika, besi, lempung)."
  },
  {
    id: 26,
    category: "Batuan Sedimen",
    front: "Apa arti warna merah dan hitam/gelap pada batuan sedimen?",
    back: "Warna merah: menunjukkan lingkungan OKSIDASI.\\nWarna hitam atau gelap: menunjukkan lingkungan REDUKSI."
  },
  {
    id: 27,
    category: "Batuan Sedimen",
    front: "Sebutkan 6 golongan batuan sedimen menurut R.P. Koesoemadinata (1981)!",
    back: "1. Golongan Detritus Kasar (Breksi, Konglomerat, Batupasir)\\n2. Golongan Detritus Halus (Lanau, Serpih, Lempung, Napal)\\n3. Golongan Karbonat (Batugamping, Dolomit)\\n4. Golongan Silika (Rijang, Radiolaria, Diatom)\\n5. Golongan Evaporit (Gips, Anhidrit, Halit)\\n6. Golongan Batubara (Akumulasi organik rawa tertimbun cepat)"
  },
  {
    id: 28,
    category: "Struktur Sedimen",
    front: "Apa perbedaan ukuran lapisan antara Laminasi, Stratum, dan Masif?",
    back: "• Laminasi: tebal < 1 cm\\n• Stratum: tebal > 1 cm\\n• Beds: kumpulan beberapa laminasi dan stratum\\n• Masif: tidak menampakkan struktur dalam atau ketebalan > 120 cm"
  },
  {
    id: 29,
    category: "Struktur Sedimen",
    front: "Apa perbedaan antara Cross Lamination dan Cross Bedding?",
    back: "Keduanya berbentuk lapisan miring bersilang siur; pembedanya adalah ketebalan:\\n• Cross Lamination: ketebalan < 5 cm\\n• Cross Bedding: ketebalan > 5 cm"
  },
  {
    id: 30,
    category: "Struktur Sedimen",
    front: "Jelaskan struktur sedimen Flute Cast dan Load Cast!",
    back: "• Flute Cast: gerusan arus turbulen berbentuk celah terputus/kantong ukuran 2-10 cm yang terisi pasir di batuan dasar.\\n• Load Cast: lekukan batas perlapisan akibat pembebanan pasir di atas lapisan lumpur lunak."
  },
  {
    id: 31,
    category: "Struktur Sedimen",
    front: "Apa yang dimaksud dengan Flame Structure dan Mud Cracks?",
    back: "• Flame Structure: tonjolan lumpur menyusup ke batupasir menyerupai lidah api akibat tekanan beban dan lateral.\\n• Mud Cracks: retakan-retakan bersegi lima pada permukaan lumpur akibat pengeringan suhu dan pengerutan."
  },
  {
    id: 32,
    category: "Batuan Metamorf",
    front: "Apa definisi Batuan Metamorf?",
    back: "Batuan yang berasal dari batuan induk yang mengalami perubahan tekstur dan komposisi mineral pada FASE PADAT akibat perubahan kondisi fisik tekanan (P) dan temperatur (T)."
  },
  {
    id: 33,
    category: "Batuan Metamorf",
    front: "Sebutkan 4 struktur metamorf Foliasi berurutan dari derajat rendah ke tinggi!",
    back: "1. Slaty Cleavage (Batu sabak / Slate)\\n2. Phyllitic (Filit / Phyllite)\\n3. Schistosic (Sekis / Schist)\\n4. Gneissic (Gneis / Gneiss)"
  },
  {
    id: 34,
    category: "Batuan Metamorf",
    front: "Sebutkan 4 struktur metamorf Non-Foliasi beserta nama batuannya!",
    back: "1. Hornfelsic / Granulose (Batu tanduk / Hornfels)\\n2. Kataklastik (Kataklasit / Cataclasite)\\n3. Milonitik (Milonit / Mylonite)\\n4. Phylonitic (Filonit / Phyllonite)"
  },
  {
    id: 35,
    category: "Batuan Metamorf",
    front: "Jelaskan tekstur metamorf Lepidoblastik, Nematoblastik, dan Granoblastik!",
    back: "• Lepidoblastik: tersusun atas mineral berbentuk pipih/tabular (seperti mika)\\n• Nematoblastik: tersusun atas mineral berbentuk prismatik/jarum (seperti amfibol)\\n• Granoblastik: tersusun atas mineral butiran granular equidimensional (kuarsa, kalsit)"
  },
  {
    id: 36,
    category: "Batuan Metamorf",
    front: "Apa yang dimaksud dengan Tekstur Poikiloblastik (Sieve Texture)?",
    back: "Tekstur porfiroblastik di mana kristal mineral besar (porfiroblas) tampak melingkupi atau mengepung beberapa kristal mineral yang lebih kecil menyerupai saringan."
  },
  {
    id: 37,
    category: "Batuan Metamorf",
    front: "Apa yang dimaksud dengan Tekstur Mortar pada batuan metamorf?",
    back: "Fragmen mineral yang lebih besar berada pada massa dasar material yang berasal dari hancuran kristal yang sama akibat pemecahan mekanik (crushing)."
  },
  {
    id: 38,
    category: "Batuan Metamorf",
    front: "Apa yang dimaksud dengan Tekstur Relict / Palimpsest?",
    back: "Tekstur batuan metamorf yang masih memperlihatkan sisa-sisa tekstur batuan asalnya."
  },
  {
    id: 39,
    category: "Sifat Fisik",
    front: "Apa mineral dengan warna khas biru dan kuning-hijau menurut modul?",
    back: "Azurit (berwarna biru) dan Epidot (berwarna kuning-hijau)."
  },
  {
    id: 40,
    category: "Batuan Sedimen",
    front: "Sebutkan 6 istilah kekompakan batuan sedimen dalam modul!",
    back: "1. Dense (sangat padat)\\n2. Hard (keras dan padat)\\n3. Medium hard (agak keras, bisa digores jarum baja)\\n4. Soft (lunak, mudah tergores)\\n5. Friable (keras tapi dapat diremas dengan tangan)\\n6. Spongy (berongga)"
  }
];

const QUIZ_QUESTIONS = [
  // --- TATA TERTIB & PENDAHULUAN ---
  {
    id: 1,
    chapter: "Tata Tertib",
    question: "Berapa menit sebelum praktikum dimulai praktikan WAJIB hadir di Laboratorium FT-UNIKARTA?",
    options: ["5 menit", "10 menit", "15 menit", "30 menit"],
    answerIndex: 1,
    explanation: "Sesuai Tata Tertib Lab Poin I.5: Peserta praktikum wajib 'Hadir 10 menit sebelum praktikum dimulai'."
  },
  {
    id: 2,
    chapter: "Tata Tertib",
    question: "Sanksi berupa 'Dikeluarkan sebagai mahasiswa Jur. Teknik Pertambangan FT-UNIKARTA' dijatuhkan pada kriteria pelanggaran...",
    options: ["Kriteria A", "Kriteria C", "Kriteria D", "Kriteria E (Pelanggaran berat/pidana)"],
    answerIndex: 3,
    explanation: "Tabel Sanksi Tata Tertib: Kriteria E diperuntukkan bagi pelanggaran berat atau tindak pidana."
  },
  {
    id: 3,
    chapter: "Tata Tertib",
    question: "Jika praktikan merusak peralatan akibat kelalaian, apa kewajiban yang harus dipenuhi?",
    options: [
      "Mendapat pengurangan nilai 50%",
      "Mengganti atau memperbaiki sebagaimana perintah Ka. Lab dalam Berita Acara kejadian",
      "Dikeluarkan langsung dari kelompok",
      "Cukup meminta maaf secara lisan kepada teknisi"
    ],
    answerIndex: 1,
    explanation: "Poin I.12: Merusak peralatan akibat kelalaian, peserta wajib mengganti, memperbaiki dan sebagainya sebagaimana perintah Ka.Lab dan dinyatakan dalam Berita Acara kejadian."
  },
  // --- MINERALOGI DASAR ---
  {
    id: 4,
    chapter: "Mineralogi Dasar",
    question: "Menurut definisi dalam modul praktikum, manakah pernyataan yang BENAR mengenai mineral?",
    options: [
      "Benda padat heterogen yang dibuat di pabrik",
      "Suatu zat cair anorganik yang mengalami pembekuan di permukaan",
      "Benda padatan homogen, terjadi secara alamiah, dari bahan anorganik, memiliki komposisi kimia dan susunan atom tertentu",
      "Segala agregat tanah dan bahan lepas hasil pelapukan mekanis"
    ],
    answerIndex: 2,
    explanation: "Modul Halaman 3 & 15: 'Mineral adalah suatu benda padatan yang homogen, terjadi secara alamiah, terbentuk dari bahan anorganik, mempunyai komposisi kimia dan susunan atom tertentu.'"
  },
  {
    id: 5,
    chapter: "Mineralogi Dasar",
    question: "Berapa jumlah jenis mineral yang telah diketahui hingga sekarang dan kecepatan pertambahan maksimalnya per tahun?",
    options: [
      "Lebih dari 10.000 jenis, bertambah 100 per tahun",
      "Lebih dari 2.300 jenis, bertambah maksimal 25 mineral per tahun",
      "Sekitar 500 jenis, bertambah 5 per tahun",
      "Lebih dari 50.000 jenis, bertambah 250 per tahun"
    ],
    answerIndex: 1,
    explanation: "Modul Halaman 15: Telah diketahui bahwa ada lebih dari 2.300 mineral, dan setiap tahunnya bertambah dengan kecepatan maksimal 25 mineral per tahunnya."
  },
  {
    id: 6,
    chapter: "Mineralogi Dasar",
    question: "Manakah contoh kelompok mineral yang terbentuk melalui lingkungan SEDIMEN (evaporit dan presipitasi)?",
    options: [
      "Feldspar, biotit, olivin",
      "Andalusit, kordierit, garnet, kianit",
      "Kuarsa, karbonat, mineral lempung, anhidrit, gypsum, halit",
      "Nepelin, piroksen, gelas"
    ],
    answerIndex: 2,
    explanation: "Modul Halaman 4: Lingkungan sedimen mencakup evaporit dan presipitasi, contohnya: kuarsa, karbonat, mineral lempung, anhidrit, glaukonit, gypsum, halit."
  },
  {
    id: 7,
    chapter: "Mineralogi Dasar",
    question: "Mineral yang terbentuk akibat proses perubahan pelapukan atau sedimentasi (seperti Laumontite) diklasifikasikan sebagai...",
    options: ["Mineral Primer", "Mineral Sekunder", "Mineral Aksesoris", "Mineral Felsik"],
    answerIndex: 1,
    explanation: "Modul Halaman 17: Mineral Sekunder terbentuk akibat perubahan (alterasi/sedimentasi/pelapukan), contohnya Laumontite."
  },
  // --- SIFAT FISIK MINERAL ---
  {
    id: 8,
    chapter: "Sifat Fisik",
    question: "Bila terkena cahaya, Serpentinit memberikan kesan seperti sabun atau minyak pelumas. Jenis kilap apakah ini?",
    options: ["Kilap Kaca", "Kilap Sutera", "Kilap Lemak (Greasy Luster)", "Kilap Tanah"],
    answerIndex: 2,
    explanation: "Modul Halaman 5-6: Kilap Lemak (Greasy Luster) memberikan kesan seperti sabun/lemak bila terkena cahaya. Contoh: Serpentinit."
  },
  {
    id: 9,
    chapter: "Sifat Fisik",
    question: "Mineral yang memiliki kenampakan Kilap Sutera (Silky Luster) umumnya ditemukan pada mineral berserat, contohnya adalah...",
    options: ["Kuarsa dan Kalsit", "Asbes, Aktinolit, dan Gipsum", "Galena dan Pirit", "Kaolin dan Limonit"],
    answerIndex: 1,
    explanation: "Modul Halaman 5: Kilap Sutera terdapat pada mineral yang berserat, contoh: Asbes, Aktinolit, Gipsum."
  },
  {
    id: 10,
    chapter: "Sifat Fisik",
    question: "Pecahan yang memperlihatkan gelombang melengkung seperti kenampakan bagian luar kulit kerang atau botol pecah disebut...",
    options: ["Pecahan Runcing", "Pecahan Serat", "Pecahan Konkoidal", "Pecahan Rata"],
    answerIndex: 2,
    explanation: "Modul Halaman 6: Pecahan Konkoidal memperlihatkan gelombang seperti kenampakan bagian luar kulit kerang atau botol dipecah. Contoh: Kuarsa, Kalsedon."
  },
  {
    id: 11,
    chapter: "Sifat Fisik",
    question: "Sifat ketahanan (tenacity) mineral yang dapat diiris setipis-tipisnya menggunakan pisau disebut...",
    options: ["Brittle", "Sektil (Sectile)", "Daktil (Ductile)", "Malleable"],
    answerIndex: 1,
    explanation: "Modul Halaman 15: 'Sektil : Mineral yang bisa diiris setipis-tipisnya'."
  },
  {
    id: 12,
    chapter: "Sifat Fisik",
    question: "Mineral yang jika dibengkokkan dapat KEMBALI ke bentuk awalnya disebut memiliki sifat...",
    options: ["Fleksibel", "Elastisitas", "Brittle", "Daktil"],
    answerIndex: 1,
    explanation: "Modul Halaman 15: Elastisitas adalah mineral yang jika dibengkokkan kembali ke bentuk awal (berbeda dengan fleksibel yang tidak kembali)."
  },
  // --- SKALA MOHS & FORMULA ---
  {
    id: 13,
    chapter: "Skala Mohs",
    question: "Apakah rumus kimia untuk mineral Fluorite (Kekerasan Mohs 4)?",
    options: ["CaCO3", "CaF2", "CaSO4 · 2H2O", "Ca5(PO4)3F"],
    answerIndex: 1,
    explanation: "Modul Halaman 16 (Tabel Skala Mohs): Fluorit bernilai kekerasan 4 dengan rumus CaF2."
  },
  {
    id: 14,
    chapter: "Skala Mohs",
    question: "Apakah rumus kimia untuk mineral Apatit (Kekerasan Mohs 5)?",
    options: ["Al2SiO4", "K(AlSi3O8)", "Ca5(PO4)3F", "H2Mg3(SiO4)3"],
    answerIndex: 2,
    explanation: "Modul Halaman 16: Apatit bernilai kekerasan 5 dengan rumus unsur Ca5(PO4)3F."
  },
  {
    id: 15,
    chapter: "Skala Mohs",
    question: "Berapakah nilai kekerasan lapangan untuk kikir baja (steel file)?",
    options: ["2,5", "3,5", "5,5", "6,0 - 7,0"],
    answerIndex: 3,
    explanation: "Modul Halaman 9: Kikir Baja memiliki nilai kekerasan relatif 6,0 - 7,0."
  },
  {
    id: 16,
    chapter: "Skala Mohs",
    question: "Sebuah mineral dapat digores oleh pisau baja (5,5) namun dapat menggores uang logam (3,5). Manakah mineral yang mungkin dari Skala Mohs?",
    options: ["Talk (1)", "Gips (2)", "Fluorit (4)", "Kwarsa (7)"],
    answerIndex: 2,
    explanation: "Fluorit memiliki skala kekerasan Mohs 4 (berada di antara 3,5 dan 5,5)."
  },
  {
    id: 17,
    chapter: "Skala Mohs",
    question: "Rumus kimia dari mineral Talk (kekerasan 1) menurut tabel modul adalah...",
    options: ["H2Mg3(SiO4)3", "Mg3Si4O10(OH)2", "Al2O3", "SiO2"],
    answerIndex: 0,
    explanation: "Modul Halaman 16 tertulis secara spesifik: Talk = H2Mg3(SiO4)3."
  },
  // --- SISTEM KRISTAL ---
  {
    id: 18,
    chapter: "Sistem Kristal",
    question: "Sistem kristal dengan axial ratio a = b = c dan sudut kristalografi α = β = γ = 90° adalah...",
    options: ["Sistem Tetragonal", "Sistem Isometrik (Kubik)", "Sistem Orthorhombik", "Sistem Triklin"],
    answerIndex: 1,
    explanation: "Modul Halaman 11: Sistem Isometrik memiliki 3 sumbu yang sama panjang (a = b = c) dan saling tegak lurus (α = β = γ = 90°)."
  },
  {
    id: 19,
    chapter: "Sistem Kristal",
    question: "Sistem kristal Tetragonal memiliki parameter sumbu dan sudut yaitu...",
    options: [
      "a = b = c ; α = β = γ = 90°",
      "a = b ≠ c ; α = β = γ = 90°",
      "a ≠ b ≠ c ; α = β = γ = 90°",
      "a = b = d ≠ c ; α = β = 90°, γ = 120°"
    ],
    answerIndex: 1,
    explanation: "Modul Halaman 11: Sistem Tetragonal memiliki axial ratio a = b ≠ c dan sudut α = β = γ = 90°."
  },
  {
    id: 20,
    chapter: "Sistem Kristal",
    question: "Mineral Tourmaline dan Cinnabar (Sinabar) termasuk ke dalam sistem kristal...",
    options: ["Sistem Hexagonal", "Sistem Trigonal", "Sistem Monoklin", "Sistem Orthorhombik"],
    answerIndex: 1,
    explanation: "Modul Halaman 12: Contoh mineral dengan sistem kristal Trigonal adalah tourmaline dan cinabar."
  },
  {
    id: 21,
    chapter: "Sistem Kristal",
    question: "Sistem kristal Monoklin dicirikan oleh...",
    options: [
      "a ≠ b ≠ c dan α = β = 90° ≠ γ",
      "a = b = c dan α = β = γ = 90°",
      "a ≠ b ≠ c dan α ≠ β ≠ γ ≠ 90°",
      "a = b ≠ c dan α = β = γ = 90°"
    ],
    answerIndex: 0,
    explanation: "Modul Halaman 13: Monoklin memiliki sumbu a ≠ b ≠ c dan sudut α = β = 90° ≠ γ (sudut γ miring/tidak tegak lurus)."
  },
  {
    id: 22,
    chapter: "Sistem Kristal",
    question: "Sistem kristal Triklin dicirikan oleh...",
    options: [
      "Ketiga sumbunya sama panjang",
      "Ketiga sudutnya membentuk 90 derajat",
      "a ≠ b ≠ c dan α ≠ β ≠ γ ≠ 90° (ketiga sumbu berbeda dan ketiga sudut tidak tegak lurus)",
      "Memiliki 4 sumbu kristalografi"
    ],
    answerIndex: 2,
    explanation: "Modul Halaman 14: Triklin memiliki sumbu a ≠ b ≠ c dan sudut α ≠ β ≠ γ ≠ 90°."
  },
  {
    id: 23,
    chapter: "Sistem Kristal",
    question: "Kristal yang dibatasi sebagian oleh bidang permukaannya sendiri dan sebagian oleh bidang kristal sekitarnya disebut...",
    options: ["Euhedral", "Subhedral", "Anhedral", "Idioblastik"],
    answerIndex: 1,
    explanation: "Modul Halaman 10 & 42: Subhedral adalah bentuk kristal di antara euhedral dan anhedral di mana dibatasi sebagian oleh bidang sendiri dan sebagian oleh sekitarnya."
  },
  // --- MINERAL SILIKA & NON-SILIKA ---
  {
    id: 24,
    chapter: "Silika vs Non-Silika",
    question: "Mineral silikat Ferromagnesian dicirikan oleh ciri-ciri fisik berikut, KECUALI...",
    options: [
      "Mengandung ion besi (Fe) dan/atau magnesium (Mg)",
      "Berwarna gelap",
      "Mempunyai berat jenis antara 3,2 sampai 3,6",
      "Berwarna terang dan mempunyai berat jenis rata-rata 2,7"
    ],
    answerIndex: 3,
    explanation: "Modul Halaman 18: Warna terang dengan berat jenis rata-rata 2,7 adalah ciri khas Non-Ferromagnesian, bukan Ferromagnesian."
  },
  {
    id: 25,
    chapter: "Silika vs Non-Silika",
    question: "Manakah di bawah ini yang merupakan contoh mineral silikat Ferromagnesian?",
    options: ["Kuarsa (SiO2)", "Muskovit", "Olivin ((Mg,Fe)2SiO4)", "Ortoklas"],
    answerIndex: 2,
    explanation: "Modul Halaman 18-19: Olivin, Piroksen, Amfibol, dan Biotit adalah mineral silikat ferromagnesian yang kaya Fe dan Mg."
  },
  {
    id: 26,
    chapter: "Silika vs Non-Silika",
    question: "Mengapa mineral kuarsa tidak memiliki bidang belahan dan sangat resistan terhadap pelapukan?",
    options: [
      "Karena memiliki banyak rongga gas",
      "Karena struktur kristalnya membentuk jaringan 3 dimensi lengkap antara ion oksigen dan silikon dengan ikatan kovalen yang kuat",
      "Karena mengandung ion logam Fe yang padat",
      "Karena terbentuk dari sublimasi gas belerang murni"
    ],
    answerIndex: 1,
    explanation: "Modul Halaman 18: Struktur kristal kuarsa membentuk jaringan tiga dimensi lengkap antara ion oksigen di sekitar silikon sehingga membentuk ikatan kuat yang tidak memiliki bidang belahan."
  },
  {
    id: 27,
    chapter: "Silika vs Non-Silika",
    question: "Mineral Galena (PbS) dan Pirit (FeS2) diklasifikasikan ke dalam kelompok mineral Non-Silika...",
    options: ["Karbonat", "Oksida", "Sulfida", "Halida"],
    answerIndex: 2,
    explanation: "Modul Halaman 20: Sulfida mengandung belerang (Sulfur) dikombinasikan dengan logam, contohnya Galena (PbS) dan Pirit (FeS2)."
  },
  // --- PETROLOGI UMUM & BATUAN BEKU ---
  {
    id: 28,
    chapter: "Petrologi & Batuan Beku",
    question: "Apakah kata asal dari 'Petrologi' dan apa artinya dalam bahasa Yunani?",
    options: ["Petros = api", "Petra = batu", "Lithos = tanah", "Geo = bumi"],
    answerIndex: 1,
    explanation: "Modul Halaman 3 & 21: Kata petrologi berasal dari kata Bahasa Yunani 'petra' yang memiliki arti 'batu'."
  },
  {
    id: 29,
    chapter: "Petrologi & Batuan Beku",
    question: "Mengapa tanah dan bahan lepas hasil pelapukan mekanis/kimiawi TIDAK dimasukkan dalam definisi batuan?",
    options: [
      "Karena berwarna cokelat",
      "Karena tidak terjadi secara alamiah",
      "Karena merupakan bahan lepas yang belum mengalami litifikasi menjadi massa padat penyusun kulit bumi",
      "Karena tanah hanya mengandung bahan organik murni"
    ],
    answerIndex: 2,
    explanation: "Modul Halaman 21: 'Tanah dan bahan lepas lainnya yang merupakan hasil pelapukan kimia maupun mekanis serta proses erosi batuan tidak termasuk dalam batuan.'"
  },
  {
    id: 30,
    chapter: "Petrologi & Batuan Beku",
    question: "Batuan beku yang hampir seluruhnya tersusun oleh kristal disebut memiliki tekstur tingkat kristalisasi...",
    options: ["Holokristalin", "Hipokristalin", "Holohyalin", "Afanitik"],
    answerIndex: 0,
    explanation: "Modul Halaman 22: Holokristalin adalah batuan beku yang hampir seluruhnya disusun oleh kristal."
  },
  {
    id: 31,
    chapter: "Petrologi & Batuan Beku",
    question: "Batuan beku yang hampir seluruhnya tersusun oleh mineral-mineral berukuran kasar yang dapat dilihat kasat mata disebut bertekstur...",
    options: ["Faneritik (Phaneritic)", "Afanitik (Aphanitic)", "Equigranular", "Allotriomorf"],
    answerIndex: 0,
    explanation: "Modul Halaman 22: Phaneritic adalah batuan beku yang hampir seluruhnya tersusun oleh mineral-mineral yang berukuran kasar."
  },
  {
    id: 32,
    chapter: "Petrologi & Batuan Beku",
    question: "Batuan beku dengan kandungan mineral mafik antara 30% sampai 60% diklasifikasikan sebagai...",
    options: ["Leucocratic rock", "Mesocratic rock", "Melanocratic rock", "Hypermelanic rock"],
    answerIndex: 1,
    explanation: "Modul Halaman 23: Mesocratic rock memiliki kandungan mineral mafik 30% - 60%."
  },
  {
    id: 33,
    chapter: "Petrologi & Batuan Beku",
    question: "Berdasarkan kandungan silika (SiO2), batuan beku ASAM (acid) memiliki kandungan SiO2 sebesar...",
    options: ["< 45%", "45% - 52%", "52% - 65%", "> 65%"],
    answerIndex: 3,
    explanation: "Modul Halaman 23: Batuan beku asam memiliki kandungan SiO2 > 65% (Contoh: Granit, Riolit)."
  },
  {
    id: 34,
    chapter: "Petrologi & Batuan Beku",
    question: "Manakah pasangan batuan beku plutonik dan ekstrusif yang berkomposisi MENENGAH (intermediet)?",
    options: [
      "Granit dan Riolit",
      "Diorit dan Andesit",
      "Gabro dan Basalt",
      "Peridotit dan Komatiit"
    ],
    answerIndex: 1,
    explanation: "Modul Halaman 23: Batuan beku menengah (intermediet) memiliki SiO2 52% - 65%, contohnya Diorit dan Andesit."
  },
  // --- BATUAN SEDIMEN ---
  {
    id: 35,
    chapter: "Batuan Sedimen",
    question: "Tiga komponen utama penyusun batuan sedimen klastik adalah...",
    options: [
      "Kuarsa, feldspar, mika",
      "Butiran (grain), masa dasar (matrix), dan semen (cement)",
      "Lempung, pasir, kerikil",
      "Air, udara, padatan"
    ],
    answerIndex: 1,
    explanation: "Modul Halaman 25: Komponen pembentuk batuan sedimen klastik adalah butiran (grain), masa dasar (matrix), dan semen (cement)."
  },
  {
    id: 36,
    chapter: "Batuan Sedimen",
    question: "Masa dasar (matrix) pada batuan sedimen klastik didefinisikan memiliki ukuran butir...",
    options: ["> 2 mm", "Antara 1 mm - 2 mm", "< 1/16 mm dan diendapkan bersama butiran", "Tidak berbutir"],
    answerIndex: 2,
    explanation: "Modul Halaman 25: Matrix berukuran lebih halus dari butiran (< 1/16 mm) dan diendapkan bersama-sama dengan butiran."
  },
  {
    id: 37,
    chapter: "Batuan Sedimen",
    question: "Warna batuan sedimen merah menunjukkan lingkungan...",
    options: ["Lingkungan reduksi air dalam", "Lingkungan rawa tanpa oksigen", "Lingkungan oksidasi", "Lingkungan hidrotermal asam"],
    answerIndex: 2,
    explanation: "Modul Halaman 29: 'Warna batuan merah menunjukan lingkungan oksidasi, sedangkan warna batuan hitam atau gelap menunjukan lingkungan reduksi.'"
  },
  {
    id: 38,
    chapter: "Batuan Sedimen",
    question: "Istilah kekompakan batuan sedimen di mana batuan keras tetapi masih dapat diremas menggunakan tangan adalah...",
    options: ["Dense", "Hard", "Soft", "Friable"],
    answerIndex: 3,
    explanation: "Modul Halaman 29: Friable adalah sifat kekompakan di mana batuan keras tetapi dapat diremas dengan tangan."
  },
  {
    id: 39,
    chapter: "Batuan Sedimen",
    question: "Menurut R.P. Koesoemadinata (1981), batuan rijang (chert) dan tanah diatom termasuk ke dalam...",
    options: ["Golongan Detritus Kasar", "Golongan Karbonat", "Golongan Silika", "Golongan Evaporit"],
    answerIndex: 2,
    explanation: "Modul Halaman 30: Termasuk ke dalam Golongan Silika adalah rijang (chert), radiolaria, dan tanah diatom."
  },
  {
    id: 40,
    chapter: "Batuan Sedimen",
    question: "Batuan gipsum, anhidrit, dan batu garam (halit) menurut Koesoemadinata (1981) dikelompokkan ke dalam...",
    options: ["Golongan Detritus Halus", "Golongan Evaporit", "Golongan Karbonat", "Golongan Batubara"],
    answerIndex: 1,
    explanation: "Modul Halaman 30: Golongan Evaporit terbentuk dari larutan pekat dan penguapan tinggi, contohnya gipsum, anhidrit, dan batu garam."
  },
  // --- STRUKTUR SEDIMEN ---
  {
    id: 41,
    chapter: "Struktur Sedimen",
    question: "Suatu lapisan sedimen disebut memiliki perlapisan 'Laminasi' apabila ketebalannya...",
    options: ["Kurang dari 1 cm (< 1 cm)", "Antara 1 cm - 5 cm", "Lebih dari 5 cm", "Lebih dari 120 cm"],
    answerIndex: 0,
    explanation: "Modul Halaman 32: 'laminasi : bila tebal lapisan kurang dari 1 cm; stratum : bila tebal lapisan lebih dari 1 cm.'"
  },
  {
    id: 42,
    chapter: "Struktur Sedimen",
    question: "Lapisan sedimen yang tidak menampakkan struktur dalam atau memiliki ketebalan lebih dari 120 cm disebut...",
    options: ["Stratum", "Graded Bedding", "Massif (Masif)", "Cross Bedding"],
    answerIndex: 2,
    explanation: "Modul Halaman 33: 'A. Massif: Batuan massif bila tidak menunjukan struktur dalam atau ketebalan lebih dari 120 cm.'"
  },
  {
    id: 43,
    chapter: "Struktur Sedimen",
    question: "Perlapisan yang dicirikan oleh perubahan ukuran butir secara gradual dari bawah kasar ke atas semakin halus disebut...",
    options: ["Cross Bedding", "Normal Grading (Graded Bedding)", "Inverted Grading", "Laminasi Sejajar"],
    answerIndex: 1,
    explanation: "Modul Halaman 33: 'bila bagian bawah kasar dan keatas semakin halus disebut normal grading.'"
  },
  {
    id: 44,
    chapter: "Struktur Sedimen",
    question: "Struktur sedimen berupa celah terputus-putus berbentuk kantong berukuran 2 - 10 cm akibat pengaruh aliran turbulen terisi pasir disebut...",
    options: ["Load Cast", "Flute Cast", "Tool Marks", "Rain Print"],
    answerIndex: 1,
    explanation: "Modul Halaman 34: Flute cast adalah struktur sedimen berupa celah terputus-putus serta berbentuk kantong, ukuran 2 - 10 cm akibat aliran turbulen."
  },
  {
    id: 45,
    chapter: "Struktur Sedimen",
    question: "Struktur sedimen yang berupa retakan-retakan bersegi lima pada permukaan lumpur akibat perubahan suhu dan pengerutan disebut...",
    options: ["Mud Cracks", "Flame Structure", "Convolute Bedding", "Load Cast"],
    answerIndex: 0,
    explanation: "Modul Halaman 34: Mud cracks adalah retakan-retakan pada tubuh sedimen permukaan (lumpur), biasanya berbentuk segi lima akibat pengerutan dan perubahan suhu."
  },
  {
    id: 46,
    chapter: "Struktur Sedimen",
    question: "Struktur sedimen yang berupa tonjolan lumpur menyala/menyusup ke dalam batupasir akibat tekanan lateral dan beban disebut...",
    options: ["Tool Marks", "Flame Structure", "Rain Print", "Ball and Pillow"],
    answerIndex: 1,
    explanation: "Modul Halaman 35: Flame structure berupa bentukan lumpur licin yang menyembul ke atas memasuki batupasir akibat tekanan lateral."
  },
  {
    id: 47,
    chapter: "Struktur Sedimen",
    question: "Fragmen-fragmen tabular yang tersusun overlapping (saling menindih) dan menunjukkan arah arus ke atas pada daerah fluvial disebut...",
    options: ["Clastic Imbrication", "Primary Current Lineation", "Fossil Orientation", "Scours"],
    answerIndex: 0,
    explanation: "Modul Halaman 34: Clastic Imbrication adalah struktur sedimen dengan fragmen tabular overlapping yang menunjukkan arus ke atas pada daerah berkerikil/fluvial."
  },
  // --- BATUAN METAMORF ---
  {
    id: 48,
    chapter: "Batuan Metamorf",
    question: "Batuan asal (protolith) dari batu sabak (slate) pada umumnya adalah...",
    options: ["Batu gamping", "Batu lempung", "Granit", "Batupasir kuarsa"],
    answerIndex: 1,
    explanation: "Modul Halaman 36: 'Contoh batuan tersebut adalah batu sabak atau slate yang merupakan perubahan batu lempung.'"
  },
  {
    id: 49,
    chapter: "Batuan Metamorf",
    question: "Struktur foliasi metamorf yang umumnya ditemukan pada batuan berbutir sangat halus (mikrokristalin) dengan bidang belah planar rapat dan sejajar adalah...",
    options: ["Schistosic", "Gneissic", "Slaty Cleavage", "Phylitic"],
    answerIndex: 2,
    explanation: "Modul Halaman 37: Slaty Cleavage dicirikan oleh butiran sangat halus (mikrokristalin) dengan bidang belah planar sangat rapat, teratur, dan sejajar."
  },
  {
    id: 50,
    chapter: "Batuan Metamorf",
    question: "Struktur metamorf yang ditandai oleh perselingan lapisan penjajaran mineral granular (kuarsa, feldspar) dengan mineral ferromagnesian tabular/prismatik yang terputus-putus adalah...",
    options: ["Slaty Cleavage", "Schistosic", "Gneissic (Gnissose)", "Phylitic"],
    answerIndex: 2,
    explanation: "Modul Halaman 38: Gneissic terbentuk oleh perselingan lapisan penjajaran mineral granular dengan mineral tabular/prismatik ferromagnesian yang tidak menerus/terputus-putus."
  },
  {
    id: 51,
    chapter: "Batuan Metamorf",
    question: "Batuan tanduk (hornfels) merupakan batuan metamorf dengan struktur non-foliasi...",
    options: ["Hornfelsic / Granulose", "Kataklastik", "Milonitik", "Filonitik"],
    answerIndex: 0,
    explanation: "Modul Halaman 39: Struktur Hornfelsic/granulose terbentuk oleh mosaik mineral equidimensional dan equigranular poligonal. Batuannya disebut hornfels (batutanduk)."
  },
  {
    id: 52,
    chapter: "Batuan Metamorf",
    question: "Struktur metamorf non-foliasi hasil penggerusan mekanik hebat berbutir halus dan goresan searah yang BELUM mengalami rekristalisasi primer menghasilkan batuan...",
    options: ["Kataklasit", "Milonit (Mylonite)", "Filonit (Phyllonite)", "Sekis"],
    answerIndex: 1,
    explanation: "Modul Halaman 40: Milonitic dihasilkan penggerusan mekanik, berbutir halus, goresan searah dan belum terjadi rekristalisasi mineral primer. Batuannya disebut mylonite."
  },
  {
    id: 53,
    chapter: "Batuan Metamorf",
    question: "Apa perbedaan utama antara struktur Milonitik dengan struktur Filonitik (Phylonitic)?",
    options: [
      "Filonitik tidak memiliki goresan",
      "Pada filonitik umumnya telah terjadi rekristalisasi dan menampakkan kilap sutera",
      "Milonitik terbentuk dari batuan beku saja",
      "Filonitik merupakan batuan sedimen murni"
    ],
    answerIndex: 1,
    explanation: "Modul Halaman 41: Filonitik mempunyai kenampakan sama dengan milonitik tetapi umumnya telah terjadi rekristalisasi dan menampakkan kilap sutera."
  },
  {
    id: 54,
    chapter: "Batuan Metamorf",
    question: "Tekstur batuan metamorf yang didominasi oleh mineral-mineral penyusun berbentuk pipih atau TABULAR (seperti mika) disebut...",
    options: ["Lepidoblastik", "Nematoblastik", "Granoblastik", "Porfiroblastik"],
    answerIndex: 0,
    explanation: "Modul Halaman 42: Lepidoblastik apabila mineral penyusunnya berbentuk tabular/pipih."
  },
  {
    id: 55,
    chapter: "Batuan Metamorf",
    question: "Tekstur batuan metamorf yang didominasi oleh mineral penyusun berbentuk PRISMATIK atau jarum (seperti amfibol) disebut...",
    options: ["Lepidoblastik", "Nematoblastik", "Granoblastik", "Idioblastik"],
    answerIndex: 1,
    explanation: "Modul Halaman 42: Nematoblastik apabila mineral penyusunnya berbentuk prismatik."
  },
  {
    id: 56,
    chapter: "Batuan Metamorf",
    question: "Tekstur porfiroblastik di mana mineral kristal besar tampak melingkupi/mengepung beberapa kristal mineral kecil di dalamnya (sieve texture) disebut...",
    options: ["Poikiloblastik", "Mortar Texture", "Decussate Texture", "Saccharoidal Texture"],
    answerIndex: 0,
    explanation: "Modul Halaman 42: 'Poikloblastik/Sieve texture, tekstur porfiroblastik dengan porphyroblasts tampak melingkupi beberapa kristal yang lebih kecil.'"
  },
  {
    id: 57,
    chapter: "Batuan Metamorf",
    question: "Tekstur di mana fragmen mineral besar berada pada massa dasar hancuran kristal dari mineral yang sama akibat proses pemecahan (crushing) disebut...",
    options: ["Mortar Texture", "Decussate Texture", "Saccharoidal Texture", "Homeoblastik"],
    answerIndex: 0,
    explanation: "Modul Halaman 42: 'Mortar teksture, apabila fragmen mineral yang lebih besar terdapat pada massa dasar material yang berasal dari kristal yang sama yang terkena pemecahan (crushing).'"
  },
  {
    id: 58,
    chapter: "Batuan Metamorf",
    question: "Tekstur batuan metamorf yang kenampakan butirannya menyerupai butiran gula pasir disebut...",
    options: ["Decussate Texture", "Saccharoidal Texture", "Homeoblastik", "Granoblastik"],
    answerIndex: 1,
    explanation: "Modul Halaman 42: 'Saccaroidal Texture yaitu tekstur yang kenampakannya seperti gula pasir.'"
  },
  {
    id: 59,
    chapter: "Batuan Metamorf",
    question: "Batuan metamorf yang masih menunjukkan sisa-sisa tekstur batuan asalnya diklasifikasikan bertekstur...",
    options: ["Kristaloblastik", "Relict / Palimset / Sisa", "Idioblastik", "Xenoblastik"],
    answerIndex: 1,
    explanation: "Modul Halaman 41: Relict/Palimset/Sisa merupakan tekstur batuan metamorf yang masih menunjukkan sisa tekstur batuan asalnya."
  },
  {
    id: 60,
    chapter: "Batuan Metamorf",
    question: "Apabila batuan metamorf hanya tersusun oleh SATU macam tekstur saja, batuan tersebut dinamakan bertekstur...",
    options: ["Homeoblastik", "Poliblastik", "Heteroblastik", "Monoblastik"],
    answerIndex: 0,
    explanation: "Modul Halaman 42: 'Batuan mineral yang hanya terdiri dari satu tekstur saja, sering disebut berstektur homeoblastik.'"
  }
];

// Export to window
if (typeof window !== 'undefined') {
  window.MODULE_META = MODULE_META;
  window.CHAPTERS_DATA = CHAPTERS_DATA;
  window.MOHS_SCALE_DRILL = MOHS_SCALE_DRILL;
  window.FLASHCARDS = FLASHCARDS;
  window.QUIZ_QUESTIONS = QUIZ_QUESTIONS;
}
"""

with open('data.js', 'w', encoding='utf-8') as f:
    f.write(data_content)

print(f"data.js created successfully with length: {len(data_content)} bytes")
