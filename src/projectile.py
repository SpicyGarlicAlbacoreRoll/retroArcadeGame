class Projectile:
    def __init__(self, spawn_point, speed, color):
        self.position = spawn_point
        self.lifeTime = 0
        self.speed = speed
        self.color = color
    
    def update(self, dt):
        self.lifeTime += dt
        self.position -= self.speed * dt

