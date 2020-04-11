import math

def estimator(data):

  currentlyInfected = data['reportedCases'] * 10
  impact['currentlyInfected'] = currentlyInfected

  # factor = factorCalculator()
  if data['periodType'] == "days":
    factor = int(data['timeToElapse'] / 3)
  elif data['periodType'] == "weeks":
    factor = int((data['timeToElapse'] * 7) / 3)
  elif data['periodType'] == "months":
    factor = int((data['timeToElapse'] * 30) / 3)
    
  infectionsByRequestedTime = currentlyInfected * (2**factor)
  impact['infectionsByRequestedTime'] = infectionsByRequestedTime

  severeCasesByRequestedTime = math.floor(infectionsByRequestedTime * 0.15)
  impact['severeCasesByRequestedTime'] = severeCasesByRequestedTime

  availableBeds =availableBedsCalculator()
  hospitalBedsByRequestedTime = math.floor(availableBeds - severeCasesByRequestedTime)
  impact['hospitalBedsByRequestedTime'] = hospitalBedsByRequestedTime
  
  casesForICUByRequestedTime = math.floor(0.05 * infectionsByRequestedTime)
  impact['casesForICUByRequestedTime'] = casesForICUByRequestedTime

  casesForVentilatorsByRequestedTime = math.floor(0.02 * infectionsByRequestedTime)
  impact['casesForVentilatorsByRequestedTime'] = casesForVentilatorsByRequestedTime

  avgDailyIncomePopulation = data['region']['avgDailyIncomePopulation']
  avgDailyIncomeInUSD = data['region']['avgDailyIncomeInUSD']
  dollarsInFlight = infectionsByRequestedTime * avgDailyIncomePopulation * avgDailyIncomeInUSD * data['timeToElapse']
  impact['dollarsInFlight'] = dollarsInFlight



  currentlyInfected = data['reportedCases'] * 50
  severeImpact['currentlyInfected'] = currentlyInfected

  infectionsByRequestedTime = currentlyInfected * (2**factor)
  severeImpact['infectionsByRequestedTime'] = infectionsByRequestedTime

  severeCasesByRequestedTime = math.floor(infectionsByRequestedTime * 0.15)
  severeImpact['severeCasesByRequestedTime'] = severeCasesByRequestedTime

  hospitalBedsByRequestedTime = math.floor(availableBeds - severeCasesByRequestedTime)
  severeImpact['hospitalBedsByRequestedTime'] = hospitalBedsByRequestedTime

  casesForICUByRequestedTime = math.floor(0.05 * infectionsByRequestedTime)
  severeImpact['casesForICUByRequestedTime'] = casesForICUByRequestedTime

  casesForVentilatorsByRequestedTime = math.floor(0.02 * infectionsByRequestedTime)
  severeImpact['casesForVentilatorsByRequestedTime'] = casesForVentilatorsByRequestedTime

  dollarsInFlight = infectionsByRequestedTime * avgDailyIncomePopulation * avgDailyIncomeInUSD * data['timeToElapse']
  severeImpact['dollarsInFlight'] = dollarsInFlight

  return data

# def factorCalculator():
#   if data['periodType'] == "days":
#     factor = int(data['timeToElapse'] / 3)
#   elif data['periodType'] == "weeks":
#     factor = int((data['timeToElapse'] * 7) / 3)
#   elif data['periodType'] == "months":
#     factor = int((data['timeToElapse'] * 30) / 3)
#   return factor

def availableBedsCalculator():
  availableBeds = data['totalHospitalBeds'] * 0.35
  return availableBeds

data = {
        "region": {
            "name": "Africa",
            "avgAge": 19.7,
            "avgDailyIncomeInUSD": 5,
            "avgDailyIncomePopulation": 0.71
            },
        "periodType": "days",
        "timeToElapse": 58,
        "reportedCases": 674,
        "population": 66622705,
        "totalHospitalBeds": 1380614
      }

impact = {}
severeImpact = {}

# estimator(data)
