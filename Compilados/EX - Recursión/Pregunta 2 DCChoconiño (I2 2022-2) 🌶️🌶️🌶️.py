def contar_valeotro(choc):
    if choc >= 3:
        return choc//3 + contar_valeotro(choc%3+choc//3)
    return 0 