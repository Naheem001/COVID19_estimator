from django.db import models

# Create your models here.
class Region:
    name: str
    avgAge: float
    avgDailyIncomeInUSD: int
    avgDailyIncomePopulation: float



class Data:
    region: Region
    periodType: str
    timeToElapse: int
    reportedCases: int
    population: int
    totalHospitalBeds:int