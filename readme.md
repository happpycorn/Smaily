# Discord Bot : Snail

A bot designed to gather all messages and use them to perform various tasks, such as:

## Main Function

* Catch each message in server
* Generating a weekly report
* Creating self-reports

## Additional Function

* Tagging keywords
* Adding a "Mark as Read" button
* Sending a notification to the chat when someone joins a voice channel

The weekly and self-reports will include:

* A word cloud
* The server's / self's most popular channels
* Emoji usage counter
* Sorting of important messages (such as @everyone mentions)
* A summary generated by AI

## Project Folder Structure

The structure and purpose of each folder in the project.

```bash
discord_bot/
├── asset/
│   ├── IBMPlexSansTC-Light.ttf      # Font file for generating wordcloud
│   └── wordcloud.png                # Generated wordcloud image
├── modules/
│   ├── category_fetcher.py          # Fetches category IDs
│   ├── message_analyzer.py          # Analyzes messages
│   └── message_saver.py             # Saves messages
├── database/
│   ├── db.py                        # Database functions
│   └── database.db                  # Database file, may include multiple versions
├── .env                             # Environment variables file (create manually; see setup)
├── .gitignore                       # List of files to ignore in version control
├── main.py                          # Main program entry point
├── README.md                        # Project overview
└── requirements.txt                 # Project dependencies
```

## Setup

1. Create a `.env` file and add the following:

    ```bash
    DISCORD_TOKEN=<Your_DC_Bot_Token>
    ```

2. Install requirements from `requirement.txt`

    You can use Pip:

    ```bash
    pip install -r requirements.txt
    ```

    or use Conda:

    ```bash
    conda install conda-forge::discord.py
    conda install conda-forge::python-dotenv
    conda install conda-forge::wordcloud
    conda install conda-forge::tqdm
    conda install conda-forge::sumy
    conda install conda-forge::pandas
    ```

    but ckip_transformers still need install by pip:

    ```bash
    pip install ckip-transformers
    ```

3. Run `main.py`:

    ```bash
    python main.py
    ```
