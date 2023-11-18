import featuretools as ft
import pandas as pd

#DEFINE ENTITIES AND ENTITY SET

#CUSTOMERS
#CREATE DATAFRAME
customersData = {
    'CustomerID': [101, 102, 103],
    'Name': ['John Doe', 'Jane Smith', 'Mike Jordan'],
    'Email': ['john.doe@example.com', 'jane.smith@example.com', 'mike.jordan@example.com'],
    'SignupDate': ['2023-01-10', '2023-01-15', '2023-01-20']
}

customers_df = pd.DataFrame(customersData)

# CREATE EMPTY ENTITY SET
es = ft.EntitySet(id="eCommerce_set")

customers_entity = es.add_dataframe(
    dataframe=customers_df,  # DATAFRAME
    dataframe_name='Customers',  # SPECIFY ENTITY NAME
    index='CustomerID',  # UNIQUE IDENTIFIER FOR THE ENTITY
    time_index='SignupDate'
)

#PRODUCTS
productsData = {
    'ProductID': [201, 202, 203],
    'Name': ['Laptop', 'Tablet', 'Smartphone'],
    'Category': ['Electronics', 'Electronics', 'Electronics'],
    'Price': [1000, 500, 800]
}

products_df = pd.DataFrame(productsData)

products_entity = es.add_dataframe(
    dataframe=products_df,  
    dataframe_name='Products',  
    index='ProductID'  
)


#ORDERS
ordersData = {
    'OrderID': [301, 302, 303],
    'CustomerID': [101, 102, 103],
    'OrderDate': ['2023-02-01', '2023-02-05', '2023-02-10'],
    'ShipDate': ['2023-02-03', '2023-02-07', '2023-02-12']
}

orders_df = pd.DataFrame(ordersData)

orders_entity = es.add_dataframe(
    dataframe=orders_df,  
    dataframe_name='Orders',  
    index='OrderID' , 
    time_index='OrderDate',
)


#ORDERS DETAILS
orderDetailsData = {
    'OrderID': [301, 302, 303],
    'ProductID': [201, 202, 203],
    'Quantity': [1, 2, 1],
    'Discount': [0, 0.1, 0]
}

orderDetails_df = pd.DataFrame(orderDetailsData)

ordersDetails_entity = es.add_dataframe(
    dataframe=orderDetails_df,  
    dataframe_name='OrderDetails',  
    index='OrderID,ProductID'  
)



#ESTABLISH RELATIONSHIPS

relationship1 = es.add_relationship(
    parent_dataframe_name='Customers', 
    parent_column_name='CustomerID', 
    child_dataframe_name='Orders', 
    child_column_name='CustomerID'
)

relationship2 = es.add_relationship(
    parent_dataframe_name='Products', 
    parent_column_name='ProductID', 
    child_dataframe_name='OrderDetails', 
    child_column_name='ProductID'

)

relationship3 = es.add_relationship(
    parent_dataframe_name='Orders', 
    parent_column_name='OrderID', 
    child_dataframe_name='OrderDetails', 
    child_column_name='OrderID'

)

# PRINT THE ENTITYSET
print(es)


# SET PANDAS DISPLAY OPTIONS TO SHOW ALL COLUMNS AND ROWS
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)


# DEEP FEATURE SYNTHESIS
feature_matrix, feature_defs = ft.dfs(
    entityset=es,
    target_dataframe_name="Orders",
    verbose=True,
    max_depth=2
)

# PRINT THE GENERATED FEATURE MATRIX
print(feature_matrix)
print(feature_defs)




