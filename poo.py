class Canal:
    
    def __init__(self, nome, descricao, inscritos):
        self.nome = nome
        self.descricao = descricao
        self.inscritos = inscritos
        self.videos = []
        self.playlists:list[Playlist] = []

    def adicionar_playlist(self,playlist):
        self.playlists.append(playlist)

    def mostrar_plays(self):
        for playlist in self.playlists:
            playlist.info_playlist()

    def inscrever(self,quantidade = 1):
        self.inscritos += quantidade

    def postar(self, video):
        self.videos.append(video)

class CanalEmpresarial(Canal):
    def __init__(self, nome, descricao, inscritos):
        super().__init__(nome, descricao, inscritos)
        self.equipe = []

    def adicionar_membro_equipe(self,membro):
        if membro not in self.equipe:
            self.equipe.append(membro)        
        else:
            print(f'O membro {membro} já esta na equipe!')

    def remover_membro_equipe(self,membro):
        if membro in self.equipe:
            self.equipe.remove(membro)
        else:
            print(f'O {membro} não consta como membro da equipe')

class Video:
    def __init__(self, titulo, descricao, data_publicacao):
        self.titulo = titulo
        self.descricao = descricao
        self.data_publicacao = data_publicacao

        self.visualizacoes = 0   
        self.likes = 0
        self.deslikes = 0
        self.comentarios = []

    def __repr__(self):
        return f'<{self.titulo}>'        

    def assistir(self):
        self.visualizacoes += 1        

    def gostar(self):
        self.likes += 1
        
    def desgostar(self):
        self.deslikes += 1

    def comentar(self, comentario):
        self.comentarios.append(comentario)

    def info(self):
        print(f"""Título: {self.titulo}
Data da Publicação: {self.data_publicacao}
Visualizacões: {self.visualizacoes}
Likes: {self.likes}
Deslikes: {self.deslikes}
Comentários: {self.comentarios}\n""")

class Playlist:
    def __init__(self,titulo_playlist):
        self.titulo_playlist = titulo_playlist
        self.videos:list[Video] = []
        
        
    def adicionar_video_playlist(self,video):
        self.videos.append(video)

    def info_playlist(self):
        print(f"Titulo da Playlist: {self.titulo_playlist}")
        for video in self.videos:
            video.info()



canal_circus = CanalEmpresarial('Digital Circus', 'Bem-vindo ao mundo digital', 2000000)
canal_enygma = Canal('Enygma','Musicas geek', 1000000)

playlist_geek = Playlist('Raps Geek')
video_akaza = Video('Presságio de Destruição', 'Musica sobre o personagem Akaza', '31/05/2026')
video_kaneki = Video('Tragédia', 'Musica sobre o personagem Kaneki', '25/05/2025')

playlist_rock = Playlist('Musica de rock')
video_slipknot = Video('Nero Forte', 'Musica rock pesado','16/12/2019')
video_samurai = Video('Never Fade Way', 'Musica de rock com linda guitarra', '23/08/2019')

playlist_rock.adicionar_video_playlist(video_slipknot)
playlist_rock.adicionar_video_playlist(video_samurai)

playlist_geek.adicionar_video_playlist(video_kaneki)
playlist_geek.adicionar_video_playlist(video_akaza)
canal_enygma.adicionar_playlist(playlist_geek)
canal_enygma.adicionar_playlist(playlist_rock)
canal_enygma.mostrar_plays()
# playlist_geek.info_playlist()

#video_akaza.info()

# canal_enygma.postar(video_akaza)
# canal_enygma.postar(video_kaneki)

# print(canal_enygma.videos)




# print(video_akaza.descricao)
# print(video_akaza.visualizacoes)
# video_akaza.assistir()
# print(video_akaza.visualizacoes)
# video_akaza.gostar()
# video_akaza.gostar()
# video_akaza.desgostar()
# print(f'Likes: {video_akaza.likes}')
# print(f'Deslikes: {video_akaza.deslikes}')
# video_akaza.comentar('Muito boa a musica')
# video_akaza.comentar('Canta demais')
# video_akaza.info()
# print(f'Nome do canal: {canal_enygma.nome}')
# print(f'Descrição do canal: {canal_enygma.descricao}')
# print(f'Inscritos atuais: {canal_enygma.inscritos}')
# canal_enygma.inscrever(67)
# print(f'Inscritos atuais: {canal_enygma.inscritos}')

# canal_circus.adicionar_membro_equipe('Caim')
# print(canal_circus.equipe)
# canal_circus.adicionar_membro_equipe('Kingo')
# print(canal_circus.equipe)
# canal_circus.remover_membro_equipe('Caim')
# print(canal_circus.equipe)