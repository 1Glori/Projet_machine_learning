from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
import numpy

class Additif:
	def __init__(self, data_preparation_object):
		self.data_preparation_object = data_preparation_object
		self.model = LinearRegression()

		self.model.fit(data_preparation_object.x_train, data_preparation_object.y_train)

		y_train_predicted = self.model.predict(data_preparation_object.x_train)
		mean_train_absolute_error = numpy.mean(numpy.abs(y_train_predicted - data_preparation_object.y_train))
		print(f"sur le jeu de train : {mean_train_absolute_error=:.2f}")


		y_test_predicted = self.model.predict(data_preparation_object.x_test)
		mean_test_absolute_error = numpy.mean(numpy.abs(y_test_predicted - data_preparation_object.y_test))
		print(f"sur le jeu de test : {mean_test_absolute_error=:.2f}")

		self.show_model_predictions(y_train_predicted, y_test_predicted)

	def show_model_predictions(self, y_train_predicted, y_test_predicted):
		plt.figure(figsize=(15, 6))
		plt.plot(self.data_preparation_object.x_train.index, self.data_preparation_object.y_train,  "bo:", label ='TimesSeries Data')
		plt.plot(self.data_preparation_object.x_train.index, y_train_predicted,"b", label = 'Fitted Additive Model') 

		plt.plot(self.data_preparation_object.x_test.index, self.data_preparation_object.y_test, "ro:", label = 'True Future Data') 
		plt.plot(self.data_preparation_object.x_test.index, y_test_predicted, "r", label = 'Forecasted Additive Model Data')

		ci = 1.96 * numpy.std(y_train_predicted) / numpy.sqrt(len(self.data_preparation_object.x_train))
		plt.plot(self.data_preparation_object.x_test.index, y_test_predicted + ci, color='blue', alpha=0.1,  label = '95% Confidence Interval')

		plt.legend()
		plt.show()