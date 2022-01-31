import numpy as np


def get_s(u1, u2):
    b = np.array([[1, 1, 0, 1, 1, 1, 0, 0, 0, 1, 0, 1],
                  [1, 0, 1, 1, 1, 0, 0, 0, 1, 0, 1, 1],
                  [0, 1, 1, 1, 0, 0, 0, 1, 0, 1, 1, 1],
                  [1, 1, 1, 0, 0, 0, 1, 0, 1, 1, 0, 1],
                  [1, 1, 0, 0, 0, 1, 0, 1, 1, 0, 1, 1],
                  [1, 0, 0, 0, 1, 0, 1, 1, 0, 1, 1, 1],
                  [0, 0, 0, 1, 0, 1, 1, 0, 1, 1, 1, 1],
                  [0, 0, 1, 0, 1, 1, 0, 1, 1, 1, 0, 1],
                  [0, 1, 0, 1, 1, 0, 1, 1, 1, 0, 0, 1],
                  [1, 0, 1, 1, 0, 1, 1, 1, 0, 0, 0, 1],
                  [0, 1, 1, 0, 1, 1, 1, 0, 0, 0, 1, 1],
                  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]])
    s = u1.transpose() + np.matmul(b, u2.transpose())
    return list(map(lambda x: x % 2, s))


def get_e(s1):
    b = np.array([[1, 1, 0, 1, 1, 1, 0, 0, 0, 1, 0, 1],
                  [1, 0, 1, 1, 1, 0, 0, 0, 1, 0, 1, 1],
                  [0, 1, 1, 1, 0, 0, 0, 1, 0, 1, 1, 1],
                  [1, 1, 1, 0, 0, 0, 1, 0, 1, 1, 0, 1],
                  [1, 1, 0, 0, 0, 1, 0, 1, 1, 0, 1, 1],
                  [1, 0, 0, 0, 1, 0, 1, 1, 0, 1, 1, 1],
                  [0, 0, 0, 1, 0, 1, 1, 0, 1, 1, 1, 1],
                  [0, 0, 1, 0, 1, 1, 0, 1, 1, 1, 0, 1],
                  [0, 1, 0, 1, 1, 0, 1, 1, 1, 0, 0, 1],
                  [1, 0, 1, 1, 0, 1, 1, 1, 0, 0, 0, 1],
                  [0, 1, 1, 0, 1, 1, 1, 0, 0, 0, 1, 1],
                  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]])

    w1 = sum(s1)
    print(f'{w1=}')
    if w1 <= 3:
        return [s1, 12 * [0]]
    for i, bi in enumerate(b):
        s1_add_bi = [(x + y) % 2 for x, y in zip(s1, bi)]
        ei = 12 * [0]
        ei[i] = 1
        if sum(s1_add_bi) <= 2:
            i += 1
            print(f'{s1_add_bi=}\n{i=}')
            return [s1_add_bi, ei]

    s2 = np.matmul(b, s1.transpose())
    s2 = list(map(lambda x: x % 2, s2))

    w2 = sum(s2)
    print(f'{w2=}')
    if w2 <= 3:
        return [12 * [0], s2]
    for i, bi in enumerate(b):
        s2_add_bi = [(x + y) % 2 for x, y in zip(s2, bi)]
        ei = 12 * [0]
        ei[i] = 1
        if sum(s2_add_bi) <= 2:
            i += 1
            print(f'{s2_add_bi=}\n{i=}')
            return [ei, s2_add_bi]
    return None


def correct_u(u, e):
    c = [[(x + y) % 2 for x, y in zip(ui, ei)] for ui, ei in zip(u, e)]
    return c


def main():
    # Sprawdzamy, czy c jest poprawnym ciągiem:
    c1 = [0, 1, 1, 1, 0, 0, 1, 0, 1, 0, 0, 0]
    c2 = [1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1]
    s = get_s(np.array(c1), np.array(c2))
    print(f'{s=}')
    if sum(s):
        print("Wektor nie jest poprawny.")
    else:
        print("Wektor jest poprawny.")
        # u1 = [0, 1, 1, 1, 0, 0, 1, 0, 1, 0, 0, 1]
        # u2 = [1, 1, 0, 1, 1, 0, 0, 1, 1, 0, 1, 1]
        u1 = [0, 0, 1, 0, 0, 1, 0, 0, 1, 1, 0, 1]
        u2 = [1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0]
        u = [u1, u2]
        # Obliczamy syndrom s1:
        s1 = get_s(np.array(u1), np.array(u2))
        print(f'{s1=}')
        # Obliczamy korekcję e dla u:
        e = get_e(np.array(s1))
        print(f'{u=}')
        print(f'{e=}')
        if e:
            # Poprawiamy ciąg u:
            c = correct_u([u1, u2], e)
            print(f'+{(len(f"{c=}") - 1) * "_"}')
            print(f'{c=}')
        else:
            print("Nie można skorygować ciągu.")


if __name__ == "__main__":
    main()