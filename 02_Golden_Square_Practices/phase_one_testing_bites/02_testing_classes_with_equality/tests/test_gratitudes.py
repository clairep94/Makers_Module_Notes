from lib.gratitudes import Gratitudes

def test_formatted_gratitude():
    grat = Gratitudes()
    grat.add("my home")
    grat.add("my health")
    grat.add("my friends")
    assert grat.format() == "Be grateful for: my home, my health, my friends"