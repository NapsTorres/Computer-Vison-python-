import numpy as np
import glob
import cv2
from sklearn.neural_network import MLPClassifier
from sklearn.model_selection import train_test_split

image = cv2.imread("input/testing1.png") # read in image

# resize image while retaining aspect ratio
width = 1024
height = int(image.shape[0] * (width / image.shape[1]))
image = cv2.resize(image, (width, height), interpolation=cv2.INTER_AREA)

# create a CLAHE object to apply contrast limiting adaptive histogram equalization
output = image.copy()  # Create a copy of the image to display results
grayscale = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)  # Convert image to grayscale


def calc_histogram(img):
    mask = np.zeros(img.shape[:2], dtype="uint8")  # Create mask
    center = (int(img.shape[1] / 2), int(img.shape[0] / 2))
    cv2.circle(mask, center, 60, 255, -1)  # Draw circle
    hist = cv2.calcHist([img], [0, 1, 2], mask, [16, 16, 16], [0, 256, 0, 256, 0, 256])
    return cv2.normalize(hist, hist).flatten()  # Return normalized "flattened" histogram

    return cv2.normalize(h, h).flatten() # return normalized "flattened" histogram

def calc_hist_from_file(file):
    img = cv2.imread(file)
    return calc_histogram(img) # return histogram


class Enum(tuple):
    __getattr__ = tuple.index  # define __getattr__ to return index of tuple

# Enumerate material types for use in classifier
Material = Enum(('One', 'Five', 'Ten', 'Twenty', 'twentyfive', 'five', 'one'))

# locate sample image files
coin_one = glob.glob("train/one/*.png")
coin_five = glob.glob("train/five/*.png")
coin_ten = glob.glob("train/ten/*.png")
coin_twenty = glob.glob("train/twenty/*.png")
coin_1cents = glob.glob("train/one_cent/*.png")
coin_5cents = glob.glob("train/five_cents/*.png")
coin_25cents = glob.glob("train/twenty_five_cents/*.png")


# define training data and labels
X = []
y = []

# compute and store training data and labels
for i in coin_one:
    X.append(calc_hist_from_file(i))
    y.append(Material.One)
    
for i in coin_five:
    X.append(calc_hist_from_file(i))
    y.append(Material.Five)
    
for i in coin_ten:
    X.append(calc_hist_from_file(i))
    y.append(Material.Ten)

for i in coin_twenty:
    X.append(calc_hist_from_file(i))
    y.append(Material.Twenty)
    
for i in coin_1cents:
    X.append(calc_hist_from_file(i))
    y.append(Material.one)

for i in coin_5cents:
    X.append(calc_hist_from_file(i))
    y.append(Material.five)

for i in coin_25cents:
    X.append(calc_hist_from_file(i))
    y.append(Material.twentyfive)
    
# instantiate classifier
classifier = MLPClassifier(solver = "lbfgs")

# split samples into training and test data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.5, random_state=42)

# train and score classifier
classifier.fit(X_train, y_train) # train classifier
score = int(classifier.score(X_test, y_test) * 100) # calculate score
print("Classifier mean accuracy: ", score) # print accuracy

blurred = cv2.GaussianBlur(grayscale, (7, 7), 0)# apply edge detection to image
circles = cv2.HoughCircles(blurred, cv2.HOUGH_GRADIENT, dp=2.2, minDist=100, param1=200, param2=100, minRadius=25, maxRadius=120)


def predictMaterial(roi):
    hist = calc_histogram(roi) # calculate feature vector for region of interest
    s = classifier.predict([hist]) # predict material type
    return Material[int(s[0])] # return predicted material type

diameter = []
materials = []
coordinates = []

count = 0
# loop over the detected circles
if circles is not None:
    # append radius to list of diameters
    for (x, y, r) in circles[0, :]:
        diameter.append(r)

    circles = np.round(circles[0, :]).astype("int") # convert coordinates and radii to integers

    for (x, y, d) in circles: # loop over coordinates and radii of the circles
        count += 1

        coordinates.append((x, y)) # add coordinates to list
        roi = image[y - d:y + d, x - d:x + d] # extract region of interest
        material = predictMaterial(roi) # predict material type
        materials.append(material) # add material type to list
        # draw contour and results in the output image
        cv2.circle(output, (x, y), d, (0, 255, 0), 2)
        cv2.putText(output, material, (x - 40, y), cv2.FONT_HERSHEY_PLAIN, 1.5, (0, 0, 0), thickness = 2, lineType = cv2.LINE_AA)

# get biggest diameter
biggest = max(diameter)
i = diameter.index(biggest) # get index of biggest diameter
print(diameter) # print diameters

# scale everything according to maximum diameter
if materials[i] == "one":
    diameters = [x / biggest * 10 for x in diameter]
    scaledTo = "Scaled to 1 cents"
elif materials[i] == "five":
    diameters = [x / biggest * 16 for x in diameter]
    scaledTo = "Scaled to 5 cents"
elif materials[i] == "twentyfive":
    diameters = [x / biggest * 20 for x in diameter]
    scaledTo = "Scaled to 25 cents"
elif materials[i] == "One":
    diameters = [x / biggest * 23 for x in diameter]
    scaledTo = "Scaled to 1"
elif materials[i] == "Five":
    diameters = [x / biggest * 25 for x in diameter]
    scaledTo = "Scaled to 5"
elif materials[i] == "Ten":
    diameters = [x / biggest * 27 for x in diameter]
    scaledTo = "Scaled to 10"
elif materials[i] == "Twenty":
    diameters = [x / biggest * 30 for x in diameter]
    scaledTo = "Scaled to 20"
else:
    scaledTo = "unable to scale.."


i = 0
total = 0
while i < len(diameter): # loop over diameters
    d = diameter[i] # get diameter
    m = materials[i] # get material type
    (x, y) = coordinates[i] # get coordinates
    if m == "One": # if material is 1 peso
        t = "Peso"
    elif m == "Five": # if material is 5 peso
        t = "Pesos"
    elif m == "Ten": # if material is 10 peso
        t = "Pesos"
    elif m == "Twenty": # if material is 20 peso
        t = "Pesos"
    elif m == "one": # if material is 1 cents
        t = "cents"
    elif m == "five": # if material is 5 cents
        t = "cents"
    elif m == "twentyfive": # if material is 25 cents
        t = "cents"
    else: # if material is unknown
        t = "Unknown"
    

    # write result on output image
    cv2.putText(output, t, (x - 40, y + 22), cv2.FONT_HERSHEY_PLAIN, 1.5, (255, 255, 255), thickness = 2, lineType = cv2.LINE_AA)
    i += 1

# resize output image while retaining aspect ratio
d = 800 / output.shape[1] # calculate resize factor
dim = (800, int(output.shape[0] * d)) # get dimensions
image = cv2.resize(image, dim, interpolation=cv2.INTER_AREA) # resize image
output = cv2.resize(output, dim, interpolation=cv2.INTER_AREA) # resize output image

# write summary on output image
cv2.putText(output, scaledTo, (5, output.shape[0] - 40), cv2.FONT_HERSHEY_PLAIN, 1.0, (0, 0, 0), lineType = cv2.LINE_AA)
cv2.putText(output, "Coins detected: {}, {:2}".format(count, total / 100), (5, output.shape[0] - 24), cv2.FONT_HERSHEY_PLAIN, 1.0, (0, 0, 0), lineType = cv2.LINE_AA)
cv2.putText(output, "Classifier mean accuracy: {}%".format(score), (5, output.shape[0] - 8), cv2.FONT_HERSHEY_PLAIN, 1.0, (0, 0, 0), lineType = cv2.LINE_AA)
score = int(classifier.score(X_test, y_test) * 100)
print("Classifier mean accuracy:", score)

# show output and wait for key to terminate program
cv2.imshow("Output", output)
cv2.waitKey(0)
cv2.destroyAllWindows()


