
#SETTING THE MADLIB TO PRINT THE MESSAGE-------------------------
message = """
Dear {mem1},
I am having a {adj1} time at camp. The counselor is {adj2} and the food is {adj3}. I met {name} and we became {adj4} friends. Unfortunately, {name} is {adj5} and I {ed} my {body} so we couldn't go {ing} like everyone else. I need more {plural} and a {noun} sharpener, so please {adv} {verb1} more when you {verb2} back.
Your {mem2},
{person}
"""

message = message.format(**locals())
print message


