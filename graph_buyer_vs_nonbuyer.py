from matplotlib import pyplot as plt
import seaborn as sns
sns.set()
x = yesbuyer_vs_nonbuyer['category_probability']
avg_value = receipt['price'].sum()/receipt['customer_id'].nunique()
ax = plt.plot(x, yesbuyer_vs_nonbuyer['yes_buyer_avg_value'],'o', color = 'darkgreen', label = 'buyer avg value')
ax[0].axes.plot(x, yesbuyer_vs_nonbuyer['non_buyer_avg_value'], 'o',  color = 'darkred', label = 'non-buyer avg value')
ax[0].axes.plot(x, np.ones(yesbuyer_vs_nonbuyer.shape[0]) * avg_value, color = 'navy', label = 'all customers')
ax[0].axes.xaxis.set_major_formatter('{x:1.0%}')
ax[0].axes.yaxis.set_major_formatter('${x:1.0f}')
plt.xlabel('Probability that Product from Category is Purchased')
plt.ylabel('Average Customer Value')
plt.title('Average Value of Buyers vs. Non Buyers of Specific Categories')
plt.legend()
ax[0].axes.annotate('average customer value = $' + str(np.round(avg_value,2)),
                    (ax[0].axes.viewLim.bounds[2] * 0.95 , avg_value), color = 'navy')
for c in [4, 6, 7, 8, 9]:
    ax[0].axes.annotate(yesbuyer_vs_nonbuyer.loc[c, 'category'] + ': ' + 
                        '${:1.2f}'.format(yesbuyer_vs_nonbuyer.loc[c, 'yes_buyer_avg_value']),
                        (yesbuyer_vs_nonbuyer.loc[c, 'category_probability'], 
                         yesbuyer_vs_nonbuyer.loc[c, 'yes_buyer_avg_value'],))
for c in [2, 4, 8, 9]:
    ax[0].axes.annotate(yesbuyer_vs_nonbuyer.loc[c, 'category'] + ': ' + 
                        '${:1.2f}'.format(yesbuyer_vs_nonbuyer.loc[c, 'non_buyer_avg_value']),
                        (yesbuyer_vs_nonbuyer.loc[c, 'category_probability'], 
                         yesbuyer_vs_nonbuyer.loc[c, 'non_buyer_avg_value'],))
plt.show()
