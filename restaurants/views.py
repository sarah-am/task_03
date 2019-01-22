from django.shortcuts import render

def welcome(request):
    return render(request, 'index.html', {'msg':'Hello World!'})

def restaurant_list(request):

    context = {
    	'my_list':[
	    	{
	    		'restaurant_name':'White Castle',
	    		'food_type':'burgers',
	    	},
	    	{
	    		'restaurant_name':'Out of this Oven',
	    		'food_type':'pizza',
	    	},
	    	{
	    		'restaurant_name':'Wacky Rolls',
	    		'food_type':'sushi',
	    	},    	    	
    	]

    }
    return render(request, 'list.html', context)


def restaurant_detail(request):

    context = {
    	'my_object': {
    		'restaurant_name':'White Castle',
	    	'food_type':'burgers',
    	}
    }
    return render(request, 'detail.html', context)