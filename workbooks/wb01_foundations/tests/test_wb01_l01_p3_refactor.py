from workbooks.wb01_foundations.lesson01.rep_page import access_status as rep
from workbooks.wb01_foundations.lesson01.refactor_page import access_status as ref

def test_refactor_matches_rep():
    samples = ["OVERCLOCKED", "overclocked", "  overclocked ", "nope", ""]
    for s in samples:
        assert ref(s) == rep(s)