class Camera:
    mark = "Canon"
    cost, meagapixels, weidth = 0, 0, 0.0
    total_cost = 0

    def __init__(self, mark="Canon", cost=0, megapixels=0, weidth=0.0):
        self.mark = mark
        self.cost = cost
        self.megapixels = megapixels
        self.weidth = weidth
        Camera.total_weigth += self.cost

    def to_string(self):
        print("Mark: " + self.mark  + ", cost: "
              + str(self.cost) + ", megapixels: " + str(self.megapixels) +", weidth: " + str(self.weidth))

    def print_sum(self):
        print("A camera mark is " + self.name + " cost " + str(self.cost))

    @staticmethod
    def print_static_sum():
        print("Total weigth of all cameras = " + str(Camera.total_weigth))


if __name__ == "__main__":
    canon = Camera()
    nikon = Camera("Nikon", 30599, 36, 555.56)
    sony = Camera("Sony", 44999, 40, 300.50)
    canon.to_string()
    nikon.to_string()
    sony.to_string()
    Camera.print_static_sum()
    nikon.print_sum()
    sony.print_sum()