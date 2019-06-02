class Projectile:
    def __init__(self, spawnPoint, speed, color):
        self.position = spawnPoint
        self.lifeTime = 0
        self.speed = speed
        self.color = color
    
    def update(self, dt):
        self.lifeTime += dt
        self.position -= self.speed * dt

