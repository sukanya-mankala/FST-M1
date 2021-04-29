fruit_dict={
    "Apple":100,
    "Guava":60,
    "Grapes":80,
    "Banana":60,
    "Pears":150
}
fruit_to_chk =input("Enter a fruit name to check in dict ").title()

if(fruit_to_chk in fruit_dict):
    print("Yes, given fruit is available in dict")
else:
    print("No, given fruit is not available in dict")