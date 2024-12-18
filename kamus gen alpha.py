meme_dict = {
            "CRINGE": "Sesuatu yang sangat aneh atau memalukan",
            "SIGMA": "Orang yang keren dan dingin",
            "CREEPY": "menakutkan, tidak menyenangkan",
            "SHEESH ": "sedikit ketidaksetujuan"
}

word = input("Ketik kata yang tidak kamu mengerti")

if word in meme_dict.keys():
    print(meme_dict[word])
else:
    print(' kata yang kamu cari tidak ada!')
