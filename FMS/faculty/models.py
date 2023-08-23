from django.db import models

class Faculty(models.Model):
    name = models.CharField(max_length=250) 
    
    def __str__(self) -> str:
        return self.name    


class department(models.Model):
    name = models.CharField(max_length=130)
    faculty = models.ForeignKey(Faculty,on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.name


class Professor(models.Model):
    fname = models.CharField(max_length=100,null=True)
    lname = models.CharField(max_length=100, null=True)
    age = models.IntegerField(null=True)    
    salary = models.IntegerField(null=True)
    department = models.ForeignKey(department,on_delete=models.PROTECT,null=True)
    Faculty = models.ForeignKey(Faculty,on_delete=models.PROTECT,null=True)

    def __str__(self):
        return f"{self.fname} {self.lname}"

class Subjects(models.Model):
    name = models.CharField(max_length=130)
