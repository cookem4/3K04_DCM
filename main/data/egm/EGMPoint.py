class EGMPoint:

    def __init__(self, atrium, ventricle, atrium_time, ventricle_time):
        self.atrium = atrium
        self.ventricle = ventricle
        self.atrium_time = atrium_time
        self.ventricle_time = ventricle_time

    def __str__(self):
        return "EGM(A:" + str(self.atrium) + " V:" + str(self.ventricle) + ")"
