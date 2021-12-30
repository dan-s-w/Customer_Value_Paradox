# Let's create an empty summary DataFrame avg_customer_value to keep track of summarized results:
avg_customer_value = pd.DataFrame(columns = ['category', 'buyer_avg_value', 'expected_avg_value', 
                                             'lower_bound', 'upper_bound', 'status'])

# Let's also create a DataFrame to keep track of the simulated average customer values for each category;
sim_avg_values = pd.DataFrame(columns = ['category', 'simulated_avg_value', 'in_normal_range'])

# Let's loop through each category, compute average customer value for buyers, and run our simulation:
for category in categories:
    
    # First we indicate whether each row is the category in the current loop iteration:
    receipt['bought_category?'] = receipt['category'] == category  
    
    # Next we assess weather each customer bought the category at least once:
    bought_category_bin = receipt.groupby('customer_id').max('bought_category?')
    
    # We now select the set of customers who bought the category at least once:
    buyers = bought_category_bin[bought_category_bin['bought_category?'] == True ].reset_index()
    
    # Now we filter receipt to just buyers to create buyer_receipt:
    buyer_receipt = receipt[receipt['customer_id'].isin(buyers['customer_id'])]
    
    # For each of this categorie's buyer_receipt we compute the average customer value:
    buyer_avg_value = buyer_receipt['price'].sum()/buyer_receipt['customer_id'].nunique()
    
    # Now let's prepare the simulation to see what customer values would be expected if the category were "regular":
    
    # Let's see how many purchases there were in this category. 
    # This will be the number of 'darts' we through during each simulation round:
    purchases = receipt['bought_category?'].sum()
    
    # Let's create an empty list to keep track of the average customer value for every simulation round:
    sim_avg_value = []

    sims = 10000 # Let's run the simulation 10,000 times (the more the better, but the longer it takes):
    for s in range(sims):
        
        # Throw as many darts as there were products_bought and record the rows indices struck.
        # Note that the parameter replace = False because when an item is purchased, it cannot be bought again:
        sim_rows = np.random.choice(np.arange(receipt.shape[0]), size = purchases, replace = False)
        
        # Filter the receipt to only the rows that were hit by darts:
        sim_items = receipt.iloc[sim_rows]
        
        # Get the unique list of customers associated with each dart strike:
        sim_customers = sim_items['customer_id'].unique()
        
        # Filter the full receipt to only the lines associated with the customers who had lines hit by a dart:
        sim_receipt = receipt[receipt['customer_id'].isin(sim_customers)]
        
        # Compute the average customer value of this simulation round and append it to the list:
        sim_avg_value.append(sim_receipt['price'].sum()/sim_receipt['customer_id'].nunique())
    
    sim_avg_value = np.array(sim_avg_value) # convert sim_avg_spend list to a numpy array
    expected_avg_value = sim_avg_value.mean() # compute the mean
    avg_value_ub = np.percentile(sim_avg_value, 97.5) # compute the upper bound of a 95% confidence interval
    avg_value_lb = np.percentile(sim_avg_value, 2.5) # compute the lower bound of a 95% confidence interval
    
    # Create an array that indicates whether each simulated average spend is within the 95% confidence interval:
    in_normal_range = ((sim_avg_value <= avg_value_ub) & (sim_avg_value >= avg_value_lb))
    
    # Create a temp DataFrame, just for this product that contains all simulation data:
    sim_avg_value_p = pd.DataFrame({'category': np.repeat(category, sims), 
                                    'simulated_avg_value': sim_avg_value, 'in_normal_range': in_normal_range})
    
    # Concatenate the temp DataFrame with the master DataFrame:
    sim_avg_values = sim_avg_values.append(sim_avg_value_p, ignore_index = False)
    
    #Determine the status of this product:
    if buyer_avg_value > avg_value_ub:
        status = 'better'
    elif buyer_avg_value < avg_value_lb:
        status = 'worse'
    else:
        status = 'normal'
        
    # We now gather the relevant data points, add it to a dictionary, and append that to the avg_customer_spend DataFrame:
    row_dict = {'category': category, 'buyer_avg_value': buyer_avg_value, 'expected_avg_value': expected_avg_value,
                'lower_bound': avg_value_lb, 'upper_bound': avg_value_ub, 'status': status}
    avg_customer_value = avg_customer_value.append(row_dict, ignore_index = True)

# For the sake of cleanliness, let's drop the now unnecessary column we created in the receipt DataFrame
receipt.drop(columns = 'bought_category?', inplace = True)

#Finally, let's take a look at avg_customer_spend DataFrame:
avg_customer_value
