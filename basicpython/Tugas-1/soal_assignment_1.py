{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "bf8eb1c2",
   "metadata": {},
   "source": [
    "## Buatlah sebuah program yang menerima 3 input dari user. \n",
    "Input tersebut berupa:\n",
    "1. Nama bertipe data string\n",
    "2. Umur bertipe data integer\n",
    "3. Tinggi bertipe data float "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "id": "da55075f",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Masukkan Nama : rizal\n",
      "Masukkan Umur : 22\n",
      "Masukkan Tinggi : 178\n",
      "Nama saya rizal, Umur saya 22 tahun, Tinggi saya 178.0 cm\n"
     ]
    }
   ],
   "source": [
    "nama = str(input('Masukkan Nama : '))\n",
    "umur = int(input('Masukkan Umur : '))\n",
    "tinggi = float(input('Masukkan Tinggi : '))\n",
    "\n",
    "print(f'Nama saya {nama}, Umur saya {umur} tahun, Tinggi saya {tinggi} cm')"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "b5842834",
   "metadata": {},
   "source": [
    "## Buatlah sebuah program yang dapat menghitung luas lingkaran.\n",
    "Program meminta input dari user berupa angka sebagai jari-jari lingkaran.\n",
    "Program menghitung luas lingkaran dengan rumus πr² \n",
    "Π = 22/7\n",
    "r = jari - jari lingkaran \n",
    "Lalu tampilkan ke layar dengan format:\n",
    "Hint: untuk menampilkan tanda kuadrat gunakan print(“\\u00b2”)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "595261d1",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Pi = 22/7"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "6a45e25b",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Masukkan jari-jari : 7\n",
      "Luas lingkaran dengan jari-jari 7 cm adalah 154.0 cm²\n"
     ]
    }
   ],
   "source": [
    "r = int(input('Masukkan jari-jari : '))\n",
    "luas_lingkaran = (22/7)*r*r\n",
    "\n",
    "print(f'Luas lingkaran dengan jari-jari {r} cm adalah {luas_lingkaran} cm\\u00b2')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "e6eeda85",
   "metadata": {},
   "outputs": [],
   "source": [
    "#Bonus: Ubahlah format luas menjadi 2 angka dibelakang koma\n",
    "#Hint: Ubah string format untuk float menjadi {:.2f}"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "9aed90cd",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Masukkan jari-jari : 10\n",
      "Luas lingkaran dengan jari-jari 10 cm adalah 314.2857142857143 cm²\n"
     ]
    }
   ],
   "source": [
    "r = int(input('Masukkan jari-jari : '))\n",
    "luas_lingkaran = (22/7)*r*r\n",
    "\n",
    "print(f'Luas lingkaran dengan jari-jari {r} cm adalah {luas_lingkaran} cm\\u00b2')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "id": "364fe02c",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Luas lingkaran dengan jari-jari 10 cm adalah 314.29 cm²\n"
     ]
    }
   ],
   "source": [
    "print(f'Luas lingkaran dengan jari-jari {r} cm adalah {luas_lingkaran:.2f} cm\\u00b2')"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "cc47e088",
   "metadata": {},
   "source": [
    "## Buatlah sebuah program untuk menentukan apakah seorang siswa lulus ujian atau tidak. Siswa dinyatakan lulus apabila nilai ujian teori dan ujian praktek minimal 70. \n",
    "Program menerima input berupa nilai ujian teori dan praktek, nilai ujian dapat berupa bilangan desimal."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "5845f98e",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Masukkan nilai ujian teori : 50\n",
      "Masukkan nilai praktek : 50\n",
      "Anda harus mengulang ujian teori dan praktek\n"
     ]
    }
   ],
   "source": [
    "ujian_teori = float(input('Masukkan nilai ujian teori : '))\n",
    "ujian_praktek = float(input('Masukkan nilai praktek : '))\n",
    "\n",
    "if ujian_teori >=70 and ujian_praktek >= 70:\n",
    "    print('Selamat anda lulus!')\n",
    "    \n",
    "elif ujian_teori >= 70 and ujian_praktek < 70:\n",
    "    print('Anda harus mengulang ujian praktek')\n",
    "\n",
    "elif ujian_teori < 70 and ujian_praktek >= 70:\n",
    "    print('Anda harus mengulang ujian teori')\n",
    "    \n",
    "else:\n",
    "    print('Anda harus mengulang ujian teori dan praktek')"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.10.4"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
