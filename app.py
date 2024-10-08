import streamlit as st
import pandas as pd
import joblib
from sklearn.linear_model import LogisticRegression
from lightgbm import LGBMClassifier
import os

#streamlit run app.py
def main():
    st.title("Sentiment Pediction")

    recipe_name = ['Winning Apple Crisp', 'Grilled Huli Huli Chicken','Flavorful Chicken Fajitas', 'Cheesy Ham Chowder',
       'Stuffed Pepper Soup', 'Vegetarian Linguine',
       'Rhubarb Custard Bars', 'Rustic Italian Tortellini Soup',
       'Pineapple Orange Cake', 'Porcupine Meatballs',
       'Ham and Swiss Sliders', 'Creamy White Chili',
       'Traditional Lasagna', 'Caramel-Pecan Cheesecake Pie',
       'Moist Chocolate Cake', 'Skillet Shepherd’s Pie',
       'Enchilada Casser-Ole!',
       'Pumpkin Spice Cupcakes with Cream Cheese Frosting',
       'Favorite Chicken Potpie', 'Garlic Beef Enchiladas',
       'Smothered Chicken Breasts', 'Cheeseburger Soup', 'Cherry Bars',
       'Mom’s Meat Loaf', 'Lemon Blueberry Bread',
       'Banana Bars with Cream Cheese Frosting', 'Apple Pie',
       'Best Ever Potato Soup', 'Baked Mushroom Chicken',
       'Brown Sugar Oatmeal Pancakes', 'Amish Breakfast Casserole',
       'Pumpkin Bread', 'Corn Pudding', 'Best Ever Banana Bread',
       'Bacon Macaroni Salad', 'Chicken and Dumplings',
       'Cheeseburger Paradise Soup', 'Chocolate Chip Oatmeal Cookies',
       'Zucchini Pizza Casserole', 'Baked Spaghetti', 'Hot Milk Cake',
       'Slow-Cooker Lasagna', 'Gluten-Free Banana Bread',
       'First-Place Coconut Macaroons', 'Favorite Dutch Apple Pie',
       'Chicken Wild Rice Soup', 'Baked Tilapia', 'Basic Homemade Bread',
       'Asian Chicken Thighs', 'Ravioli Lasagna',
       'Chocolate Guinness Cake', 'Mamaw Emily’s Strawberry Cake',
       'Seafood Lasagna', 'Egg Roll Noodle Bowl', 'Caramel Heavenlies',
       'Li’l Cheddar Meat Loaves', 'Forgotten Jambalaya',
       'Pork Chops with Scalloped Potatoes', 'Basic Banana Muffins',
       'Pineapple Pudding Cake', 'Simple Au Gratin Potatoes',
       'Zucchini Cupcake', 'Pumpkin Bars',
       'Peanut Butter Chocolate Dessert', 'Chicken Penne Casserole',
       'Big Soft Ginger Cookies', 'Lime Chicken Tacos',
       'Cauliflower Soup', 'Shrimp Scampi', 'Special Banana Nut Bread',
       'Sandy’s Chocolate Cake', 'Creamy Grape Salad',
       'Homemade Peanut Butter Cups', 'Fluffy Pancakes',
       'Easy Chicken Enchiladas', 'Peanut Butter Cup Cheesecake',
       'Chocolate Caramel Candy', 'Flavorful Pot Roast',
       'Bruschetta Chicken', 'Frosted Banana Bars',
       'White Bean Chicken Chili', 'Chunky Apple Cake', 'Creamy Coleslaw',
       'Twice-Baked Potato Casserole', 'Simple Taco Soup',
       'Chocolate-Strawberry Celebration Cake', 'Macaroni Coleslaw',
       'Buttery Cornbread', 'Taco Lasagna', 'Fluffy Key Lime Pie',
       'Easy Peanut Butter Fudge', 'Tennessee Peach Pudding',
       'Black Bean ‘n’ Pumpkin Chili', 'Quick Cream of Mushroom Soup',
       'Teriyaki Chicken Thighs', 'Blueberry French Toast',
       'Contest-Winning New England Clam Chowder',
       'Comforting Chicken Noodle Soup', 'Strawberry Pretzel Salad',
       'Creamy Macaroni and Cheese']

# ['UserReputation','ReplyCount','ThumbsUpCount','ThumbsDownCount','BestScore','Review_Length']
# ['ID','RecipeName','UserID','year', 'month', 'dayofweek', 'hour']
# ['Recipe_Review']

    RecipeName = st.selectbox('Select Recipe Name',recipe_name)
    UserID = st.number_input('UserID')
    UserReputation = st.number_input("UserReputation")
    ReplyCount = st.number_input("Reply Count")
    ThumbsUpCount = st.number_input("Thumbs Up Count")
    ThumbsDownCount = st.number_input("Thumbs Down Count")
    BestScore = st.number_input("Best Score")
    ID = st.number_input("ID")
    date = st.date_input("Date")
    hour = st.number_input("Hour")
    RecipeReview = st.text_area("Recipe Review")

    if st.button("Predict"):
        st.write("You are Predicting")
        Review_Length = len(RecipeReview)
        year =date.year
        month = date.month
        dayofweek = date.weekday()

        column = ['ID','UserReputation','ReplyCount','RecipeName','UserID','ThumbsUpCount','ThumbsDownCount','BestScore','year','month','dayofweek','hour','Review_Length','Recipe_Review']

        data = [[ID,UserReputation,ReplyCount,RecipeName,UserID,ThumbsUpCount,ThumbsDownCount,BestScore,year,month,dayofweek,hour,Review_Length,RecipeReview]]

        data_df= pd.DataFrame(data,columns=column)
        st.write(data_df)

         # Load the preprocessor and model
        preprocessor_path = os.path.join('preprocessor', 'preprocessor.joblib')
        model_path = os.path.join('models', 'model.joblib')

        #st.write("Preprocessor path:", preprocessor_path)
        #st.write("Model path:", model_path)

        if os.path.exists(preprocessor_path) and os.path.exists(model_path):
            preprocessor = joblib.load(preprocessor_path)
            model = joblib.load(model_path)

            # Transform and predict
            x_test_transform = preprocessor.transform(data_df)
            pred = model.predict(x_test_transform)

            st.markdown(f'<h1> Prediction for the data is : {pred} </h1>', unsafe_allow_html=True)
        else:
            st.write("Preprocessor or model file not found. Please check the file paths.")
        #st.markdown(f'<h1> Prediction for the data is : {pred} </h1>')
if __name__  == "__main__":
    main()