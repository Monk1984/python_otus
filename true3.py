

def test_my():
    phrase = input("Введите фразу короче 15 букв:")
    assert len(phrase) < 15, print("Cool!!!")
