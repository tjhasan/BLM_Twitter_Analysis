<div id="top"></div>
<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
        <a href="#about-the-project">About The Project</a>
    </li>
    <li>
        <a href="#prerequisites">Prerequisites</a>
    </li>
    <li>
        <a href="#usage">Usage</a>
    </li>
    <li>
        <a href="#results">Results</a>
    </li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project
Todo

<!-- GETTING STARTED -->
## Prerequisites
Ensure you have the following python library installed:
* requests_html

<!-- USAGE EXAMPLES -->
## Usage
Before running the script, make sure you have done the following:

* Downloaded a Twitter Dataset as described in the following project repo: [blm_twitter_corpus](https://github.com/sjgiorgi/blm_twitter_corpus)
* In the same directory as script.py, you need to have a directory called `results`.

Given that you have the above, run the script using the following command:

```sh
python script.py <year and month directory>
```
The `year and month directory` should be in the format: `YYYY_MM_DD`. If you have gathered the Twitter Dataset from the above repository correctly, then this should be no problem.

Make sure `script.py`, the `YYYY_MM_DD` dataset, and the `results` directory are all in the same directory before running the script.

Please understand that due to the large size of the dataset, the script may run for a long time. Consider creating parallel windows to run in the background in order to prevent he script from ending prematurely.

## Results
The results of the script should appear in the file `./results/<filename>.txt` where `filename` was the original filename given from the dataset.

In the resulting file, every line will contain a list of strings seperated by a comma. This is the resulting data for each tweet. This data is organized with the following format:

`<text_body> , <hashtag_list> , <num_of_retweets> , <num_of_likes> , <is_a_retweet> , <is_a_quote>`

Here is a breakdown of this data:
* `text_body`
    * The body of the tweet. Will also include the hashtags used.
* `hashtag_list`
    * A comma seperated list of the all the hashtags in the given tweet body.
    * Please note that every string in this list will always start with the character `#`.
* `num_of_retweets`
    * The number of retweets the given tweet received.
* `num_of_likes`
    * The number of likes the given tweet received.
* `is_a_retweet`
    * Will always either be true or false. 
    * Signifies if the given tweet is a retweet
* `is_a_retweet`
    * Will always either be true or false. 
    * Signifies if the given tweet is a quote

You may see the following instances in the data:

`, , <int>, <int>, <bool>, <bool>`

These instances simply show that the given tweet did not have any text or hashtags in its body.