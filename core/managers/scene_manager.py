from core.scene import Scene

class SceneManager:
    def __init__(self):
        self.current_scene : Scene = None

    def change_scene(self, new_scene : Scene):
        self.current_scene = new_scene

    def handle_event(self, event):
        if self.current_scene:
            self.current_scene.handle_event(event)

    def update(self):
        if self.current_scene:
            self.current_scene.update()

    def render(self):
        if self.current_scene:
            self.current_scene.render()
