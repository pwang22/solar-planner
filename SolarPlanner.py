from PIL import Image

def getPixels(img):
    width, height = img.size
    total_pixels = width * height
    roof_pixels = 0;
    for pixel in img.getdata():
        if pixel == (0, 0, 0):
            roof_pixels += 1
    return [roof_pixels, total_pixels]

def main():
    print("***********CONTROL IMAGE***********")
    img1 = Image.open('Screenshot_1.jpg')
    img1_values = getPixels(img1)
    img1_percentage = img1_values[0]/img1_values[1]*100
    print("[Black pixels, total pixels]: ", img1_values)
    print("Percentage of black pixels: ", img1_percentage)
    img1.show()
    print("\n")
    
    print("**********PROCESSED IMAGE**********")
    img2 = Image.open('Screenshot_1_processed.jpg')
    img2_values = getPixels(img2)
    img2_percentage = img2_values[0]/img2_values[1]*100
    print("[Black pixels, total pixels]: ", img2_values)
    print("Percentage of black pixels: ", img2_percentage)
    img2.show()
    print("\n")
    
    #88 pixels per 200 ft    
    roof_area = img2_values[0]/88*200
    total_area = img2_values[1]/88*200
    print("Roof area: ", roof_area, " sq ft")
    print("Total area: ", total_area, " sq ft")

    print("\nApproximately 2500 solar panels of average 17.5 sq ft area can be fitted.")
    print("With 400W panels, over 700kWh can be generated per year.")
    #examples of rooftop identification algorithms:
    #http://fractalytics.io/rooftop-detection-with-keras-tensorflow
    #https://medium.com/nam-r/deep-learning-for-roof-detection-in-aerial-images-in-3-minutes-8d845f6d7f25
    #https://towardsdatascience.com/using-image-segmentation-to-identify-rooftops-in-low-resolution-satellite-images-c791975d91cc

    #sources:
    #https://www.currentresults.com/Weather/US/average-annual-sunshine-by-city.php
    #https://news.energysage.com/what-is-the-power-output-of-a-solar-panel/
    #https://www.solar-estimate.org/news/how-many-square-feet-do-you-need-and-how-much-electricity-will-it-produce
    #https://www.poughkeepsiejournal.com/story/tech/science/environment/2016/01/10/new-york-rooftop-solar-panels-rules/78407190/
    #https://www.vivintsolar.com/learning-center/how-calculate-solar-panel-output
    
    #averaging annual sunshine hrs of NYC and Buffalo, as Binghamton is without its own statistic,
    #we get about 2370 hrs of sunshine annually

    #average size solar panels are 17.5 sq ft
    #maximum output solar panels are 400 watts

    #3 ft setback from edges of roof    

    #calculate projected maximum possible annual output at 100% panel coverage
    #uses: planning tool for organizations considering conversion to solar energy
    #can calculate length of time for positive returns
    #calculate significance of solar energy towards total campus energy usage
    #how much of total campus energy can be provided by solar power?
    
main()
