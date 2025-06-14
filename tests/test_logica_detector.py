
from src.aglomeracao.logica_detector import verificar_aglomeracao

def test_verificar_aglomeracao():
    assert verificar_aglomeracao(60, 10) == True
    assert verificar_aglomeracao(30, 20) == False
