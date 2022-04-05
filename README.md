<div id="top"></div>
<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

Todo

<p align="right">(<a href="#top">back to top</a>)</p>


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

<p align="right">(<a href="#top">back to top</a>)</p>