#test load
import time

if __name__ == '__main__':
	from fastai.vision import *
	from fastai.metrics import error_rate

	defaults.device = torch.device('cuda') if torch.cuda.is_available() else torch.device('cpu')
	print(defaults.device)
	learn = load_learner('.','test_model.pkl')
	#print(learn.data)

	test_img = open_image("elephant.jpg")
	pred = learn.predict(test_img)
	#print(pred)
	#print(pred[0])

	if str(pred[0]) == "Elephants":
		print("Test classification SUCCESSFUL")