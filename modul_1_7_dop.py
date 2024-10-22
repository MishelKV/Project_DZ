grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]

tudents = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
tudents=sorted(tudents)
sred_ball={}
sred_ball.update({tudents[0]:sum(grades[0])/len(grades[0]),
                 tudents[1]:sum(grades[1])/len(grades[1]),
                 tudents[2]:sum(grades[2])/len(grades[2]),
                 tudents[3]:sum(grades[3])/len(grades[3]),
                 tudents[4]:sum(grades[4])/len(grades[4])})
print(sred_ball)
print(type(sred_ball))
