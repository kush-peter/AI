x_i = [98,85,80,70,60]
y_i = [85,95,70,65,70]

#sum of x and y
sum_x = sum(x_i)
sum_y = sum(y_i)
#mean
xBar = float (sum_x/len(x_i))
yBar = float (sum_y/len(y_i))

xi_xBar = []
yi_yBar = []
#x-xbar y-ybar
for p in x_i:
    xi_xBar.append(p - xBar)
for p in y_i:
    yi_yBar.append(p - yBar)

#xxbarsq yybarsq
sq_xxbar = []
sq_yybar = []

for q in xi_xBar:
    sq = q*q
    sq_xxbar.append(sq)
    
for q in yi_yBar:
    sq = q*q
    sq_yybar.append(sq)

diff_xy = []
for r in range(5):
    diff_xy.append((xi_xBar[r])*(yi_yBar[r]))




