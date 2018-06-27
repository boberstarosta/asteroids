from .vec import Vec2


class Camera:
	def __init__(self, pos=Vec2()):
		self.pos = pos
		self.pos_from = self.pos
		self.pos_to = self.pos
		self.timer = 0.0
		self.tween_time = 0.0
	
	def update(self, fps):
		if self.timer < self.tween_time:
			self.timer += 1/fps
			tween_value = self.tween_value(self.timer / self.tween_time)
			move = (self.pos_to - self.pos_from) * tween_value
			self.pos = self.pos_from + move
		else:
			self.pos = self.pos_to
		
	def go_to(self, newpos, time):
		self.pos_from = self.pos
		self.pos_to = Vec2(newpos)
		self.timer = 0.0
		self.tween_time = time
	
	def center_on(self, newpos, time, screen_size):
		halfscreen = Vec2(screen_size) * 0.5
		self.go_to(Vec2(newpos) - halfscreen, time)
	
	def center_on_screen(self, screenpos, time, screen_size):
		self.center_on(self.to_world(screenpos), time, screen_size)
	
	def get_center(self, screen_size):
		halfscreen = Vec2(screen_size) * 0.5
		return self.pos + halfscreen
	
	def tween_value(self, t):
		return  1 - (t-1)**4
	
	def to_world(self, screen_pos):
		return Vec2(screen_pos) + self.pos
	
	def apply(self, pos):
		return Vec2(pos) - self.pos
	
	def apply_rect(self, rect):
		return (tuple(self.apply(rect.topleft)), rect.size)


