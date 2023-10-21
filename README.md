# ChatBot Starter with Streamlit, OpenAI, and LangChain

Repositori ini berisi chatbot yang sederhana namun kuat yang dibangun dengan Streamlit, OpenAI, dan LangChain. Chatbot mempertahankan memori percakapan, yang berarti dapat merujuk pada pertukaran sebelumnya dalam tanggapannya.

## Overview

Chatbot ini merupakan demonstrasi integrasi model GPT OpenAI, pustaka LangChain, dan Streamlit untuk membuat aplikasi web interaktif. Memori percakapan bot memungkinkannya untuk mempertahankan konteks selama sesi obrolan, sehingga menghasilkan pengalaman pengguna yang lebih koheren dan menarik. Yang terpenting, aplikasi chatbot yang kaya fitur ini diimplementasikan dalam kurang dari 80 baris kode (tidak termasuk spasi dan komentar)!

### Key Features

- **Streamlit:** Kerangka kerja Python yang kuat dan cepat yang digunakan untuk membuat antarmuka web untuk chatbot.
- **OpenAI's GPT:** Model AI pemrosesan bahasa mutakhir yang menghasilkan respons chatbot.
- **LangChain:** Library pembungkus untuk model ChatGPT yang membantu mengelola riwayat percakapan dan menyusun respons model.

## Demo App

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://sahabatbk.streamlit.app/)

## Bagaimana cara menjalankannya

### Yang dibutuhkan

- Python 3.6 atau versi diatas
- Streamlit
- LangChain
- OpenAI API key

### Langkah-langkah

1. Clone repository ini.
2. Instal paket Python yang diperlukan dengan menggunakan perintah `pip install -r requirements.txt`.
3. Buat file "environment variable" dengan nama filenya (**env.**) untuk menyimpan Key API OpenAI Anda.
4. Pada file **env.** pada baris code 1 yang diisi oleh **API OpenAi** anda.
  ```
  OPENAI_API_KEY="sk-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxWV"
  ```
  **Catatan** isi variable "**OPENAI_API_KEY**" tinggal diganti saja dengan **Key API OpenAi** anda.

5. Jalankan aplikasi Streamlit menggunakan perintah `streamlit run streamlit_app.py`.

## Penggunaan

Chatbot ini dirancang khusus untuk membantu siswa dengan pertanyaan-pertanyaan mengenai bimbingan konseling. Fungsinya meliputi memberikan informasi, saran, dan arahan terkait isu-isu konseling, serta mengarahkan siswa untuk berkomunikasi langsung dengan guru BK jika diperlukan.
## Kontribusi

Kontribusi, masalah, dan permintaan fitur dipersilakan. Silakan kunjungi halaman [Masalah](https://github.com/Bijas48/AplikasiBK/issues) jika Anda ingin berkontribusi.
## Lisensi

Proyek ini dilisensikan di bawah ketentuan lisensi MIT.
#
