import pandas as pd
import numpy as np
import joblib
import streamlit as st
from sklearn.linear_model import LogisticRegression

# Load trained model
@st.cache_resource
def load_model():
    try:
        model = joblib.load("real_estate_model.pkl")
        st.success("✅ Trained model loaded successfully!")
        return model
    except FileNotFoundError:
        st.error("❌ Model file 'real_estate_model.pkl' not found!")
        st.error("Please ensure the trained model file is in the repository.")
        st.stop()
    except Exception as e:
        st.error(f"❌ Error loading model: {e}")
        st.stop()

model = load_model()

st.title("🏡 Real Estate Sale Probability Predictor")

st.markdown("""
This app predicts the probability that a real estate property will sell based on:
- House age
- Distance to nearest MRT station
- Number of convenience stores nearby
- Listing price
""")

# Streamlit UI sliders
house_age = st.slider("House Age (years)", 0, 50, 10)
mrt_dist = st.slider("Distance to MRT (meters)", 0, 5000, 300)
num_stores = st.slider("Number of Convenience Stores", 0, 20, 5)
listing_price = st.slider("Listing Price (NT$/m²)", 20.0, 100.0, 45.0)

# Input DataFrame
user_input = pd.DataFrame([{
    "house_age": house_age,
    "mrt_dist": mrt_dist,
    "num_stores": num_stores,
    "listing_price": listing_price
}])

# Predict probability of sale
try:
    prob = model.predict_proba(user_input)[0][1]
    
    # Display result with color coding
    if prob >= 0.8:
        st.success(f"### 📊 Probability of Sale: **{prob*100:.2f}%** ✅")
        st.markdown("**High probability of sale!**")
    elif prob >= 0.6:
        st.warning(f"### 📊 Probability of Sale: **{prob*100:.2f}%** ⚠️")
        st.markdown("**Moderate probability of sale.**")
    else:
        st.error(f"### 📊 Probability of Sale: **{prob*100:.2f}%** ❌")
        st.markdown("**Low probability of sale. Consider adjusting the price.**")
    
    # Business recommendations
    st.markdown("---")
    st.subheader("💡 Business Recommendations")
    
    if prob < 0.6:
        st.markdown("- Consider reducing the listing price")
        st.markdown("- Highlight proximity to convenience stores if applicable")
        st.markdown("- Emphasize MRT accessibility if distance is low")
    elif prob < 0.8:
        st.markdown("- Price is reasonable but could be optimized")
        st.markdown("- Consider minor price adjustment or marketing strategy")
    else:
        st.markdown("- Excellent pricing strategy!")
        st.markdown("- Property is likely to sell quickly")

except Exception as e:
    st.error(f"Error making prediction: {e}")
