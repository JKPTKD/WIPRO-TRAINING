class VideoPlayer:
    def play(self):
        print(f'VideoPlayer Play()')
 
class MP4(VideoPlayer):
    def play(self):
        print(f'MP4 Play()')
 
if __name__ == '__main__':
    plays =  [VideoPlayer(), MP4(),MP4(),VideoPlayer(),VideoPlayer(), MP4()]
    for obj in plays:
        obj.play()