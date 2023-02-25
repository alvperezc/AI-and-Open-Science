The script fulfills different functionalities for PDF processing.
    -First it creates a word cloud, where the key words and the most repeated words in the different documents are displayed, a word cloud is created for all the documents that are set in the "resources" folder.
    This implementation has been done using different text processing libraries such as textblop or BeautifulSoup. Where a String is created with all the keywords that are extracted and then represented graphically with worldcloud.

    -It is also able to process the number of images or figures that appear in the documents, represented in a bar chart showing how many figures appear per document.
    For this implementation we have searched the XML for all the tags that refer to "figure" and have been keeping track of each one.
    
    -Finally it has an implementation where we managed to extract from the PDF all the links and references to other pages.