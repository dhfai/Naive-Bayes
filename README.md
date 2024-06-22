# PREDIKSI PENJUALAN OBAT - DENGAN METODE NAIVE BAYES

[![forthebadge](https://forthebadge.com/images/badges/made-with-python.svg)](http://forthebadge.com)




Program ini kami buat untuk memenuhi tugas final mata kuliah `Data Mining`. Program ini bertujuan untuk memprediksi penjualan obat menggunakan metode `Naive Bayes`. Program ini dibuat menggunakan bahasa pemrograman `Python`. Data yang digunakan adalah data penjualan obat yang diperoleh dari [Kaggle](https://www.kaggle.com/uciml/drug-review-dataset). Data tersebut kemudian diolah dan diolah menggunakan metode Naive Bayes.


# Kelompok-DM
1. DHIA DHAIFULLAH
    - 105841108621
    - IF-6C
2. ARIKAL KHAIRAT
    -105841108421
    - IF-6C
3. CHALIDAH AZ-ZAHRAH. H
    - 105841107321
    - IF-6C


# Installation
1. Pastikan python sudah terinstall di komputer anda. Jika belum, silahkan download [disini](https://www.python.org/downloads/).
2. Install pip terlebih dahulu. Jika belum, silahkan download [disini](https://pip.pypa.io/en/stable/installing/).

    *Note untuk pengguna `Linux` - Jika anda menggunakan `Linux`, silahkan install `python3-pip` terlebih dahulu.*

3. Clone repository ini.
    ```bash
    git clone https://github.com/ddhaifullah/Data-Mining_Naive-Bayes.git
    ```

4. Masuk ke direktori project.
    ```bash
    cd Data-Mining_Naive-Bayes
    ```

6. Install requirements.
    ```bash
    pip install -r requirements.txt
    ```
7. Jalankan program.
    ```bash
    python main.py
    ```
8. Program akan berjalan dan menampilkan output prediksi penjualan obat.

### Output Data File
Output yang dihasilkan berupa prediksi penjualan obat berdasarkan data yang ada. File hasil prediksi akan disimpan dalam bentuk file `.xlsx` pada folder `data/prediksi/`. Berikut adalah penjelansan mengenai field-field yang ada pada file hasil prediksi:


| Waktu | Tanggal | Jam | Hari      | Jumlah Penjualan            | Prediksi Jumlah Penjualan |
|-------|---------|-----|-----------|-----------------------------|---------------------------|
| 15516 | 10      | 20  | Saturday  | 0-1                         | 0-1                       |
| 18945 | 3       | 17  | Tuesday   | 4-5                         | 0-1                       |
| 11738 | 5       | 10  | Wednesday | 1-2                         | 0-1                       |
| 27807 | 3       | 23  | Sunday    | 0-1                         | 0-1                       |
| 4482  | 7       | 2   | Tuesday   | 0-1                         | 0-1                       |
| 5828  | 9       | 4   | Tuesday   | 0-1                         | 0-1                       |


1. `Waktu` : Waktu penjualan obat.
2. `Tanggal` : Tanggal penjualan obat.
3. `Jam` : Jam penjualan obat.
4. `Hari` : Hari penjualan obat.
5. `Jumlah Penjualan` : Jumlah penjualan obat.
6. `Prediksi Jumlah Penjualan` : Prediksi jumlah penjualan obat.
      * **Binning**: Proses binning digunakan untuk mengelompokkan nilai penjualan menjadi interval-interval tertentu.
      Dalam kode, binning dilakukan dengan menentukan batas-batas (bins) dan label untuk setiap interval.
      * **Interval dan Label**: Batas (bins) yang digunakan adalah `[0, 1, 2, 3, 4, 5, float('inf')]`.
      Label yang digunakan untuk setiap interval adalah `['0-1', '1-2', '2-3', '3-4', '4-5', '5+']`.
      * **Prediksi**: Prediksi jumlah penjualan obat dilakukan dengan menggunakan metode Naive Bayes. Prediksi yang dihasilkan adalah interval jumlah penjualan obat. Jika nilai prediksi berada pada interval `[0, 1]`, mengartikan bahwa jumlah penjualan obat diprediksi berada pada rentang `0-1` yang artinya jumlah penjualan obat berada pada rentang `0 sampai 1` atau penjualan obat sedikit. Jika nilai prediksi berada pada interval `[1, 2]`, mengartikan bahwa jumlah penjualan obat diprediksi berada pada rentang `1-2` yang artinya jumlah penjualan obat berada pada rentang `1 sampai 2` atau penjualan obat sedang. Begitu seterusnya.
7. `Prediksi Jumlah Penjualan` : Prediksi jumlah penjualan obat.
    * Kurang Lebih sama dengan `Jumlah Penjualan` namun berdasarkan prediksi yang dihasilkan.
    * **Contoh**: Jika `Jumlah Penjualan` adalah `1-2` dan `Prediksi Jumlah Penjualan` adalah `0-1`, maka penjualan obat diprediksi berada pada rentang `0 sampai 1` atau penjualan obat sedikit. Jika `Jumlah Penjualan` adalah `4-5` dan `Prediksi Jumlah Penjualan` adalah `5+`, maka penjualan obat diprediksi berada pada rentang `5+` atau penjualan obat banyak.

![image](/img/img.png)



### Output Data Visualization
Output yang dihasilkan berupa prediksi penjualan obat berdasarkan data yang ada. File hasil prediksi akan disimpan dalam bentuk file `.csv` pada folder `data/prediksi/`. Berikut adalah contoh output yang dihasilkan:

- Prediksi penjualan obat `AceticAcidDerivatives`

  ![image](/img/1.png)

- Prediksi penjualan obat `PropionicAcidDerivatives`

  ![image](/img/2.png)

- Prediksi penjualan obat `SalicylicAcidDerivatives`

  ![image](/img/8.png)

- Prediksi penjualan obat `PyrazolonesAndAnilides`

  ![image](/img/3.png)

- Prediksi penjualan obat `AnxiolyticDrugs`

  ![image](/img/4.png)

- Prediksi penjualan obat `HypnoticsSndSedativesDrugs`

  ![image](/img/5.png)

- Prediksi penjualan obat `ObstructiveAirwayDrugs`

  ![image](/img/6.png)

- Prediksi penjualan obat `Antihistamines`

  ![image](/img/7.png)

