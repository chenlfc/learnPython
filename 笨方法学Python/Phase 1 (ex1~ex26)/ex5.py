# 更多的变量和打印
name = 'Oven Chen'
age = 42  # not a lie
height = 69  # inches
height_as_cm = height*2.54  # cm
weight = 168  # lbs
weight_as_kg = weight*0.4535924  # kg
eyes = 'Black'
teeth = 'White'
hair = 'Black'

print("Let's talk about %s." % name)
print("He's %d inches (%d cm) tall." % (height, height_as_cm))
print("He's %d punds (%d kg) heavy." % (weight, weight_as_kg))
print("Actually that's not too heavy.")
print("He's got %s eyes and %s hair." % (eyes, hair))
print("His teeth are usually %s depending on the coffee." % teeth)

# this line is tricky, try to get it exactly right
print("If I add %d, %d, and %d I get %d." %
      (age, height, weight, age+height+weight))
