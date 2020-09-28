# # gender detector
# d = gender.Detector(case_sensitive=False)

# # spanish better detector
# guesser = genderator.Parser()

# print(found_gender +' '+ found_gender_2 +' otro: ' + spanish_gender)
# print(votes)
# print(most_votes(votes))

# found_gender, precision, n_docs = getGenders(name)[0]
# f_gender2 = d.get_gender(name)

# # do a spanish search
# answer = guesser.guess_gender(name)
# if answer:
#     spanish_gender = answer['gender']
# else:
#     spanish_gender = 'not found'

# print(found_gender +' '+ f_gender2 +' otro: ' + spanish_gender)


# crossed columns
# gender_type = feature_column.categorical_column_with_vocabulary_list('Type', ['female', 'male', 'unknown', 'andy'])
# age = feature_column.numeric_column('Age')
# age_buckets = feature_column.bucketized_column(age, boundaries=[1, 3, 5])
# age_type_feature = feature_column.crossed_column([age_buckets, gender_type], hash_bucket_size=50)
# feature_columns.append(feature_column.indicator_column(age_type_feature))

# # model
# inputs = keras.Input(shape=(7,), name="start")
# x = layers.Dense(15, activation="relu", name="dense_1")(inputs)
# outputs = layers.Dense(8, activation="softmax", name="predictions")(x)

# model = keras.Model(inputs=inputs, outputs=outputs)

# model.compile(
#     optimizer=keras.optimizers.RMSprop(),  # Optimizer
#     # Loss function to minimize
#     loss=keras.losses.SparseCategoricalCrossentropy(),
#     # List of metrics to monitor
#     metrics=[keras.metrics.SparseCategoricalAccuracy()],
# )

# print("Fit model on training data")
# history = model.fit(
#     train,
#     batch_size=15,
#     epochs=5,
#     # We pass some validation for
#     # monitoring validation loss and metrics
#     # at the end of each epoch
#     validation_data=(test),
# )

# print("Evaluate on test data")
# results = model.evaluate(test, batch_size=15)
# print("test loss, test acc:", results)