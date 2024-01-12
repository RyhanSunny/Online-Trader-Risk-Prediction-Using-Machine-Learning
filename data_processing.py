def preprocess_data(df, is_train=True):
    # Handle missing values
    df.fillna(method="ffill", inplace=True)
    
    # One-hot encoding for categorical variables
    categorical_columns = ["Z_METHODE", "Z_CARD_ART", "Z_LAST_NAME", "WEEKDAY_ORDER"]
    df = pd.get_dummies(df, columns=categorical_columns)
    
    # Replace '?' with NaN and convert 'TIME_ORDER' to minutes past midnight
    df['TIME_ORDER'] = df['TIME_ORDER'].replace('?', np.nan)
    df['TIME_ORDER'] = pd.to_datetime(df['TIME_ORDER'], errors='coerce').dt.hour * 60 + pd.to_datetime(df['TIME_ORDER'], errors='coerce').dt.minute
    mean_time = df['TIME_ORDER'].mean()
    df['TIME_ORDER'].fillna(mean_time, inplace=True)
    
    # Label encoding
    label_encoder = LabelEncoder()
    encoded_columns = ['B_EMAIL', 'B_TELEFON', 'FLAG_NEWSLETTER', 'CHK_LADR', 'CHK_RADR', 'CHK_KTO',
                       'CHK_CARD', 'CHK_COOKIE', 'CHK_IP', 'FAIL_LPLZ', 'FAIL_LORT', 'FAIL_LPLZORTMATCH',
                       'FAIL_RPLZ', 'FAIL_RORT', 'FAIL_RPLZORTMATCH', 'NEUKUNDE', 'FLAG_LRIDENTISCH']
    for column in encoded_columns:
        df[column] = label_encoder.fit_transform(df[column].astype(str))  # Cast to string to avoid issues with mixed types
    
    # Convert 'B_BIRTHDATE' to 'AGE' and drop 'B_BIRTHDATE'
    df['AGE'] = df['B_BIRTHDATE'].apply(calculate_age)
    df.drop(columns=['B_BIRTHDATE'], inplace=True)
    
    # Replace "?" with 0 in specific columns
    columns_to_replace_question_mark = [
        'ANUMMER_02', 'ANUMMER_03', 'ANUMMER_04', 'ANUMMER_05',
        'ANUMMER_06', 'ANUMMER_07', 'ANUMMER_08', 'ANUMMER_09',
        'ANUMMER_10', 'DATE_LORDER', 'MAHN_AKT', 'MAHN_HOECHST'
    ]
    df[columns_to_replace_question_mark] = df[columns_to_replace_question_mark].replace('?', 0)
    
    # Convert 'DATE_LORDER' to epoch time
    df['DATE_LORDER'] = pd.to_datetime(df['DATE_LORDER']).values.astype(np.int64) // 10 ** 9

    # Split the data into features and target variable if it's the training data
    if is_train:
        X = df.drop("CLASS", axis=1)
        y = df["CLASS"]
        return X, y
    else:
        X = df.drop("CLASS", axis=1, errors='ignore')  # 'errors' param to ignore if 'CLASS' is not present
        return X
