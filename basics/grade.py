mark_art = input("Enter mark for art : ")
mark_art = int(mark_art)
mark_science = input("Enter mark for science : ")
mark_science = int(mark_science)
mark_lit = input("Enter mark for Literature : ")
mark_lit = int(mark_lit)

avg_mark = (mark_art + mark_science + mark_lit) / 3
print(f"Your average mark : {avg_mark}")

if avg_mark >= 50 : 
    print("Grade A")
elif avg_mark >= 30 : 
    print("Grade B")
elif avg_mark >=15 : 
    print("Grade C")
else: 
    print("Grade D")
