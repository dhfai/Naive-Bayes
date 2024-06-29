import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score, classification_report
from sklearn.preprocessing import LabelEncoder
import matplotlib.pyplot as plt


file_path = './data/PharmaDrugSales.xlsx'
data = pd.read_excel(file_path)

data = data.dropna()
data = data[data['Year'] != '#VALUE!']  
data['Year'] = data['Year'].astype(int)
data['Month'] = data['Month'].astype(int)
data['Date'] = data['Date'].astype(int)
data['Hour'] = data['Hour'].astype(int)

label_encoder = LabelEncoder()
data['Day'] = label_encoder.fit_transform(data['Day'])


target_columns = [
    'AceticAcidDerivatives', 'PropionicAcidDerivatives', 'SalicylicAcidDerivatives', 
    'PyrazolonesAndAnilides', 'AnxiolyticDrugs', 'HypnoticsSndSedativesDrugs', 
    'ObstructiveAirwayDrugs', 'Antihistamines'
]


features = ['Year', 'Month', 'Date', 'Hour', 'Day']
X = data[features]


model = GaussianNB()


for target in target_columns:
    
    bins = [0, 1, 2, 3, 4, 5, float('inf')]  
    labels = ['0-1', '1-2', '2-3', '3-4', '4-5', '5+']  
    data[target] = pd.cut(data[target], bins=bins, labels=labels, right=False)
    
    y = data[target]
    
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
    
    
    model.fit(X_train, y_train)
    
    
    y_pred = model.predict(X_test)
    
    
    predictions_df = pd.DataFrame({
        'Waktu': X_test.index,  
        'Tanggal': X_test['Date'],  
        'Jam': X_test['Hour'],  
        'Hari': X_test['Day'],  
        'Jumlah Penjualan': y_test.values,  
        'Prediksi Jumlah Penjualan': y_pred  
    })
    
    
    predictions_df['Hari'] = label_encoder.inverse_transform(predictions_df['Hari'])  

    
    predictions_df.to_excel(f'./data/prediksi/predictions_{target}.xlsx', index=False)

    
    accuracy = accuracy_score(y_test, y_pred)
    print(f'Akurasi untuk {target}: {accuracy}')
    print(classification_report(y_test, y_pred))
    
    
    plt.figure(figsize=(10, 6))
    plt.plot(y_test.values, label='Jumlah Penjualan Sebenarnya')
    plt.plot(y_pred, label='Prediksi Jumlah Penjualan')
    plt.title(f'Prediksi untuk {target}')
    plt.xlabel('Observasi')
    plt.ylabel('Jumlah Penjualan')
    plt.legend()
    plt.show()