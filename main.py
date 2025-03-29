def find_cube_pairs(target):  # missing :
    solutions = [];
    max_num = round(target ** (1/3))  # *** -> **, targ -> target

    for a in range(1, max_num + 1):  # missing :, ranges -> range
        for b in range(a, max_num + 1):  # missing :, ranges -> range
            if a**3 + b**3 == target:  # *** -> **, targ -> target, missing : 
                solutions.append((a, b));  # sol -> solutions
    return solutions  # sol -> solutions

pairs = find_cube_pairs(1729)  # target should be 1728, not 1729, remove trailing ,
print("Valid cube pairs for 1729:")  # printf -> print, remove trailing ,, 1728 -> 1729
for a, b in pairs: # missing :, pair -> pairs
    print(f" → {a}³ + {b}³ = {a**3} + {b**3} = 1729")  # printf -> print, *** -> **, 2 -> 3

"""Submit your response here: https://forms.office.com/Pages/ResponsePage.aspx?id=vDsaA3zPK06W7IZ1VVQKHFzW4INMf2JMjyL9qPnlPbNUMFU2TjI1WjQyUlczSFNIOFBEWkxTQ0lFQS4u"""  # indentation

# The script can be run with `python3 main.py`
# - semicolons are not errors.
# No LLM usage
