import json
import logging
import os
from typing import List, TypeGuard
from punctuators.models.punc_cap_seg_model import PunctCapSegModelONNX, PunctCapSegConfigONNX

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


def is_list_of_strings(lst: List[str] | List[List[str]]) -> TypeGuard[List[str]]:
    return all(isinstance(x, str) for x in lst)

# Our single input results in a list of sentences once punctuation has been added
def extract_result(results: (List[str] | List[List[str]])) -> List[str]:
    if results and isinstance(results[0], list):
        return results[0]
    if is_list_of_strings(results):
        return results
    raise TypeError("Unexpected input type")

def main():
    logging.info("Starting Punctuators script")

    # Get the prompt
    input = os.environ.get('INPUT_TEXT', 'punctuation and casing are missing where should they go')
    input_texts: List[str] = [input]

    # Configure models
    model_config = PunctCapSegConfigONNX(
        directory="models/",  # Directory containing your model files
        spe_filename="spe_32k_lc_en.model",      # Name of your SentencePiece model file
        model_filename="punct_cap_seg_en.onnx",  # Name of your ONNX model file
        config_filename="config.yaml" # Name of your config file
    )

    try:
        # Instantiate the model
        m = PunctCapSegModelONNX(cfg=model_config)

        # Run inference and extract first result
        result = extract_result(m.infer(input_texts))

        # Format output
        output = {
            'input_text': input,
            'output_text': result,
            'status': 'success'
        }

    except Exception as e:
        output = {
            'input_text': input,
            'error': str(e),
            'status': 'error'
        }

    # Save output to the designated output directory
    os.makedirs('/outputs', exist_ok=True)
    output_path = '/outputs/result.json'

    with open(output_path, 'w') as f:
        json.dump(output, f, indent=2)

if __name__ == "__main__":
    main()
