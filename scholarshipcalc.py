print("Welcome to scholarship calculator")
print("To have scholarship you need at least 70 percents")
while True:
  reg_mid = float(input("Write your register midterm: "))
  if reg_mid < 25:
    print("Register midterm below 25, Retake ❌")
    break
  else:
    reg_end = float(input("Write your register endterm: "))
    if reg_end < 25:
      print("Register endterm below 25, Retake ❌")
      break
    else:
      reg_term = (reg_mid + reg_end)/2
      if reg_term < 50:
        print(f"Register term: {reg_term} below 50, Retake ❌")
        break
      else:
        reg_final = (70 - reg_term * 0.6) / 0.4
        if reg_final < 50:
          reg_final = 50
        high_final = (90 - reg_term * 0.6) / 0.4
        if high_final > 100:
          high_final = "Impossible"
        print(f"For scholarship final exam: {reg_final:.2f}\nFor high scholarship final exam: {high_final:.2f}")
        break