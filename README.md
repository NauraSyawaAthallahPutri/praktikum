# Kalkulator Bangun Ruang
#### By Naura Syawal Athallah Putri 
#### NIM: 2390116032

## Technologies Used
* Python

## Deskripsi
#### Sebuah kalkulator bangun ruang sederana yang memungkinkan penggunanya untuk menghitung volume bola, tabung, dan limas segitiga. Pengguna dapat menginput bilangan apapun (dalam satuan m) yang mereka inginkan, yang kemudian akan dihitung hasilnya oleh kalkulator ini

## Flowchart 
#### Page1
![Flowchart Postest 1-Page-1 drawio (1)](https://github.com/NauraSyawaAthallahPutri/praktikum/assets/144810430/6239a297-7f21-4b95-b794-49573e628314)
#### Page 2
![Flowchart Postest 1-Page-2 drawio](https://github.com/NauraSyawaAthallahPutri/praktikum/assets/144810430/f068c393-e88a-40dd-973f-b5314d747dff)

## Penjelasan Mekanisme Program
Pertama, user berada pada login page yang dimana user perlu untuk memasukkan nama serta kelas. Selanjutnya, user perlu untuk memasukkan NIM dan pin dalam bentuk angka. Apabila inputan yang dimasukkan bukan berupa angka, maka akan terjadi looping yang menuruh user untuk terus memasukkan NIM dan pin tersebut dalam bentuk angka. Jika keduanya diinput dalam bentuk angka, maka looping akan berhenti dan program akan mengasilkan oput berupa ucapan selamat datang.

Selanjutnya user harus memilih salah satu diantara ketiga bangun ruang yang ingin kita hitung volumenya. Input yang dimasukkan harus berupa angka dalam interval 1 sampai 3. Apabila user memasukkan angka selain 1-3, maka terjadi looping dan program akan menyuruh user untuk memasukkan angkadalam interval tersebut. Apabila user memasukkan selain angka, maka terjadi looping dan program akan menyuruh user untuk memasukkan angka. Apabila kedua syarat sudah terpenuhi, user akan dibawa pada laman selanjutnya tergantung dengan pilihan user.

Jika user memilih angka 1 (Bola) atau 2 (Tabung), maka user akan disuruh untuk menginputkan tinggi dan jari-jari dari bangun ruang yang akan dihitung. Apabila jari-jari yang diinput merupakan kelipatan 7, maka phi yang digunakan adalah 22/7 dan jika tidak, phi yang digunakan  adalah 3,14. Selanjutnya, jika user tadinya memilih angka 1 maka program akan menghitung volume bola dan jika tidak, program akan menghitung volume tabung

Jika user memilih angka 3, maka user akan disuruh untuk menginputkan alas segitiga, tinggi segitiga, serta tinggi limas dari bangun ruang yang akan dihitung. Program akan menghitung volume dari limas segitiga tersebut.

Jika sudah selesai, program akan menampilkan hasil akhir dari bangun ruang yang telah user pilih dan nilai yang telah user input dalam besaran m³

## Ouput  
#### Apabila NIM dan PIN yang diinput bukan angka
![Postest 1 py - Visual Studio Code 9_26_2023 2_30_47 AM](https://github.com/NauraSyawaAthallahPutri/praktikum/assets/144810430/b2e420b4-2b6b-4e15-ae05-791f671eed63)
#### Apabila berhasil memasukkan PIN dan NIM
![Postest 1 py - Visual Studio Code 9_26_2023 2_32_41 AM](https://github.com/NauraSyawaAthallahPutri/praktikum/assets/144810430/e3c5a7d7-8736-4ee6-b7e3-d111ff756392)
#### Apabila pilihan yang dimasukkan bukan angka dan berada di luar interval 1-3
![Postest 1 py - Visual Studio Code 9_26_2023 2_32_58 AM](https://github.com/NauraSyawaAthallahPutri/praktikum/assets/144810430/3c5de24f-ff3f-4ab1-8642-9df923d45b49)
#### Contoh dari perhitungan volume bangun ruang
* Bola:
![Postest 1 py - Visual Studio Code 9_26_2023 2_39_56 AM](https://github.com/NauraSyawaAthallahPutri/praktikum/assets/144810430/9b7ad6f1-8a19-4be0-81fa-955ef9138c41)
* Tabung:
![Postest 1 py - Visual Studio Code 9_26_2023 2_47_13 AM](https://github.com/NauraSyawaAthallahPutri/praktikum/assets/144810430/02c472e4-530a-436a-ab6f-61b6cb983a8c)
* Limas Segitiga:
![Postest 1 py - Visual Studio Code 9_26_2023 2_41_36 AM](https://github.com/NauraSyawaAthallahPutri/praktikum/assets/144810430/c3344d4a-4d78-4dfa-8b91-10cd44b15045)


Copyright (c) _date_ _author name(s)_
