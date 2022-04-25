violator_songs = {
    'World in My Eyes': 4.86,
    'Sweetest Perfection': 4.43,
    'Personal Jesus': 4.56,
    'Halo': 4.9,
    'Waiting for the Night': 6.07,
    'Enjoy the Silence': 4.20,
    'Policy of Truth': 4.76,
    'Blue Dress': 4.29,
    'Clean': 5.83
}

songsCount = int(input("Сколько песен выбрать? "))

summ_time = 0

for i_song in range(songsCount):
    print("Название", i_song + 1, "песни: ", end="")
    song = input()
    summ_time += violator_songs[song]

print("\nОбщее время звучания песен:", round(summ_time, 2), "минут")

# зачтено
