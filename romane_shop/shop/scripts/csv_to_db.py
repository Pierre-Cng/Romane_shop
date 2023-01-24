from shop.models import Product
import csv

def delete_model(model):
    model.objects.all().delete()

def loader(path = None):
    if path is None:
        raise Exception('No path was given for csv to database loading.')
    with open(path) as file:
        reader = csv.reader(file)
        next(reader) # jump the header
        for row in reader:
            row = row[0].split(';')
            product = Product(product_name = row[0],
                              category = row[1],
                              image_name = row[2],
                              price = row[3],
                              quantity = row[4],
                              description = row[5],
                              size = row[6],
                              weight = row[7],
                              color = row[8],
                              material = row[9])
            product.save()

def run(*args):
    loader(*args)
