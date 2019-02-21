import sdl2
import sdl2.ext

class Display(object):
  def __init__(self, width, height):
    sdl2.ext.init()

    self.width, self.height = width, height
    self.window = sdl2.ext.Window("SLAM", size=(width,height), position=(0,0))

    # Showing Window 
    self.window.show()

  def paint(self, img):
    # Gets all SDL events that are currently on the event queue.
    events = sdl2.ext.get_events()
    for event in events:
      if event.type == sdl2.SDL_QUIT:
        exit(0)

    # draw a 3D pixel array, based on numpy.ndarray, from the passed source
    surf = sdl2.ext.pixels3d(self.window.get_surface())
    surf[:, :, 0:3] = img.swapaxes(0,1)

    # blit
    self.window.refresh()