# Real Estate Valuation - Business Analysis with Logistic Regression

A machine learning project that uses logistic regression to predict real estate sale probability and support business decision-making.

## 📋 Business Analysis Summary

### Dataset and Features
**Real Estate Valuation Dataset** from UCI Machine Learning Repository contains 414 property records with the following key features:
- **House Age**: Age of the property in years
- **Distance to MRT**: Distance to nearest Mass Rapid Transit station (meters)
- **Number of Convenience Stores**: Count of nearby convenience stores
- **Unit Price**: House price per unit area (NT$/m²)
- **Location**: Latitude and longitude coordinates

### Classification Problem
**Objective**: Predict whether a real estate property will sell based on its characteristics and listing price.

**Target Variable**: Binary classification
- `1` = Property will likely sell (priced within 120% of market average)
- `0` = Property will likely NOT sell (priced above 120% of market average)

**Model Performance**: 
- Training Accuracy: 99.7%
- Test Accuracy: 99.2%

### Business Decision Support
This logistic regression model supports several critical business decisions:

1. **Pricing Strategy**: Determine optimal listing price to maximize sale probability
2. **Market Analysis**: Identify properties likely to sell quickly vs. those requiring price adjustments
3. **Investment Decisions**: Assess property attractiveness based on location and characteristics
4. **Risk Assessment**: Quantify the probability of a successful sale before listing

**Business Impact**: Real estate agents and property investors can use this model to make data-driven pricing decisions, reducing time on market and maximizing profitability.

## 🚀 Project Features

- **Jupyter Notebook Analysis**: Complete data exploration, model training, and evaluation
- **Interactive Streamlit App**: Web interface for real-time property sale probability predictions
- **Model Persistence**: Trained model saved for production use
- **Visualization**: Price vs. probability charts and business insights

## 📁 Project Structure

```
real_estate/
├── businessAnalysis_realEstateValuation.ipynb  # Main analysis notebook
├── real_estate_app.py                         # Streamlit web application
├── real_estate_model.pkl                      # Trained logistic regression model
├── data/
│   ├── Real estate valuation data set.xlsx    # Original dataset
│   └── real+estate+valuation+data+set.zip    # Backup data
└── README.md                                  # This file
```

## 🛠️ Installation and Setup

1. **Clone the repository**:

   ```bash
   git clone https://github.com/mobius29er/realEstateValuation.git
   cd realEstateValuation
   ```

2. **Install required packages**:

   ```bash
   pip install pandas numpy scikit-learn matplotlib streamlit joblib openpyxl
   ```

3. **Run the Jupyter Notebook**:

   ```bash
   jupyter notebook businessAnalysis_realEstateValuation.ipynb
   ```

4. **Launch the Streamlit App**:

   ```bash
   streamlit run real_estate_app.py
   ```

## 🌐 Streamlit Cloud Deployment

To deploy this app on Streamlit Cloud:

1. **Fork or clone** this repository to your GitHub account
2. **Visit** [share.streamlit.io](https://share.streamlit.io)
3. **Connect your GitHub** account and select this repository
4. **Set the main file path** to: `real_estate_app.py`
5. **Deploy** - Streamlit Cloud will automatically install dependencies from `requirements.txt`

**Live Demo**: The app can be deployed and accessed via Streamlit Cloud for interactive demonstrations.

## 💡 Usage

### Jupyter Notebook

Open `businessAnalysis_realEstateValuation.ipynb` to explore:

- Data loading and preprocessing
- Model training and evaluation
- Price sensitivity analysis
- Business insights and recommendations

### Streamlit Web App

Launch the app to interactively:

- Input property characteristics (age, MRT distance, convenience stores, price)
- Get real-time sale probability predictions
- Receive business recommendations
- Visualize results with color-coded feedback

## 📊 Model Details

- **Algorithm**: Logistic Regression
- **Features**: House age, MRT distance, convenience stores count, listing price
- **Target**: Binary classification (will sell / won't sell)
- **Performance**: 99.2% test accuracy
- **Business Rule**: Properties priced within 120% of market average are likely to sell

## 🎯 Business Applications

This model can be used by:

- **Real Estate Agents**: Optimize listing prices for faster sales
- **Property Investors**: Assess investment opportunities
- **Homeowners**: Determine competitive pricing strategies
- **Market Analysts**: Understand pricing dynamics

## 📈 Key Insights

- Properties priced within 120% of market average have high sale probability
- Distance to MRT station significantly impacts sale likelihood
- Number of nearby convenience stores affects property attractiveness
- House age influences buyer preferences

## 🔧 Technical Stack

- **Python 3.13+**
- **pandas**: Data manipulation and analysis
- **scikit-learn**: Machine learning algorithms
- **matplotlib**: Data visualization
- **streamlit**: Web application framework
- **joblib**: Model serialization

## 📝 License

This project is part of an educational assignment for AI/ML coursework.

## 🤝 Contributing

This is an educational project. Feel free to fork and experiment with different models or features.