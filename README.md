# 📸 PhotoPilot AI

An AI-powered photography assistant that generates professional captions and image descriptions using Google's Gemini Vision API.

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![Streamlit](https://img.shields.io/badge/Streamlit-1.58.0-red.svg)
![Google Gemini](https://img.shields.io/badge/Google-Gemini-orange.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)

## 🎯 Overview

PhotoPilot AI is a web-based application that leverages Google's advanced Gemini Vision API to analyze images and generate:
- **Professional Captions**: Short, engaging descriptions perfect for social media and blogs
- **Detailed Descriptions**: Comprehensive analysis of image content, composition, and visual elements

This tool is ideal for photographers, content creators, bloggers, and social media managers who want to enhance their workflow with AI-powered image analysis.

## ✨ Features

- 🖼️ **Easy Image Upload**: Drag-and-drop support for JPG, JPEG, and PNG formats
- 🤖 **AI-Powered Analysis**: Utilizes Google's state-of-the-art Gemini Vision API
- 📝 **Dual Output**: 
  - Concise captions for social media and headlines
  - In-depth descriptions for articles and documentation
- ⬇️ **Download Results**: Export generated content as text files
- 🎨 **User-Friendly Interface**: Clean, responsive web UI built with Streamlit
- ⚡ **Fast Processing**: Real-time image analysis with visual feedback
- 🔒 **Secure**: Works with your own API keys

## 🚀 Quick Start

### Prerequisites

- Python 3.8 or higher
- Google API key for Gemini API
- pip (Python package manager)

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/rashed4t4y/PhotoPilot-AI.git
   cd PhotoPilot-AI
   ```

2. **Create a virtual environment** (recommended)
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Get your Google API Key**
   - Visit [Google AI Studio](https://aistudio.google.com/app/apikey)
   - Create a new API key
   - Copy the key

5. **Set up environment variables**
   ```bash
   # Create a .env file in the project root
   echo "GEMINI_API_KEY=your_api_key_here" > .env
   ```

6. **Run the application**
   ```bash
   streamlit run app.py
   ```

7. **Access the application**
   - Open your browser and navigate to `http://localhost:8501`

## 📋 Usage

1. **Upload an Image**
   - Click on the upload area
   - Select a JPG, JPEG, or PNG image from your device
   - The image will be displayed after successful upload

2. **Analyze the Image**
   - Click the "✨ Analyze Image" button
   - Wait for the AI to process (you'll see a loading spinner)

3. **View Results**
   - **Caption**: Professional, concise description suitable for social media
   - **Description**: Detailed analysis of the image content

4. **Download Results**
   - Click "⬇ Download Result" to save both caption and description as a text file
   - The file will be named `photo_description.txt`

## 📁 Project Structure

```
PhotoPilot-AI/
├── app.py                 # Main Streamlit application
├── requirements.txt       # Python dependencies
├── .gitignore            # Git ignore rules
├── utils/
│   └── gemini.py         # Google Gemini API integration
└── README.md             # Project documentation
```

## 🔧 Configuration

### Environment Variables

Create a `.env` file in the project root:

```env
GEMINI_API_KEY=your_api_key_here
```

### Customization

You can customize the following in `app.py`:

- **Supported image formats**: Line 71 (currently: jpg, jpeg, png)
- **UI styling**: Lines 16-49 (CSS styles)
- **Page layout**: Line 10 (centered or wide)
- **Button text and icons**: Throughout the file

## 📦 Dependencies

Key dependencies used in this project:

| Package | Version | Purpose |
|---------|---------|---------|
| streamlit | 1.58.0+ | Web framework for UI |
| google-genai | 2.10.0+ | Google Gemini API client |
| python-dotenv | 1.2.2+ | Environment variable management |
| Pillow | 12.2.0+ | Image processing |
| requests | 2.34.2+ | HTTP requests |

For complete list, see `requirements.txt`

## 💡 How It Works

1. **Image Input**: User uploads an image through the Streamlit interface
2. **API Processing**: Image is sent to Google's Gemini Vision API
3. **AI Analysis**: Gemini analyzes the image and generates:
   - A professional caption
   - A detailed description
4. **Display & Export**: Results are displayed in the UI and can be downloaded

## 🛠️ Development

### Prerequisites for Development
- Git
- Code editor (VS Code, PyCharm, etc.)

### Running in Development Mode

```bash
streamlit run app.py --logger.level=debug
```

### Building Upon This Project

- **Add more analysis types**: Extend `generate_content()` in `utils/gemini.py`
- **Batch processing**: Add support for processing multiple images
- **Database integration**: Store image analysis history
- **API endpoints**: Convert to a FastAPI backend
- **Image effects**: Add post-processing filters
- **Language support**: Add multi-language caption generation

## 🐛 Troubleshooting

### API Key Not Working
- Ensure the API key is correctly set in the `.env` file
- Verify the key has access to Gemini API
- Check your Google Cloud quota hasn't been exceeded

### Image Upload Fails
- Supported formats: JPG, JPEG, PNG
- Maximum file size depends on your system memory
- Try converting the image format if issues persist

### Streamlit Connection Issues
- Ensure port 8501 is not in use
- Run: `streamlit run app.py --server.port 8502` to use a different port

### Slow Processing
- First API call may be slower due to initialization
- Large images may take longer to process
- Check your internet connection

## 📊 Performance Tips

- Use compressed images for faster processing
- Optimal image size: 1-5 MB
- First run initializes the API client (~5 seconds)
- Subsequent runs are faster (~2-3 seconds)

## 🔐 Security Notes

- **Never commit your API key** to version control
- The `.gitignore` file includes `.env` to prevent accidental commits
- Always use environment variables for sensitive data
- Be aware of API rate limits and costs

## 📄 License

This project is open source and available under the MIT License.

## 🙋 Support & Contribution

### Issues
If you encounter any problems, please [open an issue](https://github.com/rashed4t4y/PhotoPilot-AI/issues) with:
- Detailed description of the problem
- Steps to reproduce
- Error messages or screenshots

### Contributing
Contributions are welcome! Here's how to contribute:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 👨‍💻 Author

**Rashed Ahmed**
- GitHub: [@rashed4t4y](https://github.com/rashed4t4y)

## 🙏 Acknowledgments

- [Google Gemini Vision API](https://ai.google.dev/) for the powerful AI capabilities
- [Streamlit](https://streamlit.io/) for the amazing web framework
- The open-source community

## 📞 Contact

For questions, suggestions, or feedback, please feel free to:
- Open an issue on GitHub
- Contact via GitHub discussions

## 🔄 Version History

- **v1.0.0** (July 2026): Initial release
  - Image upload functionality
  - Gemini Vision API integration
  - Caption and description generation
  - Download results feature

---

<div align="center">

**Made with ❤️ using Streamlit & Google Gemini AI**

⭐ If you find this project helpful, please consider giving it a star!

</div>
