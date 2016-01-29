from django import forms

from .models import game, user

class PostUser(forms.ModelForm):
	class Meta:
		model = user
		fields = [
			"username",
			"email",
			"steamusername"
		]

class PostGame(forms.ModelForm):
	class Meta:
		model = game
		fields = [
			"title",
			"linearity",
			"replayability",
			"learning_curve",
			"story",
			"sound",
			"graphic_dependency",
			"review",
			"image",
			"video",
		]