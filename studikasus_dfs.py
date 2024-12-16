peta={
    'A':['B'],
    'B':['A','C'],
    'C':['D','H','I','B'],
    'D':['E','F','G','H','C'],
    'E':['D'],
    'F':['G','H','D'],
    'G':['H','D','F'],
    'H':['D','G','L','C'],
    'I':['C','K','J'],
    'J':['I'],
    'K':['L','I'],
    'L':['K','H']
}

def dfs(peta, mulai, tujuan):
    stack = [[mulai]]
    visited = set()

    while stack:
        # Ambil jalur terakhir dari stack
        jalur = stack.pop()

        # Dapatkan node terakhir dari jalur
        node = jalur[-1]

        # Jika node belum dikunjungi
        if node not in visited:
            neighbours = peta[node]

            # Telusuri semua neighbour
            for neighbour in neighbours:
                new_jalur = list(jalur)
                new_jalur.append(neighbour)
                stack.append(new_jalur)

                # Jika neighbour adalah tujuan, return jalur
                if neighbour == tujuan:
                    return new_jalur

            # Tandai node sebagai sudah dikunjungi
            visited.add(node)

    # Jika tidak ada jalur yang ditemukan
    return None

mulai = 'C'
tujuan = 'L'
jalur = dfs(peta, mulai, tujuan)

if jalur:
    print(f"Jalur terpendek dari {mulai} ke {tujuan} adalah:", "->".join(jalur))
else:
    print(f"Tidak ada jalur dari {mulai} ke {tujuan}")