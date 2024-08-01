marks = [60,77,80,55,30,65,70,90,99,120,110]
grade = ""
for i in marks:
    if i > 100:
        grade ="Invalid marks"
    else:
        if i < 40:
            grade = "Fail"
        elif i < 60:
            grade = "C"
        elif i < 70:
            grade ="B"
        elif i < 90:
            grade ="A"
        elif i <= 100:
            grade ="A1"
    print(f"{i} - {grade} Grade")
