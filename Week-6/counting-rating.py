def main():
    reviewFile = open('restaurant_reviews.txt')

    reviewsCountDict = {}

    for line in reviewFile:
        line = line.strip()

        name, rating, comment = line.split(';')
        ratingComments = reviewsCountDict.get(rating, [])
        ratingComments.append(comment)
        reviewsCountDict[rating] = ratingComments

        #reviewsCountDict[rating] = ratingComments.append(comment)

    print(reviewsCountDict['Fair'])

    for ratingKey in reviewsCountDict:
        commentsList = reviewsCountDict[ratingKey]
        print('{}: {}'.format(ratingKey, len(commentsList)))


main()
