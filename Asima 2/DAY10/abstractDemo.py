from abc import ABC, abstractmethod
 
class MediaPlayer(ABC):#grouping of different classes
    @abstractmethod
    def play(self):
        pass
 
class VideoPlayer(MediaPlayer):
    def _resizeWindow(self):
        print('Resizing window')
 
    def play(self):
        self._resizeWindow()
        print(f'VideoPlayer Play()')
 
class AudioPlayer(MediaPlayer):
    def _minimize(self):
        print('minized on your task bar')
    def play(self):
        self._minimize()
        print(f'AudioPlayer Play()')
 
class MP4(VideoPlayer):
    def play(self):
        print(f'MP4 Play()')
 
if __name__ == '__main__':
    plays =  [AudioPlayer(),VideoPlayer(), MP4(),MP4(),AudioPlayer(),VideoPlayer(),VideoPlayer(), MP4(),AudioPlayer()]
    for obj in plays:
        obj.play()
 
   
 