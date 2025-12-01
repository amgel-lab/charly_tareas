"""
    Nombre: Angel Javier García Nieto
    Matrícula: 2530425
    Grupo: IM 1-1

    Este archivo...


"""

# Problem 1

full_name = input("Insert your full name: ")
full_name = full_name.strip()
if full_name == "":
    print("Error: Please insert a name.")
    exit()

words = full_name.split()
if len(words) < 2:
    print("Error: Please insert at least a first name and a last name.")
    exit()

clean_full_name = " ".join(words)
formatted_name = clean_full_name.title()

initials = ""
for word in words:
    initials += word[0].upper() + "."

print("Formatted Name: ", formatted_name)
print("Initials: ", initials)



