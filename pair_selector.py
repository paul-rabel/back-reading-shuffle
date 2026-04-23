import random
import pandas as pd
import csv

print("\n" * 2)
print("-" * 65)
print("Making a random pairing of tas...")
print("-" * 65)
tas = {}
"""
Extract TA names and workload from ta_workload.csv. Put them in a dictionary:
  - 3 Assignments: TA1, TA5, TA7
  - 6 Assignments: TA2, TA3, TA6
  - 9 Assignments: TA 4
"""
with open("ta_workload.csv", mode='r') as work_file :
    reader = csv.DictReader(work_file)
    for line in reader :
        clean_ta = line['name'].strip()
        ta_work = int(line['workload'])
        if ta_work not in tas :
            tas[ta_work] = []
        tas[ta_work].append(clean_ta)

"""
Shuffle each TA group that has common workload. Add the shuffled TAs to the selection
list.
"""
sorted_tas = []
for work in tas :
    # Fisher Yates shuffle
    random.shuffle(tas[work])
    sorted_tas.extend(tas[work])

"""
Create an interleaved list for the circular selection in the following step. We will go
from a list like [1, 2, 3, 4, 5, 6, 7]
to a list like   [1, 7, 2, 6, 3, 5, 4]
"""
ta_circle = []
left = 0
right = len(sorted_tas) - 1

while left <= right:
    ta_circle.append(sorted_tas[left])
    if left != right:
        ta_circle.append(sorted_tas[right])
    left += 1
    right -= 1

"""
Lead notification for uneven TA count
"""
if len(ta_circle) % 2 == 1 :
    print(f"Backreading Lead must also review {ta_circle[1]} for Behavior/Concepts")

"""
Circular assignment such that a TA 1 will backread TA 2 and TA 3 while TA 2 will
backread TA 3 and TA 4, etc.
"""
data = []
for i in range(len(ta_circle)) :
    ta = ta_circle[i]
    category = "Code Quality/Final Slide" if i % 2 == 0 else "Behavior/Concepts"
    reviewee1 = ta_circle[(i + 1) % len(ta_circle)]
    reviewee2 = ta_circle[(i + 2) % len(ta_circle)]
    data.append({
        "Your 🫵 Name ⬇️" : ta,
        "Your Backreading Category" : category,
        "Done?" : "",
        "TAs to Backread" : f"{reviewee1}, {reviewee2}",
        "Piece of Feedback Left" : ""
    })
 
df = pd.DataFrame(data).sort_values(by="Your 🫵 Name ⬇️")
df.to_excel("backreading.xlsx", index=False)

print("-" * 65)
print("Created a randomized mapping: 'backreading.xlsx'")
print("-" * 65)
print("\n" * 2)
print(ta_circle)