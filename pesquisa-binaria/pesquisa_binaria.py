def pesquisa_binaria(lista, item):
    baixo = 0
    alto = len(lista) - 1

    while baixo <= alto:
        meio = (baixo + alto) // 2
        chute = lista[meio]

        if chute == item:
            return meio
        if chute > item:
            alto = meio - 1
        else:
            baixo = meio + 1
    return None
    
minha_lista = [1, 3, 5, 7, 9]

jogos = ["Assassin's Creed", "Bloodborne", "Celeste", "Dark Souls", "Elden Ring", 
         "God of War", "Hades", "Hollow Knight", "Overwatch", "The Last of Us"]

series = ["Breaking Bad", "Chernobyl", "Friends", "Game of Thrones", "Loki", 
          "Sherlock", "Stranger Things", "The Mandalorian", "The Office", "The Witcher"]

personagens = ["Arthur Morgan", "Ellie", "Geralt", "Kratos", "Lara Croft", 
               "Link", "Mario", "Nathan Drake", "Samus", "Zelda"]

times = ["Barcelona", "Chelsea", "Flamengo", "Juventus", "Liverpool", 
         "Manchester City", "PSG", "Real Madrid", "Santos", "Tottenham"]

nomes = ["Alice", "Bianca", "Carlos", "Daniel", "Fernanda", 
         "Gabriel", "Lucas", "Mariana", "Renato", "Thiago"]

persona_5_royal = ["Ann Takamaki", "Caroline", "Chihaya Mifune", "Futaba Sakura", "Haru Okumura", 
                   "Igor", "Joker", "Jose", "Kasumi Yoshizawa", "Makoto Niijima", 
                   "Morgana", "Ryuji Sakamoto", "Sae Niijima", "Shinya Oda", 
                   "Sojiro Sakura", "Sumire Yoshizawa", "Takuto Maruki", "Yusuke Kitagawa", "Zenkichi Hasegawa"]


print (pesquisa_binaria(jogos, "The Last of Us"))
print (pesquisa_binaria(persona_5_royal, "Sae Niijima"))
print (pesquisa_binaria(personagens, "Kratos"))
print (pesquisa_binaria(nomes, "Lucas"))
print (pesquisa_binaria(times, "Flamengo"))
print (pesquisa_binaria(series, "Friends"))