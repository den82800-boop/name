from customtkinter import *
import pygame


pygame.mixer.init()
music_play = False

class win(CTk):
    def __init__(self):
        super().__init__()
        self.geometry("700x500")
        self.title("Music")

        self.songs = []
        self.Container = CTkFrame(self, width=350, height=400, corner_radius=15)
        self.Container.place(x=320, y=60)

        self.playlist = CTkFrame(self, width=250, height=350, corner_radius=15)
        self.playlist.place(x=30, y=110)

        self.open = CTkFrame(self, width=250, height=40, corner_radius=15)
        self.open.place(x=30, y=60)

        self.play_button = CTkButton(self.Container, text="▶", text_color="white",width=250, height=50, corner_radius=25, command=self.play_music)
        self.play_button.place(x=55, y=250)

        self.music_name = CTkLabel(self.Container,  text="Text", width=150, height=30, font=("Arial",20, "bold"))
        self.music_name.place(x=15, y=50)

        self.timeline = CTkSlider(
            self.Container,
            width=300,
            height=10,
            from_=0,
            to=0,
            command=self.seek_music
        )
        self.timeline.place(x=30, y=200)

        self.playlist_name = CTkLabel(self, text="Playlist", width=150, height=30, font=("Arial",36, "bold"), bg_color="transparent")
        self.playlist_name.place(x=25, y=10)

        self.open_button = CTkButton(self.open, text='📄', width=40, height=40, corner_radius=10 ,command=self.load_file)
        self.open_button.place(x=0, y=0)

        self.loaded_file = -1

        self.length_minutes = 0

        self.dunno = 0

    def play_music(self):
        global music_play
        pygame.mixer.music.load(self.song_name[-1])
        a = pygame.mixer.Sound(self.song_name[-1])
        length = a.get_length()
        print(length)
        self.length_minutes = int(length // 60)
        self.length_seconds = int(length % 60)
        minutes = 0
        seconds = 0
        self.timeline.configure(to=int(length))
        self.time = CTkLabel(self.Container, text=f"{minutes}:{seconds}/{self.length_minutes}:{self.length_seconds:02d}", font=("Arial",24, "bold"))
        self.time.place(x=140, y=160)
        if music_play:
            pygame.mixer.music.stop()
            music_play = False
            self.play_button.configure(text="▶")
        else:
            music_play = True
            pygame.mixer.music.play()
            self.play_button.configure(text="⏹")



            #test


    def load_file(self):
        global file_name
        file_name = filedialog.askopenfilename()
        if file_name:
            self.songs.append(file_name)
            self.song_name = file_name.split("/")
            self.loaded_file += 1
            pygame.mixer.music.load(file_name)
            self.create_button_playlist()

    def change_music_name(self,music):
        self.music_name.configure(text=self.song_name[-1])

    def create_button_playlist(self):
        music_playlist = CTkButton(
            self.playlist,
            text=self.song_name[-1],
            width=250,
            height=20,
            corner_radius=15,
            command=lambda path=self.songs[-1]: self.play_selected(path)
        )
        if self.loaded_file == 1:
            y=0
        music_playlist.place(x=0, y=self.loaded_file * 22.5)

    def play_selected(self, path):
        global music_play
        pygame.mixer.music.load(path)
        pygame.mixer.music.play()
        music_play = True

        self.music_name.configure(text=path.split("/")[-1])
        self.play_button.configure(text="⏹")

    def seek_music(self, value):
        global music_play
        if not music_play:
            return
        new_pos = int(value)
        pygame.mixer.music.play(start=new_pos)

        self.minutes = new_pos // 60
        self.seconds = new_pos % 60
        self.time.configure(
            text=f"{minutes}:{seconds:02d}/{self.length_minutes}:{self.length_seconds:02d}"
        )


file_name = None

wind = win()
wind.mainloop()