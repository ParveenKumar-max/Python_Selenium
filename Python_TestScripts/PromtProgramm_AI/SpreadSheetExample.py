scores_names = [
    "Ethan (93)", "Olivia (67)", "Benjamin (42)", "Emma (94)", "Noah (76)",
    "Sophia (89)", "Lucas (51)", "Mia (62)", "Alexander (80)", "Isabella (95)",
    "Henry (34)", "Ava (71)", "James (87)", "Charlotte (58)", "Antonio (96)",
    "Harper (78)", "Matthew (49)", "Amelia (92)", "Samuel (64)", "Evelyn (83)",
    "Alicia (100)", "Abigail (88)", "David (39)", "Emily (70)", "Oliver (94)",
    "Elizabeth (60)", "William (81)", "Sofia (68)", "Michael (77)", "Grace (93)"
]
# Sort the scores and names in descending order
sorted_scores_names = sorted(scores_names, key=lambda x: int(x.split(" ")[-1][1:-1]), reverse=False)

# Format the scores and names as "Name (score)" pairs
formatted_scores_names = [f"{item.split(' ')[0]} ({item.split(' ')[-1][1:-1]})" for item in sorted_scores_names]

print(*formatted_scores_names, sep = ", ")