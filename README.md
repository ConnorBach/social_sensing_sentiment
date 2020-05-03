# sentiment_analysis

Important: add your Twitter keys to the crawler.py file
and the getTweetSentiment.py file

Command to run api:  
python3.6 api.py  
  
API Usage:
GET http://URL_OF_API:5000?query=search  
  
Replace the word search with your desired search term
  
API will return a JSON formatted as follows:  
{  
    positive:  20  
    negative:  30  
    neutral:   50  
}  
  
This represents the percentage of tweets having the specified sentiment.  

