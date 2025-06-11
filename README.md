End to End Text-Summarization-Project

## Installation

### Prerequisites
- Python 3.8 or higher
- pip

### Setup Instructions

1. Clone the repository:
```bash
git clone <repository-url>
cd NLP-Text-Summarization
```

2. Install the required dependencies:
```bash
pip install -r requirements.txt
```

3. **Important Note**: If you encounter any of the following errors:
```
PegasusTokenizer requires the SentencePiece library but it was not found in your environment.
```
```
Converting from Tiktoken failed, if a converter for SentencePiece is available...
```
```
{0} requires the Cython library but it was not found in your environment.
```
```
Error initializing PegasusTokenizer: [various protobuf-related errors]
```
Make sure to restart your runtime/kernel after installing the requirements. The updated requirements.txt includes all necessary dependencies (sentencepiece, tiktoken, Cython, and protobuf 3.20.0) to resolve these issues.

**Note about Protobuf**: SentencePiece requires a compatible version of protobuf. The code has been updated to automatically check for and install protobuf 3.20.0, which is known to work well with SentencePiece. If you encounter protobuf-related errors, you can manually install the compatible version with:
```bash
pip install protobuf==3.20.0
```

The code has been updated to include a fallback mechanism that will attempt to use AutoTokenizer if PegasusTokenizer fails, but for optimal performance, it's recommended to properly install sentencepiece and restart your environment.

For Jupyter Notebook users:
- After installing requirements, restart the kernel: Kernel > Restart
- Then run your cells again

For command line users:
- After installing requirements, restart your terminal or Python environment

### Verifying Your Environment

To verify that all required dependencies are properly installed and accessible in your environment, run:
```bash
python verify_environment.py
```

This script will check for all required packages and test the initialization of PegasusTokenizer specifically. If any issues are found, the script will provide recommendations for resolving them.

**Note**: You may see warnings about NumPy compatibility (e.g., "A module that was compiled using NumPy 1.x cannot be run in NumPy 2.0.1"). These warnings don't prevent the script from running successfully and can be safely ignored for this project.

## Project Workflow
i.   Update config/config.yaml
ii.  Update NLP-Text_Summarization/params.yaml
iii. Update src/textSummarizer/entity
iv.  Update src/textSummarizer/config/configuration.py
v.   Update src/textSummarizer/components
vi.  Update the src/textSummarizer/pipeline
vii. Update NLP-Text_Summarization/main.py 
viii.Update NLP-Text_Summarization/app.py
