f, axs = plt.subplots(1, 3, figsize=(15, 4))

for c, cat in reversed(list(enumerate(categories))):
    ax = axs[2 - c]
    sns.histplot(x = sim_avg_values[sim_avg_values['category'] == cat]['simulated_avg_value'], palette = ['grey', 'green'],
                 hue = sim_avg_values[sim_avg_values['category'] == cat]['in_normal_range'], legend = False, ax=ax, )
    ax.set(ylabel = None)
    ax.set(xlabel = 'Simulated Average Customer Value')
    ax.set(yticklabels = [])
    ax.grid(False)
    ax.patch.set_alpha(0.7)
    x = avg_customer_value.loc[c, 'buyer_avg_value']
    y = ax.dataLim.bounds[3]/2
    lb = avg_customer_value.loc[c, 'lower_bound']
    ub = avg_customer_value.loc[c, 'upper_bound']
    ax.fill_betweenx([0 , ax.viewLim.bounds[3]] , [lb, lb], [ub, ub], alpha = 0.2)
    ax.axvline(x, color = 'purple')
    ax.axvline(lb, color = 'green', dashes = (2,1), lw = 0.5)
    ax.annotate('Expected\nAvg.\nValue\nRange', (lb, y * 1.5), color = 'green')
    ax.axvline(ub, color = 'green', dashes = (2,1), lw = 0.5)
    ax.xaxis.set_major_formatter('${x:1.2f}')
    shift = ax.dataLim.bounds[2]/32
    ax.annotate(cat + ' Buyers\nAvg Value:\n$' + str(round(x,2)), (x + shift, y), color = 'purple')    
    ax.set_title(cat, size = 15) 

plt.show()
f.tight_layout()
