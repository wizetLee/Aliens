




class Settings():
    # 存储外星人入侵的所有设置的类

    def __init__(self, ):
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)
        
        self.ship_speed_factor = 30
        # 飞机可撞击aliens的数目，也就是只有3条命...
        self.ship_limit = 3

        # 子弹的配置
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
        self.bullet_speed_factor = 10
        self.bullets_allowed = 10

        # 外星人设置
        self.alien_speed_factor = 1.5
        self.fleet_drop_speed = 10
        # fleet_driection 为1表示向右移，-1表示向左移
        self.fleet_direction = 1



