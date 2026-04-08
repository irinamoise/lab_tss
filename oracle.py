def oracle_search(v, key):
    # metoda index a listei = referinta de incredere
    try:
        return v.index(key)
    except ValueError:
        return -1