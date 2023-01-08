import pandas as pd


def coon_pool_to_google_test(id):
    return f"https://docs.google.com/spreadsheets/d/{id}/export?format=csv&id={id}&gid=135007174"


def test_coon_pool_to_google_test():

    sheet_id = "1-Wx3MunuVlDT96K_fz18P1HgBUYaxSBjUu16_KyNjDU"
    url = coon_pool_to_google_test(id=sheet_id)
    df = pd.read_csv(url)

    assert len(df) != 0

