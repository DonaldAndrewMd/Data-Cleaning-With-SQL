import numpy as np
import pandas as pd
from datetime import datetime, timedelta
import random

#This seed below will ensure that anyone who runs this script will get the same dataset I did.
np.random.seed(42)
random.seed(42)

num_students = 1500

first_names =['favour','Esther','Blessing','precious','Joy','DIVINE','Ayomide','Jessica','Sharon','mercy','Anu','chinonso','chinelo','Queen','Jennifer','Waajidah','Zita','Margaret','Rachael','kiara','Treasure','Mary','olabisi','kebe','rosemary','Grace','zainab','oreoluwa','Redeem','Hellen','dorcas','Diana','Kelechi','stella','Rose','Anie','stephanie','Chiamaka','Adaeze','Victoria','Pollyanna','Blossom','sophia','Temitope','Ashley','Iyanuoluwa','katrine','Patricia','anna','Marie','Gabriel','benita','ajigbotoso','Gloria','Justin','Enny','Amala','Tife','Patience','Vika','Maryjane','Debby','marisha','Alma','prudent','Joyce','Anny','Yogamama','Bella','vanessa','Laye','Jasmine','Weneydarl','MinRee','Loveth','Rita','Ummu','Kel','Oputa','racheal','Bethel','Gem','Doria','Kaothara','Chidera','Michelle','Taiwo','Cleo','AMANDA','Omotolani','joycey','Ashimedua','William','Gemma','Abisoye','owoeye','lylian','Diepreye','velma','melody','Emmanuel','Michael','samuel','Victor','DANIEL','David','Peter','Isaac','Sam','paul','Joseph','Israel','Charles','Williams','Kingsley','kelvin','gabriel','vincent','SOLOMON','IDRIS','azeez','Richard','George','Prince','John','stephen','Alex','Walter','Raphael','Francis','Joel','Jude','Goodluck','Micheal','chidi','Pascal','Shalom','sodiq','Adewale','Muhammed','Adeyemi','Ayobami','zion','jeffrey','oyekunle','victory','Chukwuka','joy','Ekele','ejike james','kristos','Young','Prosper','Jonathan','Wales','Daniel Scott','Oluwashola','sheriff','Mavis','Ub','Toheeb','Bezaleel','Alin','Noxy','Chinenerem','amara','icety','Sylvester','bolaji','Misan','Etido','max','Elijah','Colade','Divon','Okwuchukwu','Jibrin','AUWAL','Fisayo','olaolu','monday','Gideon','timmy','ikeora mark ekene','Henry jack','Oni','rex','Kofi','kizito','Umar','JAKE','mofe','ceaser','Tini','kenny','Ahmad','Ola','James','Kester','Oscar']
last_names=['Adeoye','Adebayo','Ogunleye','Adewale','Olawale','Akinlade','Ogunyemi','Akinyemi','Ojo','Akinola','Okoro','Balogun','Okeke','Bello','Okafor','Danladi','Olaleye','Eze','Olatunji','Fashola','Owolabi','Ibrahim','Oyedele','Idris','Afolabi','Ige','Aina','Jimoh','Ajayi','Kareem','Alabi','Lawal','Aluko','Makanjuola','Momoh','Nwankwo','Nwachukwu','Obi','Nwosu','Odeyemi','Onyemaechi','Ogunbiyi','Osagie','Olufemi','Salami','Olusola','Sodiq','Olutayo','Taiwo','Owolabi','Tijani','Popoola','Umaru','Raji','Usman','Suleiman','Yusuf','Yakubu','Akinyemi','Abiodun','Akinlade','Abiola','Akinola','Adedayo','Akinyemi','Adekunle','Ogunleye','Adeola','Olawale','Adeyemi','Okoro','Adesina','Okeke','Adetola','Okafor','Ajibola','Olaleye','Alade','Olatunji','Alemika','Oyedele','Alozieuwa','Afolabi','Amusan','Aina','Anibaba','Jimoh','Anjorin','Kareem','Arigbabuwo','Lawal','Awosika','Makanjuola','Ayeni','Momoh','Bankole','Nwankwo','Bashir','Nwachukwu','Bello','Obi','Dada','Nwosu','Danjuma','Odeyemi','Ekechukwu','Ogunbiyi','Ezeokafor','Olufemi','Fashola','Olusola','Ganiyu','Olutayo','Hassan','Owolabi','Ibrahimovitch','Popoola','Idrisovitch','Rajiovitch','Igeovitch','Suleimanovitch','Yakubuovitch']

# Intentionally created typo variants
# last_name_variants = {
#     "Okafor": ["Okafor", "Okafore", "Okaforr", "Okafoor"],
#     "Adeyemi": ["Adeyemi", "Adeyemmi", "Adeyemie"],
#     "Balogun": ["Balogun", "Balogoon", "Balogunn"],
#     "Lawal": ["Lawal", "Lawall", "Lawaal"],
#     "Obi": ["Obi", "Obie", "Obii"]
# }

parent_titles = [
    "Mr", "Mr.", "Mister", "MR", "mr",
    "Mrs", "Mrs.", "Misses", "MRS", "mrs"
]

classes = {
    "SS1": ("Miss Ademide Joanna", "08031234567"),
    "SS2": ("Mr Okoye John", "08033445566"),
    "SS3": ("Mr Yusuf Ibrahim", "08023455599"),
}

subjects = {
    "Mathematics": "Mr Bello Ahmed",
    "English": "Mrs Johnson Mary",
    "Biology": "Dr Adebayo Tunde",
    "Chemistry": "Mr Musa Lawal",
    "Physics": "Mr Okonkwo James"
}

terms = [("1st", 2024), ("2nd", 2024)]

rows = []
students = []

# Generating Students
for i in range(num_students):
    fname = random.choice(first_names)

    canonical_lname = random.choice(list(last_name_variants.keys()))
    lname = random.choice(last_name_variants[canonical_lname])

    # Random casing / spaces
    if random.random() < 0.2:
        lname = lname.upper()
    if random.random() < 0.1:
        lname = f" {lname} "

    student_name = f"{fname} {lname}".strip()
    student_id = f"STU{str(i+1).zfill(4)}"
    gender = random.choice(["M", "F"])

    title = random.choice(parent_titles)
    parent_name = f"{title} {lname}".strip()
    parent_phone = f"080{random.randint(10000000, 99999999)}"

    students.append((student_id, student_name, gender, parent_name, parent_phone))

# expansion of the records
for student_id, student_name, gender, parent_name, parent_phone in students:

    class_name = random.choice(list(classes.keys()))
    class_teacher, teacher_phone = classes[class_name]

    for term_name, year in terms:
        fees_paid = random.choice(["Yes", "No"])

        # payment_date = (
        #     datetime(2024, 1, 1) + timedelta(days=random.randint(1, 120))
        #     if fees_paid == "Yes"
        #     else pd.NaT
        # )
        #The above code generates a timestamp thats incompatible with Postgres date format
        #The one below is better conforming:

          payment_date = ((datetime(2024, 1, 1) + timedelta(days=random.randint(1, 120))).strftime('%Y-%m-%d') if fees_paid == "Yes" else '')

        for subject_name, subject_teacher in subjects.items():
            ca1 = np.random.randint(5, 20)
            ca2 = np.random.randint(5, 20)
            exam = np.random.randint(30, 60)

            total = ca1 + ca2 + exam
            grade = "A" if total >= 70 else "B" if total >= 60 else "C" if total >= 50 else "F"

            rows.append([
                student_id, student_name, gender,
                class_name, class_teacher, teacher_phone,
                subject_name, subject_teacher,
                term_name, year,
                ca1, ca2, exam, total, grade,
                fees_paid, payment_date,
                parent_name, parent_phone
            ])

columns = [
    "student_id", "student_name", "gender", "class_name",
    "class_teacher", "teacher_phone",
    "subject_name", "subject_teacher",
    "term_name", "year",
    "ca1", "ca2", "exam", "total", "grade",
    "school_fees_paid", "payment_date",
    "parent_name", "parent_phone"
]

df_dirty = pd.DataFrame(rows, columns=columns)
df_dirty.to_csv("BFSS_MASTER_RECORD.csv", index=False)


