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


Copyright (c) _date_ _author name(s)_
