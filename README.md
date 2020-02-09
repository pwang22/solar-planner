# solar-planner

This is a hackathon project designed during HackBU 2020.
Recommended method of running: run through IDLE using Python 3.7

As we know, solar panels generate clean, renewable energy from the sun, and are often mounted on rooftops.
In order to promote solar energy and reduce ecological footprint, we designed an algorithm to model potential costs and benefits of solar panel installation.
We hope our algorithm can be used effectively as a tool for urban planners or organizations such as college campuses.
For our project, we used Binghamton University as an example.

We first retrieved an image of the Brain from Google Maps.
Originally, we tried to use computer vision with Keras and Tensorflow to identify rooftops from satellite images.
Unfortunately, we did not find this achievable in 24 hours.
However, we know for sure that using machine learning to identify rooftops is very much possible and accurate, from previous unrelated work of others on the Web.

So, rather than focusing on training our own object recognition, we tried to simulate the effects of an object recognition algorithm that was previously successful in separating satellite imagery into rooftop and non-rooftop layers.

We assumed the success of said algorithm, filled the rooftops in black (RGB 0,0,0), then used Python's Pillow library to iteratively deduce the total rooftop area in pixels.
We chose black as this was an uncommon pixel color within the image and therefore would result in low error. 
To make sure, we scanned the image for black pixels before isolating the rooftops, which detected 0.01% of the image to be black pixels, i.e. 99.99% of the image was not black.
After isolating the rooftops, we found approximately 11.13% of the image to be black pixels.

We then scaled the pixel measurements to calculate available roof space in sq ft, which resulted in around 45,000 sq ft of rooftop space around the Brain.
Average solar panel area is 17.5 sq ft, so this means approximately 2500 residential sized solar panels can be fitted.
Residential size solar panels can generate up to 400 watts. According to a formula from Vivint Solar, over 700 kWh of electricity can be generated per year.

These values could be compared against statistics on current electricty usage on campus to determine how significant the impact would be on our campus's ecological footprint.
However, we were unable to find such statistics.

Note: After adding labels to images for clarity, measurements were slightly changed. These changes are not reflected here. Images without labels that will correctly reproduce these results can be found in imgbackup folder.

Ways we could make this model better:
Actually implement machine learning and automate process
Get more data and add more features, e.g. costs, return calculations
Add more precision/accuracy; we assumed several things such as panel size and efficiency,
we didn't take into account roof setback (solar panels in NYS need to be at least 3 feet away from roof edges, according to some sources), panel orientation,
variable weather conditions, and many other factors


examples of rooftop identification algorithms:
http://fractalytics.io/rooftop-detection-with-keras-tensorflow
https://medium.com/nam-r/deep-learning-for-roof-detection-in-aerial-images-in-3-minutes-8d845f6d7f25
https://towardsdatascience.com/using-image-segmentation-to-identify-rooftops-in-low-resolution-satellite-images-c791975d91cc

sources:
https://www.currentresults.com/Weather/US/average-annual-sunshine-by-city.php
https://news.energysage.com/what-is-the-power-output-of-a-solar-panel/
https://www.solar-estimate.org/news/how-many-square-feet-do-you-need-and-how-much-electricity-will-it-produce
https://www.poughkeepsiejournal.com/story/tech/science/environment/2016/01/10/new-york-rooftop-solar-panels-rules/78407190/
https://www.vivintsolar.com/learning-center/how-calculate-solar-panel-output
