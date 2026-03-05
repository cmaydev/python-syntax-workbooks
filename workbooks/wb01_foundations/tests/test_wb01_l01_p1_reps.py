from workbooks.wb01_foundations.lesson01.rep_page import access_status

def test_access_status_exact_match():
    assert access_status("OVERCLOCKED") == "ACCESS GRANTED"
    assert access_status("wrong") == "ACCESS DENIED"

def test_access_status_strips_and_cases():
    assert access_status("  overclocked  ") == "ACCESS GRANTED"
    assert access_status("\toverclocked\n") == "ACCESS GRANTED"