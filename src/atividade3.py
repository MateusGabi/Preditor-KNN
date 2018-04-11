#!/usr/bin/python

# -*- coding: utf-8 -*-
import csv
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.grid_search import RandomizedSearchCV

def main():
    dataset = csv.reader(open('data/alturapeso.csv'))

    x = []
    y = []
    for line in dataset:
        x.append([ float(line[0]), float(line[1]) ])
        y.append(int(line[2]))

    f = fit(x, y)

    train(f, x, y)

def fit(x, y):
    neigh = KNeighborsClassifier()
    neigh.fit(x, y)
    return neigh

def train(neigh, x, y):
    #Test com tamanho de 25%
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.25, random_state=42)

    k_range = list(range(1, 75))
    weight_options = ['uniform', 'distance']
    param_dist = dict(n_neighbors=k_range, weights=weight_options)

    rscv = RandomizedSearchCV(neigh, param_dist, cv=10, scoring='accuracy', n_iter=10, random_state=42)
    rscv.fit(x_train, y_train)

    print("Best parameters set found:",rscv.best_params_)

if __name__ == '__main__':
    main()