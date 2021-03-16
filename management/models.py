from django.db import models

class Camera(models.Model):
    Camera_Name=models.CharField(max_length=100)
    Camera_Brand=models.CharField(max_length=100)
    Camera_Details=models.CharField(max_length=200)

    def __str__(self):
        return self.Camera_Name

class Location(models.Model):
    Loc_Name=models.CharField(max_length=100)
    Loc_Address=models.CharField(max_length=100)
    Loc_Survelliance=models.CharField(max_length=10)
    Loc_Area=models.CharField(max_length=100)

    def __str__(self):
        return self.Loc_Name

class CameraSurvelliance(models.Model):
    Loc_ID=models.IntegerField(primary_key=True)
    Camera_ID=models.IntegerField()
    Install_on=models.CharField(max_length=100)
    StreamServer=models.CharField(max_length=100)
    def __int__(self):
        return self.Loc_ID

class Camerachoose(models.Model):
    Cameraname=models.CharField(max_length=100)

    def __str__(self):
        return self.Cameraname