from sklearn.model_selection import train_test_split

class Splitter:
    def split(X, y, test_part=0.2, val_part=0.25):
        X_train, X_test, y_train, y_test \
            = train_test_split(X, y, test_size=test_part, random_state=1)
        X_train, X_val, y_train, y_val \
            = train_test_split(X_train, y_train, test_size=val_part, random_state=1)
        return X_train, X_test, X_val, y_train, y_test, y_val
