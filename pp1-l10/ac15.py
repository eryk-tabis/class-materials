class TV():
    def __init__(self):
        self.is_on = False
        self.channel_no = 1
        self.channel_list = []
        self.volume = 0

    def turn_on(self):
        self.is_on = True

    def turn_off(self):
        self.is_on = False

    def show_status(self):
        print(f"TV is on, channel {self.channel_no}, volume: {self.volume}") if self.is_on else print("TV is off")

    def set_channel(self, new_channel_no):
        self.channel_no = new_channel_no

    def set_channels(self, channel_list):
        self.channel_list = channel_list

    def show_channels(self):
        print("Chanel list:")
        for i in range(len(self.channel_list)):
            print(f"{i+1}.{self.channel_list[i]}")

    def increase_volume(self):
        if self.volume+1 > 10:
            pass
        else:
            self.volume += 1

    def decrease_volume(self):
        if self.volume-1 < 0:
            pass
        else:
            self.volume -= 1
