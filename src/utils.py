"""
    utileria de limpieza y resumen
"""

def to_mnx(valor, taza: float = 18.58) -> float:
    """
        convierte valor a MNX
        multiplicado por taza
    """
    return float(valor)*float(taza)

def clean_str(s_txt: str):
    """
        limpiar espacios y  capitaliza
    """
    return " ".join(s_txt.strip().title().split())

#   "    DanIELl     MarTIN      LImon     GaRcIa      "

#   strip: "DanIELl     MarTIN      LImon     GaRcIa"

#   title: "Daniell     Martin      Limon     Garcia"
