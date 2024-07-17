# N-gram Model Visualizer

This folder contains a web-based visualization tool for the 4-gram language model.

## Setup

1. Ensure you have Python 3.7+ installed.
2. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

## Running the Visualizer

1. Make sure you've run the main n-gram model script to generate the `ngram_probs.npy` file in the `dev/` directory.
2. From this directory, run:
   ```
   python ngram_visualizer.py
   ```
3. Open a web browser and go to `http://127.0.0.1:8050/`

## How to Use

1. Enter a 3-letter context in the input field.
2. The graph will update to show the probabilities of each letter being the next character in the sequence.
3. Experiment with different contexts to see how the model's predictions change.

## Contributing

Feel free to submit issues or pull requests if you have ideas for improving the visualization or adding new features!