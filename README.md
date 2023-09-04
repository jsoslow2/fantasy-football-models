# Fantasy Football Draft Optimizer

This is the new github link. Now in python and with a webapp.

The model is two parts:
1. Basic ML to predict distributions of "points above replacement" for each player
2. Optimizations that takes in the prediction distribution, who's been picked, and who's likely to be on the board by your next pick, to optimize for the relative value of picking a player now vs waiting for your very specific team in your league with very specific rules.

## Website

Visit [fantasyfootballmodels.com](https://fantasyfootballmodels.com)

The website was built primarily through ChatGPT as I don't know webdev - so this is all an experiment. If it works, yay! If not, we'll learn. You gotta be arena maxxing.


## Installation

To run this project locally, follow these steps:

1. Clone the repository:
    ```bash
    git clone https://github.com/your_username/fantasy-football-models.git
    ```
2. Navigate to the project directory:
    ```bash
    cd fantasy-football-models
    ```
3. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```
4. Set up environment variables:
    ```bash
    export SECRET_KEY=your_secret_key_here
    ```
5. Run the application:
    ```bash
    flask run
    ```

## Contributing

If you'd like to contribute, please fork the repository and make changes as you'd like. Pull requests are warmly welcome.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.

## Contact

For more information, [contact Jack Soslow on Twitter](https://twitter.com/JackSoslow)

---
