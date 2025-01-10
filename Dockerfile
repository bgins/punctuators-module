FROM python:3.11-slim

# Set working directory
WORKDIR /workspace

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Add models
RUN mkdir models
ADD https://huggingface.co/1-800-BAD-CODE/punctuation_fullstop_truecase_english/resolve/main/punct_cap_seg_en.onnx models/
ADD https://huggingface.co/1-800-BAD-CODE/punctuation_fullstop_truecase_english/resolve/main/spe_32k_lc_en.model models/
ADD https://huggingface.co/1-800-BAD-CODE/punctuation_fullstop_truecase_english/resolve/main/config.yaml models/

# Create output directory
RUN mkdir -p /outputs

# Copy inference script
COPY run_punctuators.py .

# Set entrypoint
ENTRYPOINT ["python", "/workspace/run_punctuators.py"]
