from Classes.Vector2 import Vector2
# from Classes.Texture import Texture

class ClickPos(Vector2):
    """
    クリック位置を取得するクラス
    """
    def __init__(self, pos:Vector2):
        self.pos = pos # クリック位置の座標

    def update(self):
        pass

    def draw(self):
        pass

    def is_clicked(self,click_pos:Vector2):
        return self.pos.x <= click_pos.x <= self.pos.x + 1 and self.pos.y <= click_pos.y <= self.pos.y + 1
    
    def is_in_texture_range(self,target:Vector2):
        print("is_in_texture_range")
        return target.pos.x <= self.pos.x <= target.pos.x + target.texture.size.x and target.pos.y <= self.pos.y <= target.pos.y + target.texture.size.y