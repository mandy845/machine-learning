import matplotlib.pyplot as plt
score_names=["Andy", "Mandy", "Amanda", "Asanda"]
score_test= [86, 94, 66,25]
x_pos = [i for i, _ in enumerate(score_names)] #labels on the x-axis
#labeling and visuals
plt.bar(x_pos, score_test, color='green')
plt.xlabel("Names")
plt.ylabel("score results")
plt.title("score for the final exam test")
plt.xticks(x_pos, score_names)
plt.show()