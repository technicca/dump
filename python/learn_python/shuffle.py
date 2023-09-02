import random

ml_words = [
    "algorithm", "neural", "network", "deep", "learning", "regression", 
    "classification", "clustering", "reinforcement", "supervised", 
    "unsupervised", "semi-supervised", "decision", "tree", "random", 
    "forest", "gradient", "boosting", "bagging", "SVM", "KNN", "K-means", 
    "DBSCAN", "PCA", "logistic", "linear", "naive", "bayes", "perceptron", 
    "ANN", "CNN", "RNN", "GAN", "autoencoder", "overfitting", "underfitting", 
    "bias", "variance", "cross-validation", "hyperparameter", "tuning", 
    "loss", "function", "activation", "ReLU", "sigmoid", "tanh", "softmax", 
    "backpropagation", "epoch", "batch", "size", "learning", "rate", 
    "momentum", "dropout", "regularization", "L1", "L2", "data", "set", 
    "training", "validation", "test", "feature", "extraction", "selection", 
    "engineering", "label", "target", "prediction", "error", "accuracy", 
    "precision", "recall", "F1", "score", "confusion", "matrix", "ROC", 
    "AUC", "overfitting", "underfitting", "ensemble", "stacking", "pipeline", 
    "feature", "scaling", "normalization", "standardization", "outlier", 
    "dimensionality", "reduction", "grid", "search", "time", "series", 
    "sequence", "prediction", "NLP", "computer", "vision", "recommender", 
    "system", "unsupervised", "learning"
]

random.shuffle(ml_words)

print('\n'.join(ml_words))

