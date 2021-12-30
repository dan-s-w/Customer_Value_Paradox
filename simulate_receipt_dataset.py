# Let's start by importing our libraries:
import numpy as np
import pandas as pd

np.random.seed(0) # set random seed so results are repeatable

# Let's start with our four types of customers, their respective purchases, and their probabilities of being selected: 
customer_types = ['Frugal Fannie', 'Regular Rachel', 'Loyal Laurie', 'Shop-aholic Shirley']
customer_purchases = [1, 3, 10, 50]
customer_probabilities = [0.4, 0.3, 0.2, 0.1]

# Let's now define our categories and their probabilities of being selected:
categories = ['Scarves', 'Belts', 'Shoes', 'PJs', 'Dresses', 'Sweaters', 'Skirts', 'Shorts', 'Pants', 'Tops']
category_probabilities = [0.0087, 0.013, 0.017, 0.0323, 0.045, 0.067, 0.101, 0.151, 0.226, 0.339]

# OK let's randomly select 1,000 customers, each with the right qty of items per the above probabilities:
customers = np.random.choice(customer_types, size = 1000, p = customer_probabilities)

# Now let's create our "Receipt"! We will start by creating a blank DataFrame:
receipt = pd.DataFrame(columns = ['customer_id', 'customer_type', 'category', 'price'])

# We then loop through each customer customers, randomly select the categories for their purchases, the qty of which
# is determined by the customer's type and the price of which is set at $1 for simplicity, and append all that info to 
# the receipt DataFrame (Note this will take a minute or two):
for c_num, c_type in enumerate(customers):
    purchases = customer_purchases[customer_types.index(c_type)] #lookup the purchase count for this customer type
    category = np.random.choice(categories, size = purchases, p = category_probabilities) #randomly select the categories
    customer_id = [c_num + 1] * purchases #convert the customer_id into a purchase-length list
    customer_type = [c_type] * purchases #convert the customer_type into a purchase_length list
    price = [1] * purchases #convert the $1 price into a purchase_length list
    
    #Append the above data to the receipt DataFrame
    receipt = receipt.append(pd.DataFrame({'customer_id': customer_id, 'customer_type': customer_type, 
                                           'category': category, 'price': price}), ignore_index = True)
    
#Let's take a quick look at our receipt:
receipt.head(10)
