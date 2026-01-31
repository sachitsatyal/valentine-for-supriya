import streamlit as st
import random

# Page config
st.set_page_config(
    page_title="A Special Question for my Supriya 💕",
    page_icon="💝",
    layout="centered"
)

# Custom CSS for romantic styling
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@400;600;700&family=Quicksand:wght@400;500;600&family=Dancing+Script:wght@500;600;700&display=swap');

/* Hide Streamlit branding */
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
header {visibility: hidden;}

/* Main container styling */
.stApp {
    background: linear-gradient(135deg, #ffeef8 0%, #fff5f5 50%, #fef0f5 100%);
}

/* Floating hearts animation */
.hearts-container {
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    pointer-events: none;
    overflow: hidden;
    z-index: 0;
}

.heart {
    position: absolute;
    font-size: 20px;
    animation: float-up 6s ease-in infinite;
    opacity: 0.6;
}

@keyframes float-up {
    0% {
        transform: translateY(100vh) rotate(0deg);
        opacity: 0;
    }
    10% {
        opacity: 0.6;
    }
    90% {
        opacity: 0.6;
    }
    100% {
        transform: translateY(-100px) rotate(360deg);
        opacity: 0;
    }
}

/* Title styling */
.main-title {
    font-family: 'Playfair Display', serif;
    font-size: 3.5rem;
    font-weight: 700;
    background: linear-gradient(135deg, #e91e63 0%, #ff6b9d 50%, #c2185b 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
    text-align: center;
    margin-bottom: 0.5rem;
    text-shadow: 2px 2px 4px rgba(233, 30, 99, 0.1);
}

.subtitle {
    font-family: 'Quicksand', sans-serif;
    font-size: 1.4rem;
    color: #ad1457;
    text-align: center;
    margin-bottom: 2rem;
    font-weight: 500;
}

/* Question styling */
.question-text {
    font-family: 'Playfair Display', serif;
    font-size: 2.2rem;
    color: #880e4f;
    text-align: center;
    margin: 2rem 0;
    line-height: 1.4;
}

/* Yes button styling */
div.stButton > button:first-child {
    font-family: 'Quicksand', sans-serif;
    font-size: 1.5rem;
    font-weight: 600;
    padding: 1rem 3rem;
    border-radius: 50px;
    border: none;
    background: linear-gradient(135deg, #e91e63 0%, #ff4081 100%);
    color: white;
    box-shadow: 0 8px 25px rgba(233, 30, 99, 0.4);
    transition: all 0.3s ease;
    cursor: pointer;
}

div.stButton > button:first-child:hover {
    transform: scale(1.1);
    box-shadow: 0 12px 35px rgba(233, 30, 99, 0.5);
}

/* Photo gallery styling */
.gallery-title {
    font-family: 'Playfair Display', serif;
    font-size: 2.5rem;
    color: #c2185b;
    text-align: center;
    margin: 1rem 0 2rem 0;
}

.celebration-text {
    font-family: 'Quicksand', sans-serif;
    font-size: 1.3rem;
    color: #ad1457;
    text-align: center;
    margin: 1rem 0;
}

/* Photo card styling */
.photo-card {
    background: white;
    border-radius: 20px;
    padding: 1.5rem;
    margin: 2rem 0;
    box-shadow: 0 10px 40px rgba(233, 30, 99, 0.15);
    transition: transform 0.3s ease;
}

.photo-card:hover {
    transform: translateY(-5px);
}

.photo-number {
    font-family: 'Dancing Script', cursive;
    font-size: 1.5rem;
    color: #e91e63;
    margin-bottom: 0.5rem;
}

.photo-message {
    font-family: 'Quicksand', sans-serif;
    font-size: 1.15rem;
    color: #6d4c5c;
    line-height: 1.7;
    padding: 1rem 0.5rem;
    border-left: 3px solid #f8bbd9;
    margin-top: 1rem;
    padding-left: 1rem;
    background: linear-gradient(90deg, #fce4ec 0%, transparent 100%);
    border-radius: 0 10px 10px 0;
}

/* Confetti */
.confetti {
    position: fixed;
    width: 10px;
    height: 10px;
    top: -10px;
    animation: confetti-fall 5s linear infinite;
}

@keyframes confetti-fall {
    0% {
        transform: translateY(0) rotate(0deg);
        opacity: 1;
    }
    100% {
        transform: translateY(100vh) rotate(720deg);
        opacity: 0;
    }
}

/* Final message styling */
.final-message {
    background: linear-gradient(135deg, #e91e63 0%, #ff4081 100%);
    padding: 2.5rem;
    border-radius: 25px;
    text-align: center;
    margin: 3rem 0;
    box-shadow: 0 15px 40px rgba(233, 30, 99, 0.35);
}

.final-title {
    font-family: 'Dancing Script', cursive;
    color: white;
    font-size: 2.5rem;
    margin-bottom: 1rem;
}

.final-text {
    font-family: 'Quicksand', sans-serif;
    color: #fce4ec;
    font-size: 1.2rem;
    line-height: 1.8;
}

.budget-note {
    font-family: 'Quicksand', sans-serif;
    color: #ffcdd2;
    font-size: 1rem;
    margin-top: 1.5rem;
    font-style: italic;
    opacity: 0.9;
}

/* Scroll indicator */
.scroll-indicator {
    text-align: center;
    margin: 2rem 0;
    animation: bounce 2s infinite;
}

@keyframes bounce {
    0%, 20%, 50%, 80%, 100% {
        transform: translateY(0);
    }
    40% {
        transform: translateY(-10px);
    }
    60% {
        transform: translateY(-5px);
    }
}
</style>
""", unsafe_allow_html=True)

# Floating hearts HTML
hearts_html = """
<div class="hearts-container">
"""
for i in range(15):
    left = random.randint(0, 100)
    delay = random.uniform(0, 5)
    duration = random.uniform(4, 8)
    hearts_html += f'<div class="heart" style="left: {left}%; animation-delay: {delay}s; animation-duration: {duration}s;">💕</div>'
hearts_html += "</div>"

st.markdown(hearts_html, unsafe_allow_html=True)

# Initialize session state
if 'page' not in st.session_state:
    st.session_state.page = 'question'
if 'no_position' not in st.session_state:
    st.session_state.no_position = {'top': 50, 'left': 70}
if 'no_clicks' not in st.session_state:
    st.session_state.no_clicks = 0

def move_no_button():
    """Move the No button to a random position"""
    st.session_state.no_position = {
        'top': random.randint(10, 80),
        'left': random.randint(10, 80)
    }
    st.session_state.no_clicks += 1

def say_yes():
    """Handle Yes button click"""
    st.session_state.page = 'gallery'

# Photo messages dictionary - customize your messages here!
photo_messages = {
    "photo1": {
        "title": "The Cutest Human Ever ✨",
        "message": "Look at you! 😍 How is it even legal to be THIS adorable?! Your smile could literally outshine the sun, and those eyes? Pure magic! ✨ Every time I look at you, I wonder what I did to deserve someone so incredibly, breathtakingly, ridiculously CUTE! You're not just cute, you're the definition of it. Webster's Dictionary should just put your photo next to the word! 🥺💖🦋"
    },
    "photo2": {
        "title": "Certified Hottie Alert 🔥",
        "message": "Okay okay okay... let's talk about this pose! 😏🔥 Someone was feeling themselves that day, huh? And honestly? VALID. Those goggles aren't just sitting on your face, they're having the honor of their lifetime! Looking like a whole snack... no wait, a full course meal! 🍽️ I'm not saying I'm lucky, but I'm basically winning the lottery every single day! 😎✨"
    },
    "photo3": {
        "title": "My Personal Chef 👩‍🍳💕",
        "message": "They say the way to a man's heart is through his stomach, and baby, you've got a HIGHWAY straight to mine! 🛣️❤️ Every dish you make tastes like love with extra seasoning of care. Coming home to your cooking is literally the highlight of my day! You don't just feed my stomach, you feed my soul. Gordon Ramsay could NEVER! 👨‍🍳🍳💝"
    },
    "photo4": {
        "title": "The Perfect Fit 🤗",
        "message": "Look at us! We look SO good together it should be illegal! 👫✨ But can we talk about how perfectly you fit in my arms? Like you were literally made to be there! Every hug from you feels like coming home. I could hold you forever and it still wouldn't be enough. We're not just a couple, we're a POWER couple! 💪❤️🔥"
    },
    "photo5": {
        "title": "Us vs The Problem 💪",
        "message": "Yes, we fight. Yes, we argue. But you know what? We also patch up faster than WiFi reconnecting! 📶😂 No fight is bigger than us, no argument can separate what we have. We might be stubborn, but we're stubborn TOGETHER. It's always us against the problem, never us against each other. And that's on FOREVER! 🔐💕 We're stuck with each other, and honestly? Best deal ever! 🤝❤️"
    },
    "photo6": {
        "title": "You're Welcome 😏",
        "message": "So... just a reminder of what you're getting here! 💪😂 Not only do you get a caring, loving, devoted boyfriend who would do anything for you... but ALSO this hot package! *flexes* 🏋️ It's basically a 2-in-1 deal - emotional support AND eye candy! You hit the jackpot, baby! 🎰🔥 Don't worry, this subscription is lifetime and non-refundable! 😘💝"
    },
    "photo7": {
        "title": "My Absolute Favorite 🖤",
        "message": "THIS. This is my favorite photo of you, and I will die on this hill! ⚰️✨ The way you looked in black that day? STUNNING doesn't even begin to cover it! You literally took my breath away (I almost forgot how to function). Black is definitely your color because you absolutely SLAYED! 🖤👑 I stare at this photo way more than I'd like to admit... 👀💕"
    },
    "photo8": {
        "title": "Lazy Days = Best Days 🛋️",
        "message": "Who needs fancy dates when we have THIS? 🥰 Our lazy days together are my favorite kind of days. No makeup, messy hair, just us being comfortable and silly together. You make even doing absolutely nothing feel like the most incredible adventure! Netflix, snacks, and you? That's my definition of paradise! 🍿📺💕 Every boring moment becomes special with you! ✨"
    },
    "photo9": {
        "title": "A Message From Our Baby Mochi 🐱",
        "message": "\"Meow! Mochi here 🐾 Hi Mommy! It's me, your favorite but irritating pet ! I just wanted to say that I love you SO much and I really really REALLY want you to be my Daddy's Valentine! 😺💕 He's pretty cool (he gives good head scratches), and you make him so happy! Plus, who else will I cuddle with?! Please say yes so we can be one happy family forever! Purrrr... 🐱❤️ Love, Your Baby\""
    },
    "photo10": {
        "title": "Supriya and Sachit: Forever & Always 💍",
        "message": "Look at us. Just look at us! 🥹💕 This is it. This is forever. We both know it, we both feel it. You're not just my girlfriend, you're my best friend, my soulmate, my everything. This photo isn't just a memory, it's a promise - a promise that no matter what life throws at us, we're in this TOGETHER. Forever isn't long enough with you, but it's a good start! 🌟💝∞"
    }
}

# QUESTION PAGE
if st.session_state.page == 'question':
    st.markdown('<h1 class="main-title">Hey Beautiful 💕</h1>', unsafe_allow_html=True)
    st.markdown('<p class="subtitle">I have something special to ask my baby...</p>', unsafe_allow_html=True)
    
    # Add some cute decoration
    st.markdown("<br>", unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.markdown('<p class="question-text">Will you be my Valentine Mutu? 🌹</p>', unsafe_allow_html=True)
    
    st.markdown("<br><br>", unsafe_allow_html=True)
    
    # Messages that appear when trying to click No
    no_messages = [
        "Oops! Try again 😜",
        "Haha, you can't click me!",
        "Not so fast! 💨",
        "Are you sure? Think again!",
        "The No button is shy 🙈",
        "Maybe try Yes instead? 😉",
        "I don't think you meant that!",
        "Nope, not happening! 💝",
        "Your finger slipped, right?",
        "The universe says YES! ✨"
    ]
    
    # Display message if No was attempted
    if st.session_state.no_clicks > 0:
        message = no_messages[min(st.session_state.no_clicks - 1, len(no_messages) - 1)]
        st.markdown(f"""
            <div style="
                text-align: center;
                background: linear-gradient(135deg, #ffcdd2 0%, #f8bbd9 100%);
                padding: 12px 24px;
                border-radius: 20px;
                font-family: 'Quicksand', sans-serif;
                color: #c2185b;
                font-weight: 600;
                box-shadow: 0 4px 15px rgba(0,0,0,0.1);
                margin: 1rem auto;
                max-width: 300px;
            ">
                {message}
            </div>
        """, unsafe_allow_html=True)
    
    # Button layout - No button moves to different position each click
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Create 5 columns for button positions
    positions = [0, 1, 2, 3, 4]
    no_position = st.session_state.no_clicks % 5
    
    # Make sure No is never in same position as Yes (Yes is always position 2)
    if no_position == 2:
        no_position = (no_position + 1) % 5
    
    cols = st.columns(5)
    
    # Yes button always in middle
    with cols[2]:
        if st.button("💖 YES! 💖", key="yes_btn", use_container_width=True):
            say_yes()
            st.rerun()
    
    # No button moves around
    with cols[no_position]:
        if st.button("No 😢", key="no_btn", use_container_width=True):
            st.session_state.no_clicks += 1
            st.rerun()

# GALLERY PAGE
elif st.session_state.page == 'gallery':
    # Confetti celebration
    confetti_colors = ['#e91e63', '#ff4081', '#f48fb1', '#fce4ec', '#ff80ab', '#f50057', '#c2185b', '#ad1457']
    confetti_html = ""
    for i in range(50):
        left = random.randint(0, 100)
        delay = random.uniform(0, 3)
        color = random.choice(confetti_colors)
        size = random.randint(8, 15)
        confetti_html += f"""
            <div style="
                position: fixed;
                width: {size}px;
                height: {size}px;
                background: {color};
                left: {left}%;
                top: -20px;
                animation: confetti-fall {random.uniform(3, 6)}s linear {delay}s infinite;
                border-radius: {random.choice(['50%', '0%', '30%'])};
                z-index: 1000;
            "></div>
        """
    st.markdown(confetti_html, unsafe_allow_html=True)
    
    st.markdown('<h1 class="main-title">🎉 YAY! 🎉</h1>', unsafe_allow_html=True)
    st.markdown('<p class="celebration-text">I knew you\'d say yes! You just made me the happiest person! 💕</p>', unsafe_allow_html=True)
    
    # Scroll indicator
    st.markdown("""
        <div class="scroll-indicator">
            <p style="font-family: 'Quicksand', sans-serif; color: #ad1457;">
                👇 Scroll down for our memories 👇
            </p>
        </div>
    """, unsafe_allow_html=True)
    
    st.markdown('<h2 class="gallery-title">Our Beautiful Memories 📸</h2>', unsafe_allow_html=True)
    
    # Try to load photos from a 'photos' folder
    from pathlib import Path
    
    photos_dir = Path("photos")
    
    # Check if photos directory exists and has images
    if photos_dir.exists():
        image_extensions = {'.jpg', '.jpeg', '.png', '.gif', '.webp'}
        photos = [f for f in photos_dir.iterdir() if f.suffix.lower() in image_extensions]
        # Sort numerically by extracting numbers from filename
        import re
        def get_number(filename):
            numbers = re.findall(r'\d+', filename.stem)
            return int(numbers[0]) if numbers else 0
        photos.sort(key=get_number)
        
        if photos:
            # Display photos with personalized messages
            for i, photo_path in enumerate(photos):
                photo_key = f"photo{i + 1}"
                
                # Get message or use default
                if photo_key in photo_messages:
                    title = photo_messages[photo_key]["title"]
                    message = photo_messages[photo_key]["message"]
                else:
                    title = f"Memory #{i + 1} 💕"
                    message = "Another beautiful moment with you! ❤️"
                
                # Create a beautiful card for each photo
                st.markdown(f"""
                    <div class="photo-card">
                        <p class="photo-number">Memory #{i + 1}</p>
                        <h3 style="
                            font-family: 'Playfair Display', serif;
                            color: #c2185b;
                            font-size: 1.6rem;
                            margin-bottom: 1rem;
                        ">{title}</h3>
                    </div>
                """, unsafe_allow_html=True)
                
                # Display the image
                st.image(str(photo_path), use_container_width=True)
                
                # Display the message
                st.markdown(f"""
                    <div class="photo-message">
                        {message}
                    </div>
                    <br><br>
                """, unsafe_allow_html=True)
        else:
            st.info("📷 No photos found in the 'photos' folder. Add some memories!")
    else:
        # Show placeholder with sample cards
        st.markdown("""
            <div style="
                background: linear-gradient(135deg, #fce4ec 0%, #f8bbd9 100%);
                padding: 1.5rem;
                border-radius: 15px;
                text-align: center;
                margin-bottom: 2rem;
            ">
                <p style="color: #c2185b; font-family: 'Quicksand', sans-serif;">
                    📌 <strong>To see your photos:</strong> Create a <code>photos</code> folder and add photo1.jpg through photo10.jpg
                </p>
            </div>
        """, unsafe_allow_html=True)
        
        # Show preview of what the cards will look like
        for i in range(1, 11):
            photo_key = f"photo{i}"
            title = photo_messages[photo_key]["title"]
            message = photo_messages[photo_key]["message"]
            
            st.markdown(f"""
                <div class="photo-card">
                    <p class="photo-number">Memory #{i}</p>
                    <h3 style="
                        font-family: 'Playfair Display', serif;
                        color: #c2185b;
                        font-size: 1.6rem;
                        margin-bottom: 1rem;
                    ">{title}</h3>
                    <div style="
                        background: linear-gradient(135deg, #f8bbd9 0%, #fce4ec 100%);
                        height: 250px;
                        border-radius: 15px;
                        display: flex;
                        align-items: center;
                        justify-content: center;
                    ">
                        <p style="color: #c2185b; font-family: 'Quicksand', sans-serif;">
                            📷 photo{i}.jpg will appear here
                        </p>
                    </div>
                    <div class="photo-message">
                        {message}
                    </div>
                </div>
            """, unsafe_allow_html=True)
    
    # Final message at the bottom
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("""
        <div class="final-message">
            <p class="final-title">🎊 Congratulations, My Love! 🎊</p>
            <p class="final-text">
                You're not just locked in for this Valentine's Day...<br>
                <strong>You're locked in for the REST OF YOUR LIFE!</strong> 🔐💕<br><br>
                I can't wait to build a beautiful future with you.<br>
                Every dream, every adventure, every lazy Sunday...<br>
                I want it all with YOU! 💍✨<br><br>
                Thank you for choosing me, today and always.<br>
                <strong>I love you more than words could ever express!</strong>
            </p>
            <p class="budget-note">
                P.S. - Budget was a little tight this year, so no grand gesture like last time... 😅<br>
                But hey, you got this adorable website AND my heart! That's priceless, right? 💝
            </p>
        </div>
    """, unsafe_allow_html=True)
    
    # Love message
    st.markdown("""
        <div style="
            text-align: center;
            margin: 2rem 0;
            padding: 1rem;
        ">
            <p style="
                font-family: 'Dancing Script', cursive;
                font-size: 2.5rem;
                color: #e91e63;
            ">
                Forever Yours 💕
            </p>
        </div>
    """, unsafe_allow_html=True)
    
    # Reset button (hidden at the bottom)
    st.markdown("<br><br>", unsafe_allow_html=True)
    if st.button("← Start Over", key="reset"):
        st.session_state.page = 'question'
        st.session_state.no_clicks = 0
        st.rerun()