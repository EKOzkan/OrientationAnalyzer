# Hashtag Based Orientation Analysis 🔍

This Python script performs sentiment analysis on tweets containing specific hashtags and calculates sentiment-based points according to predefined weights. The results are printed to the console and saved in a CSV file.
<br/>

## Project Goals

The goal of this project is to provide a proof of concept for analyzing Twitter user data and creating an orientation based on a given hashtag list. By detecting and creating a key hashtag list, such as the #maga hashtag for political orientation analysis, the script can analyze tweets and assign sentiment-based points to determine a user's alignment.

I wanted to keep the script as simple as possible, avoiding the need for training complex deep learning models. The aim was to demonstrate that orientation analysis could be achieved using basic natural language processing techniques and predefined hashtag weights.

With this script, you can perform orientation analysis without the need for extensive model training or complex setups.

## Prerequisites

- Python 3.x
- textblob library (can be installed using `pip install textblob`)

## Getting Started

1. Clone the repository or download the project files.

2. Place the following files in the same directory as the Python script:
   - `hashtags.csv`: Contains the list of hashtags, their types, and weights.
   - `tweets.txt`: Contains the tweets to be analyzed.

3. Update the `hashtags.csv` file with the desired hashtags, types (type_1, type_2 etc.), and weights.

4. Run the script using the command: `python hashtag_sentiment_analysis.py`.

5. The script will analyze the tweets in `tweets.txt` that contain the specified hashtags, perform sentiment analysis using the TextBlob library, calculate the sentiment-based points based on the weights, and display the results on the console.

6. The results, along with the tweets and their NLP points, will be saved in a file named `calc.csv` within a folder named `calc`.

## Output

The script will display the following information on the console:
- Points calculated for Type 1
- Points calculated for Type 2 etc...

Additionally, a `calc.csv` file will be generated in the `calc` folder. The CSV file will contain two columns:
- `Tweet`: The tweet that matched the specified hashtags.
- `Points`: The sentiment-based points calculated for each tweet.


## Example Hashtag Table

| Hashtag      | Type 1 | Type 2 |
|--------------|--------|--------|
| #hashtag1    | +1     | -1     |
| #hashtag2    | -0.5   | +0.5   |
| #maga        | +1     | -1     |
| #climate     | +1     | +1     |
| #technology  | -1     | -1     |

Feel free to customize the example table to match your specific hashtag requirements and weights.

## Things to Improve

- NLP Technique: The current sentiment analysis technique using the TextBlob library may not be equally successful for all languages or nuanced contexts. Consider exploring alternative NLP libraries or techniques better suited to your specific language or domain of interest.

- Twitter API Integration: Instead of manually providing a `tweets.txt` file, you can consider integrating the Twitter API to automate the tweet scraping process. This would allow real-time analysis of tweets and expand the potential for more comprehensive and up-to-date results.

- User Interface: Enhance the script by developing a user-friendly interface that allows users to input hashtags, select options, and visualize the results in a more intuitive manner.

- Performance Optimization: Optimize the script for larger datasets by implementing parallel processing techniques or utilizing distributed computing frameworks to improve efficiency and reduce processing time.

- Error Handling: Implement robust error handling and exception handling mechanisms to handle potential errors, such as network connectivity issues or invalid inputs, gracefully.

Feel free to customize the script and explore additional enhancements based on your specific needs and goals.

