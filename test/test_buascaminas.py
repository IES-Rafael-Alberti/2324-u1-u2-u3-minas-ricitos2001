import pytest
from src.buscaminas import colocar_cuadro
@pytest.mark.parametrize(
    "jugador_cuadro,impresion",
    [
        ([[-1, -1, -1, -1, -1, -1, -1, -1, -1], [-1, -1, -1, -1, -1, -1, -1, -1, -1], [-1, -1, -1, -1, -1, -1, -1, -1, -1], [-1, -1, -1, -1, -1, -1, -1, -1, -1], [-1, -1, -1, -1, -1, -1, -1, -1, -1], [-1, -1, -1, -1, -1, -1, -1, -1, -1], [-1, -1, -1, -1, -1, -1, -1, -1, -1], [-1, -1, -1, -1, -1, -1, -1, -1, -1], [-1, -1, -1, -1, -1, -1, -1, -1, -1]],'· · · · · · · · · \n· · · · · · · · · \n· · · · · · · · · \n· · · · · · · · · \n· · · · · · · · · \n· · · · · · · · · \n· · · · · · · · · \n· · · · · · · · · \n· · · · · · · · · \n'),
    ]
)
def test_colocar_cuadro_params(jugador_cuadro,impresion):
    assert colocar_cuadro(jugador_cuadro)==impresion




