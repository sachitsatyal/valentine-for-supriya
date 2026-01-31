# 💕 Valentine's Day Proposal App

A cute Streamlit app to ask your special someone to be your Valentine!

## Features

- 🌹 Beautiful romantic design with floating hearts
- 😜 **Escaping "No" button** - it runs away when she tries to click it!
- 📸 **Photo gallery** - displays your memories together after she says YES
- 🎉 Confetti celebration when she accepts

## Quick Start

### 1. Install Streamlit
```bash
pip install streamlit
```

### 2. Add Your Photos
Create a `photos` folder in the same directory as `valentine_app.py`:
```
your-folder/
├── valentine_app.py
├── requirements.txt
└── photos/
    ├── photo1.jpg
    ├── photo2.jpg
    ├── photo3.jpg
    ... (add up to 10 photos)
```

**Supported formats:** `.jpg`, `.jpeg`, `.png`, `.gif`, `.webp`

### 3. Run the App
```bash
streamlit run valentine_app.py
```

### 4. Deploy to Streamlit Cloud (Free!)

1. Push your code to a GitHub repository
2. Go to [share.streamlit.io](https://share.streamlit.io)
3. Sign in with GitHub
4. Click "New app"
5. Select your repository and `valentine_app.py`
6. Click "Deploy!"

**Note:** For deployment, make sure your `photos` folder is also committed to GitHub.

## Customization

### Change the Messages
Open `valentine_app.py` and edit:
- The title: Look for `"Hey Beautiful 💕"`
- The question: Look for `"Will you be my Valentine?"`
- The celebration message: Look for `"I knew you'd say yes!"`
- The final love note: Look for `"I love you more than words can say!"`

### Change the "No" Button Messages
Find the `no_messages` list and customize the teasing messages!

## Share the Love! 💝

Send her the deployed link and watch the magic happen! 🌹
