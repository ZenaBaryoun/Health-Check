# Zena Baryoun, Project 2, Due: 2/21/21
# Honor Code Staement: I received no assistance on this assignment that violates the ethical guidlines set forth by professor and class syllabus
def blood_pressure(systolic, diastolic):
	mean_pressure = (systolic + 2 * diastolic) / 3
	if (systolic > 180) or (diastolic > 120): 
		return round(1.4 * mean_pressure,2)
	elif (systolic >= 140) or (diastolic >= 90):
		return round(1.3 * mean_pressure,2)
	elif (systolic >= 130 and systolic <= 139) or (diastolic >= 80 and diastolic <= 89):
		return round(1.2 * mean_pressure,2)
	elif (systolic >= 120 and systolic <= 129) and (diastolic < 80):
		return round(1.1 * mean_pressure, 2)
	elif systolic < 120 and diastolic < 80:
		return round(1 * mean_pressure, 2)  

def standard_BMI(weight, height, ISU):
	if not ISU: 
		weight = weight / 35 
		height = height * .025
	return round (weight / height ** 2, 2)

def BMI_chart(weight, height, age, gender):
	bmi = standard_BMI(weight, height, True) 
	if age >= 18: 
		if bmi < 18.5: 
			return "underweight"
		elif bmi <= 25:
			return "normal"
		elif bmi <= 30:
			return "overweight"
		elif bmi > 30:
			return "obese"
	else: 
		if gender == "male":
			if bmi < 14:
				return "underweight"
			if bmi <= 19:
				return "normal"
			if bmi <= 22:
				return "overweight"
			if bmi > 22:
				return "obese" 
		elif gender == "female":
			if bmi < 15:
				return "underweight"
			if bmi <= 20:
				return "normal"
			if bmi <= 23:
				return "overweight"
			if bmi > 23:
				return "obese"

def HCT(red_cells, total_cells, age, gender):
	if total_cells < 1000000:
		return False
	else: 
		percent = (red_cells / total_cells) * 100  
		if age < 18 and (percent >= 36 and percent <= 40):
			return True
		elif age >= 18 and gender == "female" and (percent >= 36.1 and percent <= 44.3):
			return True 
		elif age >= 18 and gender == "male" and (percent >= 40.7 and percent <= 50.3):
			return True
		else: 
			return False 

def LDL(total, HDL, trig, age, gender):
	k = 0.2
	value = 0
	if trig < 11.3 or trig > 43.5:
		k = 0
	if total >= 250 and trig >= 43.5:
		k = .19-(int((total-250)/10)/100)
	LDL_total = int(total - HDL - (k * trig))
	if age >= 18:
		if LDL_total < 120:
			value = 0
		elif LDL_total >= 120 and LDL_total < 140: 
			value = 1 
		elif LDL_total >= 140 and LDL_total < 160:
			value = 2 
		elif LDL_total >= 160 and LDL_total < 180:
			value = 3 
		elif LDL_total >= 180 and LDL_total < 200:
			value = 4 
		elif LDL_total >= 200: 
			value = 5
		if (gender == "male" and HDL < 40) or (gender == "female" and HDL < 50):
			if value < 5:
				value += 1
		elif HDL > 70:
			if value > 0: 
				value -= 1
	elif age < 18: 
		if LDL_total < 100:
			value = 0 
		elif LDL_total >= 100 and LDL_total < 115:
			value = 1
		elif LDL_total >=115 and LDL_total < 130: 
			value = 2
		elif LDL_total >= 130 and LDL_total < 145:
			value = 3
		elif LDL_total >= 145 and LDL_total < 160: 
			value = 4 
		elif LDL_total >= 160: 
			value = 5
	return value 









