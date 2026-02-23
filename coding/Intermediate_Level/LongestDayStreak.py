#Step 1: Understand the Problem Clearly
#You have:
#m → number of microservices --> ( 3 )
#days → list of strings --> ["YYY", "YYY", "YNN", "YYN", "YYN"]
#Each string represents one day --> ["YYY" is 1, "YYY" is 2, "YNN" is 3, "YYN" is 4, "YYN" is 5]
#Each character in the string represents one microservice status --> YYY means 3 services
#'Y' → Passed
#'N' → Failed


def longest_streak(m, days):
    all_pass = "Y" * m    # y * 3
    current_streak = 0
    max_streak = 0

    for day in days:
        if day == all_pass:
            current_streak += 1
            max_streak = max(max_streak, current_streak)
        else:
            current_streak = 0

    return max_streak


# Example
m = 3
days = ["YYY", "YYY", "YNN", "YYN", "YYN"]

print(longest_streak(m, days))