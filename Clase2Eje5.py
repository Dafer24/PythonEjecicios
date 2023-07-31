class IPodPlayer:

    def __init__(self, max_capacity):   # Atributos del reproductor de música.
        self.max_capacity = max_capacity
        self.current_capacity = 0
        self.playlist = []

    def add_song(self, song, size): # Método para agregar una canción al reproductor de música si hay suficiente espacio.
        if self.current_capacity + size <= self.max_capacity:
            self.playlist.append(song)
            self.current_capacity += size
            print(f"Song '{song}' added to the iPod.")
        else:
            print("Not enough space on the iPod to add this song.")

    def remove_song(self, song):    # Método para eliminar una canción de la playlist del reproductor de música.
        if song in self.playlist:
            self.playlist.remove(song)
            print(f"Song '{song}' removed from the iPod.")
        else:
            print(f"The song '{song}' is not found in the playlist.")

    def play(self): # Método para reproducir la playlist de canciones del reproductor de música.
        
        if len(self.playlist) > 0:
            print("Playing playlist:")
            for song in self.playlist:
                print(f" - {song}")
        else:
            print("The playlist is empty. Add songs to the iPod before playing.")

    def empty(self):    # Método para vaciar completamente la playlist del reproductor de música.
        self.playlist.clear()
        self.current_capacity = 0
        print("The iPod has been emptied. The playlist is now empty.")

# Ejemplo de uso del reproductor de música.
ipod = IPodPlayer(1000) # Crear un nuevo iPod con capacidad máxima de 1000 MB.

ipod.add_song("Song 1", 150) # Agregar canciones al iPod.
ipod.add_song("Song 2", 200)
ipod.add_song("Song 3", 300)

ipod.play()  # Reproducir la playlist del iPod.
ipod.remove_song("Song 2")  # Eliminar una canción del iPod.
ipod.empty()  # Vaciar completamente la playlist del iPod.
ipod.add_song("Song 4", 800)  # Intentar agregar una canción que excede la capacidad máxima del iPod.
ipod.play()  # Reproducir la playlist nuevamente (que debe estar vacía).
