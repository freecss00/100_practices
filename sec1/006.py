import ngram

if __name__ == '__main__':
    s1 = 'paraparaparadise'
    s2 = 'paragraph'
    X = set(ngram.n_gram(2, s1, ngram.CHAR))
    Y = set(ngram.n_gram(2, s2, ngram.CHAR))

    print('Union        :', X | Y)
    print('Difference   :', X - Y)
    print('Intersection :', X & Y)
    print('Is "se" belong to both X and Y?: ', 'se' in (X & Y))
