from src.text_analyzer import is_haiku


def test_haiku_detector():
    text = "лежу на траве. выше меня лишь одно синее небо."
    assert is_haiku(text)
