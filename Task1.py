v=int(input("enter the final velocity of the object in a motion."))
u=int(input("enter the initial velocity of the object in a motion."))
t=int(input("enter the time taken by the object."))
a=lambda v,u,t:(v-u)/t
print("The acceleration of the obejct in motion is ",a(v,u,t))
