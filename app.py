import streamlit as st
import pandas as pd
import numpy as np

# =========================================================
# PAGE CONFIGURATION
# =========================================================

st.set_page_config(
    page_title="Smart Delivery Time Prediction",
    page_icon="🚚",
    layout="wide"
)

# =========================================================
# CUSTOM STYLING
# =========================================================

st.markdown("""
<style>

.stApp {
    background-color: #111827;
    color: #f9fafb;
}

.block-container {
    max-width: 1400px;
    padding-top: 1.5rem;
    padding-bottom: 3rem;
}

/* Streamlit title */
h1 {
    color: #f9fafb !important;
    font-weight: 800 !important;
}

/* Section headings */
h2, h3, h4, h5, h6 {
    color: #f9fafb !important;
}

/* Section labels */
.section-title {
    color: #9ca3af;
    font-size: 12px;
    font-weight: 800;
    letter-spacing: 1.2px;
    text-transform: uppercase;
    margin-top: 28px;
    margin-bottom: 14px;
}

/* KPI cards */
div[data-testid="stMetric"] {
    background: #1f2937;
    border: 1px solid #374151;
    border-radius: 16px;
    padding: 20px;
}

div[data-testid="stMetricLabel"] {
    color: #9ca3af !important;
    font-size: 13px !important;
    font-weight: 600 !important;
}

div[data-testid="stMetricValue"] {
    color: #ffffff !important;
    font-size: 28px !important;
    font-weight: 800 !important;
}

div[data-testid="stMetricDelta"] {
    font-size: 12px !important;
}

/* Select boxes */
div[data-baseweb="select"] > div {
    background-color: #374151 !important;
    border: 1px solid #4b5563 !important;
    border-radius: 14px !important;
    color: #ffffff !important;
    min-height: 48px;
}

div[data-baseweb="select"] span {
    color: #ffffff !important;
}

div[data-baseweb="select"] svg {
    fill: #ffffff !important;
}

/* Sliders */
div[data-testid="stSlider"] [role="slider"] {
    background-color: #ff7518 !important;
    border-color: #ff7518 !important;
}

/* Predictor area */
.predictor-area {
    background: #1f2937;
    border: 1px solid #374151;
    border-radius: 18px;
    padding: 25px;
    margin-top: 10px;
}

/* Predictor column headings */
.column-title {
    color: #ff7518;
    font-size: 14px;
    font-weight: 800;
    letter-spacing: 0.6px;
    margin-bottom: 18px;
}

/* Prediction box */
.prediction-box {
    background: #2d3748;
    border: 1px solid #465466;
    border-radius: 16px;
    padding: 20px;
    margin-top: 20px;
}

/* Prediction metric */
.prediction-box div[data-testid="stMetric"] {
    background: transparent !important;
    border: none !important;
    padding: 0 !important;
    text-align: right;
}

.prediction-box div[data-testid="stMetricLabel"] {
    color: #aeb8c7 !important;
    font-size: 14px !important;
    font-weight: 600 !important;
    text-transform: uppercase;
}

.prediction-box div[data-testid="stMetricValue"] {
    color: #ff7518 !important;
    font-size: 38px !important;
    font-weight: 900 !important;
}

/* Predict button */
div[data-testid="stButton"] button {
    background-color: #ff7518 !important;
    color: #ffffff !important;
    border: none !important;
    border-radius: 14px !important;
    font-size: 18px !important;
    font-weight: 700 !important;
    min-height: 62px;
    box-shadow: 0 8px 20px rgba(255, 117, 24, 0.25);
}

div[data-testid="stButton"] button:hover {
    background-color: #ea580c !important;
    color: #ffffff !important;
}

/* Divider */
hr {
    border-color: #374151 !important;
}

/* Mobile */
@media (max-width: 768px) {

    .block-container {
        padding-left: 1rem;
        padding-right: 1rem;
    }

    .predictor-area {
        padding: 18px;
    }

    .prediction-box div[data-testid="stMetric"] {
        text-align: left;
    }

}

</style>
""", unsafe_allow_html=True)


# =========================================================
# HEADER
# =========================================================

st.title("🚚 Smart Delivery Time Prediction")



# =========================================================
# SAMPLE DATA
# =========================================================

city_data = pd.DataFrame({
    "City": [
        "Metropolitian",
        "Urban",
        "Semi-Urban"
    ],
    "Orders": [
        34388,
        10134,
        1071
    ],
    "Avg Time": [
        27.2,
        22.9,
        49.7
    ]
})


daily_orders = pd.DataFrame({
    "Week": [
        "Feb 11",
        "Feb 18",
        "Feb 25",
        "Mar 4",
        "Mar 11",
        "Mar 18",
        "Mar 25",
        "Apr 1"
    ],
    "Orders": [
        1200,
        1850,
        2400,
        3100,
        2900,
        3500,
        4200,
        3900
    ]
})


distance_data = pd.DataFrame({
    "Distance": [
        "0-3 km",
        "3-7 km",
        "7-12 km",
        "12-16 km",
        "16+ km"
    ],
    "Avg Delivery Time": [
        18.4,
        23.5,
        29.1,
        34.6,
        42.8
    ]
})


traffic_data = pd.DataFrame({
    "Traffic": [
        "Low",
        "Medium",
        "High",
        "Jam"
    ],
    "Avg Time": [
        21.2,
        26.8,
        31.4,
        45.1
    ]
})


weather_data = pd.DataFrame({
    "Weather": [
        "Sunny",
        "Cloudy",
        "Windy",
        "Fog",
        "Stormy",
        "Sandstorm"
    ],
    "Avg Time": [
        21.8,
        24.2,
        26.1,
        28.9,
        31.5,
        33.2
    ]
})


vehicle_data = pd.DataFrame({
    "Vehicle": [
        "Motorcycle",
        "Scooter",
        "E-Scooter",
        "Bicycle"
    ],
    "Avg Time": [
        27.5,
        25.1,
        24.2,
        33.8
    ]
})


# =========================================================
# 1. KEY PERFORMANCE INDICATORS
# =========================================================

st.markdown(
    '<div class="section-title">1. Key Performance Indicators</div>',
    unsafe_allow_html=True
)

k1, k2, k3 = st.columns(3)

with k1:
    st.metric(
        label="⏱️ Avg Delivery Time",
        value="26.3 min",
        delta="-4.2%"
    )

with k2:
    st.metric(
        label="📦 Total Orders",
        value="45,593",
        delta="+12.8%"
    )

with k3:
    st.metric(
        label="⭐ Avg Driver Rating",
        value="4.63 / 5",
        delta="High Satisfaction"
    )


# =========================================================
# 2. DELIVERY OVERVIEW
# =========================================================

st.markdown(
    '<div class="section-title">2. Delivery Overview</div>',
    unsafe_allow_html=True
)

col1, col2 = st.columns(2)

with col1:

    st.subheader("📍 Order Distribution by City")

    st.bar_chart(
        city_data.set_index("City")["Orders"],
        height=280
    )


with col2:

    st.subheader("📈 Daily Order Volume Trend")

    st.line_chart(
        daily_orders.set_index("Week")["Orders"],
        height=280
    )


# =========================================================
# 3. CITY & TIME ANALYSIS
# =========================================================

st.markdown(
    '<div class="section-title">3. City & Time Analysis</div>',
    unsafe_allow_html=True
)

col1, col2 = st.columns(2)

with col1:

    st.subheader("🏙️ Average Delivery Time by City")

    st.bar_chart(
        city_data.set_index("City")["Avg Time"],
        height=280
    )


with col2:

    st.subheader("📏 Delivery Time vs Distance")

    st.bar_chart(
        distance_data.set_index("Distance")["Avg Delivery Time"],
        height=280
    )


# =========================================================
# 4. ENVIRONMENTAL & VEHICLE FACTORS
# =========================================================

st.markdown(
    '<div class="section-title">4. Environmental & Vehicle Factors</div>',
    unsafe_allow_html=True
)

c1, c2, c3 = st.columns(3)

with c1:

    st.subheader("🚦 Traffic Impact")

    st.bar_chart(
        traffic_data.set_index("Traffic")["Avg Time"],
        height=280
    )


with c2:

    st.subheader("🌦️ Weather Impact")

    st.bar_chart(
        weather_data.set_index("Weather")["Avg Time"],
        height=280
    )


with c3:

    st.subheader("🛵 Average Time by Vehicle")

    st.bar_chart(
        vehicle_data.set_index("Vehicle")["Avg Time"],
        height=280
    )


# =========================================================
# 5. DELIVERY TIME PREDICTOR ENGINE
# =========================================================

st.markdown(
    '<div class="section-title">5. Delivery Time Predictor Engine</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="predictor-area">',
    unsafe_allow_html=True
)

col1, col2, col3 = st.columns(3)


# =========================================================
# DRIVER DETAILS
# =========================================================

with col1:

    st.markdown(
        '<div class="column-title">DRIVER DETAILS</div>',
        unsafe_allow_html=True
    )

    age = st.slider(
        "Driver Age",
        18,
        60,
        25,
        key="driver_age"
    )

    rating = st.slider(
        "Driver Rating",
        1.0,
        5.0,
        4.5,
        0.1,
        key="driver_rating"
    )

    deliveries = st.selectbox(
        "Multiple Deliveries Assigned",
        [0, 1, 2, 3],
        format_func=lambda x:
            "0 (Single Delivery)"
            if x == 0
            else (
                "1 Active Order"
                if x == 1
                else f"{x} Active Orders"
            ),
        key="multiple_deliveries"
    )


# =========================================================
# ENVIRONMENT & VEHICLE
# =========================================================

with col2:

    st.markdown(
        '<div class="column-title">ENVIRONMENT & VEHICLE</div>',
        unsafe_allow_html=True
    )

    weather = st.selectbox(
        "Weather Condition",
        [
            "Sunny",
            "Cloudy",
            "Windy",
            "Fog",
            "Stormy",
            "Sandstorms"
        ],
        key="weather"
    )

    traffic = st.selectbox(
        "Road Traffic Density",
        [
            "Low",
            "Medium",
            "High",
            "Jam"
        ],
        format_func=lambda x:
            f"{x} Traffic",
        key="traffic"
    )

    vehicle = st.selectbox(
        "Type of Vehicle",
        [
            "motorcycle",
            "scooter",
            "electric_scooter",
            "bicycle"
        ],
        format_func=lambda x: {
            "motorcycle": "Motorcycle",
            "scooter": "Scooter",
            "electric_scooter": "Electric Scooter",
            "bicycle": "Bicycle"
        }[x],
        key="vehicle"
    )


# =========================================================
# ORDER & LOCATION
# =========================================================

with col3:

    st.markdown(
        '<div class="column-title">ORDER & LOCATION</div>',
        unsafe_allow_html=True
    )

    distance = st.slider(
        "Distance",
        0.5,
        25.0,
        6.5,
        0.5,
        key="distance"
    )

    city = st.selectbox(
        "City Type",
        [
            "Metropolitian",
            "Urban",
            "Semi-Urban"
        ],
        key="city"
    )

    festival = st.selectbox(
        "Festival Rush?",
        [
            "No",
            "Yes"
        ],
        key="festival"
    )


st.markdown(
    '</div>',
    unsafe_allow_html=True
)


# =========================================================
# DELIVERY TIME PREDICTION FUNCTION
# =========================================================

def predict_delivery_time(
    age,
    rating,
    deliveries,
    weather,
    traffic,
    vehicle,
    distance,
    city,
    festival
):

    time = 15.0

    # Distance effect
    time += distance * 1.35

    # Driver age effect
    time += (30 - age) * 0.15

    # Driver rating effect
    time += (5.0 - rating) * 3.2

    # Multiple deliveries effect
    time += deliveries * 4.5

    # Weather effect
    weather_weights = {
        "Sunny": 0,
        "Cloudy": 2,
        "Windy": 3,
        "Fog": 5,
        "Stormy": 8,
        "Sandstorms": 9
    }

    time += weather_weights.get(weather, 0)

    # Traffic effect
    traffic_weights = {
        "Low": 0,
        "Medium": 4,
        "High": 8,
        "Jam": 16
    }

    time += traffic_weights.get(traffic, 0)

    # Vehicle effect
    vehicle_weights = {
        "motorcycle": 1,
        "scooter": 0,
        "electric_scooter": -1,
        "bicycle": 7
    }

    time += vehicle_weights.get(vehicle, 0)

    # City effect
    if city == "Metropolitian":
        time += 2

    elif city == "Semi-Urban":
        time += 12

    # Festival effect
    if festival == "Yes":
        time += 11

    return max(time, 1)


# =========================================================
# PREDICTION BAR
# =========================================================

st.markdown(
    '<div class="prediction-box">',
    unsafe_allow_html=True
)

button_col, result_col = st.columns(
    [1.7, 1],
    gap="large"
)


# =========================================================
# PREDICT BUTTON
# =========================================================

with button_col:

    st.write("")

    predict_button = st.button(
        "🧮 Predict Delivery Time",
        type="primary",
        use_container_width=True,
        key="predict_delivery"
    )


# =========================================================
# RUN PREDICTION
# =========================================================

if predict_button:

    prediction = predict_delivery_time(
        age=age,
        rating=rating,
        deliveries=deliveries,
        weather=weather,
        traffic=traffic,
        vehicle=vehicle,
        distance=distance,
        city=city,
        festival=festival
    )

    st.session_state["prediction"] = prediction


# =========================================================
# DISPLAY RESULT
# =========================================================

with result_col:

    prediction = st.session_state.get(
        "prediction",
        None
    )

    if prediction is None:

        st.metric(
            label="ESTIMATED DURATION",
            value="-- min"
        )

    else:

        st.metric(
            label="ESTIMATED DURATION",
            value=f"{prediction:.1f} min"
        )


st.markdown(
    '</div>',
    unsafe_allow_html=True
)


# =========================================================
# FOOTER
# =========================================================

st.write("")

st.divider()

st.caption(
    "🚚 FoodExpress Analytics • Smart Delivery Time Prediction Dashboard"
)