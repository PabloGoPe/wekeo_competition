#The following line imports the HDA python library

from hda import Client

c = Client(debug=True)

#The following line contains the descriptor query. Think about changing it to the dataset, region and parameters needed

query = {
  "datasetId": "EO:ESA:DAT:SENTINEL-3:OL_2_LFR___",
  "boundingBoxValues": [
    {
      "name": "bbox",
      "bbox": [
        -7.499583333333334,
        42.3020216796485,
        11.999333333333333,
        54.75429195536845
      ]
    }
  ],
  "dateRangeSelectValues": [
    {
      "name": "position",
      "start": "2021-01-01T00:00:00.000Z",
      "end": "2021-01-02T00:00:00.000Z"
    }
  ],
  "stringChoiceValues": [
    {
      "name": "productType",
      "value": "LFR"
    },
    {
      "name": "processingLevel",
      "value": "LEVEL2"
    }
  ]
}

# The following line runs the query
matches = c.search(query)

# The following line prints the products returned by the query
print(matches)

#The download starts. All the products found in the query are downloaded consecutively
matches.download()

