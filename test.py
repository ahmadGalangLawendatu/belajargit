from helloworld.hewan import Hewan


def test_suara_hewan():
    # Membuat instance hewan untuk pengujian
    cat = Hewan("Whiskers", "Cat", "Meow")
    dog = Hewan("Buddy", "Dog", "Woof")
    duck = Hewan("Daffy", "Duck", "Quack")

    # Memeriksa hasil suara hewan
    assert cat.buat_suara() == 'Whiskers bersuara Meow'
    assert dog.buat_suara() == 'Buddy bersuara Woof'
    assert duck.buat_suara() == 'Daffy bersuara Quack'

    # Menampilkan daftar pilihan hewan
    print(Hewan.hewan_choices)

    # Pilih hewan pertama
    hewan_pilihan = Hewan.hewan_choices[0]

    # Memanggil metode buat_suara() pada hewan yang dipilih
    suara_hewan_pilihan = hewan_pilihan.buat_suara()
    print(suara_hewan_pilihan)


if __name__ == "__main__":
    test_suara_hewan()
