# smart-delivery-time-prediction
# 🚚 FoodExpress Analytics

### ML Insights & Delivery Prediction Engine

FoodExpress Analytics is an interactive Streamlit dashboard designed to analyze food delivery operations and estimate delivery time based on different delivery-related factors.

The dashboard provides key performance indicators, visual analytics, and an interactive delivery-time prediction engine.

---

## 📌 Project Overview

Food delivery time can be affected by several factors such as:

- 📏 Delivery distance
- 🚦 Road traffic
- 🌦️ Weather conditions
- 🛵 Vehicle type
- 👨‍🚴 Driver characteristics
- ⭐ Driver rating
- 📦 Multiple deliveries
- 🏙️ City type
- 🎉 Festival rush

FoodExpress Analytics brings these factors together in a single dashboard to help understand delivery performance and estimate the expected delivery duration.

---

## 🎯 Objectives

The main objectives of this project are:

1. Analyze food delivery performance.
2. Visualize order distribution across different city types.
3. Analyze delivery time based on distance.
4. Understand the impact of traffic on delivery time.
5. Analyze the effect of weather conditions.
6. Compare delivery performance across different vehicles.
7. Provide an interactive delivery-time prediction interface.
8. Present the results through an easy-to-use dashboard.

---

## 📊 Dashboard Features

### 1. Key Performance Indicators

The dashboard displays important business metrics including:

- ⏱️ Average Delivery Time
- 📦 Total Orders
- ⭐ Average Driver Rating

These KPIs provide a quick overview of delivery performance.

---

### 2. Delivery Overview

The dashboard contains visualizations for:

- 📍 Order Distribution by City
- 📈 Daily Order Volume Trend

These charts help understand order patterns and demand across different periods and locations.

---

### 3. City & Time Analysis

This section analyzes:

- 🏙️ Average Delivery Time by City
- 📏 Delivery Time vs Distance

The distance analysis helps demonstrate how delivery duration changes as the delivery distance increases.

---

### 4. Environmental & Vehicle Analysis

The dashboard analyzes the relationship between delivery time and:

- 🚦 Traffic conditions
- 🌦️ Weather conditions
- 🛵 Vehicle type

This helps identify environmental and transportation factors that may influence delivery performance.

---

## 🧮 Delivery Time Predictor

FoodExpress Analytics includes an interactive prediction engine.

Users can enter:

### Driver Details
- Driver Age
- Driver Rating
- Number of Multiple Deliveries

### Environment & Vehicle
- Weather Condition
- Road Traffic Density
- Vehicle Type

### Order & Location
- Delivery Distance
- City Type
- Festival Rush

After entering the required information, the user can click:

**🧮 Predict Delivery Time**

The dashboard then displays the estimated delivery duration.

---

## 🔢 Prediction Logic

The current prototype calculates delivery time using a weighted rule-based formula.

The prediction starts with a base delivery time and adjusts it according to different factors.

For example:

- Greater distance increases delivery time.
- Lower driver ratings increase estimated time.
- Multiple active deliveries increase estimated time.
- Poor weather conditions increase estimated time.
- Heavy traffic increases estimated time.
- Vehicle type affects delivery duration.
- City type affects delivery duration.
- Festival rush adds additional delivery time.

