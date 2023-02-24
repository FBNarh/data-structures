'''
COMPUTER APPLICATIONS IN CIVIL ENGINEERING CE 257_ASSIGNMENT
    @author: Favour B. Narh_6942221
    github Link: ( https://github.com/FBNarh )
Program to provide knowledge of the sales prices of available car brands in a car dealership.
'''
carBrand = {
    'Volvo':'55,000',
    'Toyota':'33,795',
    'Ford':'40,000',
    'Audi':'44,600',
    'BMW':'42,300',
    'Mercedes-Benz':'57,450',
    'Kia':'31,690',
    'Renault':'35,000',
    'Peugeot':'51,200',
    'Lamborghini':'200,000'
}           # Names & prices of available car brands
brandName=input('Please enter a car brand to check availability: ')    # get user input for car brand in interest
if brandName in carBrand:
    print('Yes, this brand is available.')
    print('The {} car costs ${}.'.format(brandName, carBrand[brandName]))
else:
    print('No, this brand is not available at the moment.')