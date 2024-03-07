if camel > 8:
    done = True
    print("Your camel died of exhaustion.")
elif camel > 5:
    print("Your camel is getting tired.")
if natives >= player:
    print("The natives have caught you, you lost!")
elif (natives - player) < 15:
    print("The natives are getting close!")