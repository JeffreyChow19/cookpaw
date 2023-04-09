import sqlite3
import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from controller.controller import *

if __name__ == "__main__":
    if not os.path.exists("src/database/cookpaw.db"):
            conn = sqlite3.connect("src/database/cookpaw.db")
            c = conn.cursor()
            c.execute("""
            CREATE TABLE IF NOT EXISTS articles (
            article_id integer PRIMARY KEY AUTOINCREMENT,
            title text,
            content text,
            author text,
            publish_date date
            )
            """)
            c.execute("""
            CREATE TABLE IF NOT EXISTS notes (
            note_id integer PRIMARY KEY AUTOINCREMENT,
            title text,
            content text,
            publish_date date
            )
            """)
            c.execute("""
            CREATE TABLE IF NOT EXISTS recipes (
            recipe_id integer PRIMARY KEY AUTOINCREMENT,
            title text,
            utensils text,
            ingredients text,
            steps text,
            last_modified text,
            author text DEFAULT 'system'
            )
            """)
            c.execute("""
            CREATE TABLE IF NOT EXISTS photos (
            photo_id integer PRIMARY KEY AUTOINCREMENT,
            path text
            )
            """)
            c.execute("""
            CREATE TABLE IF NOT EXISTS recipe_photos (
            recipe_id integer,
            photo_id integer,
            PRIMARY KEY (recipe_id, photo_id),
            FOREIGN KEY (recipe_id) REFERENCES recipes(recipe_id),
            FOREIGN KEY (photo_id) REFERENCES photos(photo_id)
            )
            """)
            c.execute("""
            CREATE TABLE IF NOT EXISTS notes_photos (
            notes_id integer,
            photo_id integer,
            PRIMARY KEY (notes_id, photo_id),
            FOREIGN KEY (notes_id) REFERENCES notes(notes_id),
            FOREIGN KEY (photo_id) REFERENCES photos(photo_id)
            )
            """)
            c.execute("""
            CREATE TABLE IF NOT EXISTS article_photos (
            article_id integer,
            photo_id integer,
            PRIMARY KEY (article_id, photo_id),
            FOREIGN KEY (article_id) REFERENCES articles(article_id),
            FOREIGN KEY (photo_id) REFERENCES photos(photo_id)
            )
            """)
            conn.commit()
            conn.close()


    article_seeder=[
          {
            "title":"Indonesian Cuisine: A Delicious and Diverse Culinary Experience",
            "content":"Indonesian cuisine is a rich and diverse culinary experience that draws from the many different cultures and regions that make up this beautiful archipelago. From spicy and savory dishes to sweet and refreshing desserts, Indonesian food offers something for everyone.\nOne of the most popular dishes in Indonesian cuisine is nasi goreng, a fried rice dish made with a variety of spices and ingredients such as shrimp, chicken, eggs, and vegetables. Another staple of Indonesian cuisine is satay, which consists of skewered and grilled meat that is typically served with peanut sauce and rice cakes.\n For those with a taste for spicy food, sambal is a must-try condiment. Made with chili peppers, garlic, and other seasonings, sambal can be found in many Indonesian dishes and adds a delicious kick to any meal.\n Indonesian cuisine also offers a wide range of sweet treats, including kue, traditional cakes made from rice flour, coconut milk, and sugar. One popular example is kue lapis, a colorful layered cake that is often served during celebrations and holidays.\n Beyond the delicious food, Indonesian cuisine is also a reflection of the country's rich history and cultural heritage. The influences of Chinese, Indian, and Dutch cuisine can be seen in many dishes, while local ingredients and cooking techniques give Indonesian food its unique flavor and character.\n So if you're looking for a delicious and diverse culinary experience, be sure to try Indonesian cuisine. With its bold flavors and wide range of dishes, it's sure to be a feast for the senses.\n"
          },
          {
            "title":"Exploring the Delicious World of Indonesian Street Food",
            "content":"Indonesia is a country known for its vibrant street food scene, offering a diverse range of flavors and textures that tantalize the taste buds. From savory snacks to sweet treats, Indonesian street food has something for everyone.\nOne popular street food snack is martabak, a crispy fried pancake filled with various toppings such as cheese, meat, and vegetables. Another must-try street food is bakso, a type of meatball soup that is both hearty and flavorful. Sate, or grilled skewered meat, is also a popular street food that comes in many variations, such as chicken, beef, and even rabbit.\nIndonesian street food also offers plenty of sweet treats, such as es campur, a refreshing dessert made with shaved ice, fruit, and sweet syrup. Kue putu, a steamed rice cake filled with coconut and palm sugar, is another popular street food dessert.\nIn addition to its delicious flavors, Indonesian street food is also affordable and easily accessible, with vendors and food stalls lining the streets of cities and towns across the country. Street food is also a great way to connect with locals and experience the culture firsthand.\nHowever, it's important to be mindful of food safety when indulging in Indonesian street food. Look for vendors with clean and hygienic preparation areas, and avoid eating raw or undercooked foods. With these precautions in mind, exploring the world of Indonesian street food can be a tasty and unforgettable experience.\nSo next time you're in Indonesia, be sure to hit the streets and try some of the many delicious and affordable street food options. Your taste buds (and wallet) will thank you!"
          },
          {
            "title":"The Art of French Cooking",
            "content":"France is renowned for its rich culinary traditions and fine cuisine, and for good reason. French cooking is a true art form, with a long and fascinating history that has been refined over centuries. From the humble bistro to the Michelin-starred restaurant, French cuisine is celebrated worldwide for its exquisite flavors and impeccable presentation.\n\nAt the heart of French cooking is a focus on fresh, high-quality ingredients. French chefs take great care in selecting the best produce, meats, and seafood, and then skillfully prepare these ingredients using a range of techniques, from slow braising to high-heat searing. One of the hallmarks of French cuisine is its rich sauces, which are often made using classic techniques like reduction and emulsification.\n\nFrench cuisine is also renowned for its use of herbs and spices, which are used to add depth and complexity to dishes. Some of the most common herbs used in French cooking include thyme, parsley, rosemary, and tarragon, while classic spices like nutmeg, cinnamon, and clove are also used to great effect.\n\nPerhaps the most famous dish in French cuisine is coq au vin, a hearty stew made with chicken and red wine. Other classic French dishes include ratatouille, a vegetable stew made with eggplant, zucchini, and peppers, and bouillabaisse, a seafood soup that originated in Marseille. French pastries and desserts are also world-famous, with croissants, macarons, and crème brûlée being just a few examples of the many delicious treats that France has to offer.\n\nIf you're interested in learning more about French cooking, there are many resources available to help you get started. From cookbooks to online courses, you can find a wealth of information on classic French techniques and recipes. And with French cuisine being celebrated around the world\n\nyou're sure to find plenty of opportunities to sample its delicious flavors and exquisite presentation."
          }
    ]
    recipe_seeder = [
        {
            "title":"Spicy Shrimp Tacos",
            "utensils": "grill pan, tongs, mixing bowls, cutting board, knife",
            "ingredients":"1 lb large shrimp, peeled and deveined; 8-10 small tortillas; 1 avocado, diced; 1/2 red onion, sliced; 1 jalapeno, sliced; 1/4 cup chopped cilantro; 2 tbsp olive oil; 2 tbsp taco seasoning",
            "steps":"1. Preheat grill pan over medium-high heat.\n2. In a mixing bowl, toss the shrimp with olive oil and taco seasoning.\n3. Grill the shrimp for 2-3 minutes per side, until pink and slightly charred.\n4. Warm tortillas on the grill for 30 seconds per side.\n5. Assemble tacos by filling each tortilla with shrimp, avocado, red onion, jalapeno, and cilantro.\n6. Serve and enjoy!"
        },
        {
            "title":"Spicy Thai Basil Chicken",
            "utensils":"Large skillet, wooden spoon, cutting board, chef’s knife, mixing bowl",
            "ingredients":"1 lb boneless chicken thighs, cut into small pieces; 1 cup fresh basil leaves; 1 red bell pepper, sliced; 2 garlic cloves, minced; 2 Thai chilies, sliced; 2 tbsp soy sauce; 1 tbsp oyster sauce; 1 tbsp fish sauce; 1 tbsp brown sugar; 1 tbsp vegetable oil",
            "steps":"1. Heat vegetable oil in a large skillet over medium-high heat. Add garlic and chilies and cook until fragrant, about 1 minute.\n2. Add chicken and stir-fry until cooked through, about 5-7 minutes.\n3. Add red bell pepper, soy sauce, oyster sauce, fish sauce, and brown sugar. Stir-fry for another 2-3 minutes.\n4. Add fresh basil leaves and stir-fry until wilted, about 1 minute.\n5. Serve hot with steamed rice."
        },
        {
            "title":"Creamy Mushroom Risotto",
            "utensils":"Large pot, Wooden spoon, Medium pot, Pan",
            "ingredients":"1 cup Arborio rice, 1 onion, 2 garlic cloves, 1/2 cup white wine, 4 cups chicken or vegetable stock, 1 lb. sliced mushrooms, 1/2 cup grated Parmesan cheese, 1/4 cup heavy cream, Salt and pepper to taste",
            "steps":"1. Heat the stock in a medium pot and keep it at a simmer. \n2. In a large pot, heat olive oil over medium heat. Add chopped onions and garlic and sauté until they are translucent. \n3. Add the Arborio rice and stir well to coat it with the onion and garlic mixture. Cook for 2-3 minutes until the rice starts to become translucent. \n4. Pour in the white wine and stir constantly until the wine is absorbed by the rice. \n5. Add a ladleful of hot stock to the rice and stir until it is absorbed. \n6. Keep adding hot stock, one ladleful at a time, stirring constantly until the rice is cooked al dente. \n7. In a separate pan, sauté the sliced mushrooms until they are browned and tender. \n8. Once the rice is cooked, add the grated Parmesan cheese, heavy cream, and sautéed mushrooms to the pot. Stir until everything is well combined and the cheese has melted. \n9. Season with salt and pepper to taste. Serve hot!"
        }
    ]

    article_photos = [
          {
            "article_id": 1,
            "path": "images_article/indonesia_cuisine.jpg"
          },
          {
            "article_id": 2,
            "path": "images_article/indonesia_streetfood.jpg"
          },
          {
            "article_id": 3,
            "path": "images_article/french_cooking.jpg"
          }
    ]

    recipe_photos = [
          {
            "recipe_id": 1,
            "path": "images_recipe/spicy_shrimp_taco.jpg"
          },
          {
            "recipe_id": 2,
            "path": "images_recipe/spicy_thai_basil.jpg"
          },
          {
            "recipe_id": 3,
            "path":"images_recipe/creamy_mushroom_risotto.jpg"
          }
    ]

    controller = Controller("src/database/cookpaw.db")

    for article in article_seeder:
         controller.create_article(article)

    for recipe in recipe_seeder:
         controller.create_recipe(recipe)
    
    for photo in article_photos:
         controller.add_article_photo(photo)

    for photo in recipe_photos:
         controller.add_recipe_photo(photo)

    # create a connection to the database
    conn = sqlite3.connect("src/database/cookpaw.db")

    # create a cursor object
    c = conn.cursor()

    # execute a SELECT statement to retrieve data from the articles table
    c.execute("SELECT * FROM articles")

    # fetch all the rows from the result set
    rows = c.fetchall()
            



