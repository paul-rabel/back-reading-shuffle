import random
import pandas as pd

print("\n" * 2)
print("-" * 50)
print("Making a random pairing of tas...")
print("-" * 50)
tas = []
with open("ta.txt", mode='r') as ta_file :
    # Get list of ta names
    for ta in ta_file :
        clean_ta = ta.strip()
        tas.append(clean_ta)

# Fisher Yates shuffle
curr = 0
for ta in tas : 
    idx = random.randint(curr, len(tas) - 1)
    tas[curr], tas[idx] = tas[idx], tas[curr]
    curr += 1

if len(tas) % 2 == 1 :
    print(f"Backreading Lead must also review {tas[-1]}")

data = []
for i in range(len(tas)) :
    ta = tas[i]
    category = "Code Quality/Final Slide" if i % 2 == 0 else "Behavior/Concepts"
    reviewee1 = tas[(i + 1) % len(tas)]
    reviewee2 = tas[(i + 2) % len(tas)]
    data.append({
        "Your 🫵 Name ⬇️" : ta,
        "Your Backreading Category" : category,
        "Done?" : "",
        "TAs to Backread" : f"{reviewee1}, {reviewee2}",
        "Piece of Feedback Left" : ""
    })  
 
df = pd.DataFrame(data).sort_values(by="Your 🫵 Name ⬇️")
df.to_excel("backreading.xlsx", index=False)

print("-" * 50)
print("Created a randomized mapping: 'backreading.xlsx'")
print("-" * 50)
print("\n" * 2)