# set of production
rules = """
    K -> S P | X1 Ket | X1 Pel | X1 X2

    X1 -> S P
    X2 -> Pel Ket

    S -> NP Det | NP Noun | NP AdjP
    P -> NP NP
    Ket -> Prep NP | Prep NumP
    Pel -> Det AdjP | Det VP | Adv AdjP
    NP -> Noun | Pronoun | NP Noun | NP Pronoun | NP Ket | NP AdjP | NP Det
    AdjP -> Adj | AdjP Adv | Adv AdjP | AdjP NP
    VP -> Verb | VP Verb | Adv VP | VP NP
    VP1 -> Verb1 NP
    PP -> Prep NP | Prep PP | Prep AdjP
    NumP -> Num | NumP NP | NP NumP

    Noun -> ketua | koperasi | pasar | badung | mahasiswa | baru | i | putu | gede | guru | olahraga | sekolah | ibu | puspa | dosen | matematika | kampus | timpal | nasi | goreng | ajengan | bapak | bupati | gianyar | semeton | adin | dasar | tahun | taun | pragina | desan | nyoman | budi | sopir | motor | trunyan | juru | parkir | sepedane | wayan | darta | bapane | carik | pak | polisi | lalu-lintas | denpasar | jero | balian | sakit | basang | putu | gede | umah | memen | desane | baju | baru | lemarine | tukang | pns | luh | sari | serombotan | anake | bapakne | pianakne | diri | tingkat | 2020 | desa
    Pronoun -> tiang | tiange | ipun | titiang
    Adj -> lanang | wanen | jegeg | demenin | luh | becik | seleg | sesai | luung | sakti | jegeg-jegeg | sekancan
    Adv -> paling | pisan | rauh | semeng
    Verb -> ngajar | anggone | ngatehin | ngatur | ngubadin | meli
    Verb1 -> pinaka
    Num -> telung | limang | dasa | besik
    Prep -> di | ring | saking | uli | ka | sampun | tuni | dados
    Det -> punika | puniki | sane | ento
"""