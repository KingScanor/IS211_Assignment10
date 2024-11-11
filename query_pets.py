#Assignment 10

import sqlite3


def query_person_and_pets(person_id):
    conn = sqlite3.connect('pets.db')
    cur = conn.cursor()

    cur.execute("SELECT first_name, last_name, age FROM person WHERE id=?", (person_id,))
    person_data = cur.fetchone()

    cur.execute("SELECT pet.name, pet.breed, pet.age FROM pet JOIN person_pet ON pet.id = person_pet.pet_id WHERE person_pet.person_id=?", (person_id,))
    pets_data = cur.fetchall()

    conn.close()

    return person_data, pets_data

if __name__ == "__main__":
    while True:
        person_id = input("Enter person's ID number (or enter -1 to exit): ")

        if person_id == "-1":
            break

        try:
            person_id = int(person_id)
            person_data, pets_data = query_person_and_pets(person_id)

            if person_data:
                print(f"{person_data[0]} {person_data[1]}, {person_data[2]} years old")
                for pet in pets_data:
                    print(f"Owned {pet[0]}, a {pet[1]}, that is {pet[2]} years old")

            else:
                print("Person not found")
        except ValueError:
            print("Invalid input. Please enter a valid person ID.")