import builtins
from workbooks.wb01_foundations.lesson01.solve_page import prompt_access

def test_prompt_access_uses_input_and_prints(capsys, monkeypatch):
    monkeypatch.setattr(builtins, "input", lambda prompt="": " overclocked ")
    result = prompt_access()

    captured = capsys.readouterr()
    assert "ACCESS GRANTED" in captured.out
    assert result == "ACCESS GRANTED"