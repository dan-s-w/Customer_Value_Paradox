# Let's use just three categories this time: Dresses, which overindex among the best customers and underindexes among the
# worst, Shoes which do the reverse, and Tops which are evenly distributed.
categories = ['Dresses', 'Tops', 'Shoes']

# In this probability matrix, the row represents the customer type (in order from Frugal Fannie to Shop-aholic Shirley)
# and the column represents the category. As you can see, the first category (the left-most column) is Dresses. It is much 
# more likely to be purchased by the better customers, and the third category (the right-most column) is Shoes. It is  much 
# more likely to be bought by the worse customers. The second category (the middle column) is Tops. It is equally likely to
# be purchased by all customers. Note also that the sum of the rows is always 1 because each customer must by a product:
category_probabilities = [[0.1, 0.5, 0.4],
                          [0.2, 0.5, 0.3],
                          [0.3, 0.5, 0.2],
                          [0.4, 0.5, 0.1]]

# Now let's recreate our "receipt" We will start by creating a blank DataFrame (We do not need to define the customer
# types, because we can use the customer objects that we created earlier:
receipt = pd.DataFrame(columns = ['customer_id', 'customer_type', 'category', 'price'])

# We then loop through each customer in customers and randomly select their categories as we did earlier. Note that thks
# time the probability that each customer will select a particular category varies by customer type:
for c_id, c_type in enumerate(customers): #remember customers is our list of 1,000 customers
    c_type_index = customer_types.index(c_type)
    purchases = customer_purchases[c_type_index]
    customer_id = [c_id + 1] * purchases
    customer_type = [c_type] * purchases
    category = np.random.choice(categories, size = purchases, p = category_probabilities[c_type_index])
    price = [1] * purchases
    #Append the above data to the receipt DataFrame
    receipt = receipt.append(pd.DataFrame({'customer_id': customer_id, 'customer_type': customer_type, 
                                           'category': category, 'price': price}), ignore_index = True)

#Let's take a quick look at our receipt:
receipt.head(10)
