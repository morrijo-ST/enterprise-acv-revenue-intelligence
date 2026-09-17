from core import load_data,kpis

def test_kpis():
    d=load_data()
    m=kpis(d)
    assert m['starting_acv']>0
    assert m['customers']>=300
